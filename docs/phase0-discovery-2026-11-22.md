# Phase 0 discovery — live using-it.dk (2026-11-22)

Non-destructive, read-only recon of the **public** production site. No credentials used, no changes made to production. References: project-playbook #50 (plan), #51 (content audit). Repeatable via `python3 scripts/inventory_site.py`.

## Environment facts

| Fact | Value | Evidence |
| --- | --- | --- |
| Hosting | Simply.com, Apache (`server: Simply.com`, `simplycom-server: Apache`) | response headers |
| CMS | WordPress 7.1.5, theme `elite-blog` (+ `marvel-blog` assets) | `<meta name="generator">`, wp-content theme CSS |
| SEO plugin | **Rank Math** (not Yoast) — canonical, OG, description rendered per post | sitemap footer, post `<head>` |
| Analytics on pages | **None found** — no GA/GTM/Matomo/Plausible/Clarity/Hotjar tags, no `G-`/`UA-` IDs, no cookies set on home/post pages | full-HTML scan of `/` and one post |
| Search Console | Unknown — needs account access (blocked on Alexander) | — |
| XML-RPC | Disabled (405) — good | `/xmlrpc.php` |
| Login | `/wp-login.php` 455, `/wp-admin/` 302 → login | status checks |
| Directory listing | Off: `/wp-content/uploads/` 403, `/timecalc/` 403 | status checks |
| PHP version | Not exposed (no `X-Powered-By`) | headers |

## Protected paths — never touch on the server

- `/timecalc/timecalc.html` — **200**
- `/timecalc/BO.html` — **200**
- `/timecalc/` directory — 403 (listing off)
- All of `public_html` outside the blog scope; no recursive delete/sync ever (per #50)

## URL inventory (all recorded in `url-inventory-2026-11-22.csv`, 40 URLs)

- Sitemap index: `sitemap_index.xml` → `post-sitemap.xml` (10) + `page-sitemap.xml` (6 + image attachment pages). **All 30 sitemap URLs return 200.**
- 9 published posts: IDs 165, 178, 312, 378, 386, 391, 407, 557, 598 (slugs = trailing-slash permalinks, unchanged in the Astro build).
- 6 published pages: about-me (31), **blogposts (124)**, youtube (373), tools-2 (564), remote-support (586), microsoft-licenses (605).
- RSS: `/feed/` 200 with 9 items (matches posts). `/feed` and `/wp-sitemap.xml` 301-redirect.
- Draft page `/tools/` → 403 (draft, not public).
- 14 image attachment pages under `/wp-content/uploads/...` are in the sitemaps and return 200.

## Content inventory (public WP REST)

- 9 posts + 6 pages retrieved with id/date/modified/slug/categories/featured_media (`/tmp` capture; repo map below).
- Categories: 12 (intune-mem ×4, edge, conditionalaccess, windows-365, hyper-v, powershell, apple, microsoft, uncategorized, + 0-count home-assistant/ism/osdcloud). **Tags: none** (all posts `tags: []`).
- Featured images per post: 598→603, 557→560, 407→417, 391→433, 386→387, 378→382, 312→530, 178→239, 165→415.
- Media library: `X-WP-Total: 34`; **28 items retrievable via public REST** (listed in `media-inventory-2026-11-22.csv`); the remainder need the authenticated WXR/export. Existing `docs/media-list.txt` covers only 6 — superseded by the full inventory CSV.

## Reconciliation vs. this repo

- `docs/migration-map.csv` covers all 9 published posts + 6 pages **except published page `blogposts` (WP id 124)** — added to the map in this change; the Astro route `src/pages/blogposts.astro` already serves `/blogposts/`.
- `content/posts/` has 17 files = 9 published + 8 drafts in the map; `content/pages/` has 6 = 5 published + 1 draft (tools). Frontmatter spot-check matches WP (wordpress_id, original_url, dates, categories).
- Gaps for Phase 3: full media pull (34 items, incl. in-content images), Rank Math per-post SEO fields (not exposed via public REST — need admin/export), and draft content verification.

## Blockers (need Alexander)

1. WordPress admin export (WXR + DB/uploads backup) — for drafts, SEO meta, and the 6 non-public media items.
2. Search Console access — indexing/traffic baseline (#51).
3. Simply.com control-panel/SFTP details — deploy path, `.htaccess`/301 capability, staging option (Phase 5).

## Next action

With the WP export + Simply.com access: verify recoverable backup (Gate 0), then run the content-review batches from #51 against `url-inventory-2026-11-22.csv` before any production change.
