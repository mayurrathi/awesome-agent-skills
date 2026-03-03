---
name: 07 Firebase & BaaS Infrastructure
description: Firebase ecosystem patterns including Auth, Firestore data modeling, Cloud Functions, FCM, Hosting, Security Rules, Firebase Studio workspaces, and cost optimization for indie projects.
version: 1.0.0
---

# 07 Firebase & BaaS Infrastructure

This skill defines the architectural patterns for leveraging Firebase as a complete Backend-as-a-Service across all projects, with emphasis on cost efficiency for indie/bootstrapped applications.

## 1. Firebase Authentication
**Goal:** Frictionless, secure user identity management.
*   **Anonymous Auth:** Always implement `signInAnonymously()` as the default on first launch. This enables immediate usage without barriers while creating a persistent UID for data association.
*   **Account Linking:** When the user is ready to commit (after value delivery), use `linkWithCredential()` to upgrade their anonymous account to Google OAuth, Apple Sign-In, or Email/Password. All their existing data travels with them — zero data loss.
*   **Provider Priority:** Google OAuth first (highest conversion on Android), Apple Sign-In (required by Apple for apps with third-party login), Email/Password as fallback.
*   **Security:** Enable Email Enumeration Protection in Firebase Console. Set session duration appropriately. Implement multi-factor authentication (MFA) for admin/sensitive flows.

## 2. Firestore Data Modeling
**Goal:** Schema design optimized for read performance, cost, and real-time sync.
*   **Denormalization:** Firestore is not a relational database. Duplicate data across documents to avoid joins. A user's display name should exist in every document that renders it — not fetched via a reference.
*   **Collection Structure:** Use top-level collections for primary entities (`users`, `games`, `sessions`). Use subcollections for owned data (`users/{uid}/tickets`, `games/{gameId}/players`).
*   **Document Size:** Keep documents under 20KB for fast reads and real-time sync efficiency. Move large blobs (images, audio) to Cloud Storage and store only the URL reference.
*   **Indexes:** Create composite indexes proactively for any query combining `where()` clauses on different fields with `orderBy()`. Monitor the Firestore console for auto-suggested indexes.
*   **Reads Optimization:** Use `getDoc()` for one-time reads, `onSnapshot()` only when real-time updates are needed. Implement pagination with `startAfter()` and `limit()` to cap reads.

## 3. Firestore Security Rules
**Goal:** Zero-trust security enforced at the database level.
*   **Default Deny:** Start every ruleset with `allow read, write: if false;` and open access incrementally.
*   **Authentication Check:** Every rule must verify `request.auth != null` before granting any access.
*   **Ownership Enforcement:** Users can only read/write their own documents: `allow read, write: if request.auth.uid == resource.data.userId;`
*   **Data Validation:** Use `request.resource.data` to validate incoming writes: check field types, string lengths, required fields, and value ranges.
*   **Rate Limiting:** Combine rules with Cloud Functions for write-heavy operations. Rules alone cannot rate-limit, but they can reject obviously invalid payloads.

## 4. Cloud Functions
**Goal:** Server-side logic without managing infrastructure.
*   **Triggers:** Use Firestore triggers (`onCreate`, `onUpdate`, `onDelete`) for reactive backend logic (e.g., recalculating leaderboards on score write). Use HTTPS callable functions for client-initiated server actions.
*   **Cold Start Mitigation:** Set `minInstances: 1` for latency-critical functions. Keep function packages lean — avoid importing the entire Firebase Admin SDK when you only need Firestore.
*   **Idempotency:** All functions must be idempotent. Firestore triggers can fire multiple times. Use transaction-based writes and check for existing state before mutating.
*   **Environment Config:** Store secrets in Secret Manager (not environment variables). Access via `defineSecret()` in Firebase Functions v2.

## 5. Firebase Cloud Messaging (FCM)
**Goal:** Contextual, behavior-driven push notifications.
*   **Token Management:** Request notification permission after user demonstrates engagement (never on first load). Store the FCM token in the user's Firestore document. Refresh and update on every app launch.
*   **Topic Subscriptions:** Use topics for broadcast messages (e.g., `topic: "game-updates"`). Use individual tokens for personalized nudges.
*   **Payload Design:** Use `data` messages (not `notification`) for full control over display. Handle the message in the service worker's `push` event to show custom notifications with actions.
*   **Batch Sending:** Use `sendEachForMulticast()` for sending to multiple tokens. Handle `messaging/registration-token-not-registered` errors by cleaning stale tokens.

## 6. Firebase Hosting
**Goal:** Fast, secure hosting with CDN and SSL out of the box.
*   **Configuration:** Set `public` to `dist`. Add rewrites for SPA: `{ "source": "**", "destination": "/index.html" }`.
*   **Headers:** Set `Cache-Control` headers for static assets (long cache for hashed filenames, short for `index.html`). Add security headers: `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`.
*   **Preview Channels:** Use `firebase hosting:channel:deploy <channel-name>` for temporary preview URLs during development.
*   **Multi-Site:** Use `firebase hosting:sites:create <site-name>` for hosting multiple apps under one Firebase project.

## 7. Cost Optimization for Indie Projects
**Goal:** Stay within Firebase's free Spark plan as long as possible; optimize Blaze plan usage.
*   **Reads:** Cache Firestore responses on the client (IndexedDB or in-memory). Use `onSnapshot()` listeners sparingly — they count reads on every change. Batch reads with `getAll()`.
*   **Writes:** Batch Firestore writes with `writeBatch()` (counts as one operation per document, but reduces round trips). Debounce client-side writes.
*   **Cloud Functions:** Minimize invocations. Use client-side logic for non-sensitive computations. Set memory allocation to minimum needed (128MB or 256MB).
*   **Storage:** Compress images before upload. Use Cloud Storage lifecycle rules to auto-delete temporary files.
*   **Budget Alerts:** Set budget alerts in Google Cloud Console at $5, $10, $25 thresholds. Monitor usage weekly in Firebase Console → Usage and billing.

## 8. Firebase Studio Workspaces
**Goal:** Leverage cloud-based development environments for rapid prototyping.
*   **Access:** Utilize the 30 workspaces available via Google Developer Program. Each workspace provides a full cloud IDE with AI assistance.
*   **Use Cases:** Rapid prototyping of new app ideas, testing Firebase integrations in isolation, collaborative development sessions.
*   **Limitations:** Workspaces are transient — commit and push code to GitHub before closing. Don't rely on workspace-local storage for persistent work.
