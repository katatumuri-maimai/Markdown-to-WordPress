>------------<
- タイトル:[【7】React Nativeでテキストエディタを作ってみる！【エクスポート・バックアップ編】]
- WordPressにアップロードしますか？:y[]はいn[x]まだしない
- 投稿時:p[]公開d[x]下書き
- カスタムURL:[React-Native-challenge-to-create-text-editor-7]
- カテゴリID:[3,11,12]
- タグID:[]
- 見出し画像のID:[]
- 識別番号[]
>------------<

<!-- ↓続き
[kanren id=""] -->

こんにちは！かたつむり([@Katatumuri_nyan](https://twitter.com/Katatumuri_nyan))です！

Reactを触ってみて、サイト的なものは作れるようになりました(*´ω｀)
そこで、次はReactNativeを触ってみようと思い、簡単なテキストエディタを作成しようと企んでおります(笑)

データの読み書きはできたので、今回はファイルとしてエクスポートしたいと思います！
バックアップもとれるようにしていけたらな～！


[GitHub](https://github.com/katatumuri-maimai/ReactNative-TextEditer)でソースコードを管理しています！

**最初から見る↓**
[kanren id="557"]

**前回を見る↓**
[kanren id="590"]

## ファイルとしてエクスポート
データはJSONとして保存されているみたいです。
これ、メモ帳だけのアプリならいいですが、Markdownテキストエディタとしては不十分なので、ファイルとしてエクスポートしたいと思います(*´ω｀)