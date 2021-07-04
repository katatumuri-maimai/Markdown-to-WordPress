>------------<
- タイトル:[【5】React Nativeでテキストエディタを作ってみる！【テキストエリア作成編】]
- WordPressにアップロードしますか？:y[x]はいn[]まだしない
- 投稿時:p[x]公開d[]下書き
- カスタムURL:[React-Native-challenge-to-create-text-editor-5]
- カテゴリID:[3,11,12]
- タグID:[]
- 見出し画像のID:[]
- 識別番号[HPawWtD9Sf46]
>------------<



こんにちは！かたつむり([@Katatumuri_nyan](https://twitter.com/Katatumuri_nyan))です！

Reactを触ってみて、サイト的なものは作れるようになりました(*´ω｀)
そこで、次はReactNativeを触ってみようと思い、簡単なテキストエディタを作成しようと企んでおります(笑)

Dockerでの環境構築が難しかったので、やっとWSLで環境構築できました～！
これからテキストエリアを作成していきたいと思います！


**最初から見る↓**
[kanren id="557"]

**前回を見る↓**
[kanren id="572"]



## 環境
- Windows10
- WSL2
- Expo
- React Native
- AndroidStudio
- iPhone
- iPad

WSL2にReact NativeとExpoが入っています！

とりあえず、タブレット用の画面を作っていきます！
iPadとAndroidStudioのタブレットエミュレーターを確認しながら作ります。

![picture 2](images/ef373b0ce77e519ede33f71aa3c880af4de7a798abfaf12630fa3df6bba0686e.png)  

iPadは横向きになるけど、Androidはならないですね💦
ExpoかReact Native側の設定かなー💦

横向きはできるんですが、Expoを開くと横から縦になるんですよね。なんでだろう。
iPhoneも横向きにならない💦
コードで改善するかもなので進めます。


## 画面の向き検知

[【ReactNative】端末の向き変更を検知する](https://zenn.dev/nekoniki/articles/a5dfc8f7c78a61)
↑より、コード変更してみます。
コンソールってどこに表示されるのかなｗ(npm start したターミナルや19002の開発ツールに表示されました！)

[React Nativeで画面を回転させた際に再描画させる方法](https://hacknote.jp/archives/28348/)


[expoでdefaultの画面の向きを設定する。](https://qiita.com/kaba/items/e1469b034bd2d7be433e)
↑これで一応横にはなりました！でも、次は縦にならないｗｗ

とりあえず、横向きになったので、これでいきます！


## テキストエリアの作成
React Nativeにテキストエリアコンポーネントの準備がない！
自作するとエラーがでる！
ってことで↓
[What is an alternative of textarea in react-native?](https://stackoverflow.com/questions/41678570/what-is-an-alternative-of-textarea-in-react-native)

TeaxtInputコンポーネントが使えるそうなので使います。

でか、HTMLもCSSも使えないじゃん！
Reactと違いすぎるｗ

困ってしまってワンワンわわん
ウェブビューみたいなの使ったら使えた気もしますが、、ちょっと分からないので進めていきます。


## スタイルの設定
[React Nativeで動的スタイルを作成できますか？](https://www.it-swarm-ja.com/ja/css/react-native%E3%81%A7%E5%8B%95%E7%9A%84%E3%82%B9%E3%82%BF%E3%82%A4%E3%83%AB%E3%82%92%E4%BD%9C%E6%88%90%E3%81%A7%E3%81%8D%E3%81%BE%E3%81%99%E3%81%8B%EF%BC%9F/1052490967/)

この辺から集中して作ってるので、メモ書きになります💦
URLとかペタペタ張っていくかも。

とりあえず、関数による動的なスタイルの作成の仕方が分かった。

```javascript
import React from 'react';
import { FC, useEffect, useState} from 'react';
import { StyleSheet, TextInput, View, Dimensions} from 'react-native';

export default function App() {
  const [windowWidth, setWidth] = useState(100)
  const [windowHeight, setHeight] = useState(100)

  useEffect(() => {
    let Width = Dimensions.get('window').width;
    let Height = Dimensions.get('window').height;
    setWidth(Width)
    setHeight(Height)
  }, []);
  
  function AppStyle(){
    return ({
      flex: 1,
      flexDirection: 'row',
      flexWrap: 'wrap',
      alignItems: 'stretch',
      width: windowWidth,
      height: windowHeight,
      backgroundColor: 'black',
    })
  }

  return (
    <View style={AppStyle()}>
        <MyPanel
        value="panel"
        />
      <MyTextArea/>
        <MyPreview
          value="ぷれびゅ～"
        />
    </View>
  );
}
```

![picture 3](images/7533da69b617e20c6e3cc11c0d73dbc3e3391ee7b515a6a2fa7bc0184054e962.png)  

大分怪しい見た目ですが、とりあえず、パネル+テキストエリア+ぷれびゅ～のエリアは作成できました。

## 入力をぷれびゅ～に反映
マークダウンで書くことを想定しているので、PreviewはHTMLのつもりです。
ですが、まずはテキストエリアに書いた物をそのままPreviewしていきたいと思います。

![picture 4](images/3ad0710eb7e2735ae5101e627ab185869c2e9ae93054c1b9e520b14d87e81af8.png)  
できたぁ

これはReactのコンポーネント間の値の受け渡し方と一緒ですね。

## テキストエリアのスタイル変更

### テキストエリアの文字の位置変更
なぜかAndroidだけ、テキストエリアの真ん中に文字がくるので変えます。

[公式ドキュメント](https://reactnative.dev/docs/text-style-props)にありました！

`textAlignVertical`

ちなみに、CSS的な物を書けるのですが、数値は`0`みたいに数字だけ書くか、`"0%"`みたいに％つけてクウォーテーションで囲むらしいです。
AndroidとiPadと全然適応が違いすぎてむずかしいですう。

## テキストの頭に数字をつける
できなさそう…。

## マークダウンに対応してみる。
[iamacup/react-native-markdown-display](https://github.com/iamacup/react-native-markdown-display)
ライブラリの使い方がまだ謎ですが、挑戦してみます！

`npm install -S react-native-markdown-display`

とりあえず、使ってみましたがエラー…？
```
Failed building JavaScript bundle.
Unable to resolve module punycode from /home/mymai/ReactNative_TextEditor/node_modules/markdown-it/lib/index.js: punycode could not be found within the project.
```

`punycode`がないらしいですね。
`npm i punycode`してみます。
expo再起動
（果たしてライブラリが使えるように私はなるのか！）

![picture 5](images/49d247b064e5356d30183aced82d0a95fb9bd8ab2e2a4403eb78dbbfc798a384.png)  

↑いけました！
右上の`text`ってやつですね。中身は`## text`なので、ちゃんとできてます。

Previewコンポーネントと置き換えていきます。

![picture 6](images/77e4599fbdd315490579542ff7dc7aae7d67a1cf6511293b747f20c5a104fd9e.png)  
なぜか文字を打つと右側に出現するようになりましたｗｗ

どうやら置き換えるんじゃなくて、中に入れるといいらしい

```javascript
<Markdown style={styles.preview}>
    {props.value}
  </Markdown>
```
↓
```javascript
<Text style={styles.preview}>
    <Markdown>
      {props.value}
      </Markdown>
  </Text>
```

iPadでpaddingがきかない😢
Androidは入力中にMarkdownコンポーネントが動くｗｗｗ
なんやこれｗ

- Android→謎
- iPad→Markdownコンポーネントが浮いてるっぽい

こちらは、Markdownライブラリのスタイルを上書きすることで治りました。

![picture 7](images/c9ff96627445b40b601b7010e57eb924abbf0b6cb5d109795438c1920d152a75.png)  


## メニューバーの追加
メニューバーを上に追加していきます。
こればコンポーネントでいけそう

[View](https://reactnative.dev/docs/next/view)コンポーネントがHTMLでいう`div`みたいな物っぽいので、それを使っていきます。

![picture 8](images/bd5ac515089cde35a9ab91e3a1475484c0e58b9b5d3f41dbe3d9a27f2dcf0152.png)  

```javascript
import React, { Component } from 'react';
import { View,StyleSheet, Text} from 'react-native';

export default function MenuBar(props) {

  return (
    <View style={styles.menuBar}>
      <Text>バー</Text>
    </View>
      
  );
};

const styles = StyleSheet.create({
  menuBar: {
    backgroundColor: '#35071e'
  }
});
```
色が怪しいですが、こんな感じで基礎を作りました。

ここに閉じるボタンとかおきたい。

### ボタンの追加
[ボタン](https://reactnative.dev/docs/next/button)コンポーネント使っていきます。

ボタンのスタイルが変えられない💦

[Expo](https://docs.expo.io/ui-programming/react-native-styling-buttons/)にボタンの作り方があったのでこちらからボタンを作ります。

あと、iPhoneなどで角が見切れちゃうので、メニューバーの`View`を`SafeAreaView`に変更。

![picture 9](images/829f130b52c724942e63f5d5c49d752ad3d93b800e533fe1476bdc88391a5bbf.png)  

またまた怪しいですが、とりあえずのボタン完成ですｗ

```javascript
<SafeAreaView style={styles.menuBar}>
    <Pressable style={styles.button}>
      <Text style={styles.buttonText}>閉じたい</Text>
    </Pressable>
    <Text>🐌SimpleMarkdown</Text>
</SafeAreaView>
```

こんな調子でパネルやメニューバーに、色んなボタンを作っていこうかなと思います。


とりあえず、アプリが作れることは分かってきたので、今日はこの辺で終わります(*´ω｀)

わーい！たのしい！

↓続き
[kanren id="590"]