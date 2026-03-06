---
name: Web Design Guidelines
description: A portable design system (Typography, Spacing, Accessibility). Preventing "ugly" default UI generation by enforcing specific CSS standards.
version: 1.0.0
---

# 2.1.4 Web Design Guidelines

This meta-skill acts as a strict firewall against generic, default, or "ugly" UI generation in web applications.

## 1. Typography
- **Kill Defaults:** Never use Times New Roman or default browser sans-serif. Inject modern fonts like Inter, Roboto, or system UI fonts immediately.
- **Hierarchy:** Use a strict mathematical scale (e.g., 1.25 ratio) for headings to body text.

## 2. Spacing & Layout
- **The 8pt Grid:** Use margins and paddings in multiples of 4 or 8 (`8px, 16px, 24px, 32px`). Avoid arbitrary pixel values.
- **Breathing Room:** Liberal use of whitespace is mandatory. Dense UIs are unacceptable unless building a dashboard.

## 3. Color & Aesthetics
- **Never Pure Colors:** Do not use `red`, `blue`, or `#000000`. Use curated, slightly muted hex codes or HSL values (e.g., `#1e293b` for black).
- **Subtlety:** Use very subtle box shadows (`rgba(0,0,0,0.05)`) and slight border radii (`8px` or `12px`) to soften layouts.
