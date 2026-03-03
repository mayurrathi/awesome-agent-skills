---
name: 03 Growth Engineering & Technical Marketing
description: Technical architecture, logic flows, and metadata strategies for built-in marketing, viral loops, and ASO/SEO optimization for App Store, Google Play, and PWAs.
version: 1.0.0
---

# 03 Growth Engineering & Technical Marketing

As a Principal Growth Engineer and Technical ASO/SEO Expert, this skill defines the programmable growth loops, technical marketing architecture, and algorithmic store optimizations necessary strictly within the app's codebase and store consoles. External marketing strategies (like social media posting) are excluded.

## 1. Frictionless Onboarding (The 30-Second Rule)
**Goal:** Delay forced account creation until the user experiences the app's core value.
*   **Logic:** Implement Anonymous Authentication (e.g., Firebase Auth `signInAnonymously()`) silently on the first launch. 
*   **Flow:** Route the user directly to the core utility (the game board, the tool). Persist their progress, generated assets, or high scores locally via `IndexedDB` or tied to the anonymous UID in the cloud.
*   **Conversion Trigger:** Only after a high-value action (e.g., winning a game, creating 3 reports), trigger a soft "Save Your Progress" or "Sync to Cloud" modal that links their anonymous account to a permanent OAuth/Email provider (`linkWithCredential()`).

## 2. Double-Sided Referral Logic
**Goal:** Instantly reward both the sender and the receiver when a referral code is used.
*   **Database Schema:** A `Referrals` table mapping: `ReceiverID`, `SenderID`, `ReferralCode`, `Status` (pending/completed).
*   **Backend Flow:** User A shares a Deep Link (e.g., `app.domain.com/invite/XYZ`). User B installs and opens the app. The app parses the deep link parameter on launch and writes a `pending` referral record.
*   **Reward Trigger:** Do not reward strictly on install (prevents bot abuse). Reward on the *First Milestone*. When User B completes a specific action (e.g., plays 1 full game), a Cloud Function transactionally credits User A's wallet and User B's wallet simultaneously, updating the `Referrals` status to `completed`.

## 3. Feature Gating (Invite Lock)
**Goal:** Lock specific desirable tools until the user successfully invites one friend.
*   **State Management:** Maintain a `user.unlockedFeatures` array in the user's database document.
*   **Logic:** A premium UI element (e.g., a "Multiplayer Mode" button) is conditionally wrapped in a `<GatedFeature requires="invite_1">` component. If locked, it renders a padlock overlay.
*   **Unlock Flow:** Clicking the padlock invokes the native `navigator.share()` API with the user's deep link. The lock remains until the backend verifies a successful double-sided referral (from Step 2). Once verified, the backend emits a real-time event (e.g., via Firestore listener) updating the client state, instantly dissolving the padlock.

## 4. Dynamic Shareable Assets
**Goal:** Dynamically generate personalized, visually appealing progress summaries perfectly sized for native sharing to Instagram Stories or TikTok.
*   **Technical Approach:** Use HTML5 `<canvas>` or a library like `html2canvas` to render off-screen UI components.
*   **Formatting:** Hardcode the canvas to optimal vertical video dimensions (1080x1920). Draw the user's avatar, stats, customized app branding, and a QR code (linking to their unique referral tracking link) onto the canvas.
*   **Execution:** Convert the canvas to a Blob (`canvas.toBlob()`), wrap it in a `File` object, and pass it to the Web Share API (`navigator.share({ files: [shareFile] })`). This natively invokes the OS share sheet with the generated image pre-attached, removing friction for the user.

## 5. Technical LLM SEO & ASO
**Goal:** Structure PWA HTML tags and Store descriptions to rank for conversational AI queries (ChatGPT, Gemini) and high-intent, long-tail keywords.
*   **PWA HTML:** Use semantic HTML5 `<article>`, `<section>`, and explicit Schema.org JSON-LD microdata (`SoftwareApplication`, `Game`) in the `<head>` of `index.html`. This ensures LLMs can easily parse the app's utility and capabilities.
*   **Store Descriptions:** Ditch traditional marketing fluff. Structure descriptions as natural-language Q&A formats ("What is [App Name]?", "How does [App] solve [Problem]?") targeting long-tail, high-intent queries. Use exact matchmaking for phrases users speak to voice assistants.

## 6. Contextual Store Listings
**Goal:** Set up custom store listings to match the exact demographic or entry point of the user.
*   **Google Play (Custom Store Listings):** Create varying store listings targeting specific URL parameters (from ad campaigns) or countries. If a user clicks an ad for a specific niche use-case, they must land on a CSL with screenshots and copy *exclusively* highlighting that use-case.
*   **Apple App Store (Custom Product Pages):** Utilize CPPs to create up to 35 different variations of the App Store page. Tie the `apple_id=...` parameters to specific entry points to ensure the promo text and visuals align perfectly with the user's implicit intent.

## 7. Event-Based Rating Prompts
**Goal:** Fire native review APIs strictly after a successful, positive action.
*   **Trigger Logic:** Track user milestones locally in `localStorage` or `IndexedDB` (e.g., `valuable_actions_completed = X`). *Never* ask on app launch, and *never* ask after a crash or user failure state.
*   **Execution:** Immediately after a peak satisfaction event (e.g., claiming a prize, hitting a streak, exporting a successful file), invoke the native rating API (`SKStoreReviewController.requestReview()` on iOS, `ReviewManager` on Android, or Capacitor's `App.requestReview()`). Set a local flag (`has_been_prompted = true`) to ensure this is suppressed for at least 3-6 months if dismissed.

## 8. Behavioral Push Notifications
**Goal:** Track user behavior events and trigger contextual nudges instead of generic broadcast messages.
*   **Architecture:** Avoid generic CRON jobs. Build an event-driven architecture using Firebase Cloud Messaging (FCM) or OneSignal triggered by backend Cloud Functions.
*   **Logic:** When a user completes an action, log an event (`Event: User Played Level 1`). A background worker calculates their expected return time based on cohort velocity. If the user does not return within that window, a Cloud Task triggers a highly contextual nudge referencing their exact state: *"Your winning streak is fading, come back to claim your daily tokens!"* rather than *"Play our game today."*
