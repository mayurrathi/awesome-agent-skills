---
name: 36 MCP Server Builder
description: Meta-skill for extending agent capabilities. Scaffolding new Model Context Protocol servers to connect to private APIs.
version: 1.0.0
---

# 36 MCP Server Builder

Use this skill when tasked with extending the agent's capabilities by building a new Model Context Protocol (MCP) server.

## 1. Project Scaffolding
- **Initialization:** Scaffold standard Node.js or Python projects configured for MCP.
- **Dependencies:** Install the official `@modelcontextprotocol/sdk` or the Python equivalent.

## 2. Server Architecture
- **Tool Definitions:** Define strict JSON schema definitions for all resources and tools the MCP server exposes.
- **Protocol Handlers:** Map incoming JSON-RPC calls from the MCP client to the private API endpoints.

## 3. Security & Context
- **API Keys:** Never hardcode private API keys in the MCP server. Read them cleanly from the local environment or `.env`.
- **Error Handling:** Return descriptive error contexts back over the MCP protocol so the agent can self-correct when API calls fail.
