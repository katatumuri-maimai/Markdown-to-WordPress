# -*- coding: utf-8 -*-
import markdown
import json
import glob

print("はじめるよ")

filelist = glob.glob('posts/*.md')
print(filelist)
# for i in filelist:
    # with open(filelist[i], mode='r', encoding='UTF-8') as fh:
    #     text = fh.read()
    #     md = markdown.Markdown()
    #     html = md.convert(text)
    #     print(html)
