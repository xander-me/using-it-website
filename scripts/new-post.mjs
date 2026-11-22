#!/usr/bin/env node
/**
 * new-post.mjs — blog post scaffold ("publishing template", project-playbook#36 Workstream B)
 * Usage: npm run new "My great article title"
 * Creates content/posts/<slug>.md with full frontmatter + LinkedIn draft placeholder.
 */
import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const title = process.argv[2];
if (!title) {
  console.error('Usage: npm run new "Article title"');
  process.exit(1);
}
const slug = title.toLowerCase()
  .replace(/[^a-z0-9\s-]/g, '')
  .trim().replace(/\s+/g, '-').replace(/-+/g, '-');
const dir = join(process.cwd(), 'content/posts');
const file = join(dir, `${slug}.md`);
if (existsSync(file)) {
  console.error(`Already exists: ${file}`);
  process.exit(1);
}
const now = new Date().toISOString().slice(0, 16).replace('T', ' ');
const fm = `---
title: "${title.replace(/"/g, '\'')}"
description: ""
pubDate: "${now}"
slug: "${slug}"
draft: true
publish_status: "draft"
categories:
  - "intune"
tags: []
original_url: ""
# Editorial pipeline (docs/editorial-flow.md, linkedin-content#2):
content_id: ""        # stable ID, e.g. uit-2026-001 — shared with linkedin-content stages
source_issue: ""      # idea issue URL, e.g. https://github.com/xander-me/project-playbook/issues/NN
language: "en"        # da | en
linkedin_post: ""     # path in linkedin-content/05-linkedin-posts/<lang>/<content_id>.md
review_status: "idea" # idea -> planned -> challenge_review -> drafted -> technical_review -> approved
---

Write the article here. Publishing checklist (project-playbook#36):

- [ ] One clear search intent; title matches what users search for
- [ ] Lead paragraph answers the question in plain language
- [ ] Code tested; screenshots redacted; alt text on all images
- [ ] Version/product names verified against current Microsoft docs
- [ ] Thumbnail generated (16:9, brand tokens from brand/BRAND-GUIDELINES.md)
- [ ] LinkedIn derivative drafted in linkedin-content (05-linkedin-posts), path set in frontmatter
- [ ] review_status: approved and human approval before draft: false / publish_status: published
`;

mkdirSync(dir, { recursive: true });
writeFileSync(file, fm, 'utf8');
console.log(`Created: ${file}`);
console.log(`Next: fill in content, set draft: false after approval.`);