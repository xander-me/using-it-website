# ADR-001 — SEO and traffic statistics on using-it.dk 2.0

Date: 2026-11-22. Status: Accepted for implementation (code only; no production deploy, no tracker live). References: project-playbook #50 (plan, non-negotiables), #51 (privacy-first analytics strategy).

## Context

Discovery (docs/phase0-discovery-2026-11-22.md) showed the live WordPress site has **no client-side analytics and sets no cookies**; SEO is handled by Rank Math (canonical, OG, description per post). Hosting is Simply.com shared webhotel (Apache logs available via control panel). Budget target from #50: 0 DKK incremental. #51 requires privacy-first analytics and forbids production tracking changes without explicit approval.

## Decision

### SEO — technical, no third parties

1. Ship with what Astro gives plus explicit metadata: sitemap (`@astrojs/sitemap`), RSS, robots.txt, per-page canonical, `og:url`/`og:image`/`twitter:card`, and JSON-LD `Article` schema on posts (implemented in `src/layouts/Base.astro` + `src/pages/[...slug].astro`). `public/llms.txt` added for AI crawlers.
2. URLs stay byte-identical to WordPress (trailing-slash slugs via the root catch-all), so no redirect reliance; a server-level 301 map is generated only for genuine path changes (Phase 3/6, verified with real HTTP codes on Simply.com).
3. Per-post SEO fields (Rank Math title/description/focus keyword, OG image) are migrated from the WP export in Phase 3 into frontmatter, keeping today's search snippets stable.
4. At cutover (Gate 6): verify the domain in **Search Console** (DNS or HTML-file method — needs Alexander's access), submit `sitemap_index.xml`, and record the indexing baseline from #51.

### Traffic statistics — privacy-first, zero cookies

| Option | What it gives | Cost | Cookies/banner | Verdict |
| --- | --- | --- | --- | --- |
| A. Search Console only | Impressions, clicks, queries, coverage | Free | None | **Baseline — yes** |
| B. Log-based (GoAccess on Simply.com Apache logs) | Pageviews, referrers, 404s from server logs | Free | None — nothing added to pages | **Yes, from launch** |
| C. Self-hosted cookie-less analytics (Umami/Plausible self-hosted on the home Proxmox box, exposed as `stats.using-it.dk`) | Real-time dashboard, events | Free (own hardware) | No cookies, no banner, but a JS snippet and a home-server dependency for a public site | **Optional later** — only if A+B prove insufficient; requires explicit approval + availability plan |
| D. Analytics SaaS (Plausible Cloud, GA, etc.) | Dashboard | Paid or data-for-service | Third-party data transfer | **Rejected** — conflicts with 0 DKK target and the privacy-first stance in #51 |

**No tracker snippet is shipped in this change.** The site sets no cookies and loads no third-party scripts, so no consent banner is required (GDPR). If option C is later approved, add the snippet in `Base.astro` behind an explicit build flag and record it here.

## Consequences

- Positive: no consent banner, no third-party requests, fastest possible page loads, full GDPR compliance by construction; Search Console + logs cover the #51 audit needs.
- Negative: no real-time dashboard until/unless C is approved; log analytics depend on Simply.com log retention.
- Follow-up: when Alexander provides Search Console access, record the baseline; when the WP export arrives, port Rank Math fields per post.
