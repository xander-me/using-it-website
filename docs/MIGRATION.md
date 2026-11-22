# Migration — WordPress → Astro (using-it.dk 2.0)

References: project-playbook #36 (brand), #50 (migration plan), #51 (content audit).

## State (22 Nov 2026)

- GitHub Pages preview live at https://xander-me.github.io/using-it-website/ (source: GitHub Actions); deploy green since 2026-11-20 13:06 UTC after the Pages source was switched from the API to manual repo settings. Stale auto-created "Pages deploy failure" issues (#1–#6) closed; workflows now auto-close their own failure reports on the next green run.
- Local build verified 2026-11-22: 20 pages, internal-link check 0 errors.
- 17 posts + 6 pages migrated (see migration-map.csv). Production using-it.dk remains WordPress; cutover follows the gates in project-playbook #50 and is blocked on WP export, URL inventory and Simply.com access (Phase 0).
