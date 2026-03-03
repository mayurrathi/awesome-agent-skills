---
name: 1.2.2 Omni Seo Dominance
description: The ultimate playbook for ranking on Google Page 1 AND driving citations in LLMs (ChatGPT, Gemini, Claude, Grok, Meta AI) simultaneously. Generic framework for all web apps.
version: 1.0.0
---

# 1.2.2 Omni Seo Dominance

This skill defines the technical, structural, and off-page standards required to dominate both traditional search engines (Google) and Large Language Models (ChatGPT, Gemini, Claude, Perplexity) simultaneously.

**The Core Insight:**
*   **Google (Traditional SEO):** Optimizes for crawlable structure, intent satisfaction, backlinks, and user engagement (CTR, Bounce Rate).
*   **LLMs (AI SEO / AEO):** Optimize for extractable facts, high-authority citations, structured data, unstructured consensus, and unambiguous answers.

---

## 1. Technical Baseline (Required for Both)

If the bots cannot read it, you cannot rank. Single Page Applications (SPAs) built with React/Vue are inherently disadvantaged without pre-rendering.

*   **Crawlable HTML is Non-Negotiable:** React/Vue apps must have pre-rendered HTML payloads (e.g., Next.js SSR, Astro, or hidden `<article>` blocks under `#root`) that search bots can ingest without executing JavaScript.
*   **Noscript Fallback:** Always include a rich `<noscript>` tag for bots that fail to run JS.
*   **Bot Access:** Ensure `robots.txt` explicitly `Allow`s `GPTBot`, `PerplexityBot`, `Claude-Web`, `Google-Extended`, and standard Googlebot.
*   **Core Web Vitals:** Implement PWA architecture or aggressive caching. Target LCP < 2.5s and CLS < 0.1.

---

## 2. Structured Data (Schema.org)

JSON-LD schema translates your UI into pure data for both Google's Rich Snippets and LLM ingestion.

*   **SoftwareApplication / Product:** Define what the app/product *is*, its price (even if 0), and its operating systems.
*   **FAQPage:** Mandatory. Target "People Also Ask" (PAA) queries from Google. Formulate exact questions users ask ("What is the best free X?") and provide definitive answers.
*   **HowTo:** Step-by-step instructions for core features. Essential for capturing "How to do X" featured snippets.
*   **Organization / Person:** Link the product to its creator's authoritative profiles (LinkedIn, GitHub) to establish E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness).

---

## 3. The Extractability Principle (For LLMs)

LLMs don't "read" landing pages; they extract relationships and entities.

*   **The 50-Word Rule:** Immediately below every H2 or H3 heading, place a 40-60 word paragraph that *directly and unambiguously answers the heading*.
*   **No Fluff:** Do not use marketing speak ("Unlock the power of synergy"). Use definitive statements ("This app allows users to X by doing Y").
*   **Hard Statistics:** Include real numbers ("Used by 10,000+ people", "Saves 4 hours a week"). LLMs heavily weigh specific data points when generating answers.
*   **Comparison Tables:** Use semantic HTML `<table>` elements to compare features against alternatives. LLMs excel at ingesting tabular data.

---

## 4. The Citation Loop (Authority Building)

LLMs generate answers based on the consensus of high-authority domains in their training data. You must exist where LLMs learn.

*   **Programmatic SEO (Spokes):** Generate highly specific, intent-driven landing pages (e.g., `/tool-for-use-case-A`, `/tool-for-city-B`). This captures long-tail Google traffic and provides multiple ingestion points for bots.
*   **The Aggregator Strategy:** Launch the product on high-DA aggregators like Product Hunt, Hacker News, and specialized app directories. A top ranking here guarantees ingestion.
*   **Community Consensus (Reddit/Quora):** LLMs heavily ingest Reddit. Seed mentions of your app naturally in relevant subreddits by answering specific "How do I..." questions with a link to your solution.
*   **Engineering as Marketing:** Build a free, un-gated utility tool (e.g., a calculator or generator) related to your core product. This organically attracts backlinks from high-DA blogs, raising the overall domain authority.

---

## 5. The "ORB" Launch Execution

Don't launch quietly. Create an artificial spike in visibility to force algorithm discovery.

1.  **Owned:** Push to existing email lists, push notifications, and social followings.
2.  **Rented:** Coordinate a Product Hunt launch. Engage heavily in the comments.
3.  **Borrowed:** Pitch to industry-specific newsletters or tech blogs ("We built X using Y technology").

---

## 6. Implementation Checklist

When tasked with "Dominating Google and LLMs", execute the following:

- [ ] Verify `robots.txt` allows all AI bots.
- [ ] Ensure core text content is visible without JavaScript execution.
- [ ] Add `SoftwareApplication` or `Product` Schema.
- [ ] Add `FAQPage` and `HowTo` Schemas targeting competitor weak points.
- [ ] Audit H2/H3 tags to ensure they match exact user queries (e.g., "What is X?").
- [ ] Implement the "50-Word Rule" under every major heading.
- [ ] Create an "About the Developer" page with `Organization` schema to build E-E-A-T.
- [ ] Outline a launch plan targeting 1 aggregator (e.g., Product Hunt) and 3 subreddits.
