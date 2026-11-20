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
    draft: z.boolean().default(false),
    categories: strList,
    tags: strList,
    wordpress_id: z.string().optional(),
    original_url: z.string().optional(),
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
    draft: z.boolean().default(false),
    wordpress_id: z.string().optional(),
    original_url: z.string().optional(),
  }),
});

export const collections = { posts, pages };