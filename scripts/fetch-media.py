#!/usr/bin/env python3
"""Download all wp-content media referenced by migrated content.
Usage: python3 scripts/fetch-media.py docs/media-list.txt public"""
import sys
import urllib.request
from pathlib import Path

def main(listfile, outdir):
    Path(outdir).mkdir(parents=True, exist_ok=True)
    urls = [u.strip() for u in open(listfile) if u.strip().startswith('http')]
    ok = miss = 0
    for url in urls:
        rel = url.split('using-it.dk/', 1)[1]
        dest = Path(outdir, rel)
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists():
            ok += 1
            continue
        try:
            urllib.request.urlretrieve(url, dest)
            ok += 1
            print('ok  ', rel)
        except Exception as e:
            miss += 1
            print('FAIL', rel, e)
    print(f'done: {ok} ok, {miss} missing')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])