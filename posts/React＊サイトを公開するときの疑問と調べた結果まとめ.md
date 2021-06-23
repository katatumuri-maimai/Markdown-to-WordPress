# React＊サイトを公開するときの疑問と調べた結果まとめ

こんにちは！かたつむり([@Katatumuri_nyan](https://twitter.com/Katatumuri_nyan))です！

**「はじめてReactで作ったサイトをせっかくなら公開したい！けど、公開の仕方が分からない…。」**
なんて思っていませんか～？（思っていたら仲間です！ｗ）

Reactでサイトを作ったはいいものの、どうやって公開したらいいのか分からなかったので、その時の疑問をまとめてみました。

ちなみに、`GitHub`というサイトの`GitHub Pages`を利用して公開できました(*´ω｀)

では、疑問と調べた結果を紹介します～！

## 公開の仕方の疑問
まずは、公開に関して疑問に思ったことを書いていきます～！

<div class="sng-box box2">

- create-react-appしてReactサイトを作ったけど、どうしたら公開できる？
- Dockerを利用してReactサイトを作ったけど、コンテナごと公開するの…？
- 公開先ってどこ？（レンタルサーバーとか？）

</div>


### Q.create-react-appしてReactサイトを作ったけど、どうしたら公開できる？
なんだかよくわからないままReactを始めたわたくし。
とりあえず、`create-react-app`してReactサイトのひな型を作って、編集したはいいけど、、、。

- このまま丸ごとReactが入っているであろうフォルダごとWebサーバー等にアップロードするのかな…？
- ローカルではReact用のサーバーを起動させてたけど、Webサーバー上でも起動させるのかな…？

と、大変混乱…しましたｗ
HTMLやwebサーバー上のWordPressでサイトを公開することはありましたが、今回のパターンは初めてですｗ

#### A.ビルドしてデプロイ用のファイルを作って公開する
[CreateReactAppの公式ドキュメント](https://create-react-app.dev/docs/deployment/)にあるように、`build`という段階を踏んで、デプロイ（公開）するとのことです。

**なんやねんビルド！**って感じですが、だいたいは`npm build`とか、コマンドを打つと勝手にやってくれます。
（公開先によってちょっとずつ違う）

ビルドすることで、公開しやすい形にReactを整えてくれます。
公開用の設定ファイルを作って、整ったReactを公開先にアップロードすると、公開できるようになります。


### Q.Dockerを利用してReactサイトを作ったけど、コンテナごと公開するの…？
コンテナ…？Dockerとは…？
みたいな状態でReact開発を始めたので、よくわかっていなくて、、、ｗ

上で書いた疑問とごっちゃになって考えていましたｗｗｗ

#### A.コンテナごと公開することもできる
これはまだやったことがないので、あまり理解していませんが、Dockerイメージをそのまま公開できるサービスが複数あるみたいです。

参考:[Docker composeとAWS(ECR/ECS)デプロイ](https://zenn.dev/soreiyu/articles/29fe1cacc071bd)


### Q.公開先ってどこ？（レンタルサーバーとか？）
そもそも<a href="https://px.a8.net/svt/ejp?a8mat=3HEC9T+5OTGGA+CO4+609HU" rel="nofollow">エックスサーバー</a><img border="0" width="1" height="1" src="https://www19.a8.net/0.gif?a8mat=3HEC9T+5OTGGA+CO4+609HU" alt="">などの普通のレンタルサーバーで公開できるのか…？
と疑問でしたｗ

#### A.レンタルサーバーでも公開できる。公開用のサービスも沢山ある
色んなデプロイ（公開）用のサービスがあるみたいですね。

<div class="sng-box box2">

- <a href="https://px.a8.net/svt/ejp?a8mat=3HEC9T+5OTGGA+CO4+609HU" rel="nofollow">エックスサーバー</a><img border="0" width="1" height="1" src="https://www19.a8.net/0.gif?a8mat=3HEC9T+5OTGGA+CO4+609HU" alt="">などのレンタルサーバー
- [AWS Amplify](https://aws.amazon.com/jp/amplify/)
- [Azure](https://azure.microsoft.com/ja-jp/)
- [Firebase](https://firebase.google.com/)
- [GitHub Pages](https://pages.github.com/)
- [Netlify](https://www.netlify.com/)

</div>

参考:[CreateReactAppの公式ドキュメント](https://create-react-app.dev/docs/deployment/)では、各サービスでReactアプリを公開する手順が紹介されています。

参考:[Reactアプリケーションを最小構成で静的ホスティング環境にデプロイしてみた](https://outputable.com/post/prod-react-minimal/)
こちらの方は、静的なサーバー（レンタルサーバーなど）で公開してみたとのことですよ。

## 専門用語の疑問
<div class="sng-box box2">

- デプロイって何？
- ビルドって何？
- Reactで作ったのはアプリ？サイト？

</div>

### Q.デプロイって何？
「React　公開　やり方」　とかで調べていると、ちらほら**「デプロイ」**という言葉を見かけます。
デプロイ…？

#### A.ざっくりいうと公開すること
Reactでデプロイっていうと、公開するって意味で使われていることが多いですね。
`deploy`は`展開`みたいな意味もあります。

プログラミング界隈では、**ユーザーが使える状態にすることをデプロイ**というみたいですね。

参考:[デプロイ（英：deploy）とは](https://wa3.i-3-i.info/word16767.html)

### Q.ビルドって何？
じゃぁデプロイしよう！って思って調べて行くと、次はビルドって言葉が出てきますよね。
デプロイ…？ビルド…？相当困惑しましたｗ

#### A.デプロイする前処理

上の方でも少し説明しましたが、デプロイするには前処理が必要な場合があります。

HTML/CSSで作った静的なサイトなら、そのままアップロードしても公開できますが、
Reactみたいな動的（HTML生成したりする）なサイトは、前処理をしてデプロイすることが必要みたいです。

その**前処理をビルド**というんですね！

参考:[ビルド（英：build）とは](https://wa3.i-3-i.info/word12775.html)

### Q.Reactで作ったのはアプリ？サイト？
Reactアプリって呼びますよね。
でも、サイトを作ってる気分なんだよなぁ…。
**Reactで作ったらアプリなの…？**

そもそもサイトとアプリの違いってもはや何…？と困惑してきました←

#### A.ユーザーが動かせたらアプリ
色んなサイトやアプリがあるので、明確な基準はないみたいですが、、、
Twitterみたいに、ユーザーが投稿したり設定を変更したりということができると、アプリ（ソフト）という認識みたいです。

**ユーザー**が**使う**と認識できるようなサイトは、アプリという方があっているのかもしれませんね。

参考:[Webアプリとは？特徴やアプリケーション開発について解説](https://pantograph.co.jp/blog/production/web-app.html)

## GitHub Pagesの疑問
最後は、デプロイする時に利用したGitHub Pagesの疑問です～！

<div class="sng-box box2">

- GitHub Pagesって何？
- サブディレクトリにあるReactアプリってどうやって公開するの？
- gh-pagesで公開した後はどうやって更新するの？
- GitHubでmainなど特定のブランチにpushやmergeした時に自動的に公開してほしいけどできる？

</div>

### Q.GitHub Pagesって何？
GitHub Pagesでデプロイしてみた人がたくさんいるので、デプロイできる場所なんだ！とは思っていたのですが…。

#### A.GitHubが無料で提供しているホスティングサービス
プログラミング界隈で知らない人はほぼいないくらいの[GitHub](https://github.co.jp/)。
そこで提供されているサービスが、[GitHub Pages](https://docs.github.com/ja/pages)なんです。

簡単に言うと、GitHubにアカウントを持っていれば、**無料で使えるレンタルサーバー**ですね。（用途に制限あり）

GitHub Pagesでいいなぁって思ったのは、[GitHub Actions](https://docs.github.com/ja/actions)というサービスが使えるところ。
色んなことを自動化できるサービスですｗ

**ReactのソースコードをGitHubで管理しつつ、GitHub Actionsで公開・更新のような処理を行えるので、一度構築してしまえばめちゃくちゃ楽なんですね～！**

（**Git**？→バージョン管理ツール）
（**GitHub**？→Gitを利用してクラウド上でソースコードやバージョンを共有・共同作業できるwebサービスの一つ）

### Q.サブディレクトリにあるReactアプリってどうやって公開するの？
ReactのソースコードをGitHubで管理していたわたくし。
そのまま公開できたら便利じゃーん！って思ったけど、、、。

`rootディレクトリ`（リポジトリで一番上のディレクトリ）か、その中の`docs`というサブディレクトリにindex.htmlがあればサイトを公開できるとのこと。

でも、`create-react-app`でReactアプリを作成すると、`rootディレクトリ`の中にReactのフォルダ（サブディレクトリ）がありますよね。
その中に`public`ってフォルダがあって、その中に`index.html`があると。

私はDockerを使っていたので、rootにはDockerの設定ファイルとかもあって、サブディレクトリをリポジトリのrootにしなおすこともできず…どうしたらいいんだと頭を抱えましたｗ

#### A.GitHub Pasesなら、`gh-pages`というツールでうまい事やってくれる
良くよく調べていたら、[gh-pages](https://www.npmjs.com/package/gh-pages?activeTab=readme)というツールをみんな使っていることに気づきました。

これ、Reactの中の`package.json`をちょっと編集してから、数回簡単なコマンドを打つだけで、**さくっと勝手にGitHub Pagesに公開してくれるツール**なんです！

これで勝手に`gh-pages`というブランチができて、そこに勝手にビルドされた公開用のファイルがアップロードされ、`index.html`はrootディレクトリに置かれて、**万事解決っていうツール**です。

ちなみに、通常使っているブランチはそのままなので、とってもよきですよ。

参考:[GitHub PagesでReactアプリケーションを公開！【作りながら覚えるReact】](https://bagelee.com/programming/react/react-smart-speaker-8/)
参考:[GitHub ページを React でつくる (基礎編)](https://qiita.com/KoheiShingaiHQ/items/b4bf8dd47a99e5d14caf)

### Q.gh-pagesで公開した後はどうやって更新するの？
ということで、`gh-pages`で無事公開できたんですが、、、。

Reactサイトを更新していく予定だったので、その後の更新の仕方が分からなくなっちゃいました←

#### A.毎回`gh-pages`でビルドしなおして公開しなおす
**更新のたびにビルドしなおしてデプロイしなおすことが必要**みたいです…(;´･ω･)

とりあえず更新の仕方はわかりました！良かった！
そして、↓で**自動更新**についても考えてみました。

### Q.GitHubでmainなど特定のブランチにpushやmergeした時に自動的に公開してほしいけどできる？
毎回コマンドを打ってビルドしなおしてデプロイしなおすってめちゃくちゃめんどくさいですよね。
しかも`gh-pages`を使う時に、毎回GitHubのユーザー情報を聞かれますｗ
めっちゃだるい…
どうせなら、GitHubに`push`したり`marge`したりした時に、勝手に更新してほしい！

#### A.できます。GitHub Actionsならね
これ、ちょっと上の方の疑問のところで既にネタバレしていますが←
**GitHub Actions**を利用したら、`push`や`marge`した時に自動更新する設定ができるんです。

`yml`っていう設定ファイルを書かないといけないので、結構ハードル高めだったのですが、、、。
なんとか自動更新できるようになったので、更新がめちゃくちゃ楽になりました～！

参考:[GitHub Actionsでgh-pagesを利用してReactアプリをGitHub Pagesにデプロイする](https://qiita.com/salty-byte/items/a542e57a1a94ae4b2ab8)

## まとめ
いかがでしたか～？
同じように悩んでいる方の参考になったら嬉しいです(*´ω｀)

今後、**GitHub Actions**での設定ファイルのこととか書けたらいいな～と思っているので、良かったら見に来てください♪
