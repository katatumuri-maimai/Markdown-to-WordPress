>------------<
- タイトル:[【9】React Nativeでテキストエディタを作ってみる！【デザインからアプリの見た目作成編】]
- WordPressにアップロードしますか？:y[x]はいn[]まだしない
- 投稿時:p[x]公開d[]下書き
- カスタムURL:[React-Native-challenge-to-create-text-editor-9]
- カテゴリID:[3,11,12]
- タグID:[]
- 見出し画像のID:[]
- 識別番号[8aWGfatcMmgP]
>------------<

<!-- ↓続き
[kanren id=""] -->

こんにちは！かたつむり([@Katatumuri_nyan](https://twitter.com/Katatumuri_nyan))です！

Reactを触ってみて、サイト的なものは作れるようになりました(*´ω｀)
そこで、次はReactNativeを触ってみようと思い、簡単なテキストエディタを作成しようと企んでおります(笑)

前回、デザインから再スタートしました！
今回は、デザインにそって見た目を作っていきます(*´ω｀)

[GitHub]()でソースコードを管理しています！

**最初から見る↓**
[kanren id="557"]

**前回を見る↓**
[kanren id="622"]


## コンポーネントとデザイン
![picture 7](images/c891b8a1a4c70ce560b2bed73c4d9bc8055f83aded21edb0e2d2715f2e08c926.png)  

今回はこれらの↑コンポーネントを作っていきます。

![picture 8](images/e18a9426953d975d35a3ccf382b701d6763d181655322aaaa180e2bda190f25a.png)  
↑各コンポーネントのデザインはこんな感じ
（ちょっと足りてないですがｗ手元にはあります！）


## 環境構築
第4回目の記事でWSL2での環境構築をしました。
今回は、`expo init`からやっていきます。別のディレクトリに作りたいので、

`expo init snil_Markdown_TextEditor`しました。


## App.jsの作成
まずは、テーマを適応させるため、テーマライブラリのインストールをしました。
[react-native-elementsでtheme機能を使う](https://qiita.com/zaburo/items/b85a3cc7e10be27aee2f)
↑よりテーマ作成のために[react-native-elements](https://reactnativeelements.com/)を使うことにしました。
UIキットなので、結構色んなコンポーネントが用意されていますね(*´ω｀)
使えそう！
アイコンもあるみたいなので、後で見てみます✨

`expo install react-native-elements`します。

`expo init`で`App.js`は作成されているので、これを手直しします。


```javascript
import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { ThemeProvider } from 'react-native-elements';
import theme from './theme/theme';
import TopBar from './components/TopBar/TopBar';

export default function App() {

  return (
    <ThemeProvider theme={theme} >
      <StatusBar style="auto" />
      <View style={styles.container}>
        <Text>ここに子コンポーネント</Text>
      </View>
    </ThemeProvider>
  );
}


const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: theme.Night.main.mainBackgroundColor,
    alignItems: 'center',
    justifyContent: 'center',
  },
});
```


## `TopBar.js`の作成
ここで、タイトルやナビを表示するためのコンポーネントが必要なことに気づき、急遽`TopBar.js`を作成しました。

```javascript
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

export default function TopBar(props) {
    
    return(
        <Text>ここに子コンポーネント</Text>
    )
}
```



## テーマカラーの設定
`theme.js`を作って、テーマの色設定書きました。
`App.js`に読み込んで使います。

とりあえず、テーマのひな型を作りました。
これにそって、各テーマの色を設定していきます。

adobeXDからカラーコードを拾ってきては、追加しますｗ

```javascript
export default theme = {
    Night: {
        main: {
            mainBackgroundColor: '',
            secondBackgroundColor: '',
            scrollBarColor: ''
        },
        textView:{
            backgroundColor: '',
            textColor:''
        },
        toolBar: {
            titleTextColor: ''
        },
        nav: {
            IconColor: ''
        },
        menu: {
            TitleColor: ''
        },
        menuBtn: {
            BackgroundColor: '',
            TextColor: '',
            IconColor: '',
            onPress: {
                BackgroundColor: '',
                TextColor: '',
                IconColor: '',
            }
        },
        menuBtnChild: {
            BackgroundColor: '',
            TextColor: '',
            IconColor: '',
            BoderColor: '',
            onPress: {
                BackgroundColor: '',
                TextColor: '',
                IconColor: '',
                BoderColor: '',
            }
        },
        PlusBtn: {
            BackgroundColor: '',
            IconColor: '',
        },
        typeSelectMenu: {
            BackgroundColor: '',
            TextColor: '',
            IconColor: '',
            onPress: {
                BackgroundColor: '',
                TextColor: '',
                IconColor: '',
            }
        }
    },
}
```

これで、`theme.Night.main.mainBackgroundColor`等と呼び出すと使えるようになります。
あれ、これ、テーマ用のライブラリ要らないですよねｗ
（各コンポーネントで`theme.js`をインポートしたらよさそう…）
どっちがいいかは分からないですが、ちょっとした修正で切り替えられるので、おいておきます。


## テーマ切り替え機能の作成
テーマカラーを用意したので、ユーザーが切り替えれるようにしたいと思います。
例えば、`theme.Night.main.mainBackgroundColor`の`Night`の部分がユーザーの選択によって`RoseQuartz`とかにできるようにしたい！

`snailSetting.json`というファイルを作成して、テーマの選択をここに保存するようにします。
`FileSystem`とかで、アプリ内のディレクトリに保存されるようにしよう！
そこから読み取れば完璧ですね（なのかな）

ちなみに、プレビューコンポーネントの色をテーマのカラーと帰れるようにしたり、自動保存の設定とかもここに保存されるようにします。

```javascript
{
    "theme":"Night",
    "preview":"Inheritance",
    "autoSave":"30"
}
```
### 独自設定を保存する
[expo-file-system](https://docs.expo.io/versions/latest/sdk/filesystem/)を使って、テーマをアプリ内に保存します。
`snailSetting.json`が既に存在したら作成しない、存在しなければ作成するようにして、そこからテーマを読み取ろうとおもいます。

`expo install expo-file-system`して、使っていきます！

`readSetting.js`をつくって、`App.js`で起動時に読み込むようにしました。

```javascript
// readSetting.js
import * as FileSystem from 'expo-file-system';

const snailSetting = {
    "theme": "Night",
    "preview": "Inheritance",
    "autoSave": "30"
}

export default async function readSetting() {
    const directoryUri = FileSystem.documentDirectory + 'SimpleMarkdown/setting/'
    const settingFileName = 'snailSetting.json'
    const fileUri = directoryUri + settingFileName
    let settingData

    await FileSystem.makeDirectoryAsync(directoryUri, { intermediates: true })
        .then(e => {
        }).catch(err => {
            console.error(err);
        })

    const fileList = await FileSystem.readDirectoryAsync(directoryUri)
        .then(e => {
            return e
        }).catch(err => {
            console.error(err);
        })

    if (fileList.includes(settingFileName) === false) {
        settingData = await FileSystem.writeAsStringAsync(fileUri, JSON.stringify(snailSetting), { encoding: FileSystem.EncodingType.UTF8 })
            .then(e => {
                return e
            }).catch(err => {
                console.log(fileUri);
                console.error("writeAsStringAsync >>" + err);
            })
    } else {
        settingData = await FileSystem.readAsStringAsync(fileUri, { encoding: FileSystem.EncodingType.UTF8 })
            .then(e => {
                return e
            }).catch(err => {
                console.error("readAsStringAsync >>" + err);
            })
    }

    return JSON.parse(settingData)
}
```

```javascript
// App.js
const[appTheme,setAppTheme]=useState(null)

useEffect(()=>{
  readSetting().then(e=>{
    setAppTheme(e.theme)
    console.log('useEffect'+e.theme);
  })
}, [])
```

## `Title.js`の作成
![picture 9](images/e7f263d9ed3fbde529ba4cd73b9450be0726418bd84eab813df0cd2930e6d28d.png)  

タイトルを作っていきます(*´ω｀)
`TopBar.js`におきます！

```javascript
import React from 'react';
import {Text } from 'react-native';
import { useTheme} from 'react-native-elements';


export default function Title(props) {
    const { theme } = useTheme();

    const style={
        color: theme.topBar.titleTextColor
    }

    return (
        <Text style={style}>{props.title}</Text>
    )
}
```

`useTheme`でテーマの情報を受け取ってます(*´ω｀)

## `useContext`の設定
[こんなに簡単なの？React Hook useContextでデータ共有](https://reffect.co.jp/react/react-usecontext-understanding)
`App.js`から情報を受け取りたいので、`useContext`を使っていきます！

`props`でもいいんですが、今回煩雑になるところは`useContext`にします。

```javascript
// App.js

export const fileDataGetter = React.createContext()

export default function App() {
  const [appTheme, setAppTheme] = useState(null)
  const [title, setTitle] = useState("aaatitle")

  const fileDataGetterValue={
    appTheme,
    setAppTheme,
    title, 
    setTitle
  }

...
```
↑ちなみに、`App.js`ではこのような設定をしました。



## `Nav.js`の作成
![picture 10](images/3931e26b176c8d4ded89bc2b385145f4ec87593c5113c2bf42b3eb73da834eab.png)  

ナビを作っていきます(*´ω｀)
`react-native-elements`の`icon`に私がデザインで使ったアイコンが入ってるみたいなので、使っていきます。
→ラウンドタイプが使いたいのに、ラウンドタイプがないので、とりあえずシャープタイプのものを使っています。

[@expo/vector-icons@12.0.5](https://icons.expo.fyi/)

右から左にスワイプでナビを閉じたいので、ジェスチャーを感知するライブラリを導入します。
`expo install react-native-gesture-handler`
↑[公式ドキュメント](https://docs.swmansion.com/react-native-gesture-handler/)見てもわからな過ぎて困りましたｗ



## `readSetting.js`の変更
AndroidとiOSでFileSystemの使い分けが必要だったので、変更しました。
`expo install expo-device`をして、デバイスの情報を取得します。

他のコンポーネントでも使う可能性があるので、`App.js`で取得するようにしました。
`Device.osName`とすると、iPadもiPhoneも`iOS`として表示されるので、これで分岐をしたいと思います。

```javascript
if (os == 'iOS') {
    FS = FileSystem
} else if (os == 'Android') {
    FS = StorageAccessFramework
}
```


### AndroidのJSONの取り扱いでハマった…
↑では分岐が必要だと思っていましたが、もしかしたらJSONがダメかもです。

Androidで`JSON.parse()`するとアプリごと終了してしまう事がある…。
なんでだろう
AndroidではJSONが使えないのかもしれない…

[How to parse json data in react native](https://stackoverflow.com/questions/53777345/how-to-parse-json-data-in-react-native)
↑のような質問を結構見かけたので、JSONは使えないみたいですね…

`console.log`だときれいに表示されるけど、useStateにセットするのはできないみたい…謎



```javascript
const [appTheme, setAppTheme] = useState(null)
const os = Device.osName

useEffect(() => {
  readSetting(os).then(e => {
    console.log(JSON.parse(e).theme);
    setAppTheme(JSON.parse(e).theme)
  })
}, [])
```
問題なのは↑
`useState('Night')`にしてもエラーが出るので、useStateに文字列が入れられないことが原因見たいです。
なんでだろう…。iOSはうまくいくし、他のStateは文字列も入るんですよね。



```javascript
<ThemeProvider theme={theme[appTheme]} >
```
↑原因を突き止めていくと、これがダメ見たいです。
うーんどうしよう。


```javascript
<ThemeProvider theme={theme}>
...
```

```javascript
import fileDataGetter from '../../../App';

export default function name(props) {
  const { appTheme } = useContext(fileDataGetter)
  let { theme } = useTheme();
  theme = theme[appTheme]
...
```

とりあえず色々やってみましたが、原因が分からないまま普通に動き始めました…。
AndroidStudio謎すぎる。

謎で終わりましたが、AndroidStudioの挙動がおかしくて1日つぶしてしまったので、今回はこの辺で終わります(*´ω｀)
