#!/usr/bin/env python3
"""Generate a PDF of each published version of the Terms & Conditions.

Agreements incorporate "the general terms" without naming a version, and the
terms page is overwritten in place when a new version is published. These PDFs
are the record of what each version said, generated from the git commit that
published it, so a specialist or a client can be shown the text that applied at
a given moment.

Add a line to VERSIONS when a new version is published, then run:
    python3 docs-source/build-terms-archive.py     (from the repository root)
"""
import io, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import TEMPLATE, to_pdf, ROOT, SRC, CHROME

# (git revision that published it, label, output filename)
VERSIONS = [
    ('ca257db', 'Version 2.0, 11 October 2026', 'Reboc_BV_Terms_Conditions_v2.0.pdf'),
    ('HEAD',    'Version 2.1, 7 November 2026', 'Reboc_BV_Terms_Conditions_v2.1.pdf'),
]


def blob(rev, path):
    r = subprocess.run(['git', 'show', '%s:%s' % (rev, path)],
                       cwd=ROOT, capture_output=True, text=True)
    if r.returncode:
        sys.exit('could not read %s at %s\n%s' % (path, rev, r.stderr))
    return r.stdout


def main():
    if not os.path.exists(CHROME):
        sys.exit('Google Chrome not found at %s' % CHROME)
    print('Building Terms & Conditions archive...')
    for rev, version, out in VERSIONS:
        html = blob(rev, 'terms-conditions.html')
        m = re.search(r'<div class="content">(.*?)\n    </div>', html, re.S)
        if not m:
            sys.exit('could not find the content block at %s' % rev)
        page = TEMPLATE % {
            'title': 'Reboc B.V. - Terms & Conditions',
            'heading': 'Terms &amp; Conditions',
            'version': version,
            'content': m.group(1),
        }
        gen = os.path.join(SRC, 'terms-%s.generated.html' % version.split(',')[0].split()[-1])
        io.open(gen, 'w', encoding='utf-8').write(page)
        to_pdf(gen, os.path.join(ROOT, out))
    print('Done.')


if __name__ == '__main__':
    main()
