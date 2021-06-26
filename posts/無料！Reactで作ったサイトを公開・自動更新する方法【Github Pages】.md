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


## 環境
- ソースコードをGitHubで管理
  - GitHubにリポジトリがある
- DockerでNode.jsの環境構築
- create-react-appでReactアプリのひな形作成

※GitHubに登録済み・Reactで作ったサイト・アプリのリポジトリがあるものとして説明していきます！

### ローカルのディレクトリ（ファイル）構造
![DirectoryStructure](images/2021/06/DirectoryStructure.png)
ローカルのrootには`react-app`などのReactのディレクトリがあります！

### GitHubのリポジトリのディレクトリ構造
![DirectoryStructure_GitHub](images/2021/06/DirectoryStructure_GitHub.png)

GitHubのrootには`react-app`などのReactのディレクトリがあります！

## やりたいこと
- GitHubでmainブランチにmergeした時にReactサイトが公開・自動更新されるようにしたい


## Reactで作ったサイトを公開・自動更新する方法の手順
1. Actionsの設定
  1. workflowの作成
  2. `gh-pages.yml`ファイルの編集
2. GitHub Pagesの設定
3. デプロイ（公開）！

それでは、早速準備を進めていきましょう！

## Actionsの設定
まずは、GitHub Actionsの設定をしていきます！
GitHub Actionsの機能を使って、公開・自動更新機能を作成しちゃいます(*´ω｀)

### 1. workflowの作成
Actionsのタブから新しくworkflowを作成していきます。
![GitHubActions](images/2021/06/GitHubActions.png)

![GitHubActions_new](images/2021/06/GitHubActions_new.png)

### 2. ymlファイルの編集
workflowのファイルを作成します！
今回は、`gh-pages.yml`って名前にしましたｗ

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

## GitHub Pagesの設定
GitHub Pagesを公開する初期設定をしていきます。

### デプロイ（公開）！
実際にmainブランチにmergeして、公開を確認してみましょう～！






























## 疑問
- サブディレクトリのサイトはどうやって公開？
  この方法でどうにでもなる
※公開の方法も別で書こうかな
