---
name: Performance Marketing Ops
description: Paid advertising (Meta, Google, LinkedIn), ad creative iteration at scale, analytics tracking, and RevOps automation.
version: 1.0.0
---

# 1.4.3 Performance Marketing Ops

This skill defines the technical execution, scaling, and measurement of the revenue engine.

## 1. Paid Advertising (PPC)
**Goal:** Profitable customer acquisition through paid channels.
*   **Google Ads:** High-intent. Target "Solution" and "Competitor" keywords.
*   **Meta (FB/IG):** Demand gen. Scale using Broad targeting + Lookalikes of High-LTV customers.
*   **LinkedIn:** B2B. Use Job Title and Skill-based targeting for high-ticket offers.
*   **Optimization:** Wait 3-5 days after any major change for the platform's algorithm to re-learn.

## 2. Ad Creative Strategy
**Goal:** Beat "Ad Fatigue" through constant iteration.
*   **Angles:** Test Pain, Outcome, Social Proof, and Curiosity.
*   **Specs:** Always enforce character limits (Google RSA: 30 char headlines).
*   **Testing:** Change only one variable (Hook, Visual, or CTA) per test cycle. Use the **ab-test-setup** skill for rigor.

## 3. Analytics & Tracking
**Goal:** Data-driven decisions, not just data collection.
*   **Naming:** Use Object-Action format (e.g., `signup_completed`).
*   **Plan:** Document every event, its trigger, and the decision it informs (Skill 13).
*   **Privacy:** Implement cookie consent and ensure no PII (Personally Identifiable Information) leaks into GA4/Mixpanel.

## 4. RevOps & Lead Lifecycle
**Goal:** Frictionless flow from visitor to customer.
*   **Scoring:** Weight Fit (Who they are) and Engagement (What they do).
*   **Routing:** Round-robin or Territory-based rules ensure every lead has an owner (Skill 17).
*   **Single Source of Truth:** Sync every touchpoint to a central CRM as the canonical record.

## 5. Reporting & Attribution
*   **Attribution:** Look at "Blended CAC" across all channels, not just platform CPA.
*   **Dashboarding:** Build 3 views: Marketing (Volume), Sales (Pipeline), and Executive (ROI/LTV).
