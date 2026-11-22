# Deploy runbook — using-it.dk 2.0 cutover (Simply.com)

Date: 2026-11-22. Implements Phase 5/6 of project-playbook #50. **No production change is authorized by this document** — Gate 6 requires explicit approval. Verified facts so far: all 14 live content URLs (9 posts + 5 pages + blog index) exist as routes in the Astro build with identical trailing-slash paths; all 15 referenced media files are bundled at identical `/wp-content/uploads/...` URLs; preview builds are `noindex`; `/timecalc/timecalc.html` and `/timecalc/BO.html` are live and must never be touched.

## Stage 0 — current staging (works today, no credentials)

GitHub Pages preview: https://xander-me.github.io/using-it-website/ — auto-deploys from `main`, `noindex` (verified in build), base path `/using-it-website`. Use this for review now.

## Stage 1 — optional Simply.com staging (needs control panel)

1. Create subdomain `preview.using-it.dk` → directory `/public_html/preview/` in Simply.com panel; enable HTTPS.
2. Deploy `dist/` **into that subdirectory only**: `rsync -av dist/ user@host:/public_html/preview/` (or SFTP upload). Never touch `/public_html` root yet.
3. Verify on `preview.using-it.dk`: home, 5 sample articles, `/blogposts/`, `/rss.xml`, `/sitemap-index.xml`, one `/wp-content/uploads/...` image, both `/timecalc/` URLs still 200 on the **main** domain. Preview subdomain gets its own robots noindex via the SITE_BASE build or a `robots.txt` in the staging dir.

## Stage 2 — pre-cutover gates (need Alexander's inputs)

- [ ] **Gate 0:** WordPress export (WXR) + full backup (DB, `wp-content`, `.htaccess`, settings) downloaded and **restore-tested** on a local throwaway WP or staging.
- [ ] Simply.com panel + SFTP/SSH credentials stored as narrowly scoped GitHub Actions secrets (or manual deploy by Alexander).
- [ ] Search Console baseline recorded (#51); domain verification prepared for the new site.
- [ ] Snapshot of current webroot: `cp -a /public_html /public_html-wordpress-backup-<date>` (rename, never delete) — keeps `/timecalc/` and WP intact for rollback.

## Stage 3 — cutover (approved window)

URLs are unchanged (same slugs, same media paths), so **no 301 map is required**; verify a sample of old permalinks return 200 (not redirects) after cutover. Procedure:

1. Freeze WP editorial changes; take final WP export delta.
2. Upload the production `dist/` (built **without** SITE_BASE) to `/public_html/` root — **additive only**: `rsync -av --ignore-existing dist/ .../public_html/` so existing WP files (`index.php`, `wp-*`, `wp-content/`, `timecalc/`, `.htaccess`) are never overwritten or deleted.
3. Add/adjust `.htaccess` so static files win for blog paths while WP stays available during verification:
   ```apache
   DirectoryIndex index.html index.php
   # Blog paths are now static; WP remains reachable under /wp-admin etc. during verification
   ```
   (If Simply.com's DirectoryIndex already prefers index.html, no change is needed — verify with `curl -I https://using-it.dk/` that the Astro home is served, and `curl -I https://using-it.dk/wp-login.php` that WP still responds.)
4. Smoke test on production: home 200, 5 articles 200, `/blogposts/`, `/rss.xml`, `/sitemap-index.xml`, `/robots.txt`, one media file, `/timecalc/timecalc.html` + `/timecalc/BO.html` 200, HTTPS valid, canonical/OG correct, sitemap submitted to Search Console.
5. Only after 24–48 h stable: decommission WP (rename `index.php`/`wp-*` out of the way or keep as backup); **never** remove `/timecalc/` or `wp-content/uploads/` (old media URLs stay live from the static copy anyway).

## Rollback

`rm` nothing. Restore service by pointing `.htaccess`/DirectoryIndex back to `index.php` (or restore `/public_html` from the Stage-2 snapshot copy). Astro files are additive, so rollback = remove the added static files or revert `.htaccess`.

## Non-negotiables (from #50)

- No recursive delete/sync on `/public_html` — `/timecalc/` and sibling tools are protected.
- Original URLs stay reachable (verified: identical paths; confirm with real HTTP codes).
- No production deploy or LinkedIn post without explicit approval.
- Secrets only as narrow GitHub Actions secrets; no secrets in the repo.
