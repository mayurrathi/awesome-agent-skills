---
name: Skill Orchestrator
description: The master meta-skill for sequencing and prioritizing other skills during a project lifecycle. Defines the exact order: Planning -> Development -> SEO -> Security -> Marketing.
version: 1.0.0
---

# 3.1.3 Skill Orchestrator

This is the **Master Sequencer** skill. When a user asks you to build, launch, or scale a complete application or business, you MUST apply other skills in this strict, sequential order. Never jump to SEO or Marketing before Development is complete. Never jump to Development before Planning is approved.

## Phase 1: Planning & Architecture (Highest Priority)
**Rules:** Always start here. Do not write a single line of code until these skills are executed.
1.  **Ideation & Strategy:** Apply `simple-brainstorm` or `1.5.1 Growth And Strategy` to define the *what* and *why*.
2.  **Product Requirements & UI/UX:** Apply `2.1.1 End To End App Development` (Phases 1-4) to establish the PRD, research document, and design system.
3.  **Design Tokens:** Apply `2.1.3 Web Dev Design Systems` to lock in colors, fonts, and grid spacing.

## Phase 2: Core Development (Execution)
**Rules:** Only proceed to this phase once the user approves the Phase 1 plan. Focus strictly on building a functional, premium MVP.
1.  **Scaffolding & Architecture:** Apply `2.1.2 Project Scaffolding` and `2.1.1 End To End App Development` (Phase 5-7) to initialize the codebase.
2.  **Frontend & Logic:** Apply `2.2.1 Vercel React Best Practices` and `2.2.2 Pwa Offline First` to build the client-side app.
3.  **Backend (if required):** Apply `2.3.1 Firebase Baas` or `2.3.2 Supabase Skills` for databases and auth.

## Phase 3: Optimization (SEO & UX Polish)
**Rules:** Only apply these skills on a *working* application. Do not optimize broken code.
1.  **Technical SEO:** Apply `1.2.1 Seo Site Architecture` and `1.2.2 Omni Seo Dominance` to set up `robots.txt`, `sitemap.xml`, Open Graph tags, and JSON-LD schemas.
2.  **Copywriting:** Apply `1.3.1 Conversion Copywriting` to refine the landing page text and CTA buttons.

## Phase 4: QA & Security (Pre-Launch)
**Rules:** The app must be fully optimized before auditing.
1.  **Security Audit:** Apply `2.5.1 Trail Of Bits Security` to harden the app against XSS, SQLi, and exposed `.env` variables.
2.  **Automated Testing:** Apply `2.5.2 Webapp Testing Playwright` to write end-to-end user flows.
3.  **Deployment:** Apply `2.4.1 Cicd Git Deployment` and `2.4.3 Git Commit Formatter` to push live safely.

## Phase 5: Marketing & Growth (Post-Launch)
**Rules:** Only apply these marketing skills once the production URL is fully live, secure, and SEO-optimized.
1.  **Social Amplification:** Apply `1.1.1 Linkedin Mastery`, `1.1.2 Profile Optimizer`, and `1.1.3 Content Creator` to build an audience.
2.  **Launch Campaigns:** Apply `1.4.1 Content Product Launches` for Product Hunt and community drops.
3.  **Retention:** Apply `1.5.2 Retention Referral` to build virality loops.

**Execution Prompt for the Agent:**
"I am invoking the `3.1.3 Skill Orchestrator`. Based on the user's current project state, identify exactly which Phase (1-5) we are in, and suggest the next 2 specific sub-skills we must apply."
