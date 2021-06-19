# -*- coding: utf-8 -*-
import markdown
import json

print("はじめるよ")

with open("main.md") as fh:
    md = markdown.Markdown()
    html = md.convert(fh)
    print(html)
