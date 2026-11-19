#!/usr/bin/env python3
"""WXR -> Astro Markdown converter for using-it.dk.

Usage: python3 scripts/wxr-to-md.py <export.xml> <out_dir>
Produces:
  <out_dir>/content/posts/<slug>.md   (published + draft posts)
  <out_dir>/content/pages/<slug>.md   (published pages)
  <out_dir>/docs/migration-map.csv    (wordpress_id -> content_id -> original_url -> new_url -> status)
"""
import csv
import html
import re
import sys
import os
from pathlib import Path

def g(it, tag):
    m = re.search(rf'<{re.escape(tag)}><!\[CDATA\[(.*?)\]\]></{re.escape(tag)}>', it, re.S)
    if not m:
        m = re.search(rf'<{re.escape(tag)}>(.*?)</{re.escape(tag)}>', it, re.S)
    return m.group(1).strip() if m else ''

def slugify_cat(name):
    s = name.lower().strip()
    s = s.replace('intune / mem', 'intune').replace('mem', 'intune')
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s

CODE_fence_re = re.compile(r'<!-- wp:code -->\s*<pre[^>]*>\s*<code>(?:<code>)?(.*?)(?:</code>)?</code>\s*</pre>\s*<!-- /wp:code -->', re.S)

def guess_lang(code):
    head = code.strip().lower()
    for kw in ('get-', 'set-', 'new-', 'install-', 'param(', 'foreach', '$', 'invoke-', 'add-', 'cmd /c'):
        if kw in head:
            return 'powershell'
    if head.startswith(('{', '[')) or '"key' in head or "'key" in head:
        return 'json'
    return 'text'

def convert_code(m):
    code = m.group(1)
    code = re.sub(r'</?code>', '', code)
    code = re.sub(r'<br\s*/?>', '\n', code)
    code = html.unescape(code)
    code = code.strip()
    lang = guess_lang(code)
    return f'\n```{lang}\n{code}\n```\n'

