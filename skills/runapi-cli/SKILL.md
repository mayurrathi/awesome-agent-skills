---
name: RunAPI CLI
description: "Install and use the RunAPI CLI for one-off AI image, video, music, audio, and model API jobs. Discover commands, submit JSON requests, wait for tasks, check authentication, and handle outputs. Use an SDK for application or production integration."
source: runapi-ai/cli-skill (MIT)
risk: medium
---

# RunAPI CLI

Use the `runapi` CLI for one-off artifacts or results from supported AI
services. Use a RunAPI SDK for an application, backend, worker, library, or
other production integration.

## Install

```bash
brew install runapi-ai/tap/runapi
```

For headless Linux or macOS environments:

```bash
curl -fsSL https://runapi.ai/cli/install.sh | sh
```

The installer verifies a published SHA-256 checksum before writing the binary.

## Authentication

Check authentication before submitting a paid task:

```bash
runapi auth status
```

Prefer `RUNAPI_API_KEY` in headless environments. For interactive use, run
`runapi login`. Never print, commit, or place an API key directly in a command
argument.

## Discover commands

The installed CLI is the source of truth for supported services, actions, and
request fields. Inspect its help before composing a request:

```bash
runapi --help
runapi suno --help
runapi suno text-to-music --help
```

Proceed only with a service and action listed by the installed CLI. Do not
invent command names, models, or fields.

## Run a task

Write valid JSON to a file and pass it with `--input-file`:

```bash
runapi suno text-to-music --input-file request.json
```

The default command waits until the task completes. Use asynchronous mode only
when the user explicitly requests background execution or separate polling:

```bash
runapi suno text-to-music --async --input-file request.json
runapi wait <task-id> --service suno --action text-to-music
```

Preserve the returned task ID and exact service/action pair. JSON results go to
stdout and progress goes to stderr, so results can be piped to `jq`.

## Files and outputs

Pass a local media path directly when the selected command documents a media
URL field; the CLI uploads it before submission. Use `runapi files create` only
when the workflow needs a reusable temporary URL.

Inspect returned JSON for output URLs. Download requested artifacts to explicit
paths and report those paths to the user. Do not overwrite existing files
without confirmation.

## References

- Documentation and command catalog: <https://runapi.ai/models.md>
- Canonical skill: <https://github.com/runapi-ai/cli-skill>
