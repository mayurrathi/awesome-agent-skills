---
name: 45 Skill Installer
description: Recursive capability. An agent skill that allows the agent to find and install other skills autonomously.
version: 1.0.0
---

# 45 Skill Installer

This is a recursive meta-skill. Use it when the user requests a capability you do not currently possess, allowing you to scaffold a new skill for yourself.

## 1. The Skill Installation Loop
- **Identify Gap:** Acknowledge you do not currently have the requested skill in `.agent/skills/`.
- **Formulate Design:** Determine the core principles, rules, and best practices defining the new skill.
- **Self-Modification:** Create a new folder (e.g., `46_new_capability`) and generate an exhaustive `SKILL.md` file using your `write_to_file` tool.
- **Verify Integration:** Read the newly created skill file back to ensure it meets the skill architecture schema (Name, Description, Version, and structured H2 rules).

## 2. Formatting Requirements
Every autonomously installed skill MUST have:
1. YAML Frontmatter (name, description, version).
2. A main H1 title.
3. At least 3 H2 sections outlining distinct rules or workflows.
4. Actionable, concrete directives rather than vague suggestions.
