---
name: Pwa Offline First
description: Service worker lifecycle, caching strategies, install prompts, offline data sync, IndexedDB patterns, Web App Manifest best practices, and Lighthouse scoring targets.
version: 1.0.0
---

# 2.2.2 Pwa Offline First

This skill defines the technical standards for building Progressive Web Apps that work reliably regardless of network conditions, install natively on devices, and pass all Lighthouse PWA audits.

## 1. Web App Manifest (`manifest.json`)
**Goal:** Ensure installability and native-like presentation on all platforms.
*   **Required Fields:** `name`, `short_name`, `start_url`, `display` (set to `standalone`), `background_color`, `theme_color`, `icons` (at minimum 192×192 and 512×512 PNG, include `maskable` purpose variant).
*   **Optional Enhancements:** `description`, `categories`, `screenshots` (for richer install UI on Android), `shortcuts` (app launcher shortcuts), `share_target` (to receive shared content).
*   **Scope:** Set `scope` to `/` or the app's root path. Ensure `start_url` falls within the declared scope.
*   **Validation:** Test with Chrome DevTools → Application → Manifest panel. Verify installability criteria are met.

## 2. Service Worker Lifecycle
**Goal:** Reliable caching and seamless updates without stale content.
*   **Registration:** Register the service worker in the app's entry point with `navigator.serviceWorker.register('/sw.js', { scope: '/' })`. Wrap in a feature check.
*   **Install Event:** Pre-cache the App Shell (HTML, CSS, JS, critical fonts, icons) during the `install` event. Use `cache.addAll()` with a versioned cache name (e.g., `app-shell-v2`).
*   **Activate Event:** Clean up old caches by iterating `caches.keys()` and deleting any cache name that doesn't match the current version. Call `clients.claim()` to immediately take control.
*   **Update Strategy:** Use `skipWaiting()` cautiously. Prefer prompting the user with a "New version available — Refresh" banner triggered by the `controllerchange` event or a Broadcast Channel message from the new SW.

## 3. Caching Strategies
**Goal:** Select the right caching strategy for each resource type.
*   **Cache First (App Shell):** HTML, CSS, JS bundles, fonts, icons. Serve from cache; update cache in background via `fetch` and store the new response for the next load.
*   **Network First (API Data):** Dynamic content, user data, real-time feeds. Try network; fall back to cached response if offline. Set a network timeout (~3 seconds) before falling back.
*   **Stale-While-Revalidate (Semi-Static Assets):** Images, locale files, non-critical JSON configs. Serve cached version immediately; update cache in background.
*   **Network Only:** Authentication endpoints, payment transactions, real-time WebSocket connections. Never cache sensitive operations.
*   **Cache Size Management:** Implement LRU eviction for dynamic caches. Cap at a reasonable entry count (e.g., 50 API responses, 100 images).

## 4. Offline Data Persistence (IndexedDB)
**Goal:** Full offline functionality for data-heavy features.
*   **Database Design:** Use IndexedDB (via `idb` wrapper library for Promise-based API) for structured data. Create object stores with appropriate key paths and indexes.
*   **CRUD Operations:** Implement complete Create, Read, Update, Delete operations with proper transaction handling (`readwrite` for mutations, `readonly` for queries).
*   **Schema Versioning:** Use `onupgradeneeded` to handle database schema migrations. Never delete user data during upgrades — migrate it forward.
*   **Storage Quota:** Check available storage with `navigator.storage.estimate()`. Request persistent storage with `navigator.storage.persist()` if the app holds critical user data.

## 5. Background Sync & Offline Queue
**Goal:** Queue user actions taken offline and replay them when connectivity returns.
*   **Sync Registration:** When a network request fails (e.g., form submission, data save), store the request payload in IndexedDB and register a `sync` event with `registration.sync.register('sync-pending-actions')`.
*   **Sync Handler:** In the service worker's `sync` event listener, read all pending actions from IndexedDB, replay them via `fetch()`, and delete them from the queue on success.
*   **Fallback:** If Background Sync API is not supported, implement a polling-based fallback that checks `navigator.onLine` and processes the queue on `online` events.
*   **Conflict Resolution:** For multi-device sync scenarios, implement last-write-wins or timestamp-based merging logic on the backend.

## 6. Install Prompt Management
**Goal:** Maximize install rates with strategic prompt timing.
*   **Capture the Event:** Listen for `beforeinstallprompt`, prevent default, and store the event reference. Never show the browser's default prompt immediately.
*   **Custom Install UI:** Display a custom install banner or button after the user demonstrates engagement (e.g., 2+ sessions, completed a key action). Use the stored event's `.prompt()` method when the user clicks.
*   **Post-Install:** Listen for `appinstalled` event. Log the conversion. Hide the install prompt permanently. Optionally show a "Welcome to the app!" onboarding flow.
*   **iOS Handling:** Detect iOS Safari via user agent. Show manual "Add to Home Screen" instructions since iOS does not support `beforeinstallprompt`.

## 7. Lighthouse PWA Audit Targets
**Goal:** Every PWA must score 100 on the Lighthouse PWA audit.
*   **Installable:** Valid manifest with required icons, registered service worker, served over HTTPS.
*   **Reliable:** Pages load offline (at least a custom offline fallback page). Response time under 200ms from cache.
*   **Fast:** First Contentful Paint < 1.8s. Largest Contentful Paint < 2.5s. Cumulative Layout Shift < 0.1. Time to Interactive < 3.8s.
*   **Engagement:** Custom splash screen, theme color set, viewport configured, content sized to viewport, no horizontal scroll.
*   **Testing Cadence:** Run Lighthouse in CI on every deploy. Block deploys that drop below target scores.
