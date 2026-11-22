# Editorial flow — idea → article → LinkedIn (using-it.dk 2.0)

Date: 2026-11-22. Implements the cross-repo contract from [linkedin-content#2](https://github.com/xander-me/linkedin-content/issues/2) and project-playbook #36/#50 (Phase 4). **No automated LinkedIn posting** — manual copy/paste is the MVP until an official integration is approved.

## Repositories and roles

| Repo | Role |
| --- | --- |
| `project-playbook` issues | Idea inbox — raw, unedited idea notes live here (original notes preserved) |
| `linkedin-content` | Editorial source of truth: `00-idea-bank` → `01-raw-ideas` → `02-article-plans` → `03-challenge-review` → `04-articles/<lang>` → `05-linkedin-posts/<lang>` → `06-graphics-prompts` → `07-published` ledger |
| `using-it-website` (this repo) | Approved, canonical site content only (`content/posts`, `content/pages`) + site build/deploy |

## State machine (per content item)

`idea → triage → planned → challenge_review → drafted → technical_review → ready_for_approval → approved → published` (+ `blocked` / `archived`). Blog and LinkedIn statuses are tracked **independently** — a draft is never "published".

## Flow

1. **Capture** — loose idea as a GitHub issue (any fields optional except the idea) or a note in `linkedin-content/01-raw-ideas`. Raw text is never edited in place.
2. **Triage** — assign stable `content_id` (e.g. `uit-2026-001`), language, intent (blog / LinkedIn / both), owner. Dedupe against existing ideas.
3. **Plan** — `02-article-plans/<content_id>.md` from `99-templates/article-plan-template.md`.
4. **Challenge review** — `03-challenge-review/` stress-tests the claim and sources (human dialogue central).
5. **Draft** — `04-articles/<lang>/<content_id>.md`, then **sync approved draft into this repo** as `content/posts/<slug>.md` via PR with `draft: true`, `content_id`, `source_issue`, `linkedin_post`, `review_status` in frontmatter (`npm run new "Title"` scaffolds exactly this).
6. **Technical review** — verify Microsoft product behavior/versions/licensing against current docs; sanitize screenshots/tenant data.
7. **Derivative assets** — LinkedIn-native copy in `05-linkedin-posts/<lang>/<content_id>.md`, thumbnail/OG from `brand/BRAND-GUIDELINES.md` tokens (06-graphics-prompts).
8. **Approve** — PR review in this repo = blog approval gate; set `review_status: approved`, then `draft: false` / `publish_status: published` **only with explicit human approval**. Merge → CI builds → Pages preview deploy (automatic); production deploy only at approved cutover (Phase 6).
9. **Publish LinkedIn** — manual copy/paste from the approved `05-linkedin-posts` file (separate opt-in action; no autopost).
10. **Track** — record real blog URL + LinkedIn URL, timestamps and asset paths in `linkedin-content/07-published` and in the post frontmatter (`original_url` once live). No URL = not confirmed published.

## Contract fields (frontmatter, `src/content.config.ts`)

`content_id`, `source_issue`, `language`, `linkedin_post`, `review_status`, `publish_status`, plus existing `slug`, `original_url`, `wordpress_id`, `draft`. These same fields are mirrored in the linkedin-content stages and the issue, so one content item is traceable end-to-end without duplicate canonical copies.
