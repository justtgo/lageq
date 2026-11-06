#!/usr/bin/env python3
"""Schimbă domeniul din canonical, sitemap, feed, Open Graph etc.
Exemplu: python3 set-domain.py https://numele-meu.netlify.app"""
import os, sys
root = os.path.dirname(os.path.abspath(__file__))
if len(sys.argv) < 2:
    sys.exit("Folosire: python3 set-domain.py https://domeniul-tau.ro")
new = sys.argv[1].rstrip("/")
f = os.path.join(root, "domain.txt")
cur = open(f).read().strip() if os.path.exists(f) else "https://lageq.ro"
n = 0
for d, _, fs in os.walk(root):
    if ".git" in d.split(os.sep): continue
    for name in fs:
        if name.endswith((".html", ".xml", ".txt")) and name != "domain.txt":
            p = os.path.join(d, name)
            s = open(p, encoding="utf-8").read()
            if cur in s:
                open(p, "w", encoding="utf-8").write(s.replace(cur, new)); n += 1
open(f, "w").write(new)
print(f"{cur} -> {new} ({n} fișiere actualizate)")
