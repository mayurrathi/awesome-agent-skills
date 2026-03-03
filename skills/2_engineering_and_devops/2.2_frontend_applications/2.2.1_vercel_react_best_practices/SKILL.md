---
name: 2.2.1 Vercel React Best Practices
description: Official engineering guidelines from Vercel for ensuring Next.js code uses proper caching, server components, and suspense boundaries.
version: 1.0.0
---

# 2.2.1 Vercel React Best Practices

When building React and Next.js applications, strictly adhere to Vercel's official engineering guidelines to maximize performance and user experience.

## 1. React Server Components (RSC) Default
- **Default to Server:** Always use Server Components by default. Only add the `"use client"` directive when interactivity, hooks (useState, useEffect), or browser APIs are explicitly required.
- **Data Fetching:** Fetch data on the server component rather than the client whenever possible.

## 2. Next.js App Router Architecture
- **Colocation:** Keep components, styles, and tests close to the routes they are used in.
- **Layouts & Pages:** Utilize `layout.tsx` for shared UI across routes, and `page.tsx` for the unique route UI.

## 3. Caching & Data Mutation
- **Fetch Caching:** Utilize Next.js extended `fetch` API for granular cache control (`force-cache`, `no-store`, `revalidate`).
- **Server Actions:** Use Server Actions for data mutations instead of manual API routes for simpler client-to-server communication.

## 4. Suspense & Streaming
- **Suspense Boundaries:** Wrap slow-loading components in `<Suspense>` boundaries with meaningful fallback skeletons.
- **Granular Loading:** Don't block the entire page on data; stream UI components in as their data resolves.
