# using-website

**using-it.dk 2.0**: static blog & site, migrated from WordPress.

Brand: "Nordisk Ro" (see `brand/BRAND-GUIDELINES.md`) · Planning: `project-playbook` #36 / #50 / #51.

## Quick start

```bash
npm install
npm run dev          # http://localhost:4321
npm run build        # static output in dist/
npm run new "Title"  # scaffold a new blog post (with publishing checklist)
```

## Structure

```
src/
  pages/            routes: / , /blog/ (archive), root catch-all = migrated WP URLs
  layouts/          Base, Article (TOC-less, copy-button, licensing CTA)
  components/       Header, Footer, PostCard, LicensingCta
  styles/           tokens.css (brand tokens) + global.css
content/
  posts/            migrated + future blog posts (Markdown, draft flag)
  pages/            migrated WP pages (about-me, remote-support, youtube, tools-2, ...)
docs/               MIGRATION.md, migration-map.csv, media-list.txt
brand/              BRAND-GUIDELINES.md, signature.html
scripts/            wxr-to-md.py, new-post.mjs, fetch-media.py, localize-media.py
.github/workflows/  ci.yml (build + internal link check artifact)
```

## Non-negotiables (from project-playbook #50)

- Never deploy destructively over `/timecalc/` or sibling tools on Simply.com.
- Original public article URLs must stay reachable (server 301 where changed).
- No automatic LinkedIn posting or production deploy without explicit approval.
- Deploy credentials only as narrowly scoped GitHub Actions secrets.

## Fonts

Self-host for privacy/perf: `npm install @fontsource-variable/inter @fontsource/jetBrains-mono`
(uncomment imports in `src/styles/global.css`).