---
name: Electron Upgrade Advisor
description: Framework migration specialist. Guiding developers through breaking changes in Electron version upgrades.
version: 1.0.0
---

# 2.6.1 Electron Upgrade Advisor

Use this skill when attempting to upgrade an Electron project to a major new version. It helps navigate breaking changes and deprecations.

## 1. Upgrade Prerequisites
- **Node/Chromium Alignment:** Always check the exact Node.js and Chromium versions bundled with the target Electron version.
- **Dependency Audit:** Verify that native dependencies (`ffi-napi`, `node-gyp` modules) support the new Node/V8 engine.

## 2. Context Isolation & IPC
- **Context Bridge:** From Electron 12+, `contextIsolation` is true by default. Ensure all IPC communication occurs strictly over `contextBridge.exposeInMainWorld()`.
- **Remote Module:** The `remote` module is completely removed in modern Electron. Migrate all remote calls to IPC patterns.

## 3. Sandboxing & Security
- **Sandbox Default:** Electron 20+ enables sandbox by default for all renderers. Review application architecture to accommodate this strict boundary.
