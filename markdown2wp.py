# -*- coding: utf-8 -*-
import markdown
import json
import glob

print("はじめるよ")

filelist = glob.glob('posts/*.md')
print(filelist)
for file in filelist:
    with open(file, mode='r', encoding='UTF-8') as fh:
        text = fh.read()
        md = markdown.Markdown(extensions=["extra"])
        html = md.convert(text)
        print(html)
