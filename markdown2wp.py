# -*- coding: utf-8 -*-
import markdown
import json

print("はじめるよ")

with open("main.md", mode='r', encoding='UTF-8') as fh:
    text = fh.read()
    md = markdown.Markdown()
    html = md.convert(text)
    print(html)
