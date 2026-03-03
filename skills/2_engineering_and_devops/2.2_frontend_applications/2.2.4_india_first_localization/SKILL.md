---
name: 2.2.4 India First Localization
description: Hindi/regional language support, low-bandwidth optimization, UPI payment flows, regional content patterns, and Tier 2/3 city user behavior for the Indian market.
version: 1.0.0
---

# 2.2.4 India First Localization

This skill defines the technical and UX standards for building applications optimized for the Indian market — the world's largest smartphone user base with unique connectivity, language, payment, and cultural considerations.

## 1. Multi-Language Architecture
**Goal:** Full Hindi and regional language support without code duplication.
*   **i18n File Structure:** Create locale JSON files per language: `locales/en.json`, `locales/hi.json`, `locales/mr.json`, etc. Keys are semantic identifiers (`"game.start"`, `"nav.home"`), values are translated strings.
*   **Runtime Switching:** Implement language toggling via UI buttons (not a buried settings menu). Store the preference in `localStorage` as `lang`. Apply immediately without page reload by re-rendering string-dependent components.
*   **Font Support:** Load Noto Sans Devanagari (or equivalent) for Hindi/Marathi/Sanskrit scripts. Use `unicode-range` in `@font-face` to avoid loading Devanagari glyphs for English-only users.
*   **Text Expansion:** Hindi text is typically 20–40% longer than English equivalents. Design UI with flexible containers. Never use fixed-width text elements. Test all layouts in Hindi before shipping.
*   **Pluralization & Gender:** Hindi has different plural forms and gendered nouns. Use ICU MessageFormat or a library like `intl-messageformat` for proper pluralization and gender agreement.

## 2. Low-Bandwidth & Offline Optimization
**Goal:** Full functionality on 2G/3G connections and in spotty coverage areas.
*   **Bundle Size Budget:** Target < 200KB initial JS bundle (gzipped). Use code-splitting with dynamic `import()` for non-critical features. Lazy-load images and heavy components.
*   **Image Strategy:** Use WebP format with aggressive compression (quality 60–70). Serve responsive images via `srcset` with appropriate sizes for mobile screens (rarely > 400px width). Implement blur-up placeholders.
*   **API Responses:** Minimize JSON payload sizes. Use field masks / selection (Firestore's `select()`) to fetch only required fields. Paginate all list endpoints.
*   **Offline Core:** The app's primary utility must work fully offline (Skill 05). Cache critical data in IndexedDB on first load. Show meaningful content even with no network.
*   **Network Detection:** Use `navigator.connection.effectiveType` to detect `2g`/`3g` and adapt: disable auto-play media, reduce image quality, defer non-essential network requests.

## 3. UPI & Indian Payment Flows
**Goal:** Support India's dominant payment infrastructure.
*   **UPI Deep Links:** For simple payments, generate UPI intent URLs: `upi://pay?pa=<vpa>&pn=<name>&am=<amount>&cu=INR&tn=<note>`. Open via `window.location.href` or an `<a>` tag on mobile.
*   **QR Code Generation:** Use a client-side library (e.g., `qrcode.js`) to render UPI payment QR codes dynamically. Encode the same UPI URL into the QR payload.
*   **Payment Verification:** UPI payments are asynchronous. Implement a server-side webhook or polling mechanism to verify payment status via the payment gateway's API. Never trust client-side payment confirmation.
*   **Razorpay/Cashfree Integration:** For subscription or recurring payments, integrate with a local payment gateway. Both support UPI, cards, wallets, and net banking with battle-tested SDKs.
*   **₹ Formatting:** Always display currency in Indian format: `₹1,00,000` (lakh grouping), not `₹100,000`. Use `Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR' })`.

## 4. Regional Content Patterns
**Goal:** Design content and interactions that resonate with Indian users.
*   **Visual Language:** Use culturally relevant iconography and illustrations. Avoid Western-centric metaphors (mailbox for email, etc.). Prefer universally understood symbols or India-specific visuals.
*   **Festivals & Seasons:** Implement seasonal theming (Diwali, Holi, Navratri, Eid) with dynamic CSS theme overrides. Schedule theme changes via date-based logic. This drives engagement and sharing.
*   **Local Units:** Support local measurement units where relevant (bigha, guntha for land; quintal for weight). Provide conversion between local and metric.
*   **WhatsApp as Primary Share Channel:** In India, WhatsApp is the dominant sharing platform. Prioritize WhatsApp share buttons. Format shared content for WhatsApp's text+image preview (message + URL with OG tags).
*   **Voice & Vernacular Input:** Consider voice input support for Hindi and regional languages using Web Speech API. Many Tier 2/3 users prefer voice over typing.

## 5. Tier 2/3 City User Behavior
**Goal:** Design for the next billion users, not Silicon Valley power users.
*   **Affordability Sensitivity:** Price points must be India-appropriate. ₹49–99/month is the sweet spot for subscriptions. Offer weekly plans. Free tiers must be generous.
*   **Storage Constraints:** Users frequently clear app data to free space. Persist critical user data in the cloud (not just locally). Implement seamless data restoration on re-install via anonymous auth → account linking.
*   **Screen Size:** Design for 5"–6.5" screens. Touch targets minimum 48px. Avoid dense information layouts. Use bottom navigation (reachable with one thumb).
*   **Digital Literacy:** Don't assume familiarity with common UI patterns (hamburger menus, swipe gestures). Use explicit labels, onboarding tooltips, and visual cues. Prefer button-based language selection over dropdown menus.
*   **Data Saver Mode:** Detect Android's Data Saver mode via `navigator.connection.saveData`. Automatically reduce data usage: lower image quality, disable prefetching, pause background sync.
