"""Inspect Elementor export trees: settings keys per widget type, page->special-widget map, referenced image URLs."""
import json, glob, os, re
from collections import Counter, defaultdict

E = r'C:/Code/PassportSchool/data/export/passport-export'
pages = json.load(open(E + '/pages.json'))
idmap = {p['ID']: p['post_name'] for p in pages}

def load(f):
    d = json.load(open(f))
    if isinstance(d, str):
        d = json.loads(d)
    return d

trees = {}
for f in glob.glob(E + '/el/*.json'):
    pid = int(os.path.basename(f)[:-5])
    try:
        trees[pid] = load(f)
    except Exception as ex:
        print('PARSE FAIL', pid, ex)

def walk(e):
    yield e
    for c in e.get('elements', []):
        yield from walk(c)

def find(e, wt):
    if e.get('widgetType') == wt:
        yield e
    for c in e.get('elements', []):
        yield from find(c, wt)

# 1) profile-card settings (faculty page)
print('==== PROFILE-CARD SAMPLE ====')
for pid, t in trees.items():
    if idmap.get(pid) == 'faculty-and-staff':
        cards = [w for e in t for w in find(e, 'profile-card-elementor-widget')]
        if cards:
            print('count:', len(cards))
            print(json.dumps(cards[0].get('settings', {}), indent=1)[:1500])
            for c in cards:
                s = c.get('settings', {})
                print('CARD:', s.get('name') or s.get('title'), '|', s.get('position') or s.get('role') or s.get('designation'),
                      '| img:', (s.get('image') or {}).get('url', '')[-60:])

# 2) ile-item-lists settings (home + calendar)
print()
print('==== ITEM-LISTS SAMPLES ====')
for slug in ('home-page', 'school-calendar'):
    pid = [i for i, s in idmap.items() if s == slug][0]
    t = trees.get(pid, [])
    lists = [w for e in t for w in find(e, 'ile-item-lists-elementor-widget')]
    for w in lists[:2]:
        print('--', slug, '--')
        print(json.dumps(w.get('settings', {}), indent=1)[:900])

# 3) smsoptin form settings
print()
print('==== FORM (smsoptin) ====')
pid = [i for i, s in idmap.items() if s == 'smsoptin'][0]
for e in trees.get(pid, []):
    for w in find(e, 'form'):
        s = w.get('settings', {})
        print('form fields:', s.get('form_fields'))
        print('buttons:', s.get('button_text'), '| submit actions:', s.get('submit_actions'), '| email:', s.get('email_to'), '| redirect:', s.get('redirect_to'))

# 4) page -> special widgets map + all referenced media URLs
print()
print('==== PAGE -> SPECIAL WIDGETS ====')
SPECIAL = {'form', 'ha-pdf-view', 'google_maps', 'video', 'media-carousel', 'countdown', 'facebook-page', 'shortcode', 'sitemap', 'tme-text_rotator', 'animated-headline'}
img_urls = Counter()
for pid, t in sorted(trees.items(), key=lambda kv: idmap.get(kv[0], '')):
    found = Counter()
    for e in t:
        for w in walk(e):
            wt = w.get('widgetType')
            if wt in SPECIAL:
                found[wt] += 1
            s = w.get('settings')
            if not isinstance(s, dict):
                s = {}
            for key in ('image', 'background_image', 'image_overlay'):
                v = s.get(key)
                if isinstance(v, dict) and v.get('url'):
                    img_urls[v['url']] += 1
            if wt == 'media-carousel':
                for sl in s.get('slides', []):
                    if isinstance(sl, dict) and sl.get('image', {}).get('url'):
                        img_urls[sl['image']['url']] += 1
    if found:
        print(idmap.get(pid, pid), '->', dict(found))

print()
print('==== REFERENCED IMAGE URLS (uploads-relative) ====')
for u, n in img_urls.most_common(40):
    print(n, u.replace('https://www.passportcharter.org/wp-content/uploads/', ''))
print('total unique referenced:', len(img_urls))

# 5) pdf/video/map targets
print()
print('==== PDF/VIDEO/MAP TARGETS ====')
for pid, t in trees.items():
    for e in t:
        for w in walk(e):
            s = w.get('settings', {})
            wt = w.get('widgetType')
            if wt == 'ha-pdf-view':
                print(idmap.get(pid), 'PDF:', str(s.get('pdf_url') or s.get('ha_pdf_url') or s.get('selected_pdf') or s.get('pdf'))[:120])
            if wt == 'video':
                print(idmap.get(pid), 'VIDEO:', str(s.get('video_url') or s.get('youtube_url') or s.get('link'))[:120])
            if wt == 'google_maps':
                print(idmap.get(pid), 'MAP:', str(s.get('address'))[:100], '|', str(s.get('link_to_google'))[:80])
