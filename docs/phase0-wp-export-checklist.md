# Phase 0 / Gate 0 checklist — WordPress export & backup (using-it.dk)

Date: 2026-11-22. Purpose: recoverable backup + full export before any migration step (project-playbook #50, Gate 0). Target location for the files: `/home/ax/dev/.private/wp-backup-2026-11-22/` (mode 0700, outside every git repo — **never commit these files**).

## A. WordPress content export (WXR) — in wp-admin

1. Log in at https://using-it.dk/wp-admin
2. **Tools → Export → "All content" → Download Export File**
   → saves e.g. `using-it.wordpress.2026-11-22.xml`
   (WXR includes posts, pages, **drafts**, comments, categories/tags, users and post meta — including Rank Math `_rank_math_*` SEO fields per post)
3. Optional: WP-CLI over SSH if enabled: `wp export --dir=/tmp` (same result)

Save as: `.private/wp-backup-2026-11-22/wxr.xml`

## B. Full server backup — Simply.com

1. Control panel → take the full backup (or schedule one) **and** download manually:
   - SFTP/SSH: download the whole `/public_html` directory (contains `wp-content/uploads/` with all 34 media files, `.htaccess`, `wp-config.php`, `index.php`, `wp-*`)
   - Database: panel → phpMyAdmin → your DB → **Export → Quick → SQL** (or panel's DB backup tool)
2. Record: Simply.com plan name, PHP version, exact `/public_html` path, whether `.htaccess` overrides are allowed (needed for the Stage-3 cutover), and whether subdomains map to subdirectories (needed for `preview.using-it.dk`).

Save as: `.private/wp-backup-2026-11-22/db.sql` and `.private/wp-backup-2026-11-22/public_html/` (or `public_html.tar.gz`)

## C. What gets verified from these files (by the agent, locally)

1. WXR well-formed; counts reconciled vs. live inventory (`docs/url-inventory-2026-11-22.csv`): expect 9 published posts, 6 published pages, 8 drafts (see `docs/migration-map.csv`), 34 media items, comments.
2. Rank Math per-post SEO (title/description/focus keyphrase/OG image) extracted → mapped to Astro frontmatter.
3. Every media URL referenced by content exists in the backup (checksum/byte-size vs. live).
4. **Restore test (Gate 0 evidence):** local Docker `wordpress` + `mysql`, import `db.sql` (+ WXR if needed), confirm the site renders → recorded in a Gate-0 evidence doc.
5. Drafts and remaining media (6 non-public items) merged into the migration map.

## D. Security

- Keep everything under `.private/` (0700) — outside all repositories; nothing is committed or pushed.
- `wp-config.php`/`db.sql` contain DB credentials: fine locally in `.private/`, but redact before sharing anywhere else.
- Public blog content only — still sanitize any tenant/customer screenshots found in media during review (Phase 3).