def html_to_md(content):
    content = re.sub(r'<!-- /?wp:[^>]*-->', '', content)
    content = CODE_fence_re.sub(convert_code, content)
    # bare pre/code fallback
    content = re.sub(r'<pre[^>]*>\s*<code>(.*?)</code>\s*</pre>', lambda m: '\n```\n' + re.sub(r'<br\s*/?>', '\n', html.unescape(m.group(1))).strip() + '\n```\n', content, flags=re.S)
    # headings
    content = re.sub(r'<h([1-4])[^>]*>\s*<strong>(.*?)</strong>\s*</h\1>', lambda m: '#'*(int(m.group(1))+0) + ' ' + m.group(2), content, flags=re.S)
    content = re.sub(r'<h([1-4])[^>]*>(.*?)</h\1>', lambda m: '#'*int(m.group(1)) + ' ' + re.sub('<[^>]+>', '', m.group(2)).strip(), content, flags=re.S)
    # images -> markdown, strip size suffix urls are kept as-is
    content = re.sub(r'<img[^>]*src="([^"]+)"[^>]*alt="([^"]*)"[^>]*/?>', lambda m: f'![{m.group(2)}]({m.group(1)})', content)
    content = re.sub(r'<img[^>]*src="([^"]+)"[^>]*/?>', lambda m: f'![]({m.group(1)})', content)
    # lists
    content = re.sub(r'<li[^>]*>', '- ', content)
    # links
    content = re.sub(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', lambda m: f'[{m.group(2)}]({m.group(1)})', content, flags=re.S)
    # emphasises inside paragraphs
    content = re.sub(r'<strong>(.*?)</strong>', r'**\1**', content, flags=re.S)
    content = re.sub(r'<em>(.*?)</em>', r'*\1*', content, flags=re.S)
    content = re.sub(r'<blockquote[^>]*>', '\n> ', content)
    # inline code -> backticks (single line)
    content = re.sub(r'<code>([^<\n]*)</code>', r'`\1`', content)
    # strip any residual code tags (e.g. double-wrapped fences)
    content = re.sub(r'</?code>', '', content)
    # paragraphs
    content = re.sub(r'</p>\s*', '\n\n', content)
    content = re.sub(r'<p[^>]*>', '', content)
    content = re.sub(r'<ul[^>]*>|</ul>|</li>', '', content)
    content = re.sub(r'<div[^>]*>|</div>', '', content)
    content = re.sub(r'\n{3,}', '\n\n', content)
    return content.strip()

def fm_escape(s):
    return s.replace('"', "'").strip()

def yaml_fm(d):
    lines = ['---']
    for k, v in d.items():
        if isinstance(v, list):
            lines.append(f'{k}:')
            for x in v:
                lines.append(f'  - "{fm_escape(x) if isinstance(x,str) else x}"')
        elif isinstance(v, bool):
            lines.append(f'{k}: {str(v).lower()}')
        else:
            lines.append(f'{k}: "{fm_escape(str(v))}"')
    lines.append('---')
    return '\n'.join(lines)

def main(wxr, out):
    data = open(wxr, encoding='utf-8').read()
    items = re.findall(r'<item>(.*?)</item>', data, re.S)
    Path(out, 'content/posts').mkdir(parents=True, exist_ok=True)
    Path(out, 'content/pages').mkdir(parents=True, exist_ok=True)
    Path(out, 'docs').mkdir(parents=True, exist_ok=True)
    rows = []
    for it in items:
        pt, st = g(it, 'wp:post_type'), g(it, 'wp:status')
        if pt not in ('post', 'page'):
            continue
        title = html.unescape(g(it, 'title'))
        slug0 = g(it, 'wp:post_name')
        if title in ('', 'Blog'):
            if slug0 in ('about-me',):
                title = 'About me'
            else:
                continue  # empty placeholder
        content = html_to_md(g(it, 'content:encoded'))
        if not content:
            continue
        pid = g(it, 'wp:post_id')
        slug = g(it, 'wp:post_name') or f'post-{pid}'
        cats = [html.unescape(c) for c in re.findall(r'<category domain="category"[^>]*><!\[CDATA\[(.*?)\]\]></category>', it)]
        tags = [html.unescape(c) for c in re.findall(r'<category domain="post_tag"[^>]*><!\[CDATA\[(.*?)\]\]></category>', it)]
        cats = [slugify_cat(c) for c in cats if slugify_cat(c) and slugify_cat(c) != 'uncategorized']
        date = g(it, 'wp:post_date')
        mod = g(it, 'wp:post_modified')
        draft = 'true' if st in ('draft', 'pending', 'auto-draft') else 'false'
        is_home_draft = (title == '' and slug == '')
        desc = html.unescape(g(it, 'excerpt:encoded')).strip()
        fm = {
            'title': title,
            'description': desc,
            'pubDate': date,
            'updatedDate': mod if mod != date else date,
            'slug': slug,
            'draft': st in ('draft', 'pending', 'auto-draft'),
        }
        if pt == 'post':
            fm['categories'] = cats if cats else ['intune']
            fm['tags'] = tags if tags else []
            fm['wordpress_id'] = pid
            fm['original_url'] = f'https://using-it.dk/{slug}/'
            subdir = 'content/posts'
        else:
            fm['wordpress_id'] = pid
            fm['original_url'] = f'https://using-it.dk/{slug}/'
            subdir = 'content/pages'
        doc = yaml_fm(fm) + '\n\n' + content + '\n'
        path = Path(out, subdir, f'{slug}.md')
        path.write_text(doc, encoding='utf-8')
        new_url = ('' if fm['draft'] else f"/{slug}/")
        rows.append([pid, slug, f'https://using-it.dk/{slug}/', new_url or '(draft)', st, pt])
    with open(Path(out, 'docs/migration-map.csv'), 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(['wordpress_id', 'content_id', 'original_url', 'new_url', 'wp_status', 'type'])
        w.writerows(rows)
    print(f"converted: {len(rows)} items")

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])