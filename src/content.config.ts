import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const strList = z.array(z.string()).nullish().transform((v) => v ?? []);

const posts = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './content/posts' }),
  schema: z.object({
    title: z.string(),
    description: z.string().default(''),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    slug: z.string(),
    image: z.string().optional(),
    draft: z.boolean().default(false),
    categories: strList,
    tags: strList,
    wordpress_id: z.string().optional(),
    original_url: z.string().optional(),
    // Editorial pipeline contract (linkedin-content#2 / docs/editorial-flow.md)
    content_id: z.string().optional(),      // stable ID shared with linkedin-content stages + issue
    source_issue: z.string().optional(),    // e.g. https://github.com/xander-me/project-playbook/issues/36
    language: z.enum(['da', 'en']).default('en'),
    linkedin_post: z.string().optional(),   // path in linkedin-content/05-linkedin-posts/...
    review_status: z.enum(['idea', 'planned', 'challenge_review', 'drafted', 'technical_review', 'approved']).optional(),
    publish_status: z.enum(['draft', 'published']).default('draft'),
  }),
});

const pages = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './content/pages' }),
  schema: z.object({
    title: z.string(),
    description: z.string().default(''),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    slug: z.string(),
    image: z.string().optional(),
    draft: z.boolean().default(false),
    wordpress_id: z.string().optional(),
    original_url: z.string().optional(),
  }),
});

export const collections = { posts, pages };