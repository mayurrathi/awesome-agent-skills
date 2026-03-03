---
name: 10 AI-Assisted Development Workflows
description: Prompt engineering for code generation, multi-agent coordination, skill authoring standards, workflow automation, and quality gates for AI-generated code.
version: 1.0.0
---

# 10 AI-Assisted Development Workflows

This skill defines the standards for working effectively with AI coding assistants (Antigravity, Firebase Studio, v0.dev, Bolt.new) to maximize code quality, minimize hallucination, and establish repeatable automation patterns.

## 1. Skill Authoring Standards
**Goal:** Every skill file must be consistent, discoverable, and actionable.
*   **File Structure:** Each skill lives in `.agent/skills/<NN>_<snake_case_name>/SKILL.md`. The numbered prefix (`01`–`99`) establishes a logical reading order.
*   **YAML Frontmatter:** Required fields: `name` (human-readable title with ID prefix), `description` (50-150 character summary for tooling), `version` (SemVer).
*   **Content Format:** Use numbered sections (`## 1. Section Title`). Each section has a bold **Goal:** line followed by bulleted instructions. Include code snippets where they add clarity.
*   **Scope:** Each skill covers one domain. Avoid overlapping responsibilities between skills. Cross-reference related skills by ID number (e.g., "See Skill 05 for PWA caching strategies").
*   **Versioning:** Increment `version` when content changes meaningfully. `PATCH` for typo/clarification fixes. `MINOR` for added sections. `MAJOR` for restructuring.

## 2. Effective Prompting Patterns
**Goal:** Get high-quality, production-ready code on the first generation.
*   **Context Loading:** Always reference relevant skills before starting implementation. Say: "Read Skill 04 and apply its design token standards" rather than re-describing the standards.
*   **Specificity:** Avoid "make it look good." Instead: "Use a dark theme with `--color-surface: hsl(230, 20%, 10%)`, glassmorphism cards with `backdrop-filter: blur(16px)`, and Inter font at 16px base."
*   **Constraints First:** State what NOT to do before what to do. "Do not use Tailwind. Do not use inline styles. Use CSS custom properties for all colors." This prevents the most common deviations.
*   **Incremental Building:** Build in layers: (1) data model/types, (2) CSS design system, (3) components, (4) page assembly, (5) interactions. Review each layer before proceeding.
*   **Verification Requests:** End prompts with specific verification steps: "After building, run the dev server and use the browser tool to verify the layout at 375px and 1280px widths."

## 3. AI Code Quality Gates
**Goal:** Never ship AI-generated code without validation.
*   **Build Check:** Every generated codebase must `npm run build` without errors or warnings before being considered complete.
*   **Lint Pass:** Run ESLint on all generated files. Fix all errors. Warnings are acceptable only with documented justification.
*   **Browser Verification:** Use the browser tool to visually verify UI at: mobile (375px), tablet (768px), and desktop (1280px). Check interactive states (hover, click, form submission).
*   **Accessibility Audit:** Run Lighthouse accessibility audit. Score must be ≥ 90. Fix all critical issues (missing labels, contrast failures, keyboard traps).
*   **Manual Code Review:** Scan generated code for: hardcoded secrets, unused imports, dead code, missing error handling, and overly complex logic. Simplify before committing.

## 4. Multi-Agent Coordination
**Goal:** Use different AI tools for their strengths.
*   **Antigravity (Primary):** Architecture decisions, skill management, multi-file refactoring, Git operations, deployment, debugging. Has full filesystem and terminal access.
*   **Firebase Studio:** Cloud-based rapid prototyping, Firebase integration testing, collaborative sessions. Use for throwaway experiments.
*   **v0.dev / Bolt.new:** Quick UI component generation. Export the generated component and integrate manually — don't rely on their project structure.
*   **Handoff Protocol:** When moving code between agents/tools, always (1) commit to Git first, (2) document the current state in README, (3) list pending tasks clearly.

## 5. Workflow Automation
**Goal:** Codify repetitive processes as executable workflows.
*   **Workflow Files:** Store in `.agent/workflows/<workflow-name>.md`. Use YAML frontmatter with `description`.
*   **Common Workflows:**
    - `new-app.md` — Step-by-step for scaffolding a new app (references Skill 09)
    - `deploy-vercel.md` — Build, test, deploy to Vercel
    - `deploy-github-pages.md` — Build, commit dist, push to gh-pages
    - `audit-skills.md` — Review all skills for applicability to current project
    - `pre-release.md` — Version bump, changelog, tag, build, deploy
*   **Turbo Annotations:** Use `// turbo` above individual safe steps or `// turbo-all` at the top for fully automated workflows. Only mark steps as turbo if they are read-only or non-destructive.
*   **Parameterization:** Use `<PLACEHOLDER>` tokens in workflow steps for values that must be filled in at execution time (app name, version number, etc.).
