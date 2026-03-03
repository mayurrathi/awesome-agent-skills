---
name: 31 Antigravity Superpowers
description: Enforces a "Plan-Act-Verify" loop. Agents must write a plan and tests before coding. Reducing bugs in complex feature builds.
version: 1.0.0
---

# 31 Antigravity Superpowers

This skill defines the core methodology for autonomous feature development to ensure reliability and reduce bugs in complex builds.

## 1. The Plan-Act-Verify Loop
Always adhere to the following strict cycle when approaching any complex development task.

### Phase 1: Plan
- **Analyze Requirements:** Fully understand the ticket, issue, or user request.
- **Architectural Plan:** Document the proposed architecture, components, and data flow.
- **Test-Driven Design:** Before writing any application code, write the testing plan or stub the tests.

### Phase 2: Act
- **Incremental Implementation:** Build out the feature in small, verifiable chunks.
- **Commit Often:** Use atomic commits that represent logical units of work.

### Phase 3: Verify
- **Execute Tests:** Run the test suite you planned in Phase 1.
- **Self-Correction:** If tests fail, analyze the logs, adjust the code, and re-verify.
- **Final Validation:** Do a final manual context check to ensure side-effects haven't broken existing functionality.
