---
name: 02 Secure Mass-Market App Deployment
description: Strict security, revenue protection, and compliance standards for the Apple App Store, Google Play Store, and PWAs.
version: 1.0.0
---

# 02 Secure Mass-Market App Deployment

Guidelines to ensure security, compliance, and revenue protection for mobile applications, PWAs, and backend infrastructure.

## 1. Platform Gatekeeping and Compliance
* **Apple App Store:** Map third-party SDK data in Privacy Manifests. Use highly specific purpose strings in `Info.plist`. Implement strict UGC filtering and reporting.
* **Google Play Store:** Enforce Android 15 (API level 35) targeting. Integrate Age Signals API for matchmaking/gambling. Never request disabling Google Play Protect.
* **DMA Compliance:** Accommodate Apple's Notarization security scanning for EU alternative distribution.

## 2. Revenue Security and In-App Purchases (IAP)
* **Zero Client Trust:** Manage sensitive purchase logic and cryptographic verification exclusively on the backend.
* **Google Play Billing:** Transmit `purchaseToken` via TLS. Validate via Google Play Developer API. Grant entitlements only for `PURCHASED` state.
* **Apple App Store:** Implement the App Store Server API (JWS payloads) and Server Notifications V2. Deprecate legacy on-device validation.

## 3. PWA Defenses
* **Service Workers:** Register to narrowest scope. Enforce strict CSP. Use Subresource Integrity (SRI) hashes.
* **Data Persistence:** Never persist JWTs/PII in `localStorage` or `sessionStorage`. Use `IndexedDB` with Web Crypto API application-level encryption.
* **Authentication:** Implement WebAuthn and FIDO2 standards (hardware biometric authenticators).

## 4. Native Hardware Keystores
* **iOS Keychain:** Use Secure Enclave (`.biometryCurrentSet`) to enforce biometric authentication prior to decryption.
* **Android Keystore:** Use Trusted Execution Environment (TEE) with `.setUserAuthenticationRequired(true)`.
* Never export raw private keys into executable memory.

## 5. Backend Infrastructure & Incident Response
* **API Gateways:** Enforce granular rate limiting and payload size limits. Trigger step-up authentication on sequential login failures.
* **Microservices:** Enforce Zero Trust (mTLS) for internal communications. Validate JWTs exclusively at the edge.
* **Response Readiness:** Ensure dependencies can be deployed within 90 days. Maintain capabilities to execute global session invalidation and rapid key revocation.
