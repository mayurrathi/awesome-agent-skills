---
name: 35 Webapp Testing (Playwright)
description: End-to-end visual testing suite. Agents write and execute their own browser tests to verify UI changes.
version: 1.0.0
---

# 35 Webapp Testing (Playwright)

When verifying web UI changes, implement and execute end-to-end tests using Playwright to ensure regressions are caught automatically.

## 1. Test Architecture
- **Location:** Keep E2E tests in a dedicated folder (e.g., `tests/e2e/` or `e2e/`).
- **Isolation:** Each test should set up its own isolated state via fixtures to prevent dependencies between test runs.

## 2. Locators and Interactions
- **User-Centric Locators:** Always prefer testing the UI the way a user interacts with it. Use `getByRole`, `getByText`, or `getByLabel` instead of brittle CSS selectors or XPaths.
- **Awaits:** Trust Playwright's auto-waiting logic. Do not use hardcoded `page.waitForTimeout` unless absolutely necessary for external animations that cannot be hooked.

## 3. Authentication & State
- **Storage State:** For tests requiring login, authenticate once in a global setup and reuse the storage state (cookies/origins) across the test suite to save time.

## 4. Visual Testing (Optional)
- **Snapshots:** Use `expect(page).toHaveScreenshot()` when layout drift needs to be strictly monitored. Ensure these are run in consistent environments (like Docker) to avoid OS-level rendering diffs.
