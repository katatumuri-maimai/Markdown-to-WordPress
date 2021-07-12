>------------<
- タイトル:[【15】React Nativeでテキストエディタを作ってみる！【端末タイプや向きによるデザインの変更・デザイン作り込み】]
- WordPressにアップロードしますか？:y[x]はいn[]まだしない
- 投稿時:p[x]公開d[]下書き
- カスタムURL:[React-Native-challenge-to-create-text-editor-15]
- カテゴリID:[3,11,12]
- タグID:[]
- 見出し画像のID:[]
- 識別番号[DaEJWJgNj1bK]
>------------<

<!-- ↓続き
[kanren id=""] -->

こんにちは！かたつむり([@Katatumuri_nyan](https://twitter.com/Katatumuri_nyan))です！

Reactを触ってみて、サイト的なものは作れるようになりました(*´ω｀)
そこで、次はReactNativeを触ってみようと思い、簡単なテキストエディタを作成しようと企んでおります(笑)

今回は、端末タイプや端末の向きによってデザインを変えていきます！
また、ボタンに影をつけたりなど、細かい修正もしていきます。

[GitHub](https://github.com/katatumuri-maimai/snail_Markdown_TextEditor)でソースコードを管理しています！

**最初から見る↓**
[kanren id="557"]

**前回を見る↓**
[kanren id="650"]

## テスト環境
- Android Studio
- iPad Pro 9.7
- iPhone 7
- iPnone X

## 手直ししたい所
1. モーダルの出る向き（iPhone）
2. 縦向きの時のインプット・プレビューエリアのレイアウト
3. 縦向きの時のモーダルのレイアウト
4. 縦向きの時にキーボードの高さに合わせて要素の高さが変更されない
5. 名前が長い時に収まりきらない
6. ボタンなどに影をつける

↑このあたりを直していきたいと思います！

## 1. モーダルの出る向き（iPhone）
![picture 1](images/a98fc6989648b7a94e5a5a049ce91d2d9b9350cd32bba9f4939d3c1990f7154d.png)  

横画面でアプリを使用していても、なぜかモーダルが出る時は縦画面になってしまいますｗ
AndroidStudioではならなかったので、iosの仕様かな…？

このあたりの設定をしていきます。

[iOS: Modal not showing in landscape orientation](https://github.com/facebook/react-native/issues/11036)を参考に、↓以下を追加するとモーダルの向きが変更されました。

```javascript
supportedOrientations={['portrait', 'portrait-upside-down', 'landscape', 'landscape-left', 'landscape-right']}
```


## 2. 縦向きの時のインプット・プレビューエリアのレイアウト
![picture 1](images/9bdccd1a5bfe042ed9e0a3d698347a679d9c1136b405d36381203a1a9355007b.png)  

スマホでアプリ画面が縦向きの時、プレビューエリアがめちゃくちゃ見にくいので、上下にするなど試行錯誤していきます！

iPadのスプリットビューにも対応したいので、アプリが縦向きの場合でアプリの横幅が一定以下の時にレイアウトを変更するようにします。


```javascript
const isWindowWidthSmall = windowWidth < 760

const style={
lexDirection: isWindowWidthSmall ? 'column-reverse': 'row',
}
```

縦向きの判断は↓3番で行っている方法で行いました。

手持ちのiPadの横幅が`768`なので、アプリの横幅が`760`より小さい時に、レイアウトを変更するように設定しました。

![picture 7](images/78d0ac4047de419d93b96de3960746e599c99cb119961fae8e10626ecee9be9d.png)  


## 3. 縦向きの時のモーダルのレイアウト
![picture 2](images/34efa42a83e74887af59c9050d866eb0af357aad19313d828af17f83f092b5cf.png)  

横の長さが足りていないので、レイアウトを変えていきますｗ

端末の向きで判断する方法もありますが、iPadでのスプリットビューでも反映されるのかちょっと分からないので、[useWindowDimensions](https://docs.expo.io/versions/v42.0.0/react-native/usewindowdimensions/)を使っていきます。

単純に、アプリが占めるwindowの、横幅と縦幅の大きさを比較して、縦か横か判断しようとおもいます。

```javascript
const windowWidth  = useWindowDimensions().width
const windowHeight = useWindowDimensions().height
const isLandscape  = (windowWidth / windowHeight) >= 1
```
↑`isLandscape`を`context.js`で定義して、各所で使えるようにしました。

## 4. 縦向きの時にキーボードの高さに合わせて要素の高さが変更されない
![picture 3](images/401d6f02380887d7c73e4ca61a3327fe46a00490807050d83f7666341e613095.png)  
![picture 5](images/331f0a9cbd8f9fdf25f7f062a176a2a7f813edbfba191a81465be19facbc140c.png)  

横画面の時は↓下のように、キーボードを避けるようになってるのですが、縦向きだと適応してくれませんｗ
適応させていきたいと思います！
![picture 6](images/d180ec7c96a954d3d17bb16183e7ba3a7690bed64984f544efffc7a207af9615.png)  

おそらく、`KeyboardAvoidingView`がちゃんと動いてないのだろうというのと、挙動がおかしいので、自分で書き換えられるか検討しました。


## 5. 名前が長い時に収まりきらない
![picture 8](images/2e25268a3aac0230cc0f4f55780ad86e4b6fe0f9e6f0705f86c4e8244a07143e.png)  
![picture 9](images/128e8a4b92f59fb42c22822851f14061b6f612094193381fcb08927952ffce9d.png)  
↑こんな風に、名前がちゃんとおさまっていない場合があるので、調節していきます。

`numberOfLines`で行数を指定し、横幅を固定することで、おさまるようにしました。


## 6.　ボタンなどに影をつける
これはもくもくとやっていきます!
[Shadow Props](https://reactnative.dev/docs/shadow-props)で影をつけます！

全部に適応するのはめんどくさいので、別のファイルで影用のスタイルを書いておいて、共通で使おうと思います。

```javascript
<View style={[style1,style2]}></View>
```

↑React Nativeでは、このようにスタイルを二つ渡すことが可能です。
[React Nativeで複数のstyleを適用する](https://qiita.com/furusin_oriver/items/a05a5327af8b9dda037a)によると、配列にして渡すとどちらも適応され、右側のスタイルの方が強いそうです。