>------------<
- タイトル:[【10】React Nativeでテキストエディタを作ってみる！【ナビ・エディタエリア作成編】]
- WordPressにアップロードしますか？:y[x]はいn[]まだしない
- 投稿時:p[x]公開d[]下書き
- カスタムURL:[React-Native-challenge-to-create-text-editor-10]
- カテゴリID:[3,11,12]
- タグID:[]
- 見出し画像のID:[]
- 識別番号[R0yqAs9Fxr6H]
>------------<

<!-- ↓続き
[kanren id=""] -->

こんにちは！かたつむり([@Katatumuri_nyan](https://twitter.com/Katatumuri_nyan))です！

Reactを触ってみて、サイト的なものは作れるようになりました(*´ω｀)
そこで、次はReactNativeを触ってみようと思い、簡単なテキストエディタを作成しようと企んでおります(笑)

今回は、ナビとエディタエリアを作成していきます(*´ω｀)


[GitHub]()でソースコードを管理しています！

**最初から見る↓**
[kanren id="557"]

**前回を見る↓**
[kanren id="628"]


## 前回までのできたところ
![picture 1](/images/69ad7d6963e8ac13dece19457387152cc2fe85216673b26b0031417e28c148da.png)  
ここまでできました～！

- App.js
- TopBar.js
- Title.js
- Nav.js
- その他関数等のファイル

↑を作成ました。


![picture 8](/images/eabf59e981fc0bdbf7783509897000b4bbf6567dae53f076a77223bba099938d.png)  
↑こちらが目標なので、がんばります！



## ナビの編集
![picture 2](/images/aef14bd2e45aa114cae4a616678a3f21b9e7e8e5c9e2c18dcadb27ed3614ed89.png)  

`Nav.js`を編集していきます！
右から左にスワイプで閉じるようにしたいです～！(*´ω｀)

[React Native Gesture Handler](https://docs.swmansion.com/react-native-gesture-handler/)を使っていきます。

公式ドキュメントが分かり難いので、[React Native Gesture Handler: Swipe, long-press, and more](https://blog.logrocket.com/react-native-gesture-handler-swipe-long-press-and-more/)こちらを参考にしました。

### サンプル作成
↓とりあえずテストを作りました

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">スワイプテスト✨ <a href="https://t.co/XGvIpOT4Sz">pic.twitter.com/XGvIpOT4Sz</a></p>&mdash; Katatumuri (@Katatumuri_nyan) <a href="https://twitter.com/Katatumuri_nyan/status/1412569760793915395?ref_src=twsrc%5Etfw">July 7, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

↓コードはコチラ
```javascript
import React from 'react';
import { Text, View, SafeAreaView} from 'react-native';
import { useTheme } from 'react-native-elements';
import Nav from './_components/Nav/Nav';
import Title from './_components/Title';
import Swipeable from 'react-native-gesture-handler/Swipeable';



export default function TopBar(props) {
    const { theme } = useTheme();

    const style ={
        position: 'relative',
        width: '100%',
        justifyContent:'center',
        alignItems: 'center',
    }

    const LeftSwipeActions =()=>{
        return(
            <View
                style={{
                    paddingHorizontal: 30,
                    paddingVertical: 20,
                    backgroundColor: 'red',
                }}
            >
                <Text style={{ fontSize: 24 }} style={{ fontSize: 20 }}>
                    LeftSwipeActions
                </Text>
            </View>
        )
    }

    const rightSwipeActions = () => {
        return (
            <View
                style={{
                    paddingHorizontal: 30,
                    paddingVertical: 20,
                    backgroundColor: 'pink',
                }}
            >
                <Text style={{ fontSize: 24 }} style={{ fontSize: 20 }}>
                    rightSwipeActions
                </Text>
            </View>
        )

    }

    const swipeFromRightOpen = () => {
        alert('Swipe from right');
    }

    const swipeFromLeftOpen = () => {
        alert('Swipe from left');
    }

    return(
        <SafeAreaView style={style}>
            <Nav/>
            <Title title={props.title}/>


            <Swipeable
                renderLeftActions={LeftSwipeActions}
                renderRightActions={rightSwipeActions}
                onSwipeableRightOpen={swipeFromRightOpen}
                onSwipeableLeftOpen={swipeFromLeftOpen}
            >
                <View
                    style={{
                        paddingHorizontal: 30,
                        paddingVertical: 20,
                        backgroundColor: 'white',
                    }}
                >
                    <Text style={{ fontSize: 24 }} style={{ fontSize: 20 }}>
                        text
                    </Text>
                </View>
            </Swipeable>


        </SafeAreaView>
    )
}
```

### スワイプ開閉するナビ完成
<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">スワイプでナビの開閉できました✨ <a href="https://t.co/HO7FSgFNTk">pic.twitter.com/HO7FSgFNTk</a></p>&mdash; Katatumuri (@Katatumuri_nyan) <a href="https://twitter.com/Katatumuri_nyan/status/1412618601706639366?ref_src=twsrc%5Etfw">July 7, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

最終的にこのようになりました(*´ω｀)
`Swipeable`ではなく、`PanGestureHandler`をつかいました～！

できたコードは↓こちら
```javascript
// Nav.js
import { PanGestureHandler} from 'react-native-gesture-handler';
export default function Nav(props) {
  const [isNavOpen, setIsNavOpen] = useState(false)
  let { theme } = useTheme();

  function onNavOpen() {
    setIsNavOpen(true)
  }

  function onNavClose() {
    console.log("swipe");
    setIsNavOpen(false)
  }

  function onSwipeEvent(event){
    const swipeX = event.nativeEvent.translationX

    if (swipeX <= 34) {
      onNavClose()
    } else if (34 < swipeX) {
      onNavOpen()
    }
  }

  const styles = {
    navContainer: {
      position: 'absolute',
      left: 10,
      top: 10,
      backgroundColor: 'pink',
      backgroundColor: theme.main.secondBackgroundColor,
      borderRadius: 20
    }
  }
  
    return (
      <PanGestureHandler onGestureEvent={(event) => { onSwipeEvent(event) }}>
        <View style={styles.navContainer}>
          {isNavOpen?
          <NavOpened color={theme.nav.iconColor} />:
          <NavClosed color={theme.nav.iconColor} onPress={onNavOpen} />
          }
        </View >
      </PanGestureHandler>
    )
}

```

## エディタエリア（`InputArea.js`）の作成
![InputArea ](/images/d1c749949fb9361040da72671015db78a030cd87cc6dbe9a373aee56dab91626.png)
↑こちらの白いエリアを作ります。

`InputArea.js`という名前で作成しました(*´ω｀)

`TextInput`を使っていきます。


![picture 3](/images/6d497b0ed4f79905fdbfaa2ea2d71c231a2db800359b0ff471ed822edbccb355.png)  
↑こんな感じにできました！
↓コードはこちら

```javascript
import React from 'react';
import {useState} from 'react';
import { TextInput} from 'react-native';
import { useTheme } from 'react-native-elements';

export default function InputArea(props) {
    const { theme } = useTheme();
    const [value, onChangeText] = useState(props.value);

    function onChange(text) {
        onChangeText(text)
    }

    const style = {
        flex: 1,
        backgroundColor: theme.textView.backgroundColor,
        color: theme.textView.textColor,
        padding: 20,
        paddingTop: 10,
        borderRadius: 20,
    }

    return (
        <TextInput
            style={style}
            multiline={true}
            scrollEnabled={true}
            textAlignVertical='top'
            onChangeText={text => onChange(text)}
            placeholder="Hello World!"
            value={value}
        />
    )
}
```
他のコンポーネントとの連携はあまり考えずに作っています。
そこはコンポーネントを追加した時に連携させていきます！

`App.js`の方でもいくらかスタイル等を設定しました！
↓こちらに一部のせておきます
```javascript
// App.js
export default function App() {
    /// 省略
  const styles = {
    app: {
      flex: 1,
      flexDirection: 'column',
      height: '100%',
      backgroundColor: theme[appTheme].main.mainBackgroundColor,
      alignItems: 'center'
    },
    editorArea:{
      flex: 1,
      padding: 20,
      paddingTop: 0,
      width: '100%'
    }
    }

  return (
    <ThemeProvider theme={theme[appTheme]}>
      <FileDataGetter.Provider value={fileDataGetterValue}>
        <SafeAreaView style={styles.app}>
          <TopBar
            title={title}
          />
          <EditorArea style={styles.editorArea}/>
        </SafeAreaView>
       </FileDataGetter.Provider>
     </ThemeProvider>
  );
}


function EditorArea(props) {
  return (
    <View style={props.style}>
      <InputArea />
    </View>
  )
}

```


## エディタエリア（`Preview.js`）の作成
![image 2](/images/2bae7dd9532f0bfde4f5f65dfa58fe2625d8590aa17182334bd585e49387aec2.png)
テキストエリアで入力したマークダウンテキストをHTMLに変換してプレビューするエリアをつくります。
↑上の画像で言うと右側のエリアです。

[iamacup/react-native-markdown-display](https://github.com/iamacup/react-native-markdown-display)こちらを使用していきます！


```
> npm install --save react-native-markdown-display
npm ERR! code ERESOLVE
npm ERR! ERESOLVE unable to resolve dependency tree
npm ERR! 
npm ERR! While resolving: undefined@undefined
npm ERR! Found: react@17.0.2
npm ERR! node_modules/react
npm ERR!   react@"17.0.2" from the root project
npm ERR! 
npm ERR! Could not resolve dependency:
npm ERR! peer react@"^16.2.0" from react-native-markdown-display@7.0.0-alpha.2
npm ERR! node_modules/react-native-markdown-display
npm ERR!   react-native-markdown-display@"*" from the root project
npm ERR! 
npm ERR! Fix the upstream dependency conflict, or retry
npm ERR! this command with --force, or --legacy-peer-deps
npm ERR! to accept an incorrect (and potentially broken) dependency resolution.
npm ERR! 
npm ERR! See /home/mymai/.npm/eresolve-report.txt for a full report.

npm ERR! A complete log of this run can be found in:
npm ERR!     /home/mymai/.npm/_logs/2021-07-07T04_44_33_558Z-debug.log
```
↑この様なエラーが出たので[ERESOLVE unable to resolve dependency treeの解決方法](https://qiita.com/koh97222/items/c46d1ef2a63b92bb6c15)をを参考にインストールしました。
`npm install react-native-markdown-display --save --legacy-peer-deps`

[【5】React Nativeでテキストエディタを作ってみる！【テキストエリア作成編】](https://katatumuri.xyz/react/575/react-native-challenge-to-create-text-editor-5/#%E3%83%9E%E3%83%BC%E3%82%AF%E3%83%80%E3%82%A6%E3%83%B3%E3%81%AB%E5%AF%BE%E5%BF%9C%E3%81%97%E3%81%A6%E3%81%BF%E3%82%8B%E3%80%82)この時に起きたエラーと同様のエラーが起きたので、解決しておきます！

### プレビューエリア作成
![picture 4](/images/e0f065cbfe864b4834a54f61b778b682880515ecc4646ecd0dc20d606c65ff55.png)  

`Preview.js`のcodeはとりあえず以下のようになりました。

```javascript
import React from 'react';
import { useState } from 'react';
import { ScrollView} from 'react-native';
import { useTheme } from 'react-native-elements';
import Markdown from 'react-native-markdown-display';

export default function Preview(props) {
    const { theme } = useTheme();
    const [value, onChangeText] = useState('プレビュー');

    const styles = {
        container: {
            flex: 1,
            backgroundColor: theme.textView.backgroundColor,
            padding: 20,
            paddingTop: 10,
            borderRadius: 20,
        },
        text: {
            body:{
                color: theme.textView.textColor,
            }
        }
    }

    return (
        <ScrollView style={styles.container}>
            <Markdown style={styles.text}>{value}</Markdown>
        </ScrollView>
    )
}
```

### `InputArea.js`との連携
`InputArea.js`のテキストエリアに入力した値を`Preview.js`に反映するようにします。

[createContextしたファイルでProviderを使わないほうが良い - it's better not to use Provider and use createContext in same file](https://dev.to/eiel/createcontext-provider-it-s-better-not-to-use-provider-and-use-createcontext-in-same-file-19he)
[How to Use Context API with Hooks Efficiently While Avoiding Performance Bottlenecks](https://www.telerik.com/blogs/how-to-use-context-api-with-hooks-efficiently-while-avoiding-performance-bottlenecks)
[useContext + useState 利用時のパフォーマンスはProviderの使い方で決まる！かも。。。？](https://qiita.com/jonakp/items/58c9c383473d02479ea7)

`useContext`を使ったので、↑こちらの記事を参考にしました✨


<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">テキストエリアとプレビューエリアの連携✨ <a href="https://t.co/d90aelr2IR">pic.twitter.com/d90aelr2IR</a></p>&mdash; Katatumuri (@Katatumuri_nyan) <a href="https://twitter.com/Katatumuri_nyan/status/1412706907177979908?ref_src=twsrc%5Etfw">July 7, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

↑こんな感じにテキストエリアに入力したものがプレビューエリアに表示されました。


`useContext`を使用する関係で、`App.js`を`Main.js`とし、新しく`App.js`を作成しました。

また、`context.js`というファイルを作成し、そこでコンテキストの設定をしました。
```javascript
// context.js
import React,{ createContext, useState} from 'react';

export const ContextObject = createContext()

export function ContextProvider(props) {
    const [appTheme, setAppTheme] = useState("Night")
    const [title, setTitle] = useState("Title")
    const [text, setText] = useState("")

    console.log(text);

    const ContextValue = {
        appTheme,
        setAppTheme,
        title,
        setTitle,
        text,
        setText
    }
    
    return (
        <ContextObject.Provider value={ContextValue}>
            {props.children}
        </ContextObject.Provider>)
}
```
↑`context.js`で`createContext`して、`ContextObject.Provider `に`ContextValue`を渡しています。
こうすることで、`ContextProvider`コンポーネントの子孫コンポーネントは、どこからでも`ContextValue`の値を読み取ったり、`State`の変更ができるようになります。

```javascript
// App.js
import React from 'react';
import { ContextProvider } from './modules/context';
import Main from './components/Main';

export default function App() {
  return (
    <ContextProvider>
      <Main/>
    </ContextProvider>
  );
}
```
↑`App.js`で、`Main`コンポーネントを`ContextProvider`コンポーネントで包みました。
これで、Main全体で値を共有できます。

```javascript
// Main.js
import React from 'react';
// 省略

export default function Main() {
    // 省略
 return (
    <ThemeProvider theme={theme[appTheme]}>
      <StatusBar hidden={false}/>
        <SafeAreaView style={styles.app}>
          <TopBar
            title={title}
          />
          <EditorArea style={styles.editorArea}/>
        </SafeAreaView>
     </ThemeProvider>
  );
}

function EditorArea(props) {
  return (
    <View style={props.style}>
      <InputArea />
      <Preview/>
    </View>
  )
}
```
↑`Main.js`にて、`InputArea`と`Preview`を組み込んでいます。

```javascript
// InputArea.js
import React, { useContext} from 'react';
import { ContextObject } from '../../modules/context';

export default function InputArea() {
    const { theme } = useTheme();
    const {
        text,
        setText
    } = useContext(ContextObject)

    function onChange(text) {
        setText(text)
    }

// 省略

    return (
        <TextInput
            style={style}
            multiline={true}
            scrollEnabled={true}
            textAlignVertical='top'
            onChangeText={text => onChange(text)}
            placeholder="Hello World!"
            value={text}
        />
    )
}
```

```javascript
// Preview.js
import React, { useContext } from 'react';
import { ContextObject } from '../../modules/context';

export default function Preview() {
    const { theme } = useTheme();
    const { text } = useContext(ContextObject)

  // 省略

    return (
        <ScrollView style={styles.container}>
            <Markdown style={styles.text}>{text}</Markdown>
        </ScrollView>
    )
}
```
↑`InputArea.js``Preview.js`では、`useContext`を使うことで`text`の値をとってきています。
`setText`で、`text`の値を変更することも可能です。


## プレビューエリアの開閉機能の追加
プレビューエリアが左右スワイプで開閉するようにしていきたいと思います(*´ω｀)
あと、真ん中がくっついてるので、そこも修正していきます！

どのエリアをスワイプしているのか調べるために、`PanGestureHandler`と[useWindowDimensions](https://docs.expo.io/versions/latest/react-native/usewindowdimensions/)を使います！



`EditorArea.js`を作成し、`Main.js`にあった`EditorArea`コンポーネントを分けました。

```javascript
// EditorArea.js
import React from 'react';
import { useContext } from 'react';
import { View } from 'react-native';
import { PanGestureHandler } from 'react-native-gesture-handler';
import { ContextObject } from '../../modules/context';
import InputArea from './InputArea/InputArea';
import Preview from './Preview/Preview';



export default function EditorArea(props) {
    const {
        windowWidth,
        isPreviewOpen,
        setIsPreviewOpen,
        setAbsoluteX
    } = useContext(ContextObject)

    const style = {
        flex: 1,
        flexDirection: 'row',
        position: 'relative',
        padding: 20,
        paddingTop: 0,
        width: '100%',
        height: '100%'
    }

    function onSwipeEvent(event) {
        const absoluteX = event.nativeEvent.absoluteX
        const previewWidth = windowWidth / 2
        const swipeX = event.nativeEvent.translationX
        const rightArea = previewWidth <= absoluteX

        if (rightArea && swipeX < 0){
            // （←）画面右半分を右から左にスワイプした時
            setIsPreviewOpen(true)
            setAbsoluteX(absoluteX)
        } else if (rightArea && swipeX > 0){
            // （→）画面右半分を左から右にスワイプした時
            setIsPreviewOpen(false)
            setAbsoluteX(absoluteX)
        }
    }


    return (
        <PanGestureHandler onGestureEvent={(event) => { onSwipeEvent(event) }}>
            <View style={style}>
                <InputArea />
                {isPreviewOpen ? <Preview />:<View/>}
            </View>
        </PanGestureHandler>
    )
}
```
↑こんな感じで開閉するようにしました(*´ω｀)


## キーボードをよける設定
![picture 5](/images/b93f46794b6cbfea2f9a7d2c207d0de21886f243687e32bb955d7176821af62e.png)  
↑こんな感じで仮想キーボードが出てきたらテキストエリアとプレビューを上に縮めます。

iOSの時、仮想キーボードがあっても勝手に縮んでくれないので、`KeyboardAvoidingView`を使用して実装しました。

```javascript
// Main.js
const os = Device.osName
const [keyboardAvoidingViewEnabled, setKeyboardAvoidingViewEnabled] = useState(true)

useEffect(() => {
  Keyboard.addListener('keyboardWillShow', keyboardWillShow);
  Keyboard.addListener('keyboardWillHide', keyboardWillHide);
}, []);

function keyboardWillHide() {
  setKeyboardAvoidingViewEnabled(false)
}

function keyboardWillShow() {
  setKeyboardAvoidingViewEnabled(true)
}

return (
      <ThemeProvider theme={theme[appTheme]}>
        <StatusBar hidden={false}/>
        <SafeAreaView style={styles.viwe}>
          <Pressable style={styles.viwe} onPress={Keyboard.dismiss}>
            <KeyboardAvoidingView
            behavior={Platform.OS == 'ios' ? 'padding' : 'height'}
            style={styles.app}
            keyboardVerticalOffset={Platform.OS == 'ios' ? '10' : '0'}
            enabled={keyboardAvoidingViewEnabled}
            >
              <TopBar
              title={title}
              />
              <EditorArea/>
            </KeyboardAvoidingView>
          </Pressable>
        </SafeAreaView>
      </ThemeProvider>
);

```

今回はこんな感じで終わります(*´ω｀)
次はメニューコンポーネントを作っていきます！

