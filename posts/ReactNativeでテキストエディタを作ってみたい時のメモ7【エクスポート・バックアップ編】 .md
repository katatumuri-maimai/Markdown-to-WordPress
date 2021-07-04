>------------<
- タイトル:[【7】React Nativeでテキストエディタを作ってみる！【エクスポート・バックアップ編】]
- WordPressにアップロードしますか？:y[x]はいn[]まだしない
- 投稿時:p[x]公開d[]下書き
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

これができたら、見た目がすごくダサいので、デザインも変えていきたい…


[GitHub](https://github.com/katatumuri-maimai/ReactNative-TextEditer)でソースコードを管理しています！

よっしゃ！やっていきます！

**最初から見る↓**
[kanren id="557"]

**前回を見る↓**
[kanren id="590"]


## 今回やりたいこと

- マークダウン・HTMLファイルとしてデータをエクスポート
- ファイルを端末内のファイルに保存できるようにする
- ファイルをGoogleドライブなどに共有できるようにする
- バックアップを取れるようにする


## ファイルとしてエクスポートして保存
データはJSONとして保存されているみたいです。
これ、メモ帳だけのアプリならいいですが、Markdownテキストエディタとしては不十分なので、ファイルとしてエクスポートしたいと思います(*´ω｀)

[Expo公式ドキュメント](https://docs.expo.io/versions/latest/sdk/filesystem/)を参考にファイルシステムを導入していきます！

（エクスポートは拡張子指定して保存したら自動でしてくれるんだろうか？）

とりあえず、公式ドキュメント難しいので、やってみます！

`documentDirectory`と`cacheDirectory`が選べるみたいです。
一時ファイルではないので、`documentDirectory`に保存するようにやっていきたいと思います。


`import * as FileSystem from 'expo-file-system';`でインポート。
よし、いけるぞ！

### ディレクトリ・ファイルを作成する
`makeDirectoryAsync`でディレクトリを作成できそうですね。
ディレクトリがない時は作成、あるときは作成しないにも`options`でできそう。

ファイルを保存するメソッドがない…
androidあるけど…？
[reactjs - React native(expo)でテキストファイルを作成する方法は？](https://base64.work/so/reactjs/1763706)
↑これより、`MediaLibrary`でできそうな気がしてきました。
`expo install expo-media-library`します。

`createAssetAsync`でいけるのかな？書いてみます。


とりあえず、ファイルも作成できるのか試してみます。
```javascript
import * as FileSystem from 'expo-file-system';

function saveMdFile(){
  const fileUri = FileSystem.documentDirectory + 'SimpleMarkdown/myFile.md'
  FileSystem.makeDirectoryAsync(fileUri, true)

}
```

```
Possible Unhandled Promise Rejection
```
エラーが出ました！どういう意味…？
`Promise Rejection`が拒否されたってことですかね。
とりあえず、処理はできなかったｗ

`MediaLibrary.requestPermissionsAsync()`
↑これでメディアライブラリへのアクセスの許可を撮ってからやってみます。

```javascript
export default async function saveMdFile(){
  await MediaLibrary.requestPermissionsAsync()
  const fileUri = await FileSystem.documentDirectory + 'SimpleMarkdown'
  FileSystem.makeDirectoryAsync(fileUri, true)
}
```
↑とりあえず、ディレクトリを作成してみます。
(゜-゜)できない。
試行錯誤します！


```javascript
export default async function saveMdFile(){
  await MediaLibrary.requestPermissionsAsync()
  const fileUri = await FileSystem.documentDirectory + 'SimpleMarkdown'
  await FileSystem.makeDirectoryAsync(fileUri, true).then(e=>{
    console.log(e);
  }).catch(err =>{
    console.error(err);
  })
}
```
↑こうしてみると↓のエラーが出ます。
```
ExceptionsManager.js:179 Error: An exception was thrown while calling `ExponentFileSystem.makeDirectoryAsync` with arguments `(
    "file://…省略",
    1
)`
```

```javascript
FileSystem.makeDirectoryAsync(fileUri)
```
もしかして引数の書き方が違う？
↑に変えてみました。
```
> null
```
引数書き間違えみたいですね！ｗｗ
` { intermediates: true }`こうでした！公式ドキュメントはよく読みましょう…

```javascript
await MediaLibrary.requestPermissionsAsync()
```
↑ちなみに、これはいりませんでした。

さて、保存されているっぽいんですが、どこにあるんだろう…
```javascript
FileSystem.readAsStringAsync(fileUri, options)
```
これで確認してみます。

```
Error: File 'file://…省略' could not be read.
```
ファイルないみたいですね！
```javascript
FileSystem.readDirectoryAsync(fileUri)
```
これでディレクトリがあるか確認してみます。


![picture 2](images/8b3312f52cc77bed3a65ffe73a6ed90e22ae2d06a92444dac86e8d6b05521ee7.png)  
いるｗｗｗｗｗ

`FileSystem.makeDirectoryAsync()`これでファイルも保存できるっぽいですね。

でも`FileSystem.readAsStringAsync()`で読み取れません。


中身がないからかもですね。
`FileSystem.writeAsStringAsync()`これで書き込んでみよう！

だめでしたｗ
書き込めません。

`FileSystem.deleteAsync()`これで消してみます。

あ、消せた。



```javascript
export default async function saveMdFile(){
  const directoryUri = FileSystem.documentDirectory + 'SimpleMarkdown/'
  const fileUri = directoryUri + 'test.md'
  FileSystem.writeAsStringAsync(fileUri, "Hello World", { encoding: FileSystem.EncodingType.UTF8 })
    .then(e => {
      console.log("writeAsStringAsync >>" + e);
    }).catch(err => {
      console.error(err);
    })

  FileSystem.readAsStringAsync(fileUri, { encoding: FileSystem.EncodingType.UTF8 })
    .then(e => {
      console.log("readAsStringAsync >>" + e);
  }).catch(err => {
    console.error(err);
  })
  FileSystem.readDirectoryAsync(directoryUri)
    .then(e => {
      console.log("readDirectoryAsync >>"+ e);
    }).catch(err => {
      console.error(err);
    })

}
```

↑の実行結果が↓です。
![picture 3](images/f4e75c7ea0e4922baacb83ba516cc25cf794ad778c83d68e0042de05fa6bca8b.png)  

ファイル作成までできちゃった。
でもどこにいるのかイマイチ分からないですね…。


[reactjs - React native(expo)でテキストファイルを作成する方法は？](https://base64.work/so/reactjs/1763706)
↑より。
 `MediaLibrary.createAssetAsync()`と`MediaLibrary.createAlbumAsync()`でユーザーから見えるところにファイル作れそうですね。
 作ってみます。

 ```
 MEDIA_LIBRARY permission is required to do this operation.
 ```
 ↑エラーが出た！ｗ

```javascript
await MediaLibrary.requestPermissionsAsync()
```
権限の許可が必要なので、再び↑追加します。
（権限の再要求とかの機能も必要そうですね。）

うーん。
```
Error: This file type is not supported yet
```
↑のように出てしまいました。
`MediaLibrary`って、メディアライブラリへの保存だし、そもそも使うものが違うんでしょうね。



`FileSystem.getContentUriAsync(fileUri)`と`share(content, options)`をしてみて、ファイルアプリで開いてみます。

![picture 4](images/cbf311fe7cddfeb284224ac58e8f38214f6f6f3d447ae78581e7ea3da8fad593.png)  
![picture 5](images/fac5b1b9524bb01b1a2e2b6eea7e596b9e6012670244e64bb6835157587b44c4.png)  
![picture 6](images/5043d3f47a4903196fafb6ca4a46d908fe03784a9229d87547d2f32f8e9903f3.png)  

できたー！！やった(*´ω｀)
普段はアプリ内に保存して、取り出したいときはエクスポートできる感じになりましたね！やった！

これならキャッシュフォルダ使えばよさそう。
うまいこと整形して以下の関数になりました～！

```javascript
export async function exportMdFile(filename,content){
  const directoryUri = FileSystem.cacheDirectory + 'SimpleMarkdown/'
  const fileUri = directoryUri + filename

  await FileSystem.makeDirectoryAsync(directoryUri, { intermediates: true })
    .then(e=>{
      console.log("makeDirectoryAsync" + e);
  }).catch(err =>{
    console.error(err);
  })

  await FileSystem.writeAsStringAsync(fileUri, content, { encoding: FileSystem.EncodingType.UTF8 })
    .then(e => {
      console.log("writeAsStringAsync >>" + e);
    }).catch(err => {
      console.error(err);
    })

  await FileSystem.readAsStringAsync(fileUri, { encoding: FileSystem.EncodingType.UTF8 })
    .then(e => {
      console.log("readAsStringAsync >>" + e);
  }).catch(err => {
    console.error(err);
  })
  await FileSystem.readDirectoryAsync(directoryUri)
    .then(e => {
      console.log("readDirectoryAsync >>"+ e);
    }).catch(err => {
      console.error(err);
    })

  const shareUrl =await FileSystem.getContentUriAsync(fileUri)
  console.log(shareUrl);
  Share.share({url:shareUrl})
    .then(e => {
      console.log(Share.sharedAction);
    }).catch(err => {
      console.error(err);
    })
  
}
```

log吐き多いですが、デバッグのためにご容赦くださいｗ

### 日本語ファイル名などで保存できるようにする
今は、冒頭行のテキストがファイル名になるようになっています。
日本語だったりスペースあったりしますよね…。

そこで日本語でも"/"こういうのはいってても保存できるようにします。
[文字列をURIエンコード（エスケープ）・デコードする](https://gray-code.com/javascript/uri-encoding-and-decoding-for-string/)
これで行ってみます！

```javascript
encodeURIComponent(removeMarks(filename))
```

[JavaScript | ファイル名に使えない記号を削除](https://amaraimusi.sakura.ne.jp/sample/js/js_not_mark_file/js_not_mark_file.html)
[String.prototype.replaceAll()](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/String/replaceAll)
"/"に関しては↑を参考にしました。


```javascript
function removeMarks(filename) {
  const marks = ["\\", '/', ':', '*', '?', 'a', "<", ">", '|', /^ */g, /^　*/g];
  let filename_removeMarks = filename;
  for (const i in marks) {
    filename_removeMarks = filename_removeMarks.replaceAll(marks[i], '')
    }
  return(filename_removeMarks);
  }
```


## ファイルを読み込めるようにする
次は、ファイルをほかのアプリ（ファイルアプリなど）から読み込めるようにしたいと思います！

[prscX/react-native-file-selector](https://github.com/prscX/react-native-file-selector)
↑が簡単そうなので、使っていきます！


`npm install react-native-file-selector --save`
`import RNFileSelector from 'react-native-file-selector';`

使えないので、[Undefined is not an object RNFileSelector.Show ](https://github.com/prscX/react-native-file-selector/issues/12#issuecomment-429608135)を見てみると、`link`する必要がありそうです。

`react-native: command not found`とでてlinkできない！
["react-native link" は何をするか](https://qiita.com/lazyppp/items/8d5969cd9a5b53587e18)

[公式ドキュメント](https://reactnative.dev/docs/linking-libraries-ios)より、`npx react-native link react-native-file-selector`してみます。

```
warn Calling react-native link [packageName] is deprecated in favor of autolinking. It will be removed in the next major release.
Autolinking documentation: https://github.com/react-native-community/cli/blob/master/docs/autolinking.md
```

このリンク先によると、`link`は非推奨らしい…


[Expoでreact-native linkが認識されない](https://qiita.com/Kuronuntius/items/83356f49be53efa6292d)
↑あ、察し…
`npm uninstall react-native-file-selector`しました。


[Expo公式ドキュメント](https://docs.expo.io/versions/latest/sdk/document-picker/)にあったので、こちらを使います。

`expo install expo-document-picker`
`import * as DocumentPicker from 'expo-document-picker';`



```javascript
export async function fileSelect(){
  const data = await DocumentPicker.getDocumentAsync()
  console.log(data);
  }
```

![picture 7](images/92ee9f247948aee48d0b9c6ece319372692d7fd3394e31f28c06b33c3f487e3e.png)  

おお！使えました(*´ω｀)

![picture 8](images/8930e62121a29b2de3734274d99f4cba60774b185dd851fd0042323249ec30e2.png)  

データはこんな感じで取り出せますね✨
やった～！


### 読みこんだファイルを保存する
読み込んだファイルは、一時ファイルになるみたいなので、アプリ内に保存できるようにします！
開いた瞬間に保存したいと思います。


```javascript
async function fileSelect() {
  const filedata = await FS.fileSelect()
  const filecontent = filedata.filecontent
  const filename = filedata.filename

  setDataKey(null)
  setTextInput('')
  setFileName('')

  const key = 'SimpleMD' + data.length + 1

  saveFileData()
}
```
`saveFileData()`で保存しています。
むむむ。
↑だとsetStateの値がすぐに更新されないですね…

> なぜセットした値が更新されていないのか？
> なぜセットした値が更新されていないのかというと、setStateで値が更新されるのは関数が呼び出された後だからです。

[【React】「useStateの値を更新しても反映されない！」の解決方法](https://zenn.dev/syu/articles/3c4aa813b57b8c)

↑を参考に改善していきます。

```javascript
async function fileSelect() {
  const filedata = await FS.fileSelect()
  const filename = filedata.filename
  const filecontent = filedata.filecontent
  const key = 'SimpleMD' + (data.length + 1)
  
  setFileData(key, filename, filecontent)
  saveFileData(filecontent, key, filename)
}
```
↑変数として持たせるようにしました。


ちょっとこの機能は難しそうなので、後回しにします！


## 削除機能の作成
データが増えると大変なので、削除機能を作成します。
（ファイルシステム2つあるから移行しないといけないかも…）

`storage.remove();`
↑これで実装していきます。

```javascript
export async function removeData(fileData){
  storage.remove(fileData)
    .then(e => {
      console.log("removeData >>" + e);
    }).catch(err => {
      console.log(fileData);
      console.error("removeData >>" + err);
    })
}
```
なぜか全消しができるようになりました…ｗ

```javascript
<Text style={styles.filelistText} onPress={props.removeData({key:key})>
```
関数を渡すときの記述が間違ってました。

削除機能完成(*´ω｀)


## バックアップ機能をつける
これもシェア機能でディレクトリごとシェアしたらいけそうな気がします。

アプリ内のデータは、`manifest.json`として保存されているので、これをそのままどこかに保存する形でもいいですね。
（この方法だとバックアップから復元もできるな…）

でも今回は、ファイルにエクスポートしたものをディレクトリごとバックアップできるようにします。


…
ファイルの時と同じ方法ではできないですねｗ
どうしよう…


```javascript
dataList.map(async e =>{
  const name = e.name
  const content = e.text
  const fileUri = cacheDirectoryUri + encodeURIComponent(removeMarks(name))

  await FileSystem.makeDirectoryAsync(cacheDirectoryUri, { intermediates: true })
    .then(e => {
      console.log("makeDirectoryAsync" + e);
    }).catch(err => {
      console.error(err);
    })

  await FileSystem.writeAsStringAsync(fileUri, content, { encoding: FileSystem.EncodingType.UTF8 })
    .then(e => {
      console.log("writeAsStringAsync >>" + e);
    }).catch(err => {
      console.log(fileUri);
      console.error("writeAsStringAsync >>" + err);
    })
Share.share({ url: cacheDirectoryUri })
  .then(e => {
    console.log(Share.sharedAction);
  }).catch(err => {
    console.error(err);
  })
}
```

ファイルアプリにはシェアできるのですが、ワンドライブとかにシェアできません。
なんでだろう。

この辺はちょっと課題ですね！


## 今後の予定

ここまでで「テキストエディタが作れるなぁ」と分かってきたので、一旦今作っているのはおいておいて、新しく作りなおそうと思います(*´ω｀)

デザインから計画を立てていくので、続きからはその様子をお伝えします～！