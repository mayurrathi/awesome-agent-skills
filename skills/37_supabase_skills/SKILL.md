---
name: 37 Supabase Skills
description: Backend optimization rules. Writing correct Row Level Security (RLS) policies and performant Postgres queries.
version: 1.0.0
---

# 37 Supabase Skills

When using Supabase as the backend/BaaS, enforce these database, security, and performance rules strictly.

## 1. Row Level Security (RLS)
- **Deny by Default:** All tables must have RLS enabled immediately (`ALTER TABLE X ENABLE ROW LEVEL SECURITY;`).
- **Policy Granularity:** Write explicit `SELECT`, `INSERT`, `UPDATE`, and `DELETE` policies referencing `auth.uid()`.
- **Security Definer:** Be extremely careful with Edge Functions or DB Functions using `SECURITY DEFINER`.

## 2. Performance & Postgres
- **Indexes:** Always create indexes on foreign keys and columns frequently used in `WHERE`, `ORDER BY`, or `JOIN` clauses.
- **View Alternatives:** Use materialized views for heavy analytical queries instead of querying raw tables repeatedly.

## 3. Edge Functions
- **TypeScript:** Write Edge Functions in TypeScript using Deno.
- **Payload Validation:** Validate incoming JSON structures securely before passing them to the database.
