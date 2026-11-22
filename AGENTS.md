# Project Agent Instructions — using-it-website

This repository is the working home for the using-it.dk 2.0 static site (Astro), migrated from WordPress. Shared workspace rules live in [project-playbook](https://github.com/xander-me/project-playbook) (decisions, portfolio model, handoff standard).

Read [README.md](README.md), [STATUS.md](STATUS.md) and [docs/MIGRATION.md](docs/MIGRATION.md) before working. Check live issues and CI before resuming.

## Core rules

- The GitHub Pages preview (https://xander-me.github.io/using-it-website/) deploys automatically from `main`. Production https://using-it.dk is still WordPress — **never deploy to production without explicit approval**.
- Never run destructive delete/sync over Simply.com `public_html`; `/timecalc/` and sibling tools must stay untouched.
- Original public article URLs must remain reachable; changed paths need verified server-level 301s.
- No automatic LinkedIn posting. No secrets in the repo — only narrowly scoped GitHub Actions secrets.
- New posts: `npm run new "Title"` (includes the publishing checklist). Keep drafts flagged `draft: true` — a draft is not live.
- Verify with `npm install && npm run build` before pushing; CI also runs the internal-link check on `main`.
- Keep brand rules in `brand/BRAND-GUIDELINES.md` (e.g. "Using-IT" naming, no em-dashes) and apply them to new content and assets.
