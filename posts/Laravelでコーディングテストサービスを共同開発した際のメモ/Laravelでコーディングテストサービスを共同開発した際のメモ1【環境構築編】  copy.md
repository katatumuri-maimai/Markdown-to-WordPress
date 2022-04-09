>------------<
- タイトル:[【1】Laravelでコーディングテストサービスを共同開発した際のメモ【環境構築編】 ]
- WordPressにアップロードしますか？:y[]はいn[x]まだしない
- 投稿時:p[]公開d[x]下書き
- カスタムURL:[joint-development-Laravel-coding-tester-1]
- カテゴリID:[12,15,16]
- タグID:[]
- 見出し画像のID:[]
- 識別番号[]
>------------<

<!-- ↓続き
[kanren id=""] -->

こんにちは！かたつむり([@Katatumuri_nyan](https://twitter.com/Katatumuri_nyan))です！

今回は、[とらちゃん](https://github.com/dt-torachan)と共同開発した際の開発メモを書いていきます！
コーディングの試験を登録できるサービスを作成しています。

[GitHub](https://github.com/dt-torachan)/CodingTester)でソースコードを管理しています！

**最初から見る↓**
[kanren id=""]

<!-- **前回を見る↓**
[kanren id=""] -->

## リポジトリのクローン
とらちゃんのリポジトリがメインなので、そちらにGitHubから招待してもらいます。
（メモ：Forkすると複雑になるの）

[GitHub](https://github.com/dt-torachan/CodingTester)から、クローンして、`feature/design`ブランチを切りました。

参考:[githubを使った共同作業の手順](https://qiita.com/future_kame/items/9fa256aea09faa28b357)

## dockerのコンテナを立てる
今回はdockerで環境構築をするので、`docker-compose up -d --build`
（すでにとらちゃんがdocker-composeファイルなどは作ってくれています。）

## `index.php`が開けない
![picture 1](../../images/724eec592544f19eb5388aa70b1e6440182fa4d66619fbf810f1ffcb7d70ffd4.png)  
