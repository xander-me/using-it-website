# Migration — WordPress → Astro (using-it.dk 2.0)

References: project-playbook #36 (brand), #50 (migration plan), #51 (content audit).

## State (22 Nov 2026)

- GitHub Pages preview live at https://xander-me.github.io/using-it-website/ (source: GitHub Actions); deploy green since 2026-11-20 13:06 UTC after the Pages source was switched from the API to manual repo settings. Stale auto-created "Pages deploy failure" issues (#1–#6) closed; workflows now auto-close their own failure reports on the next green run.
- Local build verified 2026-11-22: 20 pages, internal-link check 0 errors.
- 17 posts + 6 pages migrated (see migration-map.csv). Production using-it.dk remains WordPress; cutover follows the gates in project-playbook #50 and is blocked on WP export, URL inventory and Simply.com access (Phase 0).

## Migration readiness (22 Nov 2026)

- Content fidelity vs live WP REST: all 9 published posts 92–100% word coverage, titles match; all 14 live content URLs exist as identical trailing-slash routes in the Astro build (verified against `dist/`); no 301 map needed — spot-verify HTTP codes at cutover.
- Media: 15 referenced/featured/attachment files fetched into `public/wp-content/uploads/...` (identical URLs) and content image refs localized to local paths; verified present in `dist/`. Full library (34) is in `docs/media-inventory-2026-11-22.csv`.
- Staging: Pages preview is live and now `noindex` on preview builds (SITE_BASE), verified absent from production build.
- SEO: canonical/OG/JSON-LD/llms.txt shipped (ADR-001); sitemap/RSS/robots already present.
- Runbook: [docs/deploy-runbook.md](docs/deploy-runbook.md) — additive-only deploy, `/timecalc/` protected, rollback by rename, Gate 0–6 checklist.
- Remaining blockers (need Alexander): WP export + tested backup (Gate 0), Simply.com panel/SFTP, Search Console access, staging subdomain (optional), Gate 6 cutover approval.
