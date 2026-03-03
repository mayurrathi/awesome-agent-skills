---
name: 09 Project Scaffolding & Monorepo Management
description: Monorepo structure, Vite project initialization, shared config patterns, apps.json registry, dependency management, and new-project checklists.
version: 1.0.0
---

# 09 Project Scaffolding & Monorepo Management

This skill defines the standards for initializing new projects within the Business Idea Prototypes workspace, maintaining the monorepo structure, and managing shared configurations.

## 1. Workspace Directory Structure
**Goal:** Consistent, predictable project layout across all apps.
*   **Root Layout:**
    ```
    Business Idea Prototypes/
    ├── .agent/skills/          # Global skill directory (this directory)
    ├── packages/               # Parent for all app projects
    │   ├── .agent/             # Legacy (deprecated — use root .agent)
    │   ├── apps.example.com/   # Portal site & app directory
    │   ├── example-game/       # Example Game app
    │   ├── utility-app/        # Example utility app
    │   └── <new-app>/          # Future apps go here
    ├── Test business ideas/    # Research & ideation scratch space
    ├── src/                    # Root landing page source
    └── index.html              # Root landing page
    ```
*   **Per-App Structure:** Every app under `packages/` must follow:
    ```
    <app-name>/
    ├── public/                 # Static assets (icons, images, manifest.json)
    ├── src/                    # Source code (components, styles, utils)
    ├── dist/                   # Build output (gitignored)
    ├── index.html              # Entry point
    ├── package.json            # Dependencies & scripts
    ├── vite.config.js          # Build configuration
    ├── .gitignore              # Standard ignores
    └── README.md               # Project documentation
    ```

## 2. New Project Initialization Checklist
**Goal:** Never miss a setup step when starting a new app.
*   **Step 1 — Scaffold:** Run `npx -y create-vite@latest ./ --template react` (or `vanilla` for non-React apps) inside the new directory under `packages/`.
*   **Step 2 — Dependencies:** Install project-specific dependencies. Common baseline: `npm install firebase` (if using Firebase).
*   **Step 3 — PWA Setup:** Create `public/manifest.json` following Skill 05 standards. Create `public/sw.js` with App Shell caching. Add service worker registration to `main.js`.
*   **Step 4 — Design System:** Set up `src/index.css` with design tokens from Skill 04. Import Google Font. Define dark mode variables.
*   **Step 5 — Git:** Initialize with `git init`. Create `.gitignore`. Make initial commit: `git commit -m "feat: initial scaffold"`.
*   **Step 6 — Registry:** Add the new app entry to `apps.example.com/apps.json` with `id`, `name`, `description`, `path`, `icon`, `status`, and `tags`.
*   **Step 7 — README:** Create `README.md` with project name, description, tech stack, setup instructions, and deployment URL.

## 3. `apps.json` Registry Protocol
**Goal:** The portal at apps.example.com always has an accurate directory of all apps.
*   **Schema:**
    ```json
    {
      "id": "kebab-case-id",
      "name": "Human Readable Name",
      "description": "One-line description with key differentiators.",
      "path": "/app-id/",
      "icon": "🎯",
      "status": "Live | Beta | Development | Archived",
      "tags": ["PWA", "Firebase", "Realtime", "Offline"]
    }
    ```
*   **Status Lifecycle:** `Development` → `Beta` → `Live` → `Archived`. Update status in `apps.json` at each transition.
*   **Deployment:** The portal itself is hosted on GitHub Pages at `apps.example.com`. After updating `apps.json`, commit and push to trigger deployment.

## 4. Shared Configuration Patterns
**Goal:** Reduce boilerplate across projects.
*   **Vite Config:** Standard `vite.config.js` should include: React plugin (if React), build target `es2020`, sourcemaps enabled in dev, environment variable prefixing.
*   **ESLint:** Use a shared ESLint config. Recommended: `@eslint/js` with `globals` for browser. For React: add `eslint-plugin-react-hooks` and `eslint-plugin-react-refresh`.
*   **Environment Variables:** Prefix all client-side env vars with `VITE_`. Store sensitive values in `.env.local` (gitignored). Document required env vars in README.

## 5. Dependency Management
**Goal:** Minimize dependency bloat and security vulnerabilities.
*   **Audit:** Run `npm audit` monthly. Fix critical/high vulnerabilities immediately.
*   **Lockfile:** Always commit `package-lock.json`. Use `npm ci` in CI pipelines for deterministic installs.
*   **Bundle Analysis:** Periodically run `npx vite-bundle-visualizer` to identify oversized dependencies. Replace heavy libraries with lighter alternatives where possible.
*   **Version Pinning:** Use exact versions for critical dependencies (Firebase, Capacitor). Use caret ranges for dev dependencies.
