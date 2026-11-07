#!/usr/bin/env python3
"""Regenerate the Reboc policy PDFs.

The Human Rights Policy PDF is generated from human-rights-policy.html, so the
published page and the PDF can never drift apart. The Risk Analysis PDF has no
web page and is generated from its own source in this folder.

Usage:  python3 docs-source/build.py     (run from the repository root)
"""
import os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'docs-source')
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>%(title)s</title>
<link rel="stylesheet" href="print.css">
</head>
<body>
<div class="doc-head">
    <div class="brand">REBOC<span>.</span></div>
    <h1>%(heading)s</h1>
    <div class="meta">Reboc B.V., Den Haag, Netherlands &bull; %(version)s</div>
</div>
%(content)s
<div class="footer-note">
    Reboc B.V. &bull; KvK/Chamber of Commerce: 27263706 &bull; BTW/VAT: NL817331025B01 &bull; Goudenregenplein 61, 2565 GK Den Haag, Netherlands
</div>
</body>
</html>
'''

def extract(page, heading):
    html = open(os.path.join(ROOT, page), encoding='utf-8').read()
    m = re.search(r'<div class="content">(.*?)\n    </div>', html, re.S)
    if not m:
        sys.exit('could not find the content block in %s' % page)
    v = re.search(r'<div class="page-header">.*?<p>(.*?)</p>', html, re.S)
    return TEMPLATE % {
        'title': 'Reboc B.V. - ' + heading,
        'heading': heading,
        'version': v.group(1) if v else '',
        'content': m.group(1),
    }

def to_pdf(src_html, out_pdf):
    cmd = [CHROME, '--headless=new', '--disable-gpu', '--no-sandbox',
           '--no-pdf-header-footer', '--print-to-pdf=' + out_pdf,
           '--virtual-time-budget=4000', 'file://' + src_html]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if not os.path.exists(out_pdf):
        sys.exit('PDF not produced for %s\n%s' % (src_html, r.stderr[-800:]))
    print('  %-46s %7d bytes' % (os.path.basename(out_pdf), os.path.getsize(out_pdf)))

def main():
    if not os.path.exists(CHROME):
        sys.exit('Google Chrome not found at %s' % CHROME)
    print('Building policy PDFs...')

    gen = os.path.join(SRC, 'human-rights-policy.generated.html')
    open(gen, 'w', encoding='utf-8').write(extract('human-rights-policy.html', 'Human Rights Policy'))
    to_pdf(gen, os.path.join(ROOT, 'Reboc_BV_Human_Rights_Policy.pdf'))

    to_pdf(os.path.join(SRC, 'human-rights-risk-analysis.html'),
           os.path.join(ROOT, 'Reboc_BV_Human_Rights_Risk_Analysis_Process.pdf'))
    print('Done.')

if __name__ == '__main__':
    main()
