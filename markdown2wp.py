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
from bs4 import BeautifulSoup
import lxml
import base64
from io import BytesIO
from PIL import Image
import os

print("はじめるよ")

WP_URL = sys.argv[1]
WP_USERNAME = sys.argv[2]
WP_PASSWORD = sys.argv[3]
ADDED_FILES = sys.argv[4]
UPDATED_FILES = sys.argv[5]

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

   articleid = res.json()["id"]
   with open('articles.json', 'r') as d:
       json_articles = json.load(d)
       json_articles[serial_number]["articleid"] = articleid

   with open('articles.json', mode='wt', encoding='utf-8') as f:
       json.dump(json_articles, f, ensure_ascii=False, indent=2)
       print('idをarticles.jsonに追加しました。')

   print('＝＝＝＝＝＝「{}」の新規投稿結果 → {}:{}＝＝＝＝＝＝'.format(title, repr(res.reason),repr(res.status_code)))
   return res


#
# 更新処理関数
#
def patch_article(articleid,status, slug, title, content, category_ids, tag_ids, media_id):

   # 情報の設定
   JST = timezone(timedelta(hours=+9), 'JST')
   dt = datetime.now(JST).isoformat()
   # ボディ
   payload = {"status": status,
              "slug": slug,
              "title": title,
              "content": content,
              "categories": category_ids,
              "tags": tag_ids}
   if media_id is not None:
       payload['featured_media'] = media_id
   # 送信処理
   res = requests.patch(urljoin(WP_URL, "wp-json/wp/v2/posts")+ "/" +str(articleid),
                       data=json.dumps(payload),
                       headers={'Content-type': "application/json"},
                       auth=(WP_USERNAME, WP_PASSWORD))
   print(urljoin(WP_URL, "wp-json/wp/v2/posts")+ "/" +str(articleid))
   print(urljoin(WP_URL, "wp-json/wp/v2/posts/",articleid))
   print('＝＝＝＝＝＝「{}」の更新結果 → {}:{}＝＝＝＝＝＝'.format(title, repr(res.reason),repr(res.status_code)))
   return res


#
# ランダムに文字列を生成
#
def randomname(n):
    serial_number = ''.join(random.choices(string.ascii_letters + string.digits, k=n))
    if isSerial(serial_number):
        serial_number = ''.join(random.choices(string.ascii_letters + string.digits, k=n))
    return serial_number

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

#
# .mdファイルの冒頭に記事情報を挿入
#
def add_article_header(file):
    article_header = ""
    serial_number = ""
    file_content = ""
    with open(file, mode='r', encoding='UTF-8') as fh:
        text = fh.read()
        article_header_ini = re.findall('>-+<.*?>-+<',text, flags=re.DOTALL)
        article_header_ini_content = re.findall('>-+<(.*?)>-+<',text, flags=re.DOTALL)
        serial_ini = re.findall('識別番号\[.*?\]',text)
        serial_number_ini = re.findall('識別番号\[(.*?)\]',text)
        print(serial_number_ini)

        if not article_header_ini:
            article_header_ini=""
        else:
            article_header_ini = article_header_ini[0]

        if not serial_number_ini:
            serial_number_ini=""
        else:
            serial_number_ini = serial_number_ini[0]


        if len(serial_number_ini)==0 and len(article_header_ini)==0:
            serial_number = randomname(12)

            article_header=""">------------<
- タイトル:[]
- WordPressにアップロードしますか？:y[]はいn[]まだしない
- 投稿時:p[]公開d[]下書き
- カスタムURL:[]
- カテゴリID:[]
- タグID:[]
- 見出し画像のID:[]
- 識別番号[{}]
>------------<
""".format(serial_number)
            file_content =article_header + text
            print("1")

        elif len(serial_number_ini)!=0 and len(article_header_ini)==0:
            serial_number = randomname(12)
            article_header = """>------------<
- タイトル:[]
- WordPressにアップロードしますか？:y[]はいn[]まだしない
- 投稿時:p[]公開d[]下書き
- カスタムURL:[]
- カテゴリID:[]
- タグID:[]
- 見出し画像のID:[]
- 識別番号[{}]
>------------<""".format(serial_number)
            file_content = re.sub('識別番号\[.*?\]',article_header,text)

        elif len(serial_number_ini)==0 and len(article_header_ini)!=0:
            serial_number = randomname(12)
            if not serial_ini:
                article_header = """>------------<{}- 識別番号[{}]
>------------<""".format(article_header_ini_content[0],serial_number)
                file_content = text.replace(article_header_ini,article_header)
                print("2.5")

            else:
                article_header = article_header_ini.replace('識別番号[]','識別番号[{}]'.format(serial_number))
                print("3")
                file_content = text.replace(article_header_ini,article_header)

        elif len(serial_number_ini)!=0 and len(article_header_ini)!=0:
            file_content = text
            print("4")

        fh.close()

    if len(serial_number_ini)==0 or len(article_header_ini)==0:
        with open(file, mode='w', encoding='UTF-8') as fh:
            fh.write(file_content)
            fh.close()
            print(article_header)
            print("書き込みした")

