>------------<
- タイトル:[【1】Laravelでコーディングテストサービスを共同開発した際のメモ【環境構築編】 ]
- WordPressにアップロードしますか？:y[x]はいn[]まだしない
- 投稿時:p[x]公開d[]下書き
- カスタムURL:[joint-development-Laravel-coding-tester-1]
- カテゴリID:[12,15,16]
- タグID:[]
- 見出し画像のID:[]
- 識別番号[HSEo7AEIMiDo]
>------------<

<!-- ↓続き
[kanren id=""] -->

こんにちは！かたつむり([@Katatumuri_nyan](https://twitter.com/Katatumuri_nyan))です！

今回は、[とらちゃん](https://github.com/dt-torachan)と共同開発した際の開発メモを書いていきます！
コーディングの試験を登録できるサービスを作成しています。

[GitHub](https://github.com/dt-torachan)/CodingTester)でソースコードを管理しています！

**最初から見る↓**
[kanren id="723"]

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

コンテナ内で`composer install`します。


参考:[Laravelで…vendor/autoload.php): failed to open stream: No such file or directory というエラーによりデフォルト画面が表示されない解決方法](https://qiita.com/pugiemonn/items/3d000ac0486987dd92df)

![picture 2](../../images/e0adfa8f40c39d8fd622f88448a044d6b8fc5c688a336195fa9ff64b7df8f80d.png)  
表示されました！

中身はちょっと作ってあるのと、私もデザインを少しいじっているので、続きからやっていきます。


## データベースとの接続
![picture 3](../../images/b75eab6a33e3f208bdd78e9b31738e3590584296ada4292b3ae38fdf71f1b85b.png)  
> SQLSTATE[42S02]: Base table or view not found: 1146 Table 'laravel_db.questions' doesn't exist (SQL: select * from `questions`)
> A table was not found
> You might have forgotten to run your migrations. You can run your migrations using php artisan migrate.
> Pressing the button below will try to run your migrations.


データベースと接続できないので、解決方法をメモします。

### appコンテナ内で`php artisan migrate`してみる
![picture 4](../../images/7f31ac6647048a4da87947a995af01378cf2400d40f80dd7224578ca1360ac33.png)  
`Nothing to migrate.`

### キャッシュクリアしてみる
`php artisan cache:clear`
`php artisan config:clear`
`php artisan migrate:refresh`

![picture 5](../../images/c13a512135159f78eeb839438cde96ca36171e5b34875b33f748febfe148f7a2.png)  
> PDOException::("SQLSTATE[HY000]: General error: 1813 Tablespace '`laravel_db`.`questions`' exists.")

![picture 6](../../images/3bbdbae8ad720d3eb08cd78f4a970c665aef6b3b616e9f8409e83a2cd1964f06.png)  
ちなみにテーブルはありません

### DBコンテナを削除してみる
DBコンテナに問題があるかもしれないので、DBコンテナだけ再ビルドします。
dockerデスクトップでdbコンテナ停止・dbコンテナremove
`docker-compose up -d --build db`

もう一度
`php artisan migrate`します。

同エラーが出たのでもう一度キャッシュクリアします。
`php artisan cache:clear`
`php artisan config:clear`
`php artisan migrate:refresh`

同エラーが出ます。

### コンテナを一度削除して作成しなおす。
`docker-compose down`
`docker-compose up -d --build`
`php artisan migrate`

同エラーが出ました

### パーミッションを確認する
一応パーミッションを確認してみます。
dbのコンテナで確認します。
![picture 7](../../images/df92e6d5d19b877da171aca6fe06ac459161054688ce2de343cd14ae347cd21e.png)  
大丈夫そうですね。なんでだろうｗ

### データベースを削除
`rm -rf laravel_db`
`mkdir laravel_db`
`php artisan migrate`

![picture 8](../../images/e2044557292ab76742dacba5031954eeb7ba6352c6973e2933bbcfb7017e618a.png)  
パーミッションエラーが出たので、パーミッション変更します。

![picture 9](../../images/2ee1689094b71eb1352c9c58718859a2037ab9c0cc835a8119fc4504db6962ca.png)  
確認して

↓
`chmod 777 laravel_db`
`ls -l`
![picture 10](../../images/2fbc6aba4ed9c6078eeae784c6721e597747cc6fb6ea1f0addc1107673bb67eb.png)  
変更できました。

再び`php artisan migrate`
![picture 11](../../images/f37fc804b8c34b8281e6216cbfbd551abcf29b03e1f6030c4f51f9ee9b28ced1.png)  
できたっぽい

## データの生成
すでに問題データがあるので、`php artisan db:seed`しときます。
[Laravelでシーダーを使う](https://qiita.com/shosho/items/b69db263a494edfe3b21)

![picture 12](../../images/159181f539ffcb7ccd0e802e6afc3119a4ee4b0af72861786b4d9e8b293ec5b6.png)  

これで環境構築は終了です(*´ω｀)