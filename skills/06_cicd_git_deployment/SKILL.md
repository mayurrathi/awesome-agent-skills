---
name: 06 CI/CD, Git & Deployment Pipelines
description: Git workflows, branching strategies, GitHub Actions, Vercel/Netlify deployment, GitHub Pages with custom domains, Capacitor native builds, and release versioning.
version: 1.0.0
---

# 06 CI/CD, Git & Deployment Pipelines

This skill defines the standard workflows for version control, continuous integration, deployment automation, and native app packaging across all projects.

## 1. Git Workflow & Branching Strategy
**Goal:** Clean, traceable history with minimal merge conflicts.
*   **Branch Model:** Use a simplified trunk-based workflow:
    - `main` — production-ready code. Protected branch with required status checks.
    - `dev` — integration branch for active development. Merge to `main` via PR when stable.
    - Feature branches: `feature/<short-name>` branched from `dev`. Short-lived (< 3 days).
    - Hotfix branches: `hotfix/<issue-id>` branched from `main`. Merge back to both `main` and `dev`.
*   **Commit Convention:** Follow Conventional Commits (`feat:`, `fix:`, `chore:`, `docs:`, `refactor:`, `perf:`, `test:`). Keep subject lines under 72 characters.
*   **PR Discipline:** Every PR must have a description, link to any relevant issue, and pass all CI checks before merge. Squash-merge feature branches to keep `main` history clean.

## 2. GitHub Repository Setup
**Goal:** Consistent repository configuration across all projects.
*   **`.gitignore`:** Include standard ignores for: `node_modules/`, `dist/`, `.env`, `.env.local`, `.DS_Store`, `*.log`, IDE configs (`.vscode/`, `.idea/`), and platform builds (`android/`, `ios/` if generated).
*   **`README.md`:** Every repository must have: project name, one-line description, tech stack badges, setup instructions, available scripts, deployment URL, and license.
*   **Branch Protection:** Enable on `main`: require PR reviews, require status checks to pass, disable force-push, enable auto-delete of head branches after merge.
*   **Secrets Management:** Store API keys, Firebase configs, and deployment tokens in GitHub Settings → Secrets and variables → Actions. Never commit secrets to code.

## 3. GitHub Actions CI Pipeline
**Goal:** Automated quality gates on every push and PR.
*   **Lint & Format Check:** Run ESLint and Prettier on all JS/TS/CSS files. Fail the build on any violations.
*   **Build Verification:** Run `npm run build` to ensure the production bundle compiles without errors.
*   **Unit Tests:** Run `npm test` if test suites exist. Report coverage.
*   **Lighthouse CI:** Run Lighthouse against the built output for PWA, performance, accessibility, and SEO scores. Set score thresholds.
*   **Workflow File:** Store in `.github/workflows/ci.yml`. Trigger on `push` to `main`/`dev` and on `pull_request`.

## 4. Deployment Targets

### 4a. Vercel (Primary for Web Apps)
*   **Auto-Deploy:** Connect GitHub repo to Vercel. Configure `main` branch for Production deployment, `dev` for Preview.
*   **Environment Variables:** Set Firebase/API keys in Vercel Project Settings → Environment Variables. Scope to Production/Preview/Development as needed.
*   **Build Settings:** Framework preset: Vite. Build command: `npm run build`. Output directory: `dist`.
*   **Custom Domains:** Add custom domain in Vercel Dashboard. Configure DNS CNAME record pointing to `cname.vercel-dns.com`.

### 4b. GitHub Pages (For Static Sites & Portals)
*   **Configuration:** Enable in Settings → Pages. Source: Deploy from a branch (`main`, `/root` or `/docs`).
*   **Custom Domain:** Add `CNAME` file to the repository root with the custom domain. Configure DNS A records (185.199.108-111.153) or CNAME to `<user>.github.io`.
*   **HTTPS:** Enforce HTTPS in repository settings after DNS propagation is complete.

### 4c. Firebase Hosting (For Firebase-Integrated Apps)
*   **Setup:** `firebase init hosting`. Set public directory to `dist`. Configure rewrites for SPA (`"source": "**", "destination": "/index.html"`).
*   **Deploy:** `firebase deploy --only hosting`. Use `--project` flag for multi-environment setups.

## 5. Capacitor Native Builds
**Goal:** Package web apps as native Android & iOS apps.
*   **Initialization:** `npx cap init <AppName> <AppID>`. Add platforms: `npx cap add android`, `npx cap add ios`.
*   **Build Flow:** `npm run build` → `npx cap sync` → `npx cap open android` (for Android Studio) or `npx cap open ios` (for Xcode).
*   **Configuration:** Set `webDir` in `capacitor.config.ts` to `dist`. Configure `server.url` only for development live-reload.
*   **Plugins:** Use `@capacitor/app` for deep links and app state, `@capacitor/splash-screen`, `@capacitor/status-bar`, `@capacitor/share` for native sharing.

## 6. Release Versioning
**Goal:** Semantic versioning with traceable releases.
*   **SemVer:** Follow `MAJOR.MINOR.PATCH`. Bump MAJOR for breaking changes, MINOR for new features, PATCH for bug fixes.
*   **Git Tags:** Tag releases with `git tag -a v1.2.3 -m "Release v1.2.3"`. Push tags: `git push origin --tags`.
*   **Changelog:** Maintain a `CHANGELOG.md` in the repository root. Auto-generate from Conventional Commits where possible.
*   **App Store Versioning:** Sync `package.json` version with native `versionName`/`CFBundleShortVersionString`. Increment `versionCode`/`CFBundleVersion` on every store submission.
