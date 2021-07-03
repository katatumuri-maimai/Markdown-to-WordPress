>------------<
- タイトル:[無料！Reactで作ったサイトやアプリを公開・自動更新する方法【Github Pages】]
- WordPressにアップロードしますか？:y[x]はいn[]まだしない
- 投稿時:p[]公開d[x]下書き
- カスタムURL:[]
- カテゴリID:[]
- タグID:[]
- 見出し画像のID:[]
- 識別番号[oBjks6AzNTyV]
>------------<

こんにちは！かたつむり([@Katatumuri_nyan](https://twitter.com/Katatumuri_nyan))です！
最近、Reactでコードのデモサイトを作ったのですが、せっかくなのでそちらをデプロイ（公開）してみました♪

- Reactで作ったサイトの公開の仕方が分からない
- コードを編集したら、自動的にサイトも更新してほしい
- できれば無料で公開したい

こんな風に思っていたら、読んでみる価値あるかもです(*´ω｀)

この記事では、Reactで作ったサイト・アプリをデプロイ（公開）・自動更新する方法を紹介します！

`GitHub`というサービスの`GitHub Pages`と`GitHub Actions`という機能を使います。
いずれも無料プランの範囲内でできるので、ぜひ試してみてください♪

それでは、詳しく説明していきます！

## やりたいこと
- GitHubでmainブランチにmergeした時にReactサイトが公開・自動更新されるようにしたい

今回行う方法は、既にReactサイトをGitHUb Pagesに公開している方でも使えます！

## 環境
- ソースコードをGitHubで管理
  - GitHubに公開リポジトリがある
- DockerでNode.jsの環境構築
- create-react-appでReactアプリのひな形作成
- サブディレクトリにReactのコードがある

※GitHubに登録済み・Reactで作ったサイト・アプリのリポジトリがあるものとして説明していきます！
※無料で公開するにはリポジトリの公開設定を`public`にしておいてください

### ローカルのディレクトリ（ファイル）構造
![DirectoryStructure](images/2021/06/DirectoryStructure.png)
ローカルのrootには`react-app`などのReactのディレクトリがあります！

### GitHubのリポジトリのディレクトリ構造
![DirectoryStructure_GitHub](images/2021/06/DirectoryStructure_GitHub.png)

GitHubのrootには`react-app`などのReactのディレクトリがあります！


## Reactで作ったサイトを公開・自動更新する方法の手順
1. `package.json`の編集
2. Actionsの設定
  1. workflowの作成
  2. `gh-pages.yml`ファイルの編集
3. GitHub Pagesの設定
4. デプロイ（公開）！

それでは、早速準備を進めていきましょう！


## 1. `package.json`の編集
まずは、`package.json`にホームページやコマンドの設定を書いていきます。
ここで書いたコマンドをGitHub Actionsで使います。
```
{
  "name": "my-react-app",
  "version": "0.1.0",
  "homepage": "https://${ユーザ名}.github.io/${リポジトリ}", // ここに追加
  "dependencies": {
    // …省略
  },
  "scripts": {
    "deploy": "npm run build && gh-pages -d build", // ここに追加
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
```
↑これは、`package.json`の上の方に記載があります！
```
"homepage": "https://${ユーザ名}.github.io/${リポジトリ}", // ここに追加
```
↑`https://${ユーザ名}.github.io/${リポジトリ}`にはGitHub PagesのURLを入れてください(*´ω｀)

```
"deploy": "npm run build && gh-pages -d build", // ここに追加
```
↑これはこのまま書いちゃってOKです。

[Create React App Deployment](https://create-react-app.dev/docs/deployment/#step-2-install-gh-pages-and-add-deploy-to-scripts-in-packagejson)

## 2. Actionsの設定
次に、GitHub Actionsの設定をしていきます！
GitHub Actionsの機能を使って、公開・自動更新機能を作成しちゃいます(*´ω｀)

### 1. workflowの作成
Actionsのタブから新しくworkflowを作成していきます。
![GitHubActions](images/2021/06/GitHubActions.png)

![GitHubActions_new](images/2021/06/GitHubActions_new.png)

### 2. ymlファイルの編集
workflowのファイルを作成します！
今回は、`gh-pages.yml`って名前にしましたｗ

![yml_ini](images/2021/06/yml-ini.png)

↑この中身を↓のコードに書き換えます！

```yml
name: github pages

on:
  pull_request:
    branches:
      - main
    types:
      - closed

jobs:
  deploy:
    runs-on: ubuntu-18.04
    env:
       working-directory: ./my-react-app
       SUPER_SECRET: ${{ secrets.SuperSecret }}
    steps:
      - uses: actions/checkout@v2

      - name: Setup Node
        uses: actions/setup-node@v2
        with:
          node-version: '16'

      - name: Cache dependencies
        uses: actions/cache@v2
        with:
          path: ~/.npm
          key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
          restore-keys: |
            ${{ runner.os }}-node-

      - name: Install gh-pages
        run: npm i gh-pages --save-dev
        working-directory: ${{env.working-directory}}

      - name: Deploy with gh-pages
        working-directory: ${{env.working-directory}}
        run: |
          git remote set-url origin https://git:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git
          npm run deploy -- -u "github-actions-bot <support+actions@github.com>"
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

```

コードの説明を簡単にしていきます！

#### ワークフローに名前をつける

```yml
name: github pages # ワークフロー全体の名前
```
これは単純にワークフローに名前をつけています(*´ω｀)
自動公開・更新機能の名前だと思っておいてください

#### ワークフロー発動条件の設定
```yml
on:
  pull_request:
    branches:
      - main
```
↑これで、`main`ブランチにプルリクエストがきた時に発動するという意味になります。
```yml
    types:
      - closed
```
↑は、`プルリクエストがクローズした時`という意味です。
合わせると、プルリクエストが来てクローズした時、に発動するってことになります。

mergeされなかったときもされたときもクローズしたことになるので、mergeの有無に関わらず発動はします。

mergeされたときにだけ発動してほしい時は、条件を書くという方法もあります。
[GitHub Actions でプルリクのマージでワークフローを実行する](https://qiita.com/okazy/items/7ab46f2c20ec341a2836)

#### ワークフローの基本の設定
```yml
jobs:
  deploy:
    runs-on: ubuntu-18.04 # ubuntuを使う
    env:
       working-directory: ./my-react-app # my-react-appディレクトリのなか処理を行う
       SUPER_SECRET: ${{ secrets.SuperSecret }} # シークレットキーを使う
    steps:
      - uses: actions/checkout@v2 # ブランチをチェックアウトする
```
↑ここでワークフローの基本の設定をしています。
`working-directory: ./my-react-app`の`./my-react-app`の部分は、Reactが入っているディレクトリにご自身で設定してください！

#### NodeをGitHub上にインストール
```yml
- name: Setup Node  # ワークフローの名前
  uses: actions/setup-node@v2 # setup-node@v2を使う設定
  with:
    node-version: '16' # Nodeのバージョン設定
```
最初に、`Setup Node`というワークフローを走らせます！
NodeをGitHub上にインストールするみたいですねえ～すごいなぁ。

#### キャッシュを使う設定
```yml
- name: Cache dependencies
  uses: actions/cache@v2 # キャッシュを使うよ
  with:
    path: ~/.npm # npmの場所の指定
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }} # 'package-lock.json'を設定
    restore-keys: | # キャッシュを見つけるために使われる代理キー
      ${{ runner.os }}-node- 
```
キャッシュを使う設定をしています。
スピードが上がるんだなぁくらいに思っていますｗ
[依存関係をキャッシュしてワークフローのスピードを上げる](https://docs.github.com/ja/actions/guides/caching-dependencies-to-speed-up-workflows)

#### gh-pagesをインストール
```yml
- name: Install gh-pages
  run: npm i gh-pages --save-dev # gh-pagesのインストール
  working-directory: ${{env.working-directory}} # gh-pagesをインストールするディレクトリの設定。上の方で設定したmy-react-appディレクトリの場所を呼び出しています。
```
GitHub上にインストールしたNode.jsにgh-pagesをインストールしていきます。

#### デプロイ（公開）の設定
```yml
- name: Deploy with gh-pages
  working-directory: ${{env.working-directory}} # 以下のコマンドを実行するディレクトリの設定
  run: | # 実行するコマンド（リポジトリの設定・デプロイ）
    git remote set-url origin https://git:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git
    npm run deploy -- -u "github-actions-bot <support+actions@github.com>"
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }} # GITHUB_TOKENの設定
```
↑いよいよここでデプロイ（公開）の設定をしていきます。

```yml
git remote set-url origin https://git:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git
```
↑で、gitリポジトリを設定しています。こう書くと自動で認識してくれます！
GitHub Actionswを使用する場合、必要な工程だそうです。

```yml
npm run deploy -- -u "github-actions-bot <support+actions@github.com>"
```
↑で`package.json`に書いた`"deploy": "npm run build && gh-pages -d build",`が実行されます。

[Github ActionのヒントをREADME ＃368に追加します](https://github.com/tschaub/gh-pages/pull/368)

[gh-pages](https://www.npmjs.com/package/gh-pages)

### 2. ymlファイルのコミット
![picture 1](images/39ce4e7951a3f50e3768e9ee27cfef40d81c16d6921a20c2011b591f2d564826.png)  

ymlファイルの編集ができたら、`Start commit`のボタンからコミットメッセージを入力して`Commit new file`でコミットします。

## 3. GitHub Pagesの設定
GitHub Pagesを公開する初期設定をしていきます。

![picture 2](images/d96b6678bbe4908b2c36f763f3a950910c0e133355689cd00f7b35c67d6d3620.png)  

リポジトリの中の`Setting`に`Pages`があると思うので、そこをクリックするとこの画面になります！

![picture 3](images/53b7d1ea7ad49b360275901977a08de69b8b0d69859fb633667680ff4773738a.png)  

↑のブランチの設定を`gh-pages`にして`Save`したらOKです✨

### デプロイ（公開）！
実際にmainブランチにmergeして、公開を確認してみましょう～！
公開できていればOKです(*´ω｀)

※`GitHub Pages`の反映にちょっと時間がかかるので、1時間くらい待ってみて確認してみてください✨


**他にも、参考にした文献を↓の記事で紹介しています。**
[kanren id="486"]


