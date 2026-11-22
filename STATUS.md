# using-it-website — current handoff

Updated: 2026-11-22. Owner: Alexander. Context: Work (Using-IT brand; planning in [project-playbook #36](https://github.com/xander-me/project-playbook/issues/36), [#50](https://github.com/xander-me/project-playbook/issues/50), [#51](https://github.com/xander-me/project-playbook/issues/51)).

This repository is the sole working home for the using-it.dk 2.0 Astro site. Read [README.md](README.md), [AGENTS.md](AGENTS.md) and [docs/MIGRATION.md](docs/MIGRATION.md) first. Nothing here authorizes a production deploy or LinkedIn autoposting by itself.

## Current state (verified 2026-11-22)

- **Preview is live:** https://xander-me.github.io/using-it-website/ — GitHub Pages, source = GitHub Actions. Home, /blog/, /rss.xml and /sitemap-index.xml all return 200.
- **Deploy is green:** last deploy run [44741423172](https://github.com/xander-me/using-it-website/actions/runs/44741423172) succeeded 2026-11-20 13:06 UTC (8ca0bda). The six "Pages deploy failure on main" issues (#1–#6) were stale reports from before Pages was enabled; closed 2026-11-22. Workflows now auto-close stale failure reports on the next green main run, and only ever touch their own report titles.
- **Build verified locally 2026-11-22:** `npm install && npm run build` → 20 pages; CI internal-link check logic run against `dist/` → 0 broken links.
- **Content migrated so far:** 17 posts + 6 pages in `content/`; [docs/migration-map.csv](docs/migration-map.csv) (22 rows) maps wordpress_id → content_id → original/new URL; [docs/media-list.txt](docs/media-list.txt) tracks media.

## Production status

https://using-it.dk still runs the original WordPress site. Cutover to this Astro build is **planned but not authorized**; it follows the phase gates in project-playbook #50 (Phase 0 inventory → … → Gate 6 production acceptance).

## SEO & analytics decision — 2026-11-22

[ADR-001](docs/adr-001-seo-analytics.md): technical SEO only (sitemap, RSS, robots, canonical, OG/Twitter cards, JSON-LD Article, llms.txt — implemented and verified in the build). Traffic stats: Search Console + GoAccess on Simply.com logs (zero cookies, no banner, 0 DKK); optional later self-hosted cookie-less Umami on the home Proxmox box; **no analytics SaaS, no tracker snippet shipped** (needs explicit approval per #50/#51).

## Phase 0 discovery (public, non-destructive) — done 2026-11-22

See [docs/phase0-discovery-2026-11-22.md](docs/phase0-discovery-2026-11-22.md), [docs/url-inventory-2026-11-22.csv](docs/url-inventory-2026-11-22.csv) (40 URLs, all sitemap URLs 200), [docs/media-inventory-2026-11-22.csv](docs/media-inventory-2026-11-22.csv) (28 of 34 media via public REST). Findings: WP 7.1.5 on Simply.com Apache, Rank Math SEO, theme elite-blog, **no analytics tags or cookies on public pages**, xmlrpc disabled (405), `/timecalc/timecalc.html` + `/timecalc/BO.html` live (200) and protected, `/tools/` draft 403. All 9 published posts + 6 pages reconciled against `docs/migration-map.csv`; added the missing published page `blogposts` (WP id 124). Repeatable with `python3 scripts/inventory_site.py`.

## Blockers / next action

Phase 0 public recon is done; the remaining Phase 0 items need inputs only Alexander has: (1) WordPress admin export (WXR + DB/uploads backup) for drafts, Rank Math SEO fields and the 6 non-public media items, (2) Search Console access for the traffic/indexing baseline (#51), (3) Simply.com control-panel/SFTP details for the deploy path, `.htaccess`/301 capability and staging option. Next action: Alexander provides those; then verify the recoverable backup (Gate 0) and create the #51 content-review batches before any production change.

## Non-negotiables (from #50 / README)

- Never deploy destructively over `/timecalc/` or sibling tools on Simply.com.
- Original public article URLs stay reachable (server-level 301 where changed).
- No automatic LinkedIn posting; no production deploy without explicit approval.
- Deploy credentials only as narrowly scoped GitHub Actions secrets; no secrets in the repo.
