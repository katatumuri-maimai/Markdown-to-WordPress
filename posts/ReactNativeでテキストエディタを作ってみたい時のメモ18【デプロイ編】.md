>------------<
- タイトル:[【18】React Nativeでテキストエディタを作ってみる！【デプロイ編】]
- WordPressにアップロードしますか？:y[]はいn[x]まだしない
- 投稿時:p[]公開d[x]下書き
- カスタムURL:[React-Native-challenge-to-create-text-editor-18]
- カテゴリID:[3,11,12]
- タグID:[]
- 見出し画像のID:[]
- 識別番号[5aLARpCAw4vL]
>------------<

<!-- ↓続き
[kanren id=""] -->

こんにちは！かたつむり([@Katatumuri_nyan](https://twitter.com/Katatumuri_nyan))です！

Reactを触ってみて、サイト的なものは作れるようになりました(*´ω｀)
そこで、次はReactNativeを触ってみようと思い、簡単なテキストエディタを作成しようと企んでおります(笑)

アプリの機能としては十分できてきたと思うので、これからビルド・デプロイ・公開申請をしていきます！

[GitHub](https://github.com/katatumuri-maimai/snail_Markdown_TextEditor)でソースコードを管理しています！

**最初から見る↓**
[kanren id="557"]

**前回を見る↓**
[kanren id="661"]


## 環境
- React Native
- Expo
- windows 10

## 参考
- [React Native + Expo - WindowsでアプリビルドからAppストア申請まで！【2020年3月時点】](https://tkd708.hatenablog.com/entry/react_native_expo_windows_from_build_to_app_store_application_2020)
- [Expo公式ドキュメント](https://docs.expo.dev/distribution/building-standalone-apps/)
こちらを参考に公開申請していきます。


## 公開申請用の設定 app.jsonの構成
まず、`app.json`に公開用の設定を書いていきます。[2.app.jsonを構成します](https://docs.expo.dev/distribution/building-standalone-apps/#2-configure-appjson)

既に、`app.json`はあるので、足りなさそうな部分を書き足しました。

```javascript
{
  "expo": {
    "name": "snail_Markdown_TextEditor",
    "slug": "snail_Markdown_TextEditor",
    "version": "1.0.0",
    "icon": "./assets/icon.png",
    "splash": {
      "image": "./assets/splash.png",
      "resizeMode": "contain",
      "backgroundColor": "#ffffff"
    },
    "updates": {
      "fallbackToCacheTimeout": 0
    },
    "assetBundlePatterns": [
      "**/*"
    ],
    "ios": {
+      "bundleIdentifier": "com.katatumuri.snailmarkdowntexteditor",
+      "buildNumber": "1.0.0",
      "supportsTablet": true,
      "usesIcloudStorage":true
    },
    "android": {
+      "package": "com.katatumuri.snailmarkdowntexteditor",
+      "versionCode": 1,
      "adaptiveIcon": {
        "foregroundImage": "./assets/adaptive-icon.png",
        "backgroundColor": "#FFFFFF"
      }
    },
    "web": {
      "favicon": "./assets/favicon.png"
    }
  }
}
```

## ビルド
ビルドしていくので、とりあえず `expo start`します。

### Andoroid用にビルド

> Android用にビルドすることを選択した場合
> expo build:android -t apkAndroid向けにビルドする場合、APK（）またはAndroid App Bundle（expo build:android -t app-bundle）のビルドを選択できます。アプリバンドルをお勧めしますが、プロジェクトでGoogle Playアプリ署名が有効になっていることを確認する必要があります。詳細については、こちらをご覧ください。
> プロジェクトを初めてビルドするときに、キーストアをアップロードするか、それともGoogleに処理してもらうかを尋ねられます。キーストアが何であるかわからない場合は、キーストアを生成してもらうことができます。それ以外の場合は、自由にアップロードしてください。
> Expoにキーストアを生成させることを選択した場合は、後で キーストアを実行して安全な場所にバックアップすることを強くお勧めしますexpo fetch:android:keystore。アプリをGooglePlayストアに送信したら、そのアプリに対する今後のすべての更新 は、Googleが受け入れるために、同じキーストアで署名する必要があります。何らかの理由で、将来プロジェクトを削除したり、資格情報をクリアしたりした場合、キーストアをバックアップしていないと、アプリに更新を送信できなくなります。

Expoの公式ドキュメント通りにやっていきます。
Google Playアプリ署名がわからないので、apkでやってみますｗ
別コンソールを開いて`expo build:android -t apk`

![picture 1](../images/3d0185853a406e0fe6c183d612cd155b2be75daf557e4f54e716dff173a93b2c.png)  

Expoのアカウントがあるので、
ログインします。
![picture 2](../images/0e52d55f405ef0729a757252cc4a381fa6e785c4bf6a5b1aca5bdb63cb4e3ae5.png)  

キーストアを作るか聞かれるので、作っておきます。

![picture 3](../images/50dcf75f4948b9c10270b483516a2db7455a62f5a615e13280d9583a8fec25b1.png)  
ビルド中、Expoのホームでこんな感じで表示されてました。

![picture 4](../images/33fd8573f660274d05d7af3febe901a8bfd1b2c0abc3a8147829fc85fea5ec46.png)  
できたっぽい

### iOS用のビルド
> iOS用にビルドすることを選択した場合
> iOS用のスタンドアロンアプリは、アーカイブexpo build:ios -t archive（expo build:ios -t simulator）ビルドまたはシミュレーター（）ビルドの2つの異なるタイプでビルドできます。シミュレータービルドを使用すると、スタンドアロンアプリをシミュレーターでテストできます。アプリをストアに公開したり、TestFlightなどのツールを使用して配布したりする場合は、アーカイブを使用する必要があります。
> iOS向けにビルドする場合、独自のオーバーライドを提供する機会を持ちながら、Expoに必要なクレデンシャルを作成させるかどうかを選択できます。Apple IDとパスワードはローカルで使用され、Expoのサーバーに保存されることはありません。

公式ドキュメント通りにやっていきます。
`expo build:ios -t archive`

![picture 1](../images/7b5f288f1b8f1de0218e3e6d3e9a2982fba1f0b9c97f5b69bb77110befcf495c.png)  
Appleにログインするよう求められます。

![picture 2](../images/b999247f0ddf9486a853174e6be0d64b14bce277ce136f6e5257830b6211fd0a.png)  
Appleにログインしたら、認証をする必要があるみたいです。

![picture 3](../images/c96d5718600b3a9eedae4752adea7cd9b5b512d8ad53c1fb3f174e5df1475796.png)  
おっと！Appleに課金してないからダメみたいです。
Apple Developerアカウントを作成します。

#### Apple Developerアカウントを作成
[App Store Small Business Program](https://developer.apple.com/jp/app-store/small-business-program/)に登録します。

![picture 4](../images/1dcb6f740de6ba8d58f46bc9fe49bf19922f71f1be7e93f9fd53a0ac01a6cbe7.png)  
登録画面に移動

![picture 5](../images/23f293662f2cf822240c62089e015e388e30b7939102f050fd598f4a2135d061.png)  
ログインします。

![picture 6](../images/522dc150cc6bb7ed98f5188d8675c3013493f388fb0e3e5cda5430aa05d71713.png)  
あれ！だめでした。


![picture 7](../images/6550d328a758a18d11df942e0262c29f7028ebf09943f812518c505abb7ed046.png)  

[developerアカウント](https://developer.apple.com/account/?view=membership#!/welcome#%2Fwelcome)はあるみたいなので、どうしたらいいんだろうｗ

![picture 8](../images/17f58602728abb8504c4d7a98980ae94823eb17a0e3cbcc108e14a5cf3306dd2.png)  

[Apple Developer Program](https://developer.apple.com/jp/programs/)←登録するのはこっちでした！


![picture 9](../images/4c2e209fb4be0208d31709e7fa3e0d7176ff595a00ee9c8a59d93ecb1e3ce64f.png)  
登録していきます。

![picture 10](../images/dc1638a3d870d5b45be9e6cbb474743602a16e199323f86a3f094467c5e84bb6.png)  
個人情報の登録

![picture 11](../images/02f0b43206b014476b96a8da4125d95eebffa118c8c8254fd137eaa1f2d38327.png)  
法人の種類を選択

その後、支払いをします。

![picture 13](../images/cc50da2f0965067fec479f94340cc01a9f25d27756c45aa3af2020f5b6958991.png)  
支払いをしたものの、アクティベート用のメールが来ず、この表示のママなので、待ちます。



![picture 1](../images/e5312e24a4736287a155eb79f2a9ed177a0d2f00dca13ffea26c677036502279.png)  
数日後、アクティベートされたみたいなので、ビルドからやり直します。

#### iOS用にビルド

![picture 2](../images/6d4d191de0ba929c39827693d51c1e4071be82863a50a62eb1fe7c1359531ad1.png)  
ログインします

![picture 3](../images/3017b11df6492d65bfaf6a2bcaa3a0f7e8bf6aa2e0db3976ad0cfa4a011e2615.png)  
ログインすると、Expoを使うかどうか聞かれます。
Expo使う設定にします。

![picture 4](../images/2cc9c517f71410b560565ac594fa9c5d7dfbc035efcca12febfe476a9dc67060.png)  
全部Expoを使うようにします。

![picture 5](../images/8f4da0dccb60eb88339e46fefb730927cdaeb7020c625c176210e6ea7cdb3193.png)  
こちらもExpoにまかせます。

すると、ビルドが始まるので、待ちます。

![picture 6](../images/82b167fc94d0d78db61b80042d7cdc4cea892678d4cda8c03c6acabb810657db.png)  
ちなみに、Expoのサイト上ではこのような表示になっています。

![picture 7](../images/dc32b2f89894a10fe692784c0b1f6f2c9dd92ef69efcc53bc130657116673b79.png)  
ビルドが終わったようです。

## アプリをストアへ送信
ビルドしたアプリを各ストアへ送信していきます。

[公式ドキュメント](https://docs.expo.dev/distribution/uploading-apps/)を見ながら送信していきます。


### Google App Storeへ送信
> 重要：
> ・Googleサービスアカウントを作成し、そのJSON秘密鍵をダウンロードする必要があります。
> ・その後、Google Play Consoleでアプリを作成し、少なくとも1回は手動でアプリをアップロードする必要があります。

とのことなので、Googleサービスアカウントを作成していきます。

#### Google Play Consoleへの登録
![picture 8](../images/7bf8bdbbbbc8704a599d159d98b07a9b1103cba01e07a2e2ea1a8ded6ce2d23e.png)  

[Google Play Console](https://play.google.com/apps/publish/)にアクセスします。

![picture 9](../images/77228e1c079ec1b5480fd67677fabd62c0c071fed58268de5b58761ab9ede565.png)  
利用規約に同意。

![picture 10](../images/8cd0a7165b4f57b684bb194ba73cae6ac2b5c569de19c40431edd21417c1a7f0.png)  
デベロッパーアカウントを作成します。
（ここでも支払いが必要…(;´д｀)トホホ）

[電話番号の書き方](https://xn--jyoukyoutools-v94luk61a2521c.com/?p=3333)を参考に。

![picture 11](../images/d130d7bdd362f9847d82d691e078a7508908cac98af818af230817260d074e66.png)  
クレジットカードで購入します。

![picture 12](../images/cd1f101f79b58794e22bf866709f8a3620ff254301c325242aeccc5892cd418d.png)  
支払い完了


#### アプリの作成
[参考](https://pursue.fun/tech/how-to-android-app-release-overview/)　　

[Google Play Console](https://play.google.com/apps/publish/)で、アプリを作成していきます。

![picture 13](../images/8e9ebe1d9e071ba04c937e2f5d048549836ab276b59db0e13d286efbd798c1b4.png)  
アプリを作成を押す。

![picture 14](../images/b3c9cc77d847a0c01742ba433971e7f5dfdf905649375dab9da8ea117c6c9fc3.png)  
アプリの情報を入力していきます。
アプリを無料に設定すると、公開後に有料にすることはできないようです。

![picture 15](../images/95d4f662c8d488f160549343e6a5fec589fd562131ac7bfb00ab811da186fd0b.png)  
すべてのアプリ一覧に、新しいアプリが表示されました。

#### アプリのセットアップ
![picture 16](../images/29388a6e89e37db2e13390e013e290976c1a0745949562ac85597a006dc11818.png)  
アプリのセットアップをしていきます。

![picture 17](../images/bde3b4c0329b92f039045fb857c8d5fe09234a5f5a8649e1a651271051e95179.png)  
一つ一つ設定していきます。


#### アプリアイコン・グラフィックの作成
アプリのアイコン・グラフィック・スクリーンショットを設定しないといけないみたいなので、作成していきます。



```
Markdown Text Editor - snail

シンプルマークダウンエディタ

シンプルなマークダウンエディタです。

以下の機能が使用できます。
・マークダウン記法での入力
・マークダウンプレビュー
・テーマカラーの変更
・画像挿入（フォトアプリからのインポート）
・マークダウンファイルのインポート・エクスポート（拡張子「.md」）
・テキストファイルのインポート（拡張子「.txt」）
・HTMLファイルのインポート・エクスポート（拡張子「.html」）
・PDFファイルのエクスポート・印刷（拡張子「.pdf」）
・フォルダ分けして保存可能
```


### Apple Storeへ送信
`eas submit -p ios`します。

[WindowsからApp Store Connectにipaファイルをアップロードする](https://takamii.hatenablog.com/entry/2020/12/26/140340)