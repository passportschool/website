"""Dist-wide internal link integrity check: every local href must resolve to a built file."""
import os, re, sys
from html.parser import HTMLParser

DIST = r'C:/Code/PassportSchool/dist'

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
    def handle_starttag(self, tag, attrs):
        if tag in ('a', 'link'):
            for k, v in attrs:
                if k in ('href', 'src') and v:
                    self.hrefs.append(v)

targets = set()
for root, _, files in os.walk(DIST):
    for f in files:
        if f.endswith('.html'):
            targets.add(os.path.relpath(os.path.join(root, f), DIST).replace(os.sep, '/').replace('index.html', '').rstrip('/').lower())

missing = {}
total = 0
for root, _, files in os.walk(DIST):
    for f in files:
        if not f.endswith('.html'):
            continue
        path = os.path.join(root, f)
        rel = os.path.relpath(path, DIST).replace(os.sep, '/')
        parser = Links()
        parser.feed(open(path, encoding='utf-8', errors='ignore').read())
        for href in parser.hrefs:
            if not href.startswith('/') or href.startswith('//'):
                continue
            if href.startswith(('/uploads', '/_astro', '/favicon')) and not href.endswith(('.html',)):
                # static asset: check the file exists
                asset = os.path.join(DIST, href.lstrip('/').split('?')[0].split('#')[0])
                if not os.path.exists(asset):
                    missing.setdefault(rel, []).append(href)
                total += 1
                continue
            href = href.split('?')[0].split('#')[0]
            if not href:
                continue
            if href.rstrip('/').lstrip('/').lower() not in targets:
                missing.setdefault(rel, []).append(href)
            total += 1

print(f'checked {total} local links across all built pages')
if missing:
    for src, bad in sorted(missing.items()):
        for b in bad:
            print('BROKEN:', src, '->', b)
    sys.exit(1)
print('OK: zero broken internal links')
