import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// WordPress permalinks end with "/" — keep directory build + trailing slash
// so migrated URLs keep their exact original shape.
export default defineConfig({
  site: 'https://using-it.dk',
  trailingSlash: 'always',
  build: { format: 'directory' },
  integrations: [sitemap()],
  markdown: {
    shikiConfig: {
      theme: 'github-light',
      wrap: false,
    },
  },
});