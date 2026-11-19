# Migration — WordPress → Astro (using-it.dk 2.0)

References: project-playbook #36 (brand), #50 (migration plan), #51 (content audit).

## State (19 Nov 2026)

- **Content migrated**: all 9 published WP posts + 6 published pages converted to
  `content/posts/*.md` / `content/pages/*.md` with original slugs, dates and categories,
  via `scripts/wxr-to-md.py` from the WXR export `using-it.WordPress.2026-11-19.xml`.
- **Drafts preserved**: 8 WP drafts exported with `draft: true` (Astro excludes them
  from production builds, but the content survives for review/refresh).
- **Original URLs preserved**: posts live at `/blog/<original-slug>/`; pages keep their
  original slugs at site root (`/about-me/`, `/remote-support/`, `/youtube/`, `/tools-2/`).

## URL / redirect map

| Old URL | New URL | Method |
| --- | --- | --- |
| `/blogposts/` | `/blog/` | meta-refresh now → **301 on Simply.com at cutover** |
| `/microsoft-licenses/` | `/licensing/` | meta-refresh now → **301 at cutover** |
| all WP post permalinks (`/<slug>/`) | **unchanged** (root catch-all serves them) | none |
| `/about-me/`, `/remote-support/`, `/youtube/`, `/tools-2/` | unchanged | none |
| `/timecalc/timecalc.html`, `/timecalc/BO.html` | unchanged | **never overwrite/delete** |

Posts keep their exact original URLs via the root catch-all (`src/pages/[...slug].astro`),
so **no server-level redirects are needed for articles** — only the two meta-refresh
paths above become real 301s at cutover (add to `.htaccess` on Simply.com, verify HTTP codes).

## Media

Images inside migrated posts still point to **absolute** `https://using-it.dk/wp-content/...`
URLs. That works while WordPress hosting stays live. Before WP retirement:

1. Run `python3 scripts/fetch-media.py docs/media-list.txt public` (downloads all
   wp-content files referenced by content into the repo)
2. Run `python3 scripts/localize-media.py content/` (rewrites absolute URLs to `/wp-content/...`)
3. Commit media (or serve `/wp-content/` from static hosting root)

## Publishing flow (new posts)

```bash
npm run new "My next article title"   # scaffold with checklist frontmatter
npm run dev                            # preview at localhost:4321
# edit content/posts/<slug>.md, set draft: false after approval, push
```

## Cutover checklist (project-playbook #50, Phase 6)

- [ ] Full backup of WP (DB + wp-content) taken and tested
- [ ] Media downloaded & localized (see above)
- [ ] `.htaccess` 301 rules generated from `docs/migration-map.csv` and verified live
- [ ] `/timecalc/` paths deployed and smoke-tested FIRST
- [ ] DNS switched in Simply.com (no destructive deletion of anything)
- [ ] Post-launch: check Search Console coverage, broken links, RSS readers