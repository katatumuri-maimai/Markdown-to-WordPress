>------------<
- タイトル:[【20】React Nativeでテキストエディタを作ってみる！【EAS CLIでデプロイ編】]
- WordPressにアップロードしますか？:y[x]はいn[]まだしない
- 投稿時:p[x]公開d[]下書き
- カスタムURL:[React-Native-challenge-to-create-text-editor-20]
- カテゴリID:[3,11,12]
- タグID:[]
- 見出し画像のID:[]
- 識別番号[WrvOYZrBRd7U]
>------------<

<!-- ↓続き
[kanren id=""] -->

こんにちは！かたつむり([@Katatumuri_nyan](https://twitter.com/Katatumuri_nyan))です！

Reactを触ってみて、サイト的なものは作れるようになりました(*´ω｀)
そこで、次はReactNativeを触ってみようと思い、簡単なテキストエディタを作成しようと企んでおります(笑)

macを借りて公開するのがめんどくさすぎるので、EAS CLIを使って公開していきます。

[GitHub](https://github.com/katatumuri-maimai/snail_Markdown_TextEditor)でソースコードを管理しています！

**最初から見る↓**
[kanren id="557"]

**前回を見る↓**
[kanren id="716"]

[公式ドキュメント](https://docs.expo.dev/build/setup/)を見ながら作業していきます。

## 最新のEASCLIをインストール
`npm install -g eas-cli`

## Expoアカウントにログイン
`eas login`
EXPOのアカウントでログインします。

`eas whoami`でログインで来てるか確認

![picture 1](../../images/be78a9e1e6d23fb0b440ff93b44c41d8b254d9171a8630c321ee5b4630c91fa2.png)  

できました。

## プロジェクトを構成
`eas build:configure`

![picture 2](../../images/842a398a87352dc96a3a1026bc5364dc575730abce95042a5bc896e29eddcfd6.png)  


## ビルドを実行
`eas build --platform ios`
appleのアカウントにログインするとビルドが始まります

![picture 3](../../images/e8a5a45cdd402c875ee4624878a77d496a9254b613ddaf3dd7882555a3846351.png)  
ビルドできました

## 送信を開始
`eas submit -p ios`

![picture 4](../../images/53ef9cfaad9c09123252cc245406239df68a1db8739c4ccf935b7c6815a156ae.png)  

送信できました！

このまま申請出します。
→受かりました！