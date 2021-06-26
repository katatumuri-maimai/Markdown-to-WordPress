>------------<
- タイトル:[無料！Reactで作ったサイトを公開・自動更新する方法【Github Pages】]
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
- DockerでNode.jsの環境構築
- create-react-appでReactアプリのひな形作成

※GitHubに登録済み・リポジトリがあるものとして説明していきます！

## やりたいこと
- GitHubにリポジトリがある
- GitHubのrootには`react-app`などのReactのディレクトリがある
- mainブランチにmergeした時にデプロイ・公開されるようにする
- GitHub Pagesへのデプロイの仕方と設定
- Actionsの設定

## GitHubのリポジトリのディレクトリ（ファイル）構造
![DirectoryStructure](images/2021/06/DirectoryStructure.png)
