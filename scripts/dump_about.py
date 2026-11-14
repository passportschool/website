"""Dump the about-us (contact) page tree text + any phone/email found anywhere in the export."""
import json, re

E = r'C:/Code/PassportSchool/data/export/passport-export'
pages = json.load(open(E + '/pages.json'))
pid = [p['ID'] for p in pages if p['post_name'] == 'about-us'][0]
d = json.load(open(E + '/el/%d.json' % pid))
d = json.loads(d) if isinstance(d, str) else d

def walk(e):
    yield e
    for c in e.get('elements', []):
        yield from walk(c)

print('==== ABOUT-US (Contact Us) TEXT ====')
for e in d:
    for w in walk(e):
        s = w.get('settings') if isinstance(w.get('settings'), dict) else {}
        t = w.get('widgetType')
        if t == 'heading' and s.get('title'):
            print('H:', s['title'])
        elif t == 'text-editor' and s.get('editor'):
            print('T:', re.sub(r'\s+', ' ', re.sub('<[^>]+>', ' ', s['editor']))[:600])
        elif t == 'form':
            ff = s.get('form_fields', [])
            print('FORM fields:', [(f.get('field_label'), f.get('field_type')) for f in ff])
            print('FORM email:', s.get('email_to'))

print()
print('==== PHONES / EMAILS ANYWHERE IN DB ====')
import gzip
db = gzip.open(E + '/db.sql.gz', 'rt', encoding='utf-8', errors='ignore').read()
for m in sorted(set(re.findall(r'\(407\) ?\d{3}[.-]?\d{4}|407-\d{3}-\d{4}|tel:\+?[\d\-\.]+', db)))[:10]:
    print('PHONE:', m)
for m in sorted(set(re.findall(r'[a-zA-Z0-9._%+-]+@passportcharter\.org', db)))[:15]:
    print('MAIL:', m)
