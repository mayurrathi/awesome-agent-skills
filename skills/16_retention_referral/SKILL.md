---
name: 16 Retention & Referral Programs
description: Churn prevention (voluntary and involuntary), referral loops, affiliate program design, and product-led growth.
version: 1.0.0
---

# 16 Retention & Referral Programs

This skill defines the frameworks for keeping customers longer and turning them into acquisition engines.

## 1. Churn Prevention (Voluntary)
**Goal:** Rescue customers at the moment of cancellation.
*   **Cancel Flow:** Trigger → Exit Survey (Reason) → Dynamic Save Offer → Confirmation.
*   **Reason-Offer Mapping:**
    *   Price → Discount or Downgrade.
    *   Low Usage → Pause subscription (1-3 months).
    *   Missing Feature → Roadmap preview or Support intro.
*   **Dark Patterns:** Avoid them. Keep the "Cancel" option clear to maintain brand trust.

## 2. Dunning & Involuntary Churn
**Goal:** Recover failed payments automatically.
*   **Retry Logic:** Use "Smart Retries" (e.g., Stripe) to attempt charges on success-prone days.
*   **Communication:** 3-4 plain-text emails over 10 days escalating in urgency. Provide a "no-login" link to update payment info.
*   **In-App Alerts:** Display a persistent banner for accounts with past-due payments.

## 3. Referral Program Design
**Goal:** Engineering viral loops within the product.
*   **The Loop:** Trigger Moment (Aha moment) → Share Action → Convert Friend → Reward.
*   **Incentive Structure:** Double-sided rewards (Referrer gets X, Friend gets Y) are the most effective.
*   **Milestones:** Use tiered rewards (e.g., "Refer 5 friends for a t-shirt") to encourage repeat sharing.

## 4. Affiliate & Partner Programs
**Goal:** Scale reach through external advocates.
*   **Recruitment:** Focus on creators whose audience matches your Target Persona (Skill 14).
*   **Commissions:** Use recurring percentage-based commissions for SaaS to align long-term incentives.
*   **Enablement:** Provide affiliates with pre-made banners, email swipes, and "Vs" pages (Skill 17).

## 5. User Health Scoring
*   **Metrics:** Track login frequency, key feature usage, and support sentiment.
*   **Intervention:** For users with dropping health scores, trigger proactive outreach or re-engagement drip sequences.
