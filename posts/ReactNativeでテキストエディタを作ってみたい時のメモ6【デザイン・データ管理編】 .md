>------------<
- タイトル:[【6】React Nativeでテキストエディタを作ってみる！【データ管理編】]
- WordPressにアップロードしますか？:y[x]はいn[]まだしない
- 投稿時:p[x]公開d[]下書き
- カスタムURL:[React-Native-challenge-to-create-text-editor-6]
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

長い環境構築を経て、やっと前回ReactNativeを触ることができました✨
これで、アプリは作れそうだってことが分かったので、ここから最低限の機能を付けていきたいと思います～！

[GitHub](https://github.com/katatumuri-maimai/ReactNative-TextEditer)でソースコードを管理しています！

**最初から見る↓**
[kanren id="557"]

**前回を見る↓**
[kanren id="575"]


## ブランチを切る
作業ブランチがmasterのままなので、ブランチ切りましたｗ
今回、WSL2で環境構築した関係なのか、gitが管理者権限必要で、sourcetreeで操作できなくなっちゃいました💦
（環境構築の時に色々いじっておかしくなった可能性も）

ということで、WSL2のubuntuちゃんから、管理者権限でgitコマンド打ってます😨
何か方法あるとも思うけど、コマンド打った方が速いので←
（VScodeから手軽にコマンド打てるからひゃっほい）

[基本的なGitコマンドまとめ](https://qiita.com/2m1tsu3/items/6d49374230afab251337)

## データ管理
一応テキストエディタなので、データをどこかに格納しないといけません。
（ボタン作ってて気づきましたｗ）

今回は、アプリ開発が開始できるのか、ちゃんとコーディングできるのか、あんまり見通しが立ってなかったので、デザイン等していなくてｗ
データ管理について考えていませんでしたｗ

データ管理はどうやってするのか、ちょっと調べたいと思います。

### 端末に保存するケース
[[React Native] データ永続化についてAsyncStorageとRealmを調べてみた](https://qiita.com/ariiyu/items/0eeb96888c76512cb703)
↑これを読む感じだと、`AsyncStorage`で良い気がしますね。

以前、ReactでFirebaseを使ったことがありますが、クラウドでデータ管理するほどでもない気がしてて。
[【ReactNative】AsyncStorageを使ってデータを保存・取得する方法](https://reactnative-st.com/2020/07/10/%E3%80%90reactnative%E3%80%91asyncstorage%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E5%80%A4%E3%82%92%E4%BF%9D%E5%AD%98%E3%83%BB%E5%8F%96%E5%BE%97%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/)
↑これがReact Nativeの元の`AsyncStorage`っぽいですね。

[react-native-storageでデータを保持する](https://zenn.dev/nekoniki/articles/b295b0d123f7b1)
↑簡単そうなので、今回はこちらをベースに実装していけそう。


### クラウドに保存するケース
[react-native-storageで端末にデータを持たせる](https://nekoniki.com/20200526_reactnative_storage)
↑より

> こんな場合にオススメ
> ローカルにRDBを持つほどではないデータ(単一のフラグや日付、文字列など)
> ぱっと思いつくのは、アプリの動作に関わる設定値ですかね。
> 例えばアプリの設定画面からテーマカラーを変更できて、そのテーマカラーはアプリ内でEnumで定義されている場合、端末内に保持していれば大筋問題ないはずです。
> ※上記の場合も、同一アプリを複数端末にインストールしていて、テーマカラーを共有したい場合等はサーバーサイドにデータを持たせておくべきだとは思います。

むむむ

>同一アプリを複数端末にインストールしていて、テーマカラーを共有したい

したい！(｀･ω･´)

テーマを実装するかしないかはおいておいて、メモデータの共有はしたいですね…。

[React Nativeにおけるローカルデータベースの考察](https://www.wazalab.com/2016/08/14/react-native%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E3%83%AD%E3%83%BC%E3%82%AB%E3%83%AB%E3%83%87%E3%83%BC%E3%82%BF%E3%83%99%E3%83%BC%E3%82%B9%E3%81%AE%E8%80%83%E5%AF%9F/)
↑すごい！

クラウドでのデータの同期にはアカウント作成が必要ですよね。
アカウント作成機能までつけるのはちょっとハードルが高いですね～。
今回は、共有機能を使ってクラウド(Googleドライブとか)に保存できるくらいにとどめたいと思います。
（バックアップではなく、単純に共有にします。）

[React Native + Expo アプリでunstatedのデータを永続化](https://qiita.com/hitotch/items/f563ec8a60f05bb7edd8)

### データの保存方法決定

- ローカルストレージに保存する
- 共有機能で外部ストレージにも保存できる
- アプリを閉じた時の未保存のデータはローカルストレージに保持

で行こうと思います！


## データの読み書きをする
[React Nativeで遊んでみよう – 其ノ弐：react native storage でデータを保存](https://blog.photosynthesic.jp/2018/09/react-native%E3%81%A7%E9%81%8A%E3%82%93%E3%81%A7%E3%81%BF%E3%82%88%E3%81%86-%E5%85%B6%E3%83%8E%E5%BC%90%EF%BC%9Areact-native-storage-%E3%81%A7%E3%83%87%E3%83%BC%E3%82%BF%E3%82%92%E4%BF%9D%E5%AD%98/)
↑を参考に実装していきます！

とりあえず`npm install react-native-storage`してExpo再起動

実装手順としては、以下のようにできたらなと。

1. 保存・開くボタンを作る
2. データを保存できるようにする
3. データを開けるようにする
4. データ一覧を取得する
5. データ一覧から開けるようにする

よっしゃ！


### 1. 保存・開くボタンを作る
パネルの上にメニューバーを作って、そこに保存・開くボタンを作ります。

![picture 10](images/39644acd8046cf6a87bade3f29d0fee024c7890b75740770f8f2e1af7cbfef38.png)  

```javascript
// panelコンポーネントの上の方
<View style={styles.panelBody}>
   <View style={styles.panelMenu}>
     <Pressable style={styles.button}><Text style={styles.buttonText}>開く</Text></Pressable>
     <Pressable style={styles.button}><Text style={styles.buttonText}>保存</Text></Pressable>
   </View>
 </View>
```

### 2. データを保存できるようにする
とりあえず保存していきます！ｗ
[React Nativeで遊んでみよう – 其ノ弐：react native storage でデータを保存](https://blog.photosynthesic.jp/2018/09/react-native%E3%81%A7%E9%81%8A%E3%82%93%E3%81%A7%E3%81%BF%E3%82%88%E3%81%86-%E5%85%B6%E3%83%8E%E5%BC%90%EF%BC%9Areact-native-storage-%E3%81%A7%E3%83%87%E3%83%BC%E3%82%BF%E3%82%92%E4%BF%9D%E5%AD%98/)
↑を参考に初期設定と、保存の設定をしました。

[【ReactNative】現在の日付、時間表示をする方法](https://reactnative-st.com/2020/07/09/%E3%80%90reactnative%E3%80%91%E7%8F%BE%E5%9C%A8%E3%81%AE%E6%97%A5%E4%BB%98%E3%80%81%E6%99%82%E9%96%93%E8%A1%A8%E7%A4%BA%E3%82%92%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/)
保存時間も設定


#### データの設定
```javascript
export function fileData(filetitle, filetext) {
  const filename = filetitle + '.md'
  const date = new Date().toLocaleString()
  return ({
    key: 'loginState',
    id: 'id',
    data: {
      name: filename,
      date: date,
      text: filetext
    }
  })
}
```
↑テストデータはこんな感じ

#### データの保存関数の作成
![picture 11](images/9a4e74c5922905ec72b1fb2e36bb16a76d2bf99bbe295901cc38c303a75978af.png)  
あれ！`AsyncStorage`が非推奨だ！ｗｗｗ

[sunnylqm/react-native-storage](https://github.com/sunnylqm/react-native-storage)によると`npm install @react-native-community/async-storage`これも必要みたいです。
いれます！

```
- remove @react-native-community/async-storage from package.json
- run "expo install @react-native-async-storage/async-storage"
- update your imports manually, or run "npx expo-codemod sdk41-async-storage './**/*'".
```
expo install 使ってないからワーニングでちゃったｗ
`package.json`から`@react-native-community/async-storage`を消して、
`expo install expo install @react-native-async-storage/async-storage`します！

importも右に変えます。`import AsyncStorage from '@react-native-async-storage/async-storage'`


新たに`Storage.js`ってファイルを作って、とりあえず以下のコードにしました。
```javascript
import AsyncStorage from '@react-native-async-storage/async-storage';
import Storage from 'react-native-storage';

//ストレージの設定
var storage = new Storage({
  // 最大容量, 1000がデフォルト 
  size: 1000,

  // AsyncStorageを使う（WEBでもRNでも）。
  // セットしないとリロードでデータが消えるよ。
  storageBackend: AsyncStorage,

  // （たぶん）キャッシュの期限。デフォルトは一日(1000 * 3600 * 24 milliseconds).
  // nullにも設定できて、期限なしの意味になるよ。
  defaultExpires: 1000 * 3600 * 24,

  // メモリにキャッシュするかどうか。デフォルトは true。
  enableCache: true,

  // リモートシンクの設定（だと思う。）
  sync: {
    // これについては後述
  }
})

export function fileData(filetitle, filetext) {
  const filename = filetitle + '.md'
  const date = new Date().toLocaleString()
  return ({
    key: 'mdfile',
    id: 'id',
    data: {
      name: filename,
      date: date,
      text: filetext
    }
  })
}

export function saveFileData(fileData) {
  storage.save(fileData);
}

export function loadFileData(fileData) {
  storage.load(fileData).then(ret => {
    // ロードに成功したら
    console.log(ret.name + ' is ' + ret.text);
  }).catch(err => {
    // ロードに失敗したら
    console.warn(err.message);
    switch (err.name) {
      case 'NotFoundError':
        // 見つかんなかった場合の処理を書こう
        break;
      case 'ExpiredError':
        // キャッシュ切れの場合の処理を書こう
        break;
    }
  });
}
```


#### テキストの冒頭行からファイル名を取得
さっきの関数を使ってみます。
先頭の行をファイル名にするようにします！

テキストを配列にして、空文字じゃない先頭の行を返すようにします。

[JavaScript配列の空文字を削除](https://qiita.com/lostfind/items/e2a2ae1075c76f15c40b)

```javascript
// App.js
function saveFileData(){
  const firstRowEndPos = textInput.split('\n');
  const filetitle = firstRowEndPos.filter(Boolean)[0]
  S.saveFileData(S.fileData(filetitle, textInput))
}
```

```javascript
// App.js
<MyPanel
  saveFileData={saveFileData}
/>
```

パネルの保存ボタンに渡してみました。
保存できたっぽいんですが、できているのかわかりませんｗ



### 3. データを開けるようにする
とりあえず、保存したものをロードしてみますｗ

![picture 12](images/6a9402a076b0596e598bd5b7d4f3bfdf781a270108442aeb7c51ef8a79c360f1.png)  
開けている！！！

どこに保存しているんだろうｗ
後で保存しているところを突き止めますｗ
あと、保存できたかどうかのモーダルかポップアップも出したいな。

### 4. データ一覧を取得する
データ一覧の取得ってできるんかいな…？

[getallkeys](https://react-native-async-storage.github.io/async-storage/docs/api#getallkeys)これかな？
![picture 13](images/0310eeefe7200caddef1400bf42d40189cb2f11d1db289a5fcd9314290bb9a98.png)  

取得はできたっぽいですね。

[hoge: [object Object]の対処法](https://hacknote.jp/archives/12274/)


```javascript
// App.js コンポーネント
function GetAllData() {
  const [data, setData] = useState('')

  useEffect(() => {
    S.GetAllData().then(e => {
      console.log('App.js 4>>'+e);
    })
  }, []);
  console.log(data);
  return(
    <Text>a</Text>
  )
}
```

```javascript
// Storage.js 情報取得関数
export async function loadFileData(fileData) {
  const data = await storage.load(fileData).then(ret => {
    return ret
  }).catch(err => {
    console.warn('S 54>>'+ JSON.stringify(fileData.key) + ">>>>" + err.message + ">>>>" +err);
    switch (err.name) {
      case 'NotFoundError':
        break;
      case 'ExpiredError':
        break;
    }
  });
  return data
}

export async function GetAllData(){
    let data = []
    keys = await AsyncStorage.getAllKeys()
  
  for(let i in keys){
    const key = keys[i];
    const json = await loadFileData({ key: key }); 
    if(!json===false){
      data.push(await loadFileData({ key: key }))
    }
  }
  return data
}

```

#### データ一覧を表示
![picture 14](images/7704dc8c2d3b1c2b60ae5957699a355382b358b59bcceda31164a3830085282c.png)  
こんな感じでデータを取得できたので、表示してみたいと思います(*´ω｀)

![picture 15](images/2dd349b41cce34e2bde98a76d353be9da4cf466d459f6c5d832b2c0387b30d7d.png)  

お！表示できました。
今はTextコンポーネントで表示しているので、ボタンにしたりなんやかんやします。
あと、`App.js`に書いているので、パネルコンポーネントの方に移植します。

![picture 16](images/142efba9b65948b53068db0d5e39b332e471caf1c61a912c34894149bf0643b6.png)  

パネルに移植できました(*´ω｀)
色が絶賛やばいですが、何も考えないことにしましょうｗ

### 5. データ一覧から開けるようにする
つぎは、データ一覧のボタンをおしたら開くようにします。
親子コンポーネント間のデータの受け渡し難しい💦

とりあえず、`key`でとってこれるみたいなので、データ名を押されたときに`key`を親コンポーネントにとばしたいと思います。


![picture 17](images/3f275b57a0a24db69d7a845cb298065c8a7e0ec0377a92de9c77defd94bf998d.png)  
とりあえず、プレビューの方には反映できました！
テキストエリアにも反映したい🤔

![picture 18](images/f95dadd80a4abd4af00d79952ce3ffa91f65f35f37a9e67dc9882c3494f0a1eb.png)  

できました～！
とりあえずこれで、データを保存して開くことはできますね。

データを編集したりするのはもうちょっと手順が必要そうです。

あと、開くボタンが必要なさそうなので←
新規作成ボタンに変えます。

## 回線エラー出てきた
```
Cannot connect to the Metro server.

Try the following to fix the issue:
- Ensure that the Metro server is running and available on the same network
- Ensure that your device/emulator is connected to your machine and has USB debugging enabled - run 'adb devices' to see a list of connected devices
- If you're on a physical device connected to the same machine, run 'adb reverse tcp:8081 tcp:8081' to forward requests from your device
- If your device is on the same Wi-Fi network, set 'Debug server host & port for device' in 'Dev settings' to your machine's IP address and the port of the local dev server - e.g. 10.0.1.1:8081

URL: packager.mp-kiu.anonymous.reactnative-texteditor.exp.direct:80
```

手順に従って直してみます。
これでLAN接続できるといいな

`adb reverse tcp:8081 tcp:8081`

接続できなくなったｗｗ
パソコン再起動して事なきを得ましたｗ
LAN問題はまた今度にしよう。


## データのkey設定
データにkeyを持たせようと思います。
データの固有のID的に使えるはず。

```javascript
const [dataKey, setDataKey] = useState(null)
```

- 新規作成時→`dataKey=null`
- データ編集時→`dataKey=固有のkey`

となるようにします。

`null`の時に、連番のkeyを発行するようにしよう！
keyには`_`が使えないので、そこだけ気を付けていきます。


```javascript
// App.js
function saveFileData(){
  const firstRowEndPos = textInput.split('\n');
  const filetitle = firstRowEndPos.filter(Boolean)[0]
  let key = dataKey

  if (!key){
    key = 'SimpleMD' + data.length + 1
  }

  if (!textInput===false){
    S.saveFileData(S.fileData(key, filetitle, textInput))
  }else{
    console.log('テキストが入力されていません');
  }
}
```

できました～！ 


## 保存後にデータ一覧に反映する
新規作成して保存した時に、パネルのデータ一覧に反映するようにしました。
```javascript
// App.js
function saveFileData(){
  const firstRowEndPos = textInput.split('\n');
  const filetitle = firstRowEndPos.filter(Boolean)[0]
  let key = dataKey

  if (!key){
    key = 'SimpleMD' + data.length + 1
  }

  if (!textInput===false){
    S.saveFileData(S.fileData(key, filetitle, textInput))
  }else{
    console.log('テキストが入力されていません');
  }
  getAllData()
}
```


## 保存時にモーダルを出す
保存できたかどうか分かり難いので、モーダルを出そうと思います！
[公式ドキュメント](https://reactnative.dev/docs/modal)にモーダルコンポーネントがあるので、使っていきます。

アラートって言うコンポーネントもあるんですが、モーダルの方が可愛いので、モーダルにしますｗ
![picture 1](images/06f47713a8135377ff231dc07586c8f5ec839ce4bf265cae123cdf69c6461b0d.png)  



```javascript
// App.js
  <Modal
    animationType={'slide'}
    presentationStyle={false}
    transparent={true}
    visible={isModalOpen}
    onRequestClose={()=>{
      console.log('とじるんるん');
    }}
  >
    <View style={styles.centeredView}>
      <View style={styles.modal}>
        <Text>{isSubmit?"保存できました！":"保存できませんでした！"}</Text>
        <Pressable
        style={styles.modalBtn}
        onPress={closeModal}
        >
          <Text style={styles.modalText}>閉じる</Text>
        </Pressable>
      </View>
    </View>
  </Modal>
```

React Nativeはコンポーネントが用意されているから楽ですね～(*´ω｀)


今日はこの辺にしたいと思います！
続きをお楽しみに(*´ω｀)