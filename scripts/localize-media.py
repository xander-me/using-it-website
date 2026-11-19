#!/usr/bin/env python3
"""Rewrite absolute https://using-it.dk/wp-content/... image URLs in migrated
Markdown to local /wp-content/... paths.
Usage: python3 scripts/localize-media.py content/"""
import re
import sys
from pathlib import Path

def main(root):
    n = 0
    for f in Path(root).rglob('*.md'):
        text = f.read_text(encoding='utf-8')
        new = re.sub(r'https?://(?:www\.)?using-it\.dk/(wp-content/[^)\s]+)', r'/\1', text)
        if new != text:
            f.write_text(new, encoding='utf-8')
            n += len(re.findall(r'/wp-content/', new)) - len(re.findall(r'https?://[^)\s]*wp-content/', new))
            print('localized:', f)
    print('done')

if __name__ == '__main__':
    main(sys.argv[1])