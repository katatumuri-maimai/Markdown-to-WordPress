>------------<
- タイトル:[【18】React Nativeでテキストエディタを作ってみる！【デプロイ編】]
- WordPressにアップロードしますか？:y[x]はいn[]まだしない
- 投稿時:p[x]公開d[]下書き
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

![picture 6](../images/563fb57ca227a8f043726f9d350837a303033da8637722ea828b340957cb2937.png)  
ビルドしたファイルをダウンロードしておきます。

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
![picture 2](../images/fa162f79360eea2a084cd10386b7ffb22e8d7c9e843695b1c329d53e4c23b5f6.png)  

↑この画面で、アプリのアイコン・グラフィック・スクリーンショットを設定しないといけないみたいなので、作成していきます。

![picture 1](../images/dc75ad44d7abd6f0cff0f14112f084cdb8be9ccc84c1adcaa4985d1053560980.png)  


### アプリのリリース
![picture 3](../images/b6de427c16923181f00c703cd0515b4383c83613237ed85db76a4db12946b033.png)  
アプリを公開する前に、テストしないといけないみたいなので、、、
今回はオープンテストで行うようにしようと思います。

「誰でもGooglePlayで登録することで、アプリをテストできるようにする」を選びました。

#### 国や地域を選択
![picture 4](../images/42d3cd50cff18c4dd4fe3eaaa52aa8ff345babdc637e4f39ede09aebb258424f.png)  
タスクを確認して、リリースする国を追加します。

#### オープンテスト版リリースの作成
![picture 5](../images/c308d5a1310624092852cfb2ff9ba1d819588f868419b1fbe3c7d4e38552e957.png)  


##### アプリバンドルでのビルド
アプリバンドルが必要みたいですね…。
アプリバンドルでビルドしなおします。

`expo build:android -t app-bundle`

![picture 14](../images/32af98d2901b48c54f3e4e24f4434e2cf0c2ce19e9b4fc5252670786f3d9fb1d.png)  
おわりました！

![picture 15](../images/f910bf9f3f7d1e56ef2814647c3c642dea64e90544fe5806d18c0233fb040e72.png)  
こちらをExpoからダウンロードして、オープンテスト版リリースの作成画面でアップロードします。


#### プライバシーポリシーの追加
[こちらのサイト](https://topcourt-law.com/terms_of_service/privacy-policy-for-app)を参考に、プライバシーポリシーを作ります。
このブログの固定ページに掲載して、URLを記載することにします。

[スマホアプリ版アプリケーション・プライバシーポリシー](https://dnp-photobook.jp/app/privacypolicy/)
[]()

### Apple Storeへ送信
私はWindowsなので、直接送信できないのでは…と思い、Expoの有料プランに登録するか迷っていました。
（MacOSでしか使えなさそうなTransporterというアプリが必要）

そこでこんな記事を発見→[WindowsからApp Store Connectにipaファイルをアップロードする](https://takamii.hatenablog.com/entry/2020/12/26/140340)
ひとまずは、この方法で試していきたいと思います。


#### App Store Connectへの接続
![picture 7](../images/90516ae1352c0f6adfc873e87375cf2fc7dace1a1b6f96a729f164aee28c9e08.png)  
App Store Connectとやらに接続しないといけないみたいなので、接続していきます。

![picture 8](../images/cf4fbe549bb7bc7d508a7023ce92103fe02549ed16af0445fbaeaf5b6e42aa79.png)  
なにやら管理画面が出てきました！
「マイApp」を選択します。

#### Appを追加
![picture 9](../images/96b51d4c7ee5879386ed588238ec93582640aa4ad7cff2b949a24c95ccc5eeb5.png)  
ここからアプリを追加していきます。

![picture 10](../images/91bf39faff20dd4781b893e9159d289bd34010e118a125046471277aafc3bc77.png)  
ここでもアプリの情報を入力していきます。

![picture 12](../images/044de04f9839554bfa27e7c8edfb18c65adba11d82d924793f5d64e426a0afd9.png)  
iOSを選択

[こちら](https://zenn.dev/moutend/articles/feebf0120dce6e6426fa#%EF%BC%88%E8%A3%9C%E8%B6%B3%EF%BC%89sku%E3%83%BBapp-id%E3%83%BBbundle-id%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6)の記事によると、SKUはなんでもいいらしい！

#### App情報を追加
![picture 13](../images/a40fa22957768cbea6c81500803114db6e9f51dffc5e2005a7d2719bc4966fab.png)  
こちらで、アプリの情報を追加していきます。
追加できたら、「審査へ提出」をおします。

#### ビルド
![picture 1](../images/743ab17a6930f2e1e965bf53aaf15198952f889be104f45158cbd2bc7eedd633.png)  
アップロードツールを表示を押します。

![picture 5](../images/dfeeae6823d84d20a5695fa4cc3ab5042a4fda6acd16038a0511a0539f863fb9.png)  

Xcodeはないので、「Transporter App をダウンロード」を押したいところですが、Mac用のリンクなので、違うとこから行きます。

上の方で紹介した、[WindowsからApp Store Connectにipaファイルをアップロードする](https://takamii.hatenablog.com/entry/2020/12/26/140340)を参考に、Windows用の`Transporter`をダウンロードします。

[Transporter User Guide 2.2](https://help.apple.com/itc/transporteruserguide/en.lproj/static.html)こちらからダウンロードしていきます。
ちなみに、linux用の物もあるようです。

![picture 6](../images/5f604d9bf3c073ebe291e4327cf847154ae65070282274a3271f983d473304bb.png)  

Windowsというリンクからダウンロードできます。

![picture 7](../images/f32a3326e8c20d0931f7f8ce1cffaa08b40620661a82772d5545bba49ab4970e.png)  

詳細を押して
![picture 8](../images/646be5cb4793777f0513ee5cfd918187ea61212e2e275a3b17dbb6ae93fca35f.png)  
実行を押します。

![picture 9](../images/5c4e707f773bebb97e97243e3e835e8bf727855c6d70daddbe2150557f1d43fa.png)  

![picture 10](../images/131ca6090e14da6e9d7a0dff900b500ad274a3ced65283849123a39ab3aac623.png)  

![picture 11](../images/b863014500ada80ffdde67ba3f969b96ebf94ab9f7b25cd602e25640b8fdf85e.png)  

![picture 12](../images/eec3657a3dcd5fc216ba7cfd7169773128ebf9f591ebae58ff23d6a9cb155cb5.png)  

> 'C:\Program Files (x86)\itms というところに iTMSTransporter.cmd があるので、これをPowerShell上で実行すればよさそうです。
PowerShell上で以下を行います。

`& 'C:\Program Files (x86)\itms\iTMSTransporter.cmd' -help`

![picture 13](../images/64d0fff907bb6aacdbba23b1653c4c22698400cdef7509647b78aa58a98e51ef.png)  
こんな感じになった…ｗ
ちゃんとインストールされてますね

次は、以下をPowerShellで打ちます。

`App uploads for macOS, Linux, and Windows: Specifies the directory and filename for the app source file (.pkg or .ipa). For Linux and Windows, -assetDescription is required.`

`& 'C:\Program Files (x86)\itms\iTMSTransporter.cmd' -m upload -assetFile 【ipaファイルの場所】 -u 【Appleconnectのユーザー名】  -p 【Appleconnectのパスワード】 -assetDescription .\Desktop\AppStoreInfo.plist -v eXtreme`


あ、、、これMac無いとアップロードできないやつですね…。
詰みました💦

結局、Macでアップロードして申請提出しました🙇💦