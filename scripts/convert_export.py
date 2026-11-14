"""Convert the WordPress/Elementor export into Astro content collections + copy referenced media.

Outputs:
  src/content/pages/*.md   — long-tail pages (frontmatter carries the full URL path)
  src/content/staff/*.md    — faculty & staff directory entries
  src/content/events/*.md   — events (home "Upcoming Events" + calendar lists)
  src/content/news/*.md     — news items (home "Latest News")
  public/uploads/...       — content images (mirrored old paths)
  src/assets/...            — brand + staff + hero images for the image pipeline
Idempotent: rewrites what it owns.
"""
import json, glob, os, re, shutil, html
from datetime import datetime

ROOT = r'C:/Code/PassportSchool'
E = ROOT + '/data/export/passport-export'
UP = E + '/uploads'

PAGES_DIR = ROOT + '/src/content/pages'
STAFF_DIR = ROOT + '/src/content/staff'
EVENTS_DIR = ROOT + '/src/content/events'
NEWS_DIR = ROOT + '/src/content/news'
PUB_UP = ROOT + '/public/uploads'
ASSETS = ROOT + '/src/assets'

SPECIAL_PAGES = {
    'home-page', 'faculty-and-staff', 'school-calendar', 'smsoptin', 'about-us',
    'parents', 'parents-2', 'students', 'students-2',
}
HUB_REDIRECTS = {'parents-2': '/parents/', 'students-2': '/students/'}

def load(f):
    d = json.load(open(f))
    return json.loads(d) if isinstance(d, str) else d

def slugify(s):
    s = re.sub(r'[^a-z0-9]+', '-', (s or '').lower()).strip('-')
    return s or 'item'

def decode(s):
    return html.unescape(s or '')

def strip_tags(s):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', s or '')).strip()

def url_to_local(u):
    if not u:
        return None
    m = re.search(r'wp-content/uploads/(.+?)(?:\?|$)', u)
    if not m:
        return None
    rel = m.group(1)
    loc = os.path.join(UP, *rel.split('/'))
    return loc if os.path.exists(loc) else None

def copy_public(u, alt=''):
    """Copy an uploads image to public/uploads mirroring its old path; return web path."""
    loc = url_to_local(u)
    if not loc:
        return None, None
    rel = os.path.relpath(loc, UP).replace(os.sep, '/')
    dst = os.path.join(PUB_UP, *rel.split('/'))
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if not os.path.exists(dst):
        shutil.copy2(loc, dst)
    return '/uploads/' + rel, alt

def html_to_md(s):
    s = s or ''
    s = re.sub(r'<br\s*/?>', '\n', s, flags=re.I)
    s = re.sub(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>', r'[\2](\1)', s, flags=re.S | re.I)
    for tag in ('h1', 'h2', 'h3', 'h4'):
        s = re.sub(r'<%s[^>]*>' % tag, '\n\n#### ', s, flags=re.I)
        s = re.sub(r'</%s>' % tag, '\n', s, flags=re.I)
    s = re.sub(r'<li[^>]*>', '\n- ', s, flags=re.I)
    s = re.sub(r'</li>', '', s, flags=re.I)
    s = re.sub(r'</ul>|</ol>', '\n', s, flags=re.I)
    s = re.sub(r'<strong[^>]*>|<b>', '**', s, flags=re.I)
    s = re.sub(r'</strong>|</b>', '**', s, flags=re.I)
    s = re.sub(r'<em[^>]*>|<i>', '*', s, flags=re.I)
    s = re.sub(r'</em>|</i>', '*', s, flags=re.I)
    s = re.sub(r'</p>', '\n\n', s, flags=re.I)
    s = re.sub(r'<[^>]+>', '', s)
    s = decode(s)
    s = re.sub(r'\n{3,}', '\n\n', s)
    return s.strip()

pages = json.load(open(E + '/pages.json'))
by_slug = {p['post_name']: p for p in pages}
trees = {}
for f in glob.glob(E + '/el/*.json'):
    trees[int(os.path.basename(f)[:-5])] = load(f)

def walk(e):
    yield e
    for c in e.get('elements', []):
        yield from walk(c)

MARKER = {'form', 'ha-pdf-view', 'google_maps', 'video', 'media-carousel', 'countdown',
          'facebook-page', 'shortcode', 'sitemap', 'tme-text_rotator', 'animated-headline'}

# ---------------- staff ----------------
os.makedirs(STAFF_DIR, exist_ok=True)
staff_count = 0
pid = [p['ID'] for p in pages if p['post_name'] == 'faculty-and-staff']
pid = pid[0] if pid else None
staff_files = []
if pid:
    dept = 'Staff'
    for e in trees[pid]:
        for w in walk(e):
            s = w.get('settings') if isinstance(w.get('settings'), dict) else {}
            if w.get('widgetType') == 'heading' and s.get('title'):
                dept = strip_tags(s['title'])
            elif w.get('widgetType') == 'profile-card-elementor-widget':
                name = strip_tags(s.get('name') or '')
                role = strip_tags(s.get('position') or '')
                email = ''
                for soc in (s.get('social_icon_list') or []):
                    link = (soc or {}).get('link') or {}
                    if 'mailto:' in str(link.get('url', '')):
                        candidate = link['url'].replace('mailto:', '').strip()
                        if re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', candidate):
                            email = candidate
                photo_rel = None
                pu = (s.get('profile_image') or {}).get('url', '')
                loc = url_to_local(pu)
                if loc:
                    rel = 'staff/' + slugify(name) + os.path.splitext(loc)[1].lower()
                    dst = os.path.join(ASSETS, *rel.split('/'))
                    os.makedirs(os.path.dirname(dst), exist_ok=True)
                    if not os.path.exists(dst):
                        shutil.copy2(loc, dst)
                    photo_rel = rel
                fname = slugify(name) + '.md'
                with open(os.path.join(STAFF_DIR, fname), 'w', encoding='utf-8') as fh:
                    fh.write('---\n')
                    fh.write('title: %s\n' % json.dumps(name)[1:-1])
                    fh.write('role: %s\n' % json.dumps(role)[1:-1])
                    if photo_rel:
                        fh.write('photo: /src/assets/%s\n' % photo_rel.replace('src/assets/', ''))
                    if email:
                        fh.write('email: %s\n' % email)
                    fh.write('dept: %s\n' % json.dumps(dept)[1:-1])
                    fh.write('---\n')
                staff_files.append((name, role, dept, photo_rel))
                staff_count += 1

# ---------------- events + news (home-page lists) ----------------
os.makedirs(EVENTS_DIR, exist_ok=True)
for f in glob.glob(EVENTS_DIR + '/*.md'):
    os.remove(f)
os.makedirs(NEWS_DIR, exist_ok=True)
for f in glob.glob(NEWS_DIR + '/*.md'):
    os.remove(f)

def parse_date(title):
    t = (title or '').strip()
    t = re.sub(r'(\w+) (\d+)-\d+', r'\1 \2', t)  # "November 23-27, 2026" -> "November 23, 2026"
    for fmt in ('%B %d, %Y', '%b %d, %Y'):
        try:
            return datetime.strptime(t, fmt).date().isoformat()
        except ValueError:
            continue
    return None

home_pid = [p['ID'] for p in pages if p['post_name'] == 'home-page'][0]
mode = None
event_count = news_count = 0
for e in trees[home_pid]:
    for w in walk(e):
        s = w.get('settings') if isinstance(w.get('settings'), dict) else {}
        wt = w.get('widgetType')
        if wt == 'heading' and s.get('title'):
            h = strip_tags(s['title']).lower()
            mode = 'events' if 'upcoming events' in h else ('news' if 'latest news' in h else mode)
        elif wt == 'ile-item-lists-elementor-widget' and mode:
            for it in (s.get('material_item_lists') or []):
                title = strip_tags(it.get('material_list_items_title', ''))
                content = html_to_md(it.get('material_list_items_content', ''))
                link = ((it.get('material_list_items_link') or {}).get('url') or '')
                d = parse_date(title)
                if d:
                    fn = '%s-%s.md' % (d, slugify(content or title))
                    with open(os.path.join(EVENTS_DIR, fn), 'w', encoding='utf-8') as fh:
                        fh.write('---\ntitle: %s\ndate: %s\n' % (json.dumps(content or title)[1:-1], d))
                        if link:
                            fh.write('link: %s\n' % link)
                        fh.write('---\n')
                        if title and title.strip().lower() not in (content or '').lower():
                            fh.write('\n%s\n' % title)
                    event_count += 1
                elif mode == 'news' and (content or title):
                    nd = d or '2026-11-14'
                    fn = '%s-%s.md' % (nd, slugify(content or title)[:40])
                    with open(os.path.join(NEWS_DIR, fn), 'w', encoding='utf-8') as fh:
                        fh.write('---\ntitle: %s\ndate: %s\n' % (json.dumps(content or title)[1:-1], nd))
                        fh.write('---\n')
                    news_count += 1

# ---------------- long-tail pages ----------------
os.makedirs(PAGES_DIR, exist_ok=True)
for f in glob.glob(PAGES_DIR + '/*.md'):
    os.remove(f)

sitemap = {}
import xml.etree.ElementTree as ET
sm = ET.parse(E + '/pages-sitemap.xml').getroot()
for loc in sm.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
    u = loc.text.strip().replace('https://www.passportcharter.org/', '')
    parts = [x for x in u.strip('/').split('/') if x]
    if parts:
        sitemap[parts[-1]] = '/' + '/'.join(parts) + '/'

page_out = []
for p in pages:
    slug = p['post_name']
    if slug in SPECIAL_PAGES or p['ID'] not in trees:
        continue
    lines = []
    for e in trees[p['ID']]:
        for w in walk(e):
            wt = w.get('widgetType')
            s = w.get('settings') if isinstance(w.get('settings'), dict) else {}
            if wt == 'heading' and s.get('title'):
                lines.append('\n\n## ' + strip_tags(s['title']) + '\n')
            elif wt == 'text-editor':
                md = html_to_md(s.get('editor', ''))
                if md:
                    lines.append('\n\n' + md + '\n')
            elif wt == 'image':
                img = (s.get('image') or {})
                web, _ = copy_public(img.get('url', ''), img.get('alt', ''))
                if web:
                    lines.append('\n\n![%s](%s)\n' % (img.get('alt') or '', web))
            elif wt == 'icon-box':
                t = strip_tags(s.get('title', ''))
                d = html_to_md(s.get('description_text', ''))
                icon_img = ((s.get('selected_image') or {}) if isinstance(s.get('selected_image'), dict) else {}).get('url', '')
                web, _ = copy_public(icon_img, t)
                link = ((s.get('link') or {}).get('url') or '')
                if t and web and link:
                    lines.append('\n- [![%s](%s)](%s) — %s\n' % (t, web, link, t))
                elif t:
                    entry = '**%s**' % t
                    if d:
                        entry += ' — ' + d.replace('\n', ' ')
                    if link:
                        entry = '[%s](%s)' % (entry, link) if False else entry + '\n  <%s>' % link
                    lines.append('\n- ' + entry + '\n')
            elif wt == 'ile-item-lists-elementor-widget':
                for it in (s.get('material_item_lists') or []):
                    t = strip_tags(it.get('material_list_items_title', ''))
                    c = html_to_md(it.get('material_list_items_content', ''))
                    link = ((it.get('material_list_items_link') or {}).get('url') or '')
                    entry = ('**%s** — %s' % (t, c.replace('\n', ' '))) if t and c else (c or t)
                    if link:
                        entry += ' ([link](%s))' % link
                    lines.append('\n- ' + entry)
                lines.append('')
            elif wt in MARKER:
                lines.append('\n<!-- elementor:%s -->\n' % wt)
    body = ''.join(lines).strip()
    full_path = sitemap.get(slug, '/' + slug + '/')
    title = decode(p['post_title'])
    fn = slug + '.md'
    with open(os.path.join(PAGES_DIR, fn), 'w', encoding='utf-8') as fh:
        fh.write('---\ntitle: %s\npath: %s\nupdated: %s\n---\n\n' % (
            json.dumps(title)[1:-1], full_path, json.dumps(p['post_modified'][:10])))
        fh.write(body + '\n')
    page_out.append((slug, len(body)))

print('STAFF:', staff_count)
for n, r, d, ph in staff_files:
    print('  -', n, '|', r, '|', d, '| photo:', os.path.basename(ph) if ph else 'NONE')
print('EVENTS:', event_count, ' NEWS:', news_count)
print('PAGES:', len(page_out))
for s, ln in sorted(page_out):
    print('  -', s, '(%d chars)' % ln)
imgs = sum(len([f for f in fs]) for _, _, fs in os.walk(PUB_UP))
print('public/uploads files:', imgs)
