import re, sys
from pypdf import PdfReader
r = PdfReader(sys.argv[1])
hits = []
for i, p in enumerate(r.pages):
    t = p.extract_text() or ""
    if re.search(r"parking", t, re.I):
        hits.append((i + 1, t))
print(len(r.pages), [i for i, _ in hits])
open(sys.argv[2], "w").write("\n\n".join(f"[p{i}]\n{t}" for i, t in hits))
