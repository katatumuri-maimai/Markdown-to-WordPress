>------------<
- タイトル:[【3】React Nativeでテキストエディタを作ってみる！【テキストエリア作成編】]
- WordPressにアップロードしますか？:y[x]はいn[]まだしない
- 投稿時:p[]公開d[x]下書き
- カスタムURL:[React-Native-challenge-to-create-text-editor-3]
- カテゴリID:[3,11,12]
- タグID:[]
- 見出し画像のID:[]
- 識別番号[]
>------------<

こんにちは！かたつむり([@Katatumuri_nyan](https://twitter.com/Katatumuri_nyan))です！

Reactを触ってみて、サイト的なものは作れるようになりました(*´ω｀)
そこで、次はReactNativeを触ってみようと思い、簡単なテキストエディタを作成しようと企んでおります(笑)

環境構築があらかた終わったので、早速画面を作成してみたいと思います！


[GitHub](https://github.com/katatumuri-maimai/ReactNative-TextEditer)でソースコードを管理しています！

**最初から見る↓**
[kanren id="557"]

**前回を見る↓**
[kanren id="559"]


## いきなりエラーから始まります…
![picture 1](../images/123927f99a07ed87ca0beb39fefd9a2bbb4bd6e4ac201cd1721440248597feaf.png)  

```
/usr/src/app/node_modules/react-native-web/node_modules/fbjs/lib/ExecutionEnvironment.js
Error: ENOENT: no such file or directory, open '/usr/src/app/node_modules/react-native-web/node_modules/fbjs/lib/ExecutionEnvironment.js'
```

これは前回の記事の最後に`expo upgrade`したせいですね…。
これ、`react-native-web`がインストールされてないってことかなぁ…。
と思い、確認するとありました。
でも
`/usr/src/app/node_modules/react-native-web/node_modules/fbjs/lib/ExecutionEnvironment.js`はないですね…。

![picture 2](../images/ca86bce1f2c68e86f5281730e93a7c858bec2afd910f8c0fd69c1f0888bca77a.png)  

よく見たら、`expo upgrade`のエラーが残っていました。
内容は同じっぽいですね。


![picture 3](../images/58bfb70e2700a0384218d1d369e42e45497e76e5ead9e3073fa21e7b2cdc03db.png)  
↑一応コンテナ側で確認するも、確かに`/usr/src/app/node_modules/react-native-web/node_modules/fbjs/lib/ExecutionEnvironment.js`はない…。

`react-native-web`を入れなおしてみます。
`yarn add react-native-web`をしてインストール


![picture 4](../images/6482375d3d2861c8a0c6ef2a6b7b6dd63cb842b94bbabc7f983f16f7f2765cc6.png)  

```
/usr/src/app/node_modules/react-dom/node_modules/scheduler/index.js
Module build failed: Error: ENOENT: no such file or directory, open '/usr/src/app/node_modules/react-dom/node_modules/scheduler/index.js'
```

次はこれ↑

`yarn upgrade`もしてみたけど、とくに変わらないので、Docker imageからbuildしなおすことにしました。`expo`の初期化はなし。


## Google Chromeデベロッパーツールの拡張
やっと開発できるようになったので、デベロッパーツールでiPhoneとiPadの表示を確認しながらやっていきます。

![picture 5](../images/e44d709426e4cc366f6bf1c48a3aa46b8960aad491e86e8cea17fc3350746d29.png)  

こんなことができたので( ..)φメモメモ

三点マークを押して、`show device frame`で一部のデバイスのフレームが表示されました。

## 今のディレクトリ構成
![picture 6](../images/987bb665cb2d7fc203b662742be3172ee268680760ec4e024503d1a935f76662.png)  

`App.js`がおそらくメインの枠になるので、これに合わせてコンポーネントを作っていきます。

## ためしにテキストエリアを作成
そもそも、テキストエリアって、Inputエリアでいいのかな…？

とりあえず、`TextArea.js`を作成し、`App.js`に読み込んでみます。
素材は[公式リファレンス](https://docs.expo.io/versions/v41.0.0/react-native/textinput/)から。

```javascript
// App.js
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import UselessTextInput from './components/TextArea';

export default function App() {
  return (
    <View style={styles.container}>
      <UselessTextInput
      value="Hello World!"
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
```

```javascript
// TextArea.js
import React, { Component } from 'react';
import { TextInput } from 'react-native';

export default function UselessTextInput(props) {
  const [value, onChangeText] = React.useState(props.value);

  return (
    <TextInput
      style={{ height: 40, borderColor: 'gray', borderWidth: 1 }}
      onChangeText={text => onChangeText(text)}
      value={value}
    />
  );
};
```

![picture 7](../images/747a6f470c61e29af107d38340b8995b15e0689caca62b84333a804fca3e5712.png)  

とりあえず、文字は打てるようになりました(*´ω｀)


## テキストエディタパッケージを使用するも断念
[React Native Editor](https://www.npmjs.com/package/react-native-editor)

`npm i react-native-editor`してみる。
互換性があれば使いたい。

ちょっと使ってみたけど、読み込みが遅すぎるので再起動したらエラー…
`yarn install`しろとのことなので、しておきました。


![picture 8](../images/f1f8c3446b09f79425c29e8356c5ec12e95a2140f2c3b33445dcd8f524df7b83.png)
```  
/usr/src/app/node_modules/react-native-editor/src/RichToolbar.js  
Module not found: Can't resolve '../img/icon_format_bold.png' in '/usr/src/app/node_musr/src/app/node_modules/react-native-editor/src'
```
`RichToolbar.js `の14行目くらいを以下に変更


```javascript
function getDefaultIcon() {
    const texts = {};
    texts[actions.insertImage] = require('../img/icon_format_media@3x.png');
    texts[actions.setBold] = require('../img/icon_format_bold@3x.png');
    texts[actions.setItalic] = require('../img/icon_format_italic@3x.png');
    texts[actions.insertBulletsList] = require('../img/icon_format_ul@3x.png');
    texts[actions.insertOrderedList] = require('../img/icon_format_ol@3x.png');
    texts[actions.insertLink] = require('../img/icon_format_ol@3x.png');
    return texts;
}
```

![picture 9](../images/36998eb0ca82a7e607ecb573c18670fb0ec962baa715de7fdac052352af0e358.png)  
```
/usr/src/app/node_modules/react-native-editor/src/RichEditor.js    
react_native_1  
Module not found: Can't resolve 'react-native-webview' in '/usr/src/app/node_modules/react-native-editor/src'
```


次はこれなので、`expo install react-native-webview`してみる
[WebView](https://docs.expo.io/versions/latest/sdk/webview/)

やっぱりうまくいかない😢


`react-native-editor`は一旦やめて、自前で作ることにしました。

`npm rm react-native-editor`


## テキストエリアを作成









<!-- ↓続き
[kanren id=""] -->