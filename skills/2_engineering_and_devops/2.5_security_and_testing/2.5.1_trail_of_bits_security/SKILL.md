---
name: 2.5.1 Trail Of Bits Security
description: Security-focused code review based on OWASP Top 10. Flagging vulnerabilities (SQLi, XSS) before code is committed.
version: 1.0.0
---

# 2.5.1 Trail Of Bits Security

Act as a strict security auditor. Before committing any code, verify it against the OWASP Top 10 vulnerabilities and modern security best practices.

## 1. Injection Prevention (SQLi, NoSQLi, Command Injection)
- **Parameterized Queries:** Never concatenate user input into database queries. Always use ORMs, parameterized queries, or prepared statements.
- **Command Sanitization:** Never pass raw user input to child processes (`exec`, `spawn`).

## 2. Cross-Site Scripting (XSS) Prevention
- **Output Encoding:** Ensure all user-supplied data rendered in the browser is properly escaped (React handles this by default, but watch out for `dangerouslySetInnerHTML`).
- **Context-Aware Sanitization:** If sanitizing HTML is required, use robust libraries like DOMPurify.

## 3. Broken Authentication & Session Management
- **Secure Cookies:** Always use `HttpOnly`, `Secure`, and `SameSite` attributes on session cookies.
- **Token Storage:** Never store JWTs in `localStorage`. Use secure HttpOnly cookies.

## 4. Insecure Direct Object References (IDOR)
- **Authorization Checks:** Always verify that the currently authenticated user has correct permissions to access or modify the requested resource ID.

## 5. Security Misconfiguration
- **Headers:** Ensure security headers (CSP, HSTS, X-Content-Type-Options) are strictly configured.
- **Secrets:** Never check API keys or secrets into version control. Use `.env` files and secure secret managers.
