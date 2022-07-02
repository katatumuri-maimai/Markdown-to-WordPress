>------------<
- タイトル:[【11】React Nativeでテキストエディタを作ってみる！【メニューエリア作成編】]
- WordPressにアップロードしますか？:y[x]はいn[]まだしない
- 投稿時:p[x]公開d[]下書き
- カスタムURL:[React-Native-challenge-to-create-text-editor-11]
- カテゴリID:[3,11,12]
- タグID:[]
- 見出し画像のID:[]
- 識別番号[iPGGqq8Z2JLJ]
>------------<


こんにちは！かたつむり([@Katatumuri_nyan](https://twitter.com/Katatumuri_nyan))です！

Reactを触ってみて、サイト的なものは作れるようになりました(*´ω｀)
そこで、次はReactNativeを触ってみようと思い、簡単なテキストエディタを作成しようと企んでおります(笑)

今回は、メニューエリアを作成していきます！
機能を沢山付けるメニューエリアが一番大変なので、頑張りますｗ


[GitHub](https://github.com/katatumuri-maimai/snail_Markdown_TextEditor)でソースコードを管理しています！

**最初から見る↓**
[kanren id="557"]

**前回を見る↓**
[kanren id="630"]


## メニューエリアを作成
![image 1](/9d5ca01420effa58af28cc89368239332deb32899a0874f3d70719e9d45f0b33.png)
↑この左側に表示されるメニューエリアを作っていきます！

デザイン段階では、テキストエリアの上に被るように表示する予定でした。
しかし今回は、利便性を考えて、テキストエリアと並ぶように表示したいと思います！

### `Menu.js`の作成
![picture 6](/0758dbe29085f7d8b23a0dd8ceb7a81b8fa1a5eacaaf49aee6dc945463043115.png)  
↑こんな感じで左側にメニューエリアを作成しました。

コードは↓このようになりました。

```javascript
import React, { useContext } from 'react';
import { View, Text} from 'react-native';
import { useTheme } from 'react-native-elements';
import { ContextObject } from '../../modules/context';


export default function Menu() {
    const { theme } = useTheme();
    const {
    } = useContext(ContextObject)

    const styles = {
        menu:{
            width: 280,
            backgroundColor: theme.main.secondBackgroundColor,
            borderRadius: 20,
            marginRight: 10,
            padding:10,
            paddingTop: 20,
            flexDirection: 'column'
        },
        title:{
            color: theme.menu.titleColor,
            textAlign: 'center'
        }
    }

    return (
        <View style={styles.menu}>
            <Text style={styles.title}>設定</Text>
        </View>
    )
}
```
### メニューエリア開閉機能の作成
左から右にスワイプすることで、メニューエリアを開閉させたいと思います(*´ω｀)

```javascript
// Main.js
<PanGestureHandler onGestureEvent={(event) => { onSwipeEvent(event) }}>
    <View style={styles.wrap}>
    {isMenuOpen ? <Menu />:<View/>}
      <EditorArea/>
    </View>
</PanGestureHandler>
```
`Main.js`で↑このようにラップしました。

```javascript
// Main.js
if (lefghtArea && swipeX < 0) {
  // （←）画面左半分を右から左にスワイプした時
  setIsMenuOpen(false)
  setAbsoluteX(absoluteX)
} else if (lefghtArea && swipeX > 0) {
  // （→）画面左半分を左から右にスワイプした時
  setIsMenuOpen(true)
  setAbsoluteX(absoluteX)
}
```
また、↑のように設定して、開閉できるようになりました(^▽^)/

あと、メニューエリアが開いていると、プレビューエリアの大きさが変わるので、スワイプ判定を変えました！

## メニューボタンの作成
![picture 7](/7df072ac4b2d6c4a57d58d0a5afc87bb8eb5ddda79ab505180e0c46c285d2354.png)  
↑このようにボタンを作成しました(*´ω｀)

色々機能をつけるので、とりあえずシンプルなボタンにしました。

```javascript
// MenuBtn.js
import React, { useContext } from 'react';
import { View ,Text} from 'react-native';
import { useTheme } from 'react-native-elements';
import { Icon } from 'react-native-elements';
import { ContextObject } from '../../../modules/context';


export default function MenuBtn() {
    const { theme } = useTheme();
    const {
    } = useContext(ContextObject)

    const styles={
        wrap: {
            width: '100%',
            height: 46,
            marginTop: 10,
            backgroundColor: theme.menuBtn.BackgroundColor,
            borderRadius: 20,
            flexDirection: 'row',
            alignItems: 'center',
            paddingLeft:10,
            paddingRight: 10
        },
        icon:{
            color: theme.menuBtn.iconColor,
            marginRight: 10,
            fontSize: 28
        },
        btnText:{
            color: theme.menuBtn.TextColor,
            fontSize: 18
        }
    }

    return (
        <View style={styles.wrap}>
            <Icon
            name='settings'
            iconStyle={styles.icon}
            />
            <Text style={styles.btnText}>ボタン</Text>
        </View>
    )
}
```

```javascript
// MenuBtnChild.js
import React, { useContext } from 'react';
import { View ,Text} from 'react-native';
import { useTheme } from 'react-native-elements';
import { Icon } from 'react-native-elements';
import { ContextObject } from '../../../modules/context';

export default function MenuBtnChild() {
    const { theme } = useTheme();
    const {
    } = useContext(ContextObject)

    const styles={
        wrap: {
            alignSelf: 'flex-end',
            width: '90%',
            height: 46,
            marginTop: 10,
            backgroundColor: theme.menuBtnChild.BackgroundColor,
            borderColor: theme.menuBtnChild.BoderColor,
            borderStyle: 'solid',
            borderWidth:3,
            borderRadius: 20,
            flexDirection: 'row',
            alignItems: 'center',
            paddingLeft: 10,
            paddingRight: 10
        },
        icon:{
            color: theme.menuBtn.iconColor,
            marginRight: 10,
            fontSize: 28
        },
        btnText:{
            color: theme.menuBtn.TextColor,
            fontSize: 18
        }
    }

    return (
        <View style={styles.wrap}>
            <Icon
            name='settings'
            iconStyle={styles.icon}
            />
            <Text style={styles.btnText}>ボタン</Text>
        </View>
    )
}
```

## ナビの開閉の連動
![picture 8](/7c946d07e5a9db9bce78c78af200f1b545fd2f23bf066f031989b14db8875f39.png)  
↑こんな感じで、メニューが開いたとき、ナビも開いてほしいので、連動させます。

`Nav.js`で以下のようにしました。
```javascript
{isNavOpen | isMenuOpen?
  <NavOpened color={theme.nav.iconColor} />:
  <NavClosed color={theme.nav.iconColor} onPress={onNavOpen} />
}
```

## ナビボタンを押したときの動作設定
![picture 8](/7c946d07e5a9db9bce78c78af200f1b545fd2f23bf066f031989b14db8875f39.png)  
↑このナビボタンを押したときに、メニューが開いてほしいので、機能を付けていきます！

```javascript
// Nav.js
function onPress(icon){
    setWhichMenuOpen(icon);
  }
```
↑この様な関数を作成し、`context.js`でデータのやりとりをすることにしました。


### 押したボタンによるコンポーネントのきりかえ
```javascript
// Menu.js
function WhichMenu(params) {
    const { theme } = useTheme();
    const {
        whichMenuOpen
    } = useContext(ContextObject)

    switch (whichMenuOpen) {
        case 'settings':
            return <Settings />
            break;

        case 'folder':
            return <Folder />
            break;

        case 'file-upload':
            return <FileUpload />
            break;

        default:
            return <Settings />
            break;
    }
}
```
↑このように、`whichMenuOpen`の値によって表示するコンポーネントを変えます。

このあたりの挙動は、もうちょっと変更したい部分があるので、後で変更予定です！

## メニュー内のボタンを押したときの挙動追加

### 設定メニュー
![picture 9](/9dd33206559d33e220bd2215a25427545abda5d6ffaccf58a3e7f9087bc3dfc4.png)  
↑左のように表示したいのですが、ボタンを押すと右のように下に開くようにしたいです。
これを設定していきます！

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">開くメニュー😊 <a href="https://t.co/p9WZfH8znR">pic.twitter.com/p9WZfH8znR</a></p>&mdash; Katatumuri (@Katatumuri_nyan) <a href="https://twitter.com/Katatumuri_nyan/status/1412993295064584194?ref_src=twsrc%5Etfw">July 8, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

↑このようにできました！

```javascript
import React, { useContext, useState } from 'react';
import { View, Text} from 'react-native';
import { useTheme } from 'react-native-elements';
import { ContextObject } from '../../../modules/context';
import MenuBtn from '../_components/MenuBtn';
import MenuBtnChild from '../_components/MenuBtnChild';
import MenuTitle from '../_components/MenuTitle';

export default function Settings(props) {
    const { theme } = useTheme();
    const {
    } = useContext(ContextObject)

    const [isThemeMenuBtnOpen, setThemeMenuBtnOpen]=useState(false)
    const [isPreviewMenuBtnOpen, setPreviewMenuBtnOpen] = useState(false)
    const [isAutoSaveMenuBtnOpen, setAutoSaveMenuBtnOpen] = useState(false)

    const styles = {
        menu: {
        },
    }

    function onPress(is, set) {
        { is ? set(false) : set(true) }
    }

    return (
        <View style={styles.menu}>
            <MenuTitle>設定</MenuTitle>
            <MenuBtn 
                name='テーマ' 
                onPress={() => { onPress(isThemeMenuBtnOpen, setThemeMenuBtnOpen) }}
            />
            {isThemeMenuBtnOpen?<MenuBtnChild name='test'/>:<View/>}
            <MenuBtn
                name='プレビュー'
                onPress={() => { onPress(isPreviewMenuBtnOpen, setPreviewMenuBtnOpen) }}
            />
            {isPreviewMenuBtnOpen ? <MenuBtnChild name='てす' /> : <View />}
        </View>
    )
}
```
↑コードはこのようになりました。
`MenuBtn`と`MenuBtnChild`をコンポーネントとしてまとめようか悩みましたが、ちょっと保留です。

とりあえず、設定メニューでスイッチコンポーネントなども使うので、まとめないことにします。


### エクスポートメニュー
![picture 10](/a6160dedf69ea515c3f8e465874e0bcb41c9300ebfd0db5bb44c18c127bb6a5b.png)  
↑このようなかんじになります！
エクスポートメニューでは、開くようにはせず、押すだけのボタンにします。



```javascript
import React, { useContext, useEffect } from 'react';
import { View, Text } from 'react-native';
import { ContextObject } from '../../../modules/context';
import MenuBtn from '../_components/MenuBtn';
import MenuTitle from '../_components/MenuTitle';

export default function Export() {
    const {
        setIsMenuOpen
    } = useContext(ContextObject)

    function onPress() {
        setIsMenuOpen(false)
    }

    return (
    <View>
        <MenuTitle>エクスポート</MenuTitle>
        <MenuBtn
            name='Markdown'
            onPress={onPress}
        />
        <MenuBtn
            name='HTML'
            onPress={onPress}
        />
        <MenuBtn
            name='印刷'
            onPress={onPress}
        />
        <MenuBtn
            name='バックアップ'
            onPress={onPress}
        />
    </View>
    )
}
```
↑コードはこんな感じになりました。
今は`onPress`に仮の関数を渡していますが、後でエクスポート用の関数に変えます！


### フォルダーメニュー
![picture 11](/8a96474900cec139cea1771963165869fc629ff456c55b58dceac5d524f6bc02.png)  
↑フォルダーメニューを作成します。

ボタンを押すと開くのは設定メニューと同じですが、ファイルを選択した時などの挙動が変わるので、ちょっと難しいです。

![picture 1](/fa2a4b0b32b3f30c80bf58fa5069e3ad8d2ae4fe7a3f4dbf56b6ff1b19bfaa15.png)  

↑のようになりました。

```javascript
// Folder.js
export default function Folder(params) {
    const { theme } = useTheme();
    const {
        setIsMenuOpen
    } = useContext(ContextObject)

    const [isTypeSelectMenuOpen, setTypeSelectMenuOpen]=useState(false)
    
    const styles = {
        view:{
            position: 'relative',
            zIndex:10
        },
        plusIconContainer: {
            position: 'absolute',
            top: -10,
            left: 0,
            zIndex:100,
        },
        plusIcon:{
            fontSize: 40
        }
    }

    function onPressPlusIcon() {
        { isTypeSelectMenuOpen ? setTypeSelectMenuOpen(false):setTypeSelectMenuOpen(true)}
    }

    return (
        <View style={styles.view}>
            <Icon
                name='add-circle'
                color={theme.PlusBtn.iconColor}
                containerStyle={styles.plusIconContainer}
                iconStyle={styles.plusIcon}
                onPress={onPressPlusIcon}
            />
            {isTypeSelectMenuOpen ? <TypeSelectMenu /> : <View/>}
            <MenuTitle>プロジェクト</MenuTitle>
            <Project
                project={{
                    projectName:'test',
                    fileList:['test','test2']
                }}
            />
        </View>
    )
}
```

```javascript
// Folder.js
function Project(props) {
    const { theme } = useTheme();
    const [isOnonPressMenuBtn, setOnonPressMenuBtn] = useState(false)
    const projects = props.project
    const projectName = projects.projectName
    const fileList = projects.fileList

    const styles={
        nodata:{
            color: '#FFFFFF',
            marginTop: 30,
        },
        
    }

    function onPressMenuBtn(params) {
        { isOnonPressMenuBtn ? setOnonPressMenuBtn(false) : setOnonPressMenuBtn(true)}
    }


    return(
        <View>
            
            {!projectName ? <Text style={styles.nodata}>＋ボタンから新規作成</Text>:
                <MenuBtn
                    name={projectName}
                    iconName={isOnonPressMenuBtn ?'folder-open':'folder'}
                    onPress={onPressMenuBtn}
                />
            }
            {isOnonPressMenuBtn?
                (
                    !fileList ? <Text style={styles.nodata}>＋ボタンから新規作成</Text> :
                        (fileList.map(e=>{
                            return(
                                <MenuBtnChild
                                    name={e}
                                    iconName='text-snippet'
                                />
                            )
                        }))
                    
                ):
            <View/>}

        </View>
    )
}
```
↑コードはコチラ
ファイルシステムを使って情報を取得するので、データはダミーです！



### フォルダー・ファイル追加メニュー
![picture 12](/94b8d9ac18c8b8c939dc389ef3b3a1f49b472de9bb523bef475e7f4a38c2380b.png)  
↑このように、新規ディレクトリ・ファイルを作成できるようにします。
とりあえず、ボタンを作成しておきます。

![picture 3](/d23cbf85287cdef9cddddaf7dd001a3accbfc952dbbbba82cf1000a5128ba09d.png)  
↑このようになりました。


```javascript
// Folder.js
function TypeSelectMenuBtn(props) {
    const { theme } = useTheme();

    const [isOnPress, setOnPress] = useState(false)

    console.log(isOnPress);
    const styles = {
        view: {
            backgroundColor: isOnPress ? theme.typeSelectMenu.BackgroundColor : theme.typeSelectMenu.onPress.BackgroundColor ,
            height: '50%',
            flexDirection: 'row',
            alignItems: 'center',
            borderTopLeftRadius: props.addType == 'addProject'? 20 : 0,
            borderTopEndRadius: props.addType == 'addProject' ? 20 : 0,
            borderTopRightRadius: props.addType == 'addProject' ? 20 : 0,
            borderTopStartRadius: props.addType == 'addProject' ? 20 : 0,
            borderBottomLeftRadius: props.addType == 'addProject' ? 0 : 20,
            borderBottomEndRadius: props.addType == 'addProject' ? 0 : 20,
            borderBottomRightRadius: props.addType == 'addProject' ? 0 : 20,
            borderBottomStartRadius: props.addType == 'addProject' ? 0 : 20,
            padding:20,
            // borderBottomWidth:3
        },
        icon:{
            color: isOnPress? theme.typeSelectMenu.iconColor : theme.typeSelectMenu.onPress.iconColor,
            marginRight: 10,
            fontSize: 30
        },
        text:{
            color: isOnPress? theme.typeSelectMenu.TextColor : theme.typeSelectMenu.onPress.TextColor,
            fontSize: 20
        }
    }

    function onPress() {
        props.onPress()
        { isOnPress ? setOnPress(false) : setOnPress(true) }
        console.log('onpress');
    }

    return (
            <Pressable style={styles.view} onPress={onPress}>
                <Icon
                name={props.iconName}
                iconStyle={styles.icon}
                />
            <Text style={styles.text}>{props.text}</Text>
            </Pressable>
    )
    
}
```

↑コードはこんな感じ。

### プロジェクト・ファイル追加用のモーダル作成
デザインでは書いていなかったですが、プロジェクトやファイルを追加する際にファイル名を入力しないといけないことに気づきました。

画面いっぱいのモーダルを作って、そこにインプットエリアを追加することにします。

`Modal.js`を作っていきます！


![picture 4](/62f71a607cc6701da9ee45e9de8d91d9eef7bad720a4293cf7b49ba36c183752.png)  
↑できました!

```javascript
import React, { useContext, useEffect, useState } from 'react';
import { Modal, TextInput, View, Pressable,Text} from 'react-native';
import { useTheme } from 'react-native-elements';
import { ContextObject } from '../../modules/context';

export function SetDataNameModal(props) {
    const { theme } = useTheme();

    const {
        isSetDataNameModalOpen,
        setSetDataNameModalOpen,
        whichSetDataNameModalOpen,
        newProjectName,
        setNewProjectName,
        newFileName,
        setNewFileName
    } = useContext(ContextObject)

    const styles = {
        centeredView: {
            flex: 1,
            justifyContent: "center",
            alignItems: "center",
            backgroundColor: 'rgba(255, 255, 255,0.5)',
            paddingBottom: props.keyboardPadding
        },
        modal: {
            flexDirection: 'row',
            justifyContent: "center",
            alignItems: "center",
            backgroundColor: theme.main.mainBackgroundColor,
            textAlign: 'center',
            width: '80%',
            padding:20,
            borderRadius: 20
        },
        textInput: {
            width: '80%',
            height: 50,
            backgroundColor: theme.textView.backgroundColor,
            color: theme.textView.textColor,
            margin: 20,
            paddingHorizontal: 20,
            borderRadius: 20,
            fontSize: 20,
        },
        btn: {
            height: 50,
            justifyContent: 'center',
            alignItems: 'center',
            backgroundColor: theme.main.secondBackgroundColor,
            borderRadius: 20,
            paddingHorizontal:20,
        },
        btnText: {
            color: theme.nav.iconColor,
            fontSize: 20,
        }
    }


    function onChangeText(text) {
        if (whichSetDataNameModalOpen == 'addProject'){
            setNewProjectName(text)
        } else if (whichSetDataNameModalOpen == 'addFile') {
            setNewFileName(text)
        }
    }

    function openModal(params) {
        setSetDataNameModalOpen(true)
    }

    function closeModal(params) {
        setSetDataNameModalOpen(false)
    }

    return (
        <Modal
            transparent={true}
            presentationStyle='overFullScreen'
            onRequestClose={closeModal}
            visible={isSetDataNameModalOpen}
            animationType='fade'
        >
            <Pressable style={styles.centeredView} onPress={closeModal}>
                <Pressable style={styles.modal} onPress={openModal}>
                <TextInput
                    style={styles.textInput}
                    onChangeText={text => { onChangeText(text)}}
                    placeholder={whichSetDataNameModalOpen == 'addProject'?'新規プロジェクト名':'新規ファイル名'}
                />
                    <Pressable
                        style={styles.btn}
                            onPress={closeModal}
                    >
                        <Text style={styles.btnText}>新規作成</Text>
                    </Pressable>
                </Pressable>
            </Pressable>
        </Modal>
    )
}
```
↑コードはこんな感じ

押したボタンによって動作が変わるように設定しています。

ここから、難関のファイルシステムが始まります(((o(*ﾟ▽ﾟ*)o)))
がんばります！ｗｗ

↓続き
[kanren id="644"]