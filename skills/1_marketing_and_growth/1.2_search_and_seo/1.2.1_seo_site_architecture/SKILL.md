---
name: 1.2.1 Seo Site Architecture
description: SEO-driven site architecture, programmatic SEO, schema markup, AI SEO indexing, and technical SEO audits.
version: 1.0.0
---

# 1.2.1 Seo Site Architecture

This skill defines the technical and structural standards for making websites discoverable by both traditional (Google) and AI-based (ChatGPT, Perplexity) search engines.

## 1. Site Architecture (Information Architecture)
**Goal:** Create a logical, crawlable hierarchy.
*   **3-Click Rule:** Users (and bots) should reach any important page within 3 clicks of the homepage.
*   **URL Structure:** Use readable, hyphen-separated URLs (e.g., `/features/analytics`). Avoid dates or IDs in URLs.
*   **Internal Linking:** Use descriptive anchor text. Every page must have at least one inbound internal link (no orphan pages). Implement breadcrumbs for deep hierarchy.

## 2. On-Page & Technical SEO
**Goal:** Ensure pages are optimized for ranking and performance.
*   **Meta Elements:** Unique Title Tags (50-60 chars) and Meta Descriptions (150-160 chars) with primary keywords.
*   **Heading Hierarchy:** Single H1 per page, followed by logical H2/H3 structure. Use headings to answer intent, not just for styling.
*   **Performance:** Optimize for Core Web Vitals (LCP < 2.5s, CLS < 0.1). Use lazy-loading for images and modern formats (WebP).
*   **Sitemaps & Robots:** Maintain a clean `sitemap.xml` and ensure `robots.txt` is not blocking critical assets.

## 3. Structured Data (Schema Markup)
**Goal:** Help bots understand content via JSON-LD.
*   **Core Schemas:** Implement `Organization`, `WebSite`, `Product`, `SoftwareApplication`, and `Article` where relevant.
*   **Rich Result Schemas:** Use `FAQPage` and `HowTo` to capture more SERP real estate.
*   **Validation:** Always validate markup using Google's Rich Results Test tool.

## 4. AI SEO (AEO / GEO)
**Goal:** Optimize for AI-citations and Large Language Models.
*   **Extractability:** Use self-contained answer blocks (40-60 words) immediately following H2/H3 headings.
*   **Authority Signals:** Include specific statistics, expert quotes, and "Last Updated" dates to increase citation-trust.
*   **Bot Access:** Ensure `robots.txt` allows `GPTBot`, `PerplexityBot`, and `Google-Extended` for citations.

## 5. Programmatic SEO (pSEO)
**Goal:** Scale SEO-driven pages using templates and data.
*   **Unique Value:** Every generated page must provide unique value (e.g., specific data/analysis), not just swapped variables in a template.
*   **Playbooks:** Use patterns like "[Product] for [Audience]" (e.g., "CRM for Real Estate") or "[Product A] vs [Product B]" (e.g., "Slack vs Teams").
*   **Scalability:** Use a Hub-and-Spoke model to link many "spoke" pages back to a primary "hub" category.
