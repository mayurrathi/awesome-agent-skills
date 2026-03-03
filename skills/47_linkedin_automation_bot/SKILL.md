---
name: 47 LinkedIn Automation Bot
description: Specialized instructions for autonomous LinkedIn outbound campaigns—connection requests, DMs, follow-ups—with strict evasion and platform safety rules.
version: 1.0.0
---

# 47 LinkedIn Automation Bot (Evasion Protocol)

This skill dictates how agents should execute programmatic outbound and engagement actions on LinkedIn without getting shadow-banned.

## 1. Engagement & Warm-Up Sequences
* **The "Give Before You Get" Rule:** Before sending a connection request, you MUST like a recent post and comment on it intelligently. Do not send cold requests without prior micro-engagement.
* **Batching Limits:** Never send more than 15 connection requests per 24 hours. Never send more than 30 DMs per 24 hours.
* **Chronological Variance:** Wait at least 4 hours after a connection request is accepted before sending the first DM. Do not send DMs immediately upon acceptance—that trips spam filters.

## 2. Copywriting Evasion Tactics
* **Length:** First messages must be under 3 sentences. No paragraphs.
* **Tone:** Casual, lower-case, conversational. Avoid corporate speak ("I noticed we have mutual synergies in the B2B SaaS space").
* **Structure:** 
    - Line 1: Context (Why you are reaching out).
    - Line 2: The Ask (Low-friction question). 
* **Links:** NEVER include a URL in the first message. Only provide URLs when the prospect explicitly asks for it. Use Loom or Google Doc embeds instead of raw links if possible.

## 3. Rate Handling (HTTP 429)
* If an agent is interacting via MCP or browser automation, it must implement **Exponential Backoff**.
* Treat any `Retry-After` header as absolute law. If a 429 is hit, pause all outbound activity for that profile for at least 6 hours.

## 4. The 3-Step Follow-Up Sequence
1. **Day 0:** Post-acceptance question. "Hey [Name], saw your post on [Topic]. How are you handling [Pain point]?"
2. **Day 3 (Follow up):** Value add. "Found this article/resource that reminded me of what you're doing at [Company]. Hope it's useful!"
3. **Day 7 (Breakup):** "Looks like passing ships right now. Keep up the great work at [Company], I'll be following!"
