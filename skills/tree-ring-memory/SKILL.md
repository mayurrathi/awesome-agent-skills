---
name: Tree Ring Memory
description: "Use Tree Ring Memory for local-first AI agent memory lifecycle work: recall before risky tasks, evidence-linked learning, privacy-safe capture, redaction, audit, and forgetting."
source: TerminallyLazy/Tree-Ring-Memory (MIT)
risk: low
---

# Tree Ring Memory

Use Tree Ring Memory when an AI agent needs durable, auditable project memory
without turning chat history into a transcript dump.

Tree Ring Memory is a local-first memory lifecycle framework and portable skill.
It gives agents explicit habits for recall, remember, evidence capture,
redaction, audit, consolidation, and forgetting. The canonical implementation
ships a Rust `tree-ring` CLI backed by SQLite/FTS storage.

## When to Use

- Before changing architecture, storage, security, privacy, release, or data behavior.
- When a user correction, project decision, or validated lesson should survive the current session.
- When a failed approach should be kept visible as a warning or scar.
- When future agents need project-scoped recall with source references.
- When memory should be redacted, deleted, superseded, or audited instead of kept forever.

## Operating Rules

1. Read source files, tests, issues, PRs, and docs first. Memory points back to source truth; it does not replace it.
2. Store concise lessons, decisions, warnings, and future seeds, not full conversations.
3. Use evidence-linked memory for evaluated outcomes from tests, incidents, reviews, branches, or experiments.
4. Never store secrets, credentials, raw chain-of-thought, temporary scratchpad notes, or private identifiers.
5. Redact sensitive details when the durable lesson is useful but exact content is unsafe.
6. Delete or supersede stale and wrong memory instead of carrying it forward.
7. Prefer project scope for repo-specific rules and global scope only for durable cross-project user preferences.

## CLI Reference

Check the installed command surface before acting:

```bash
tree-ring --help
tree-ring init
tree-ring remember "Use project-scoped recall before changing release behavior." --event-type decision --scope project
tree-ring recall "release behavior" --project example-service
tree-ring evidence "Snapshot invalidation fixed stale unread chat state." --outcome promoted --evidence-ref evals/chat-state/run-042 --score 0.91
tree-ring audit --audit-type sensitive
tree-ring consolidate --period-type manual --dry-run
tree-ring maintain
```

Run broad or destructive workflows with dry-run modes first when available:

```bash
tree-ring import memories.jsonl --dry-run
tree-ring dox sync --source-root . --dry-run
tree-ring revolve sync --source-root revolve --dry-run
tree-ring integrations scan --source-root .
```

## References

- Project: <https://github.com/TerminallyLazy/Tree-Ring-Memory>
- Canonical skill: <https://github.com/TerminallyLazy/Tree-Ring-Memory/tree/main/skills/tree-ring-memory>

## Related Skills

Works well with: `agent-memory-systems`, `agent-memory-mcp`, `context-manager`,
`planning-with-files`, `architecture-decision-records`, `verification-before-completion`
