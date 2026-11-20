import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';


export async function GET(context) {
  const posts = (await getCollection('posts', ({ data }) => !data.draft))
    .sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());
  return rss({
    title: 'Using-IT',
    description: 'Modern endpoint management & IT consulting, written by a practitioner.',
    site: context.site ?? 'https://using-it.dk',
    items: posts.map((p) => ({
      title: p.data.title,
      description: p.data.description,
      pubDate: new Date(p.data.pubDate),
      link: `/${p.id}/`,
    })),
  });
}