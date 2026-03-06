---
name: Connect Automation
description: API integrations for 1,000+ services. "Send an email to the team after this build finishes."
version: 1.0.0
---

# 3.2.2 Connect Automation

Guidelines for automating scripts that bridge multiple platforms (Slack, Gmail, Jira, GitHub, etc.) via APIs.

## 1. Authentication Strategy
- **OAuth 2.0:** Utilize proper secure flows for authenticating against third-party endpoints.
- **API Keys / Webhooks:** Use secure webhook paths for automated triggers (e.g., configuring Stripe webhooks to hit a Next.js API route securely).

## 2. Payload Construction
- **Strict Typing:** Define clear TypeScript interfaces or Pydantic models for incoming and outgoing data structures to prevent runtime crashes.
- **Idempotency:** Ensure that cross-service automation endpoints are idempotent. If an email fails and is retried, do not send duplicates.

## 3. Common Use Cases
- Alerts (Slack/Discord bots on deployment failures).
- Ticketing (Creating Jira or Linear issues based on user feedback inside apps).
- Marketing logic (Syncing user sign-ups to Mailchimp/Customer.io via APIs).
