#!/usr/bin/env python3
"""Non-destructive live-site inventory for the using-it.dk migration (Phase 0/5).

Read-only: fetches the sitemap index, sub-sitemaps and well-known extra paths,
records HTTP status for each URL, and lists public WP REST posts/pages/media.
Writes CSV/JSON artifacts next to this script's ../docs/ folder.

Usage: python3 scripts/inventory_site.py [--out docs] [--base https://using-it.dk]
"""
import argparse
import csv
import json
import re
import sys
import urllib.request

BASE_DEFAULT = "https://using-it.dk"
EXTRA_PATHS = [
    "/feed/", "/timecalc/timecalc.html", "/timecalc/BO.html", "/timecalc/",
    "/tools/", "/wp-admin/", "/wp-login.php", "/xmlrpc.php", "/wp-json/",
    "/wp-content/uploads/",
]


def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": "using-it-migration-inventory/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode("utf-8", "replace"), dict(r.headers)
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace") if e.fp else "", dict(e.headers or {})
    except Exception as e:
        return 0, "", {"error": str(e)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="docs")
    ap.add_argument("--base", default=BASE_DEFAULT)
    args = ap.parse_args()
    base = args.base.rstrip("/")

    urls = set()
    status, body, _ = fetch(f"{base}/sitemap_index.xml")
    if status == 200:
        for loc in re.findall(r"<loc>([^<]+)</loc>", body):
            if loc.endswith(".xml"):
                s, sub, _ = fetch(loc)
                if s == 200:
                    urls.update(re.findall(r"<loc>([^<]+)</loc>", sub))
    for p in EXTRA_PATHS:
        urls.add(base + p)

    rows = []
    for u in sorted(urls):
        code, _, _ = fetch(u)
        rows.append((u, code))
        print(f"{code}\t{u}", file=sys.stderr)

    with open(f"{args.out}/url-inventory.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["url", "status"])
        w.writerows(rows)

    media = []
    page = 1
    while True:
        code, body, headers = fetch(
            f"{base}/wp-json/wp/v2/media?per_page=100&page={page}&_fields=id,date,mime_type,source_url"
        )
        if code != 200:
            break
        items = json.loads(body)
        if not items:
            break
        media.extend(items)
        total = int(headers.get("X-WP-Total", "0"))
        if len(media) >= total or len(items) < 100:
            break
        page += 1

    with open(f"{args.out}/media-inventory.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "mime_type", "source_url"])
        for m in sorted(media, key=lambda x: x["id"]):
            w.writerow([m["id"], m.get("mime_type", ""), m.get("source_url", "")])

    for kind in ("posts", "pages"):
        code, body, _ = fetch(
            f"{base}/wp-json/wp/v2/{kind}?per_page=100&_fields=id,date,modified,slug,link,status,featured_media,categories,tags"
        )
        if code == 200:
            with open(f"{args.out}/wp-{kind}.json", "w") as f:
                json.dump(json.loads(body), f, indent=2)

    print(f"{len(rows)} URLs, {len(media)} media items -> {args.out}/", file=sys.stderr)


if __name__ == "__main__":
    main()
