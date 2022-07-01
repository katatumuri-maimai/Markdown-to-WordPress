>------------<
- タイトル:[【19】React Nativeでテキストエディタを作ってみる！【再公開申請編】]
- WordPressにアップロードしますか？:y[x]はいn[]まだしない
- 投稿時:p[x]公開d[]下書き
- カスタムURL:[React-Native-challenge-to-create-text-editor-19]
- カテゴリID:[3,11,12]
- タグID:[]
- 見出し画像のID:[]
- 識別番号[IzC5Mdi4buJl]
>------------<



こんにちは！かたつむり([@Katatumuri_nyan](https://twitter.com/Katatumuri_nyan))です！

Reactを触ってみて、サイト的なものは作れるようになりました(*´ω｀)
そこで、次はReactNativeを触ってみようと思い、簡単なテキストエディタを作成しようと企んでおります(笑)

前回までで公開申請までできましたが、iOSバージョンが公開却下になってしまったので、再公開申請していきたいと思います(*^^*)

[GitHub](https://github.com/katatumuri-maimai/snail_Markdown_TextEditor)でソースコードを管理しています！

**最初から見る↓**
[kanren id="557"]

**前回を見る↓**
[kanren id="709"]


## 却下の原因
![picture 1](images/0ccc3f1912d073292c6c75abd6bf75eb0b7652bff145a9ea0a8180317ac4d933.png)  

公開申請をしたら却下されてしまいました(´;ω;｀)
却下の原因は以下の2点です。

- Design: Preamble
- 1.1 Legal: Privacy - Data Collection and Storage

### Design: Preamble
> Guideline 4.0 - Design
> We noticed an issue in your app that contributes to a lower quality user experience than Apple users expect:
>- Your app's modal alerts are written in English while the app is set to the Japanese localization. To help users understand why your app is requesting access to a specific feature, your app's modal alerts should be in the same language as your app's current localization.
> Appleユーザーが期待するよりも品質の低いユーザーエクスペリエンスの原因となるアプリの問題に気づきました
> 。-アプリが日本のローカリゼーションに設定されている間、アプリのモーダルアラートは英語で書かれています。アプリが特定の機能へのアクセスを要求している理由をユーザーが理解できるように、アプリのモーダルアラートはアプリの現在のローカリゼーションと同じ言語である必要があります。

なぜかモーダルの言語が一致しないということだったんですが、送られてきているスクリーンショットでは、一致していたのでスルーしてみます。

### 1.1 Legal: Privacy - Data Collection and Storage
> アプリがカメラと写真にアクセスするためのユーザーの同意を要求していることに気付きましたが、目的の文字列でのカメラと写真の使用について十分に説明していません。
> ユーザーがデータの使用方法について十分な情報に基づいて決定できるように、権限リクエストアラートでは、アプリがリクエストされた情報をどのように使用するかの例を説明し、含める必要があります。

このような表示だったので、以下のように`app.json`を編集しました
[参考](https://qiita.com/mildsummer/items/3b17cf6f80e04ad37578)

![picture 2](images/41cd29df3a9a27c7f31ed6743926bae4f4522a2fd539ded77699d1f3a6e02cab.png)  


再ビルドしてみます。

`expo build:ios -t archive --clear-provisioning-profile`


## 再度提出却下
直したのに前回と同じ文言で却下されました…ｗ

- Design: Preamble
- 1.1 Legal: Privacy - Data Collection and Storage


### Design: Preamble
> Appleユーザーが期待するよりも品質の低いユーザーエクスペリエンスの原因となるアプリの問題に気づきました
> 。-アプリが日本のローカリゼーションに設定されている間、アプリのモーダルアラートは英語で書かれています。アプリが特定の機能へのアクセスを要求している理由をユーザーが理解できるように、アプリのモーダルアラートはアプリの現在のローカリゼーションと同じ言語である必要があります。

[poでLocalization native development regionをJapanにしてDatePickerIOSを日本語にするために、app.jsonにinfoPlistを設定する的なお話](http://watanabeyu.blogspot.com/2017/09/expolocalization-native-development.html)を参考に、`app.json`の設定を変えます。

うまくいきません…ｗ

[react-nativeとexpoを使用してiOSアプリに異なる言語を設定する](https://stackoverflow.com/questions/45962000/set-up-different-language-for-ios-app-using-react-native-and-expo)これを見て、日本語にしてみます。

[iOSアプリのローカライズ](https://docs.expo.dev/distribution/app-stores/#localizing-your-ios-app)も見て設定してみました。


↓続き
[kanren id="717"]