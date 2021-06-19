# -*- coding: utf-8 -*-
import sys
import markdown
import json
import requests
import glob
from datetime import datetime

print("はじめるよ")

WP_URL = sys.argv[0]
WP_USERNAME = sys.argv[1]
WP_PASSWORD = sys.argv[2]

print (WP_URL)

filelist = glob.glob('posts/*.md')
print(filelist)
for file in filelist:
    with open(file, mode='r', encoding='UTF-8') as fh:
        text = fh.read()
        md = markdown.Markdown(extensions=["extra"])
        html = md.convert(text)
        print(html)
