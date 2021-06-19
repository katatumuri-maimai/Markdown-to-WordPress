# -*- coding: utf-8 -*-
import sys
import markdown
import json
import requests
from urllib.parse import urljoin
import glob
from datetime import datetime
import re

print("はじめるよ")

WP_URL = sys.argv[1]
WP_USERNAME = sys.argv[2]
WP_PASSWORD = sys.argv[3]

def post_article(status, slug, title, content, category_ids, tag_ids, media_id):
   """
   記事を投稿して成功した場合はTrue、失敗した場合はFalseを返します。
   :param status: 記事の状態（公開:publish, 下書き:draft）
   :param slug: 記事識別子。URLの一部になる（ex. slug=aaa-bbb/ccc -> https://wordpress-example.com/aaa-bbb/ccc）
   :param title: 記事のタイトル
   :param content: 記事の本文
   :param category_ids: 記事に付与するカテゴリIDのリスト
   :param tag_ids: 記事に付与するタグIDのリスト
   :param media_id: 見出し画像のID
   :return: レスポンス
   """
   # credential and attributes
   user_ = WP_USERNAME
   pass_ = WP_PASSWORD
   # build request body
   payload = {"status": status,
              "slug": slug,
              "title": title,
              "content": content,
              "date": datetime.now().isoformat(),
              "categories": category_ids,
              "tags": tag_ids}
   if media_id is not None:
       payload['featured_media'] = media_id
   # send POST request
   res = requests.post(urljoin(WP_URL, "wp-json/wp/v2/posts"),
                       data=json.dumps(payload),
                       headers={'Content-type': "application/json"},
                       auth=(user_, pass_))
   print('----------\n件名:「{}」の投稿リクエスト結果 res.status: {}'.format(title, repr(res.status_code)))
   return res




filelist_input = sys.argv[4]
filelist=[]

md_file_name = '.*.md'

for i in range(len(filelist_input)):
    if filelist_input[i] == '.*.md':
        print(filelist_input[i])

if len(filelist)!= 0 :
    print(".mdファイルを検出したので、HTMLに変換します。")
    for file in filelist:
        with open(file, mode='r', encoding='UTF-8') as fh:
            text = fh.read()
            md = markdown.Markdown(extensions=["extra"])
            html = md.convert(text)
            print("html")
            title=file.replace('.md','').replace('posts/','')
            h1= '<h1>'+title+'</h1>'
            content= html.replace(h1,'')

            f = open("collections.json", 'r')
            json_data = json.load(f)

            for key in json_data:
                content = content.replace(key,json_data[key])

        # 記事を下書き投稿する（'draft'ではなく、'publish'にすれば公開投稿できます。）
            post_article('draft', 'test-api-post', title, content, category_ids=[], tag_ids=[], media_id=None)

else:
    print(".mdファイルはなかったみたいです。")

print("処理が終了しました。")