#
# .mdファイルの冒頭の記事情報を検出
#
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
            upload_y = re.findall('\- WordPressにアップロードしますか？\:y\[(.*?)\]はいn\[.*?\]まだしない',heater_content, flags=re.DOTALL)[0]
            upload_n = re.findall('\- WordPressにアップロードしますか？\:y\[.*?\]はいn\[(.*?)\]まだしない',heater_content, flags=re.DOTALL)[0]
            upload = upload_y + upload_n
            status_p = re.findall('\- 投稿時\:p\[(.*?)\]公開d\[.*?\]下書き',heater_content, flags=re.DOTALL)[0]
            status_d = re.findall('\- 投稿時\:p\[.*?\]公開d\[(.*?)\]下書き',heater_content, flags=re.DOTALL)[0]
            state = status_p + status_d
            slug = re.findall('\- カスタムURL\:\[(.*?)\]',heater_content, flags=re.DOTALL)[0]
            category_ids = re.findall('\- カテゴリID\:\[(.*?)\]',heater_content, flags=re.DOTALL)[0]
            tag_ids = re.findall('\- タグID\:\[(.*?)\]',heater_content, flags=re.DOTALL)[0]
            media_id = re.findall('\- 見出し画像のID\:\[(.*?)\]',heater_content, flags=re.DOTALL)[0]
            serial_number = re.findall('識別番号\[(.*?)\]',heater_content, flags=re.DOTALL)[0]

            if len(title)==0:
                title = file_name
                print("タイトル情報がないので、ファイル名「{}」をタイトルにしました。".format(title))

            if len(upload)==0 or len(upload)==2:
                upload = False
                print("下書き状態にしておきます。")
            elif len(upload_y)==0:
                upload = False
            elif len(upload_n)==0:
                upload = True

            if len(state)==0 or len(state)==2:
                state = "draft"
                print("下書き状態にしておきます。")
            elif len(status_p)==0:
                state = "draft"
            elif len(status_d)==0:
                state = "publish"

            if len(slug)==0:
                slug = file_name
                print("カスタムURLがないので、ファイル名「{}」をカスタムURLにしました。".format(title))

            if len(media_id)==0:
                media_id= None

        else:
            print("記事投稿情報がありません。ファイル名をタイトルにしますね！")
            title = file_name

        return title, upload, state, slug, category_ids, tag_ids, media_id, serial_number, article_content

#
# 識別番号があるかないか確認
#
def isSerial(serial_number):
    Serial = False
    with open('articles.json', 'r') as d:
        json_articles = json.load(d)

        for key in json_articles:
            if key == serial_number:
                Serial = True
    return Serial

def set_article_json(serial_number,state,upload):
    # 'articles.json'に識別番号がある場合は、変更箇所だけ変更。ない場合は新しく登録。
    with open('articles.json', 'r') as d:
        json_articles = json.load(d)

        if isSerial(serial_number):
            id = json_articles[serial_number]["articleid"]
        else:
            id = "none"

        json_articles[serial_number]={
                        "status":state,
                        "upload":upload,
                        "articleid":id
                        }

    with open('articles.json', mode='wt', encoding='utf-8') as f:
        json.dump(json_articles, f, ensure_ascii=False, indent=2)
        print('articles.jsonファイルに記事情報を追加しました。')

    return id

#
# imgをbase64へ変換
#
def pil_to_base64(img):
    buffer = BytesIO()
    # print(img.format)
    img.save(buffer, format=img.format)
    img_str = base64.b64encode(buffer.getvalue()).decode("ascii")

    return img_str

#
# .mdファイルをＨＴＭＬに変換したものを返す
#
def md2html(article_content):
    # print(text)
    md = markdown.Markdown(extensions=["extra",'nl2br','sane_lists'])
    html = md.convert(article_content)
    content = html
    print("htmlに変換しました。")

    soup = BeautifulSoup(html,'lxml')
    imgs = soup.find_all('img')

    for img in imgs:
        img_data = Image.open(img['src'])

        if os.path.exists(img_data):
            img_str = pil_to_base64(img_data)
            content = content.replace(img['src'],'data:image/jpeg;base64,'+img_str)


    f = open("collections.json", 'r')
    json_data = json.load(f)

    for key in json_data:
        content = content.replace(key,json_data[key])

    return content



add_filelist = find_md_file(ADDED_FILES)
update_filelist = find_md_file(UPDATED_FILES)

filelist = add_filelist + update_filelist

if len(filelist)!= 0 :
    print(".mdファイルを検出したので、HTMLに変換します。")
    for file in filelist:
        if os.path.exists(file):
            add_article_header(file)
            title, upload, state, slug, category_ids, tag_ids, media_id, serial_number,article_content = find_article_header(file)

            articleid = set_article_json(serial_number,state,upload)
            content = md2html(article_content)

            if upload:
                print("記事をWordPressにアップロードしてみます。")
                if articleid == "none":
                    print("新規投稿します")
                    res = post_article(state, slug, title, content, category_ids=category_ids, tag_ids=tag_ids, media_id=media_id)

                else:
                    print("既存の記事を更新します")
                    res = patch_article(articleid,state, slug, title, content, category_ids=category_ids, tag_ids=tag_ids, media_id=media_id)

                if res.reason =='Not Found':
                    print("既存記事の更新ができなかったので、新規投稿します。")
                    res = post_article(state, slug, title, content, category_ids=category_ids, tag_ids=tag_ids, media_id=media_id)

            else:
                print("記事を保存しました。（WordPressにアップロードはしていません。）")


else:
    print(".mdファイルはなかったみたいです。")

print("処理が終了しました。")
