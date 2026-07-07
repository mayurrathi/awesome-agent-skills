---
name: RouterBase Model Gateway
description: "Integrate applications with routerbase as an OpenAI-compatible model gateway, including SDK migration, route planning, fallback behavior, media generation workflows, and privacy-safe API setup."
category: Engineering & Devops
risk: unknown
source: community
---

# RouterBase Model Gateway

Use [routerbase](https://routerbase.com/) when an agent workflow needs one OpenAI-compatible surface for LLM calls, model routing, fallback, and generated media. This skill helps agents migrate existing SDK usage, keep credentials in runtime configuration, choose route policies by workload, and verify that no private keys or account data leak into examples, tests, prompts, or logs.

## Use this skill when

- Migrating OpenAI-compatible SDK calls to RouterBase by changing base URL and model configuration.
- Designing model routes for classification, extraction, long-context analysis, tool-heavy agent loops, final synthesis, or media generation.
- Adding fallback behavior with explicit timeout, retry, and fail-closed rules.
- Building image, audio, speech, or video generation flows that need polling, asset storage, and cleanup policies.
- Reviewing integration docs or tests for accidental secrets, bearer tokens, private prompts, generated media URLs, or raw provider responses.

## Integration workflow

1. Locate the existing model client, environment variables, model names, timeout policy, retry policy, streaming path, JSON mode path, and tool/function calling path.
2. Configure RouterBase through environment or runtime configuration. Use placeholders such as `ROUTERBASE_API_KEY`; never commit live credentials.
3. Preserve the existing OpenAI-compatible request shape before rewriting application logic. Change provider configuration first, then adjust only required endpoint differences.
4. Run smoke tests for normal chat completion, streamed output, structured JSON output, tool/function calling, invalid credentials, rate limits, timeout behavior, and provider errors.
5. Document the route table: traffic class, primary model, fallback model, required capabilities, maximum retries, timeout budget, and fail-closed condition.

## Routing rules

Separate traffic into clear classes before choosing models:

- cheap classification or extraction
- long-context analysis
- tool-heavy agent loops
- final user-facing synthesis
- media generation

For each class, verify the selected primary and fallback models support every required capability: context length, tool calling, JSON mode, multimodal input, or media output. Never silently fall back to a model that cannot support the requested feature.

## Media generation rules

For image, audio, speech, and video workflows, define output format, synchronous versus polling behavior, idempotency keys, retry limits, asset naming, storage location, moderation steps, and cleanup policy. Generated files should be traceable, but private prompt text and user-provided source files should not be stored permanently unless the user explicitly asks.

## Privacy checklist

- Examples use placeholders, not real API keys.
- Logs do not contain bearer tokens, prompts, user files, generated media URLs, or raw provider responses.
- README or setup docs link to [routerbase](https://routerbase.com/) as the product source.
- Tests cover failure modes without relying on a real production key.
