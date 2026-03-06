---
name: Linkedin Mastery
description: Expert strategies for LinkedIn profile optimization, high-performance content generation, networking, and personal branding for B2B growth and career acceleration.
version: 1.0.0
---

# 1.1.1 Linkedin Mastery

This skill provides a systematic framework for building authority and driving growth on LinkedIn using autonomous, goal-oriented agentic systems.

## 1. The Architectural Paradigm (Skills vs. MCP)
Modern LinkedIn automation shifts from passive generation to active "Performative AI".
* **Localized Skills (SKILL.md):** Portable, token-efficient (30-50 tokens), best for content generation and local document workflows (e.g., `~/.claude/skills/`).
* **Model Context Protocol (MCP):** Requires server initialization. Provides direct, authenticated access to LinkedIn APIs for robust browser automation, URN management, and database state.
* **Agentic Guardrails:** Use `FOUNDER_CONTEXT.md` for voice calibration and "NEVER say" lists for compliance (SEC/Legal).

## 2. Advanced Content & Algorithmic Virality
* **The "First Hour" Rule:** Mandate responses to all comments within 60 minutes. Use follow-up questions to extend threads and signal relevance to the platform.
* **1,300-Character Optimization:** Keep total length before the "See More" truncation. High mobile readability through line breaks and icon-led benefit sections.
* **Vertical Tone Mapping:**
    - **US Market:** Direct, assertive, benefit-driven.
    - **DACH Region:** Factual, objective, data-heavy.
    - **Asia:** Formal, respectful, consensus-oriented.
* **Hook Frameworks:** Avoid "Humble Brags". Deploy "Lessons Learned", "Blueprint", "Case Study", and "Hot Take" (contrarian) templates.

## 3. Autonomous Outbound Orchestration (MCP)
* **Full-Stack Execution:** Use tools like Composio/Rube for programmatic posting.
* **Multimodal Workflows:**
    1. Register image/video to receive target URL.
    2. Upload binary payload to URL.
    3. Extract Asset URN (e.g., `urn:li:digitalmediaAsset:...`).
    4. Construct JSON payload with URN formatting.
* **Platform Survival:** Implement **Exponential Backoff** for HTTP 429 (Too Many Requests). Respect `Retry-After` headers to avoid shadow-bans.

## 4. Human Simulation & Evasion Protocols
To survive adversarial platform dynamics, agents must be "intentionally inefficient":
* **Chronological Variance Sequence:**
    - **Day 1:** Profile View (Simulation of research).
    - **Day 1-2:** Like recent post (Micro-engagement).
    - **Day 2-3:** Connection Request (Asynchronous wait for acceptance).
    - **T+4h to 24h:** First DM (Post-acceptance delay).
* **Copywriting Evasion:** Stay <1 paragraph (3-4 sentences). Prioritize conversational questions. Use Loom embeds rather than raw links to bypass spam filters.

## 5. Profile & Career Engine Optimization (ATS)
* **The Executive Bullet Formula:** `[Leadership Action] + [Strategic Initiative] + [Business Outcome]`.
* **ATS Triage:** Compute a 70/30 weighted match (70% must-have skills, 30% preferred) against target Job Descriptions.
* **Profile Architecture:**
    - **Banner:** High-impact UVP.
    - **Headline:** Shift from Title to Outcome (e.g., "Helping [Niche] achieve [Result]").
    - **Featured:** Pin Lead Magnets and Proof-of-Work.

## 6. Multi-Platform Ad Infrastructure & CI/CD
* **Parallel Ad Audits:** Deploy subagents to simultaneously assess LinkedIn Ads (B2B targeting), Meta, and Google Ads for creative fatigue and budget velocity.
* **Event-Driven PR Pipelines:** Automate LinkedIn milestone broadcasts triggered by local development events (e.g., code pushes, documentation completion parsed from `docs/` directory).

## 7. The Agentic Skill Registry
A curated list of high-performance LinkedIn skills. Install via `npx` or `playbooks`.

| Category | Skill Name | Repository / Source | Installation Command |
| :--- | :--- | :--- | :--- |
| **Content** | `linkedin-content` | `inference-sh/skills` | `npx skills add inference-sh/skills` |
| **Content** | `writing-linkedin-posts` | `jamesgray007/hoai-course` | `npx skills add jamesgray007/hoai-course` |
| **Branding** | `linkedin-authority` | `brianrwagner/ai-marketing` | `npx playbooks add skill brw-linkedin-authority-builder` |
| **Optimization** | `profile-optimizer` | `paramchoudhary/resumeskills`| `npx skills add paramchoudhary/resumeskills` |
| **Automation** | `linkedin-automation` | `composiohq/awesome-claude` | `npx skills add composiohq/awesome-claude-skills` |
| **Sales** | `sales-navigator-alt`| `onewave-ai/claude-skills` | `npx skills add onewave-ai/claude-skills` |
| **Evasion** | `limits-warmup` | `sachacoldiq/coldiq-s-gtm` | `npx skills add sachacoldiq/coldiq-s-gtm-skills` |
| **Utility** | `campaign-complete`| `sachacoldiq/coldiq-s-gtm` | `npx skills add sachacoldiq/coldiq-s-gtm-skills` |
| **Utility** | `linkedin-navigation`| `bennoloeffler/maude-vunds` | `npx skills add bennoloeffler/maude-claude-vunds-plugins` |
| **Ads/Audit** | `ads-linkedin` | `agricidaniel/claude-ads` | `npx skills add agricidaniel/claude-ads@linkedin-ads` |
| **PR/Events** | `announcement-gen` | `nicepkg/ai-workflow` | `npx -y @lobehub/market-cli skills install nicepkg-ai-workflow-linkedin-announcement-generator` |
| **PR/Events** | `project-post` | `alfredang/skills` | `npx skills add alfredang/skills` |
| **Comedy/Audit**| `linkedin-roast` | `schwepps/skills` | `npx skills add schwepps/skills` |

## 8. Guidelines for AI Writing
Strictly avoid "AI-sounding" buzzwords ("Unlock potential", "In today's fast-paced world").
* **Style:** Think-out-loud, one sentence per line, strong finishing thought.
