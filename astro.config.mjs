import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// WordPress permalinks end with "/" — keep directory build + trailing slash
// so migrated URLs keep their exact original shape.
//
// SITE_BASE is set only for the GitHub Pages preview build
// (https://xander-me.github.io/using-it-website/). Production keeps
// root-relative URLs on https://using-it.dk.
const siteBase = process.env.SITE_BASE ?? '';
export default defineConfig({
  site: siteBase ? 'https://xander-me.github.io' : 'https://using-it.dk',
  base: siteBase,
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