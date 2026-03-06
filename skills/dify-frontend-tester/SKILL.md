---
name: Dify Frontend Tester
description: Specialized frontend testing logic. Automating component testing specifically for the Dify platform.
version: 1.0.0
---

# 2.5.3 Dify Frontend Tester

Use this skill to execute frontend and component testing logic mapped specifically to the Dify Open-Source LLM App Development Platform.

## 1. Dify UI Component Standards
- **Mocking Contexts:** Dify relies heavily on App and Workspace contexts. Write setup scripts that properly wrap components in these mock contexts.
- **I18n Mocking:** Ensure the `next-i18next` configuration is mocked out during unit tests to avoid missing translation keys breaking renders.

## 2. API Mocking
- **MSW (Mock Service Worker):** Use MSW to intercept Dify's internal API schemas (e.g., `/console/api/apps`, `/api/parameters`). 
- **Fixtures:** Maintain strict, updated JSON fixtures matching Dify's backend responses for chat endpoints, tool schemas, and app configurations.

## 3. End-to-End Workflows
- Always test the complete loop of: App creation -> Prompt design -> Tool binding -> Publishing -> Chat execution.
