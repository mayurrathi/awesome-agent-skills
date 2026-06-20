---
name: ax-extract-workflow
description: Reconstruct how shipped work happened from local ax sessions, commits, skills, and subagent activity.
version: 1.0.0
category: Ai & Agents
---

# ax-extract-workflow

Use this skill when the user asks how a shipped result actually happened, wants
to reconstruct the workflow behind a PR, commit, feature, demo, or date range,
or asks for a repeatable playbook from past agent work.

This skill requires local ax data. Before reconstructing anything, confirm that
`ax` or `axctl` is installed, SurrealDB is running, and the relevant sessions,
commits, skills, tool calls, and subagent activity have been indexed.

## Use this skill when

- The user asks how a PR, feature, artifact, or demo was shipped.
- The user wants the workflow behind a date, commit, or release.
- The user wants to extract a repeatable playbook from a past agent session.
- The user asks which tools, skills, checks, failures, or repairs shaped the work.

Do not use this as generic memory. If the local ax graph does not contain the
data, say what is missing instead of guessing.

## Instructions

1. Identify the target artifact, commit, date range, branch, PR, or shipped
   result.
2. Query local ax sessions, commits, invoked skills, tool calls, and subagent
   activity for the relevant window.
3. Reconstruct the workflow as a factual sequence: goal, investigation, edits,
   checks, failures, repairs, and final evidence.
4. Separate observed evidence from inference.
5. Extract a reusable workflow only after the factual sequence is clear.
6. If indexing is stale or the graph is unavailable, stop and name the missing
   ingest, database, or query prerequisite.

Useful commands:

```bash
ax sessions near <sha>
ax sessions around <date> --project=<path>
ax sessions show <session-id> --all
ax recall "<topic>" --scope=here
```

## Output format

```markdown
## Workflow Reconstruction

Target:
- [Commit, PR, feature, artifact, or date window.]

Evidence used:
- [Session IDs, commits, skills, tool calls, or commands.]

Sequence:
1. [Observed step.]
2. [Observed step.]
3. [Observed step.]

Inferences:
- [Any likely connection that was not directly recorded.]

Reusable workflow:
1. [Repeatable step.]
2. [Repeatable step.]
3. [Repeatable step.]

Gaps:
- [Missing transcript, missing commit link, unindexed source, or weak evidence.]
```

## Evidence rules

- Do not invent prompts, decisions, commands, or motivations.
- Cite concrete session, commit, tool, or skill evidence when available.
- Keep speculation in the `Inferences` section.
- Prefer "the evidence shows" over broad claims like "the team usually."
- Do not send private transcripts, code, customer data, credentials, or telemetry
  to remote services.

Source project: [Necmttn/ax](https://github.com/Necmttn/ax)
