---
name: 43 Git Commit Formatter
description: Conventional Commits standard enforcer. Ensuring all agent-created commits follow a strict "feat:", "fix:", "chore:" format.
version: 1.0.0
---

# 43 Git Commit Formatter

Act as a strict enforcer of the Conventional Commits specification. Every commit generated must follow this exact format.

## 1. The Structure
```text
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

## 2. Allowed Types
- `feat`: A new feature for the user / application.
- `fix`: A bug fix.
- `docs`: Documentation changes only.
- `style`: Formatting, missing semicolons, etc. (no code change).
- `refactor`: Refactoring production code (neither fixing a bug nor adding a feature).
- `perf`: Code changes that improve performance.
- `test`: Adding missing or correcting existing tests.
- `chore`: Updating build tasks, package manager configs, etc; no production code change.

## 3. Rules
- **Imperative Mood:** The summary description must be imperative ("add feature" not "added feature").
- **Lowercase:** The type and scope should always be lowercase.
- **Short Summaries:** Keep the summary line under 50 characters if possible.
