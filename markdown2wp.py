# -*- coding: utf-8 -*-
import sys
import markdown
import json
import requests
from urllib.parse import urljoin
import glob
from datetime import datetime, timedelta, timezone
import re
import random, string

print("はじめるよ")

WP_URL = sys.argv[1]
WP_USERNAME = sys.argv[2]
WP_PASSWORD = sys.argv[3]
UPDATED_FILES = sys.argv[4]

#
# 送信処理関数
#
def post_article(status, slug, title, content, category_ids, tag_ids, media_id):

   # 情報の設定
   JST = timezone(timedelta(hours=+9), 'JST')
   dt = datetime.now(JST).isoformat()
   # ボディ
   payload = {"status": status,
              "slug": slug,
              "title": title,
              "content": content,
              "date": dt,
              "categories": category_ids,
              "tags": tag_ids}
   if media_id is not None:
       payload['featured_media'] = media_id
   # 送信処理
   res = requests.post(urljoin(WP_URL, "wp-json/wp/v2/posts"),
                       data=json.dumps(payload),
                       headers={'Content-type': "application/json"},
                       auth=(WP_USERNAME, WP_PASSWORD))
   print('＝＝＝＝＝＝「{}」の送信結果 → {}:{}＝＝＝＝＝＝'.format(title, repr(res.reason),repr(res.status_code)))
   return res


#
# ランダムに文字列を生成
#
def randomname(n):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

#
# 読み込んだファイルをリストに変換してmd検出ファイルを検出
#
def find_md_file(filelist_input):
    filelist_split=filelist_input.replace("[","").replace("]","").split(",")
    print("＝＝＝更新から読み込んだファイル＝＝＝")
    print(filelist_split)

    l_n_str = [str(n) for n in filelist_split]
    print("＝＝＝更新から読み込んだファイルをリストへ変換＝＝＝")
    print(l_n_str)

    filelist = [s for s in l_n_str if re.match('posts\/.*\.md', s)]
    print("＝＝＝検出した.mdファイルはコチラ＝＝＝")
    print(filelist)

    return filelist

def find_article_header(file):
    title =""
    status_p = ""
    status_b = ""
    state = ""
    slug = ""
    category_ids = ""
    tag_ids = ""
    media_id = ""

    with open(file, mode='r', encoding='UTF-8') as fh:
        text = fh.read()
        file_name = file.replace('.md','').replace('posts/','')
        article_header = re.findall('>-+<.*?>-+<',text, flags=re.DOTALL) #識別番号増えた

        if len(article_header[0])!=0:
            header_line = re.match('>-+<',text).group()
            heater_content = article_header[0].replace(header_line,'')
            article_content = text.replace(article_header[0],'') # 記事の中身

            # 記事情報の抽出
            title = re.findall('\- タイトル\:\[(.*?)\]',heater_content, flags=re.DOTALL)[0]
            status_p = re.findall('\- 投稿時\:p\[(.*?)\]公開d\[.*?\]下書き',heater_content, flags=re.DOTALL)[0]
            status_b = re.findall('\- 投稿時\:p\[.*?\]公開d\[(.*?)\]下書き',heater_content, flags=re.DOTALL)[0]
            state = status_p + status_b
            slug = re.findall('\- カスタムURL\:\[(.*?)\]',heater_content, flags=re.DOTALL)[0]
            category_ids = re.findall('\- カテゴリID\:\[(.*?)\]',heater_content, flags=re.DOTALL)[0]
            tag_ids = re.findall('\- タグID\:\[(.*?)\]',heater_content, flags=re.DOTALL)[0]
            media_id = re.findall('\- 見出し画像のID\:\[(.*?)\]',heater_content, flags=re.DOTALL)[0]

            if len(title)==0:
                title = file_name
                print("タイトル情報がないので、ファイル名「{}」をタイトルにしました。".format(title))

            if len(state)==0 | len(state)==2:
                state = "draft"
                print("下書き状態にしておきます。")

            if len(slug)==0:
                slug = file_name
                print("カスタムURLがないので、ファイル名「{}」をカスタムURLにしました。".format(title))

        else:
            print("記事投稿情報がありません。ファイル名をタイトルにしますね！")
            title = file_name

        return title, state, slug, category_ids, tag_ids, media_id

filelist = find_md_file(UPDATED_FILES)
if len(filelist)!= 0 :
    for file in filelist:
        with open(file, mode='r', encoding='UTF-8') as fh:
            text = fh.read()
            article_header = re.findall('>.*?>-+<.*?>-+<',text, flags=re.DOTALL)
            print(article_header)


if len(filelist)!= 0 :
    print(".mdファイルを検出したので、HTMLに変換します。")
    for file in filelist:
        with open(file, mode='r', encoding='UTF-8') as fh:
            text = fh.read()
            # print(text)
            md = markdown.Markdown(extensions=["extra",'nl2br','sane_lists'])
            html = md.convert(text)
            print("htmlに変換しました。")

            print("投稿前処理を行います。")
            title=file.replace('.md','').replace('posts/','')
            h1= '<h1>'+title+'</h1>'
            content= html.replace(h1,'')

            f = open("collections.json", 'r')
            json_data = json.load(f)

            for key in json_data:
                content = content.replace(key,json_data[key])

        # 記事を下書き投稿する（'draft'ではなく、'publish'にすれば公開投稿できます。）
            # post_article('draft', 'test-api-post', title, content, category_ids=[], tag_ids=[], media_id=None)

else:
    print(".mdファイルはなかったみたいです。")

print("処理が終了しました。")
