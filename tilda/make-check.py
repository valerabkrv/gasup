#!/usr/bin/env python3
"""Собирает из блоков tilda/blocks страницу-имитацию Тильды, чтобы поймать конфликты стилей.

    python3 tilda/make-check.py --img-base img/ --out tilda/_split-check.html
"""
import argparse, os, glob

HEAD = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Tilda split check — GASUP</title><style>
*{box-sizing:content-box}
body{margin:0;font-family:Arial,Helvetica,sans-serif;color:#000;background:#fff;font-size:16px;line-height:1.55}
img{max-width:100%;height:auto;border:0}
a{color:#ff8562;text-decoration:none}
h1,h2,h3,h4{font-weight:400;margin:0;font-family:Arial}
ul,li{list-style:none;margin:0;padding:0}
p{margin:0}
input,button,textarea,select{font-family:Arial;font-size:16px;color:#000;background:#fff;border:1px solid #ccc}
</style></head><body class="t-body"><div id="allrecords" class="t-records">
"""
FOOT = "</div></body></html>\n"

ap = argparse.ArgumentParser()
ap.add_argument('--blocks', default=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'blocks'))
ap.add_argument('--img-base', default='')
ap.add_argument('--out', required=True)
ap.add_argument('--skip', default='', help='файлы через запятую, которые не вставлять (например 15-modal.html)')
a = ap.parse_args()

skip = {s.strip() for s in a.skip.split(',') if s.strip()}
parts = [HEAD]
for path in sorted(glob.glob(os.path.join(a.blocks, '*.html'))):
    if os.path.basename(path) in skip:
        continue
    html = open(path, encoding='utf-8').read()
    if a.img_base:
        html = html.replace('https://valerabkrv.github.io/gasup/img/', a.img_base)
    parts.append('<div class="t-rec" data-record-type="123">\n%s</div>\n' % html)
parts.append(FOOT)
open(a.out, 'w', encoding='utf-8').write(''.join(parts))
print('готово:', a.out, os.path.getsize(a.out), 'байт')
