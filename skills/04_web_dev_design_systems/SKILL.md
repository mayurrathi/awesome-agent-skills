---
name: 04 Web Development & Design Systems
description: Premium UI/UX standards including design tokens, responsive layouts, dark mode, micro-animations, typography, accessibility, and component architecture for all web projects.
version: 1.0.0
---

# 04 Web Development & Design Systems

This skill defines the mandatory visual and architectural standards for every web-facing project. Every screen, component, and interaction must feel premium and state-of-the-art.

## 1. Design Token Architecture
**Goal:** Maintain a single source of truth for all visual properties.
*   **CSS Custom Properties:** Define all colors, spacing, typography, shadows, border-radii, and animation durations as CSS custom properties in a root `:root` block.
*   **Semantic Naming:** Use semantic token names (`--color-surface-primary`, `--spacing-md`, `--shadow-elevated`) rather than raw values (`#1a1a2e`, `16px`).
*   **Dark Mode:** Implement a complete dark palette using `[data-theme="dark"]` or `@media (prefers-color-scheme: dark)` selector overrides on the same token names. Never hardcode light-only colors.

## 2. Color & Visual Identity
**Goal:** Every project must have a curated, harmonious color palette.
*   **Palette Construction:** Use HSL-based color systems. Define a primary hue, then derive accent, surface, and semantic colors (success, warning, error, info) mathematically.
*   **Gradients:** Use multi-stop linear or radial gradients for hero sections, cards, and CTAs. Avoid flat, single-color backgrounds on major surfaces.
*   **Glassmorphism:** Apply `backdrop-filter: blur()` with semi-transparent backgrounds on overlay elements (modals, floating cards, navigation). Always include a fallback for browsers without support.
*   **Contrast Ratios:** Enforce WCAG 2.1 AA minimum (4.5:1 for body text, 3:1 for large text). Use tools like `color-contrast()` or manual checks.

## 3. Typography System
**Goal:** Professional, readable typography that scales across devices.
*   **Font Stack:** Load a primary font from Google Fonts (Inter, Outfit, Roboto, or Poppins) via `<link>` with `display=swap`. Define a monospace font for code (JetBrains Mono, Fira Code).
*   **Type Scale:** Use a modular scale (1.25 ratio recommended). Define `--font-size-xs` through `--font-size-4xl` as tokens. Use `clamp()` for fluid typography on headings.
*   **Line Height & Letter Spacing:** Body text: `1.5–1.6` line-height. Headings: `1.1–1.3`. Add subtle negative letter-spacing on large headings (`-0.02em`).

## 4. Responsive Layout Architecture
**Goal:** Every layout must be mobile-first and fluid.
*   **Breakpoints:** Define standard breakpoints as tokens: `--bp-sm: 640px`, `--bp-md: 768px`, `--bp-lg: 1024px`, `--bp-xl: 1280px`.
*   **Grid System:** Use CSS Grid for page-level layouts. Use Flexbox for component-level alignment. Avoid fixed pixel widths on containers.
*   **Container Queries:** Use `@container` queries for truly modular, context-aware components where browser support allows.
*   **Touch Targets:** All interactive elements must have a minimum of `44px × 44px` touch target area on mobile (Apple HIG / Material Design standard).

## 5. Micro-Animations & Transitions
**Goal:** Interfaces must feel alive and responsive to user interaction.
*   **Hover Effects:** Every clickable element must have a defined `:hover` and `:active` state. Use `transform: scale()`, `box-shadow` changes, or color transitions.
*   **Page Transitions:** Animate route changes with fade-in/slide-up using CSS `@keyframes` or `View Transitions API`.
*   **Loading States:** Use skeleton screens (pulsing placeholder shapes) instead of spinners for content loading. Implement shimmer animations with CSS gradients.
*   **Performance:** Use `transform` and `opacity` for animations (GPU-composited). Never animate `width`, `height`, `top`, or `left`. Respect `prefers-reduced-motion` media query.

## 6. Component Architecture
**Goal:** Build reusable, self-contained UI components.
*   **Naming Convention:** Use BEM-style naming for CSS classes (`block__element--modifier`) or scoped component styles.
*   **Composition:** Components should accept props/attributes for variants (size, color, state) rather than creating separate components for each variation.
*   **Slots & Projection:** Design components with content slots so they can wrap arbitrary children.
*   **State Management:** Visual state (hover, focus, disabled, loading, error) must be visually distinct and programmatically accessible via `aria-*` attributes.

## 7. Accessibility (WCAG 2.1 AA)
**Goal:** Every project must be usable by everyone.
*   **Semantic HTML:** Use `<button>` for actions, `<a>` for navigation, `<nav>`, `<main>`, `<section>`, `<article>` for structure. Never use `<div>` with click handlers.
*   **Focus Management:** Visible focus rings on all interactive elements (`:focus-visible`). Logical tab order. Focus trapping in modals.
*   **ARIA Labels:** All icon-only buttons must have `aria-label`. Dynamic content updates must use `aria-live` regions. Form inputs must have associated `<label>` elements.
*   **Keyboard Navigation:** Full keyboard operability for all interactive features. `Escape` to close modals/dropdowns. Arrow keys for lists/menus.

## 8. SEO & Performance Baseline
**Goal:** Every page must score 90+ on Lighthouse across all categories.
*   **Critical CSS:** Inline above-the-fold critical CSS. Defer non-critical stylesheets.
*   **Image Optimization:** Use `<picture>` with WebP/AVIF sources and fallback. Implement `loading="lazy"` and explicit `width`/`height` attributes.
*   **Meta Tags:** Every page must have unique `<title>`, `<meta name="description">`, Open Graph tags (`og:title`, `og:image`, `og:description`), and Twitter Card meta.
*   **Structured Data:** Embed JSON-LD Schema.org markup appropriate to the content type (`SoftwareApplication`, `WebPage`, `Organization`).
