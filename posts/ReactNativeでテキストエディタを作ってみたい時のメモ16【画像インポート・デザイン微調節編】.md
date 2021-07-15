>------------<
- タイトル:[【16】React Nativeでテキストエディタを作ってみる！【画像インポート・デザイン微調節編】]
- WordPressにアップロードしますか？:y[x]はいn[]まだしない
- 投稿時:p[x]公開d[]下書き
- カスタムURL:[React-Native-challenge-to-create-text-editor-16]
- カテゴリID:[3,11,12]
- タグID:[]
- 見出し画像のID:[]
- 識別番号[qUTKpX5eWJXe]
>------------<

<!-- ↓続き
[kanren id=""] -->

こんにちは！かたつむり([@Katatumuri_nyan](https://twitter.com/Katatumuri_nyan))です！

Reactを触ってみて、サイト的なものは作れるようになりました(*´ω｀)
そこで、次はReactNativeを触ってみようと思い、簡単なテキストエディタを作成しようと企んでおります(笑)

ほとんどできてきました！
今回は、最難関の画像インポートと、デザインの微調節をしていきます。

これが終わったら、GooglePlayStoreやAppStoreにアプリとして申請したい！
あともうちょっと！がんばります！

[GitHub](https://github.com/katatumuri-maimai/snail_Markdown_TextEditor)でソースコードを管理しています！

**最初から見る↓**
[kanren id="557"]

**前回を見る↓**
[kanren id="654"]

## 画像のインポート機能を作る
![picture 10](images/c7508733d213419243bc50f8c679a28f81905d4ec8b1a864cde3b72931e8c397.png)  
↑この画像マークを押したときに、画像をインポートできるようにしたいと思います。

インポートした画像は、
```
![image name](URL)
```
↑このように、インプットエリアに自動的に入力されるようにしたいです。

できれば、インポートした画像を一覧にして表示して、そこから選択すると、再度インプットエリアに自動的に入力されるようにもしたいです。

### イメージピッカーの導入
とりあえず、[ImagePicker](https://docs.expo.io/versions/v42.0.0/sdk/imagepicker/)で画像を選び、アプリ内のフォルダに移動しようと思います！

`expo install expo-image-picker`

### 画像を選べるようにする
`ImagePicker.launchImageLibraryAsync`で、画像を選べるようになりました！
自動的にキャッシュに保存されるみたいでした！

それと同時に、キャッシュに保存された画像のuriが返ってきます。

まずは、返ってくるデータから、`![image name](uri)`をクリップボードにコピーして、貼り付けられるようにしてみます。
[expo-clipboard](https://docs.expo.io/versions/v42.0.0/sdk/clipboard/)を利用します。

`expo install expo-clipboard`


![picture 11](images/e49e9ff53b25932d8df47bb0d4b14b4b866c5b754a6e8502b55f79d00c9455f7.png)  
↑クリップボードまでコピーはできたけど、うまくいきませんでしたｗ

uriをbase64にしてみたらうまくいきました。
でもbase64は長すぎるので、テキストエリアに貼り付けたくはないですねｗ

uriも指定できるはずなので…もうちょっと試行錯誤します。


よくよく見てみると、マークダウンを表示しているライブラリに困ったところがありました💦
```javascript
// react-native-markdown-display
// renderRules.js
  image: (
    node,
    children,
    parent,
    styles,
    allowedImageHandlers,
    defaultImageHandler,
  ) => {
    const {src, alt} = node.attributes;

    // we check that the source starts with at least one of the elements in allowedImageHandlers
    const show =
      allowedImageHandlers.filter((value) => {
        return src.toLowerCase().startsWith(value.toLowerCase());
      }).length > 0;

    if (show === false && defaultImageHandler === null) {
      return null;
    }

    const imageProps = {
      indicator: true,
      key: node.key,
      style: styles._VIEW_SAFE_image,
      source: {
        uri: show === true ? src : `${defaultImageHandler}${src}`,
      },
    };

    if (alt) {
      imageProps.accessible = true;
      imageProps.accessibilityLabel = alt;
    }

    return <FitImage {...imageProps} />;
  },
```
↑の一部を↓以下のように変更してみました。
```javascript
  const imageProps = {
    indicator: true,
    key: node.key,
    style: styles._VIEW_SAFE_image,
    source: {
      uri: show === true ? src : `file:///${src}`,
    },
  };
```
こうすると、表示されるようになりました💦

```javascript
const show =
  allowedImageHandlers.filter((value) => {
    console.log(value);
    return src.toLowerCase().startsWith(value.toLowerCase());
  }).length > 0;
```

これは、画像のuri(src)が、`http://`などで始まるかどうかを確認しているみたいですね。

srcが`http://`などではじまっていた時は、そのままsrcを返すし、はじまっていない時は`defaultImageHandler`を前につけるみたいですね。

```javascript
// react-native-markdown-display
// index.js
defaultImageHandler = 'https://',
```
↑この`https://`を`file:///`に変更したらよさそうですね。

他にも治したいところがあるので、[iamacup/react-native-markdown-display](https://github.com/iamacup/react-native-markdown-display)をフォークして自分用に使うことにしました。

`npm install --save katatumuri-maimai/react-native-markdown-display --legacy-peer-deps`

`![image](image.png)`のように、ファイル名のみで表示できるようにカスタマイズしました。


## インポートした画像を一覧をつくる
ここまでで、インポートした画像をアプリ内のディレクトリに保存して、`![image](image.png)`のようなテキストをクリップボードにコピーするという所までできました。

次は、インポートした画像を一覧で表示できるようにしたいと思います。
また、画像一覧から選択することで、再び`![image](image.png)`のようなテキストをクリップボードにコピーできるようにしたいと思います。

### インポートした画像を一覧で表示
![picture 12](images/b0af564278eb583af9c39cbd7660c168e9895abc1b9fdccbd46c3d3843e6adcb.png)  
↑こんな感じで実装しました。
やり方はプロジェクト一覧を作った時と同じです。

### 画像一覧を新着順にする
アプリ起動時に読み込む時の関数を作成し、更新時間の降順にソートした画像リストを作りました。

```javascript
export async function readImages(){
    const imageList = await FileSystem.readDirectoryAsync(imagePickerUri)
    let imageDataList=[];

    for (const i in imageList) {
        const data = await FileSystem.getInfoAsync(imagePickerUri + imageList[i])
        imageDataList.push(data);
    }

    if (imageDataList.length > 0){
         const sort_imageDataList = imageDataList.sort((a, b) => {
            if (a.modificationTime > b.modificationTime)
                return -1;
            if (a.modificationTime < b.modificationTime)
                return 1;
            return 0;
        });
        
        return sort_imageDataList
    }
}
```

### インポートしたらすぐに画像一覧に反映されるようにする
<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">画像の読み込み🖼 <a href="https://t.co/7IICjLaQCp">pic.twitter.com/7IICjLaQCp</a></p>&mdash; Katatumuri (@Katatumuri_nyan) <a href="https://twitter.com/Katatumuri_nyan/status/1414782714427760646?ref_src=twsrc%5Etfw">July 13, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

インポートした時に画像一覧を読み込みなおすのではなく、インポートした画像のみ読み込むようにして実装しました。
```javascript
async function onPressPhoto() {
    props.onPress()
    Image_List.unshift(undefined)
    const image = await importImage()
    console.log(image);
    for (let i in Image_List) {
        if (!Image_List[i]) { 
            !!image ? Image_List.splice(i, 1, image) : Image_List.splice(i, 1)
        }
    }
    props.onPressOut()
}
```
↑これなんですが、ちょっと素人考えなので、改善の余地ありそうです。

インポートボタンを押したら、最初にイメージリストの先頭に`undefind`を挿入し、`importImage`が終わったら、`image`と入れ替えるようにして実装しています。
`props.onPressOut()`がないとできないので、もうちょっと勉強必要そうです。


### iPadで画像の読み込みをキャンセルした時に関数全体がキャンセルされてしまう現象
↑上で書いたコードでだいたい動くのですが、iPadの場合で困ったことがありました。

`onPressPhoto()`では、`importImage()`の返り値を受け取って、その返り値で処理を分岐させています。
返り値がない場合に`onPressPhoto()`自体がキャンセルされてしまうという現象が起こりました。

`onPressPhoto()`は以下です↓

```javascript
export async function importImage() {
    const data = await ImagePicker.launchImageLibraryAsync({ quality: 1 }) // ここ
    console.log(data.cancelled);
    if (!data.cancelled && data.type == 'image') {
        const dataUri = data.uri
        const fileName = dataUri.match(".+/(.+?)([\?#;].*)?$")[1]
        const fileUri = imagePickerUri + fileName

        await FileSystem.makeDirectoryAsync(imagePickerUri, { intermediates: true })
        await FS.copyAsync({ from: dataUri, to: fileUri })
        const imageData= await FileSystem.getInfoAsync(fileUri)

        const text = `![image](${fileName})`
        Clipboard.setString(text)

        return imageData
    } 
}
```

![picture 13](images/58c2d841eb6eccdebf5da7e80548f36292677541544c1fad51f1e8433ce8ebb5.jpg)  
iPadで画像をインポートする際、この画像↑の赤丸の「キャンセル」ボタンを押すと、きちんと返り値があり、処理が実行されます。
ですが、画像選択のウィンドウの外をタップしてキャンセルすると、返り値がなく、`importImage()`の処理が止まってしまい、`onPressPhoto()`自体がキャンセルされてしまいます。


```javascript
const data = await ImagePicker.launchImageLibraryAsync({ quality: 1 }) // ここ
```
↑おそらく、この行でdataに値が格納されず、これ以降の処理が進まないのが原因のようです。

#### 原因の調査
ライブラリのドキュメントをみても、キャンセルの場合も返り値があるとしか書いてなく、スタックオーバーフローなどでも同様の質問を見つけられなかったので（Android関連は見かける）、エンジニアの知り合いに相談しました。
その結果、`ImagePicker`ライブラリ(`expo-image-picker`)の`launchImageLibraryAsync`に`console.log`を挿入し、どこまで処理が進んでいるのか調べることにしました。


```javascript
// build/ImagePicker.js 69行目付近
export async function launchImageLibraryAsync(options) {
    if (!ExponentImagePicker.launchImageLibraryAsync) {
        throw new UnavailabilityError('ImagePicker', 'launchImageLibraryAsync');
    }
    // ここ
    return await ExponentImagePicker.launchImageLibraryAsync(options ?? {});
}
```
↑おそらくこれですね。
`// ここ`までは処理が進んでいることが分かりました。

ということは、`ExponentImagePicker.launchImageLibraryAsync(options ?? {})`の返り値がない…？

`import ExponentImagePicker from './ExponentImagePicker'`と書いてあるので、`ExponentImagePicker`を調べます。

```javascript
// ExponentImagePicker.d.ts
declare const _default: import("@unimodules/core").ProxyNativeModule;
export default _default;

```
↑よくわかりませんｗｗｗｗ

```javascript
// build/ImagePicker.js 69行目付近
export async function launchImageLibraryAsync(options) {
    if (!ExponentImagePicker.launchImageLibraryAsync) {
        throw new UnavailabilityError('ImagePicker', 'launchImageLibraryAsync');
    }

    const data = await ExponentImagePicker.launchImageLibraryAsync(options ?? {})
    console.log('==========');
    console.log(data);
    return data
}
```
↑`launchImageLibraryAsync`をこのように書き換えました。
ウィンドウ外でのキャンセル時は`console.log('==========');`が出力されないので、`ExponentImagePicker.launchImageLibraryAsync(options ?? {})`で止まっちゃってるみたいですね。

`ExponentImagePicker`の定義とかも調べたんですが、探しきれませんでした💦
複雑そうなので、今後の課題にしておこうと思います。


### 画像をインポートした時のモーダルを出す
画像をインポートした時に、同時に`![image](image.png)`のようなテキストをクリップボードにコピーできるようにしていました。
コピーしたことが分かるように、モーダルの様な案内を出そうと思います😊

- コピーしたよ
- 好きな位置にペーストしてね

↑このような案内を出します。

画像一覧の画像をタップしても同じように出てほしいので、モーダルだと少し大げさすぎる気がしました。
そこで、`react-native-elements`の[Tooltip](https://reactnativeelements.com/docs/1.2.0/tooltip#interaction-methods)を使うことにしました！

![picture 14](images/14794031889f7498422156f6b1e122f41b9e604c77410c335c41eaa936b9bc72.png)  
↑こんな感じで表示されます😊

`Tooltip`に一部Modalコンポーネント関連のバグがあったので、ライブラリを編集しました。
今回は、ライブラリの方にプルリクエストを送ってみました。

**修正箇所**
```javascript
// node_modules/react-native-elements/dist/tooltip/Tooltip.js 201行目付近
<ModalComponent animationType="fade" visible={isVisible} transparent onShow={onOpen} 
supportedOrientations={['portrait', 'portrait-upside-down', 'landscape', 'landscape-left', 'landscape-right']} // 追加
>
          {this.renderModalContent()}
</ModalComponent>
```

## カメラからのインポートを実装
![picture 15](images/71d9f602e450ff80b578190d37756c8ef4622b9f7c22e6a5f78dff3b216d8acb.png)  
↑今までは、一番上のアルバムからのインポートのみ対応していました。
カメラからのインポートも追加していきます。

`ImagePicker`の`ImagePicker.launchCameraAsync(options)`を使っていきます！
ほぼメディアライブラリからのインポートと変わりません。

## カメラからのインポートを実装
`DocumentPicker`の`DocumentPicker.getDocumentAsync()`を使います！
ほぼメディアライブラリからのインポートと変わりません。


## 画像削除ボタンの実装
プロジェクトフォルダやファイルを削除するときに使ったやり方で実装します！

## コンポーネントの再レンダリングを監視したい
だんだんiPadの挙動が遅くなってきました。
たぶん、ステート更新しすぎで何度もレンダリングされてるからなのかなと思います。
そこで、[react-devtools](https://www.npmjs.com/package/react-devtools)をインストール。


`npm install -g react-devtools`

が、WSLのせいで開けないので辞めましたｗｗｗ

## LAN接続設定
前からできなかったLAN接続設定ができちゃったので📝
[WSL2で起動したサーバーに外部の端末からアクセスする](https://gunmagisgeek.com/blog/other/7171)を参考にしたらすんなりできちゃいました。
何だったんだろう。
ロードがtunnelモードよりも100倍早くて最高

ポートフォワーディングはタスクスケジューラに登録しました。
[【Windows】PowerShellを管理者権限で起動するコマンド](https://bizlog.tech/powershell-admin-mode/)
[管理者権限で実行するPowerShellスクリプトをタスクスケジューラーに登録](https://blog.yamk.net/posts/20200724-ps1fortaskschedulerasadmin/)


## Androidで`ScrollView`が効かない
Androidで`ScrollView`が全くきいていないことに気づきました💦
色々調べてみてスタイルとかを変えてみても、うまくいきませんでした。

[react native scrollview not scrolling on android](https://stackoverflow.com/questions/55312631/react-native-scrollview-not-scrolling-on-android)より、`import { ScrollView } from 'react-native';`を`import { ScrollView } from 'react-native-gesture-handler';`に変えるとうまくいきました😊
`react-native-gesture-handler`がこんなところで使えましたねｗ



今回はこれで終了です✨
あとはこまごまとした修正をやっていきます！

[JavaScriptで画像をbase64形式のURLに変換するやり方](https://pisuke-code.com/js-way-to-convert-img-to-base64/)