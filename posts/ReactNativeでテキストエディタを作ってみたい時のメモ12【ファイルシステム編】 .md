>------------<
- タイトル:[【12】React Nativeでテキストエディタを作ってみる！【ファイルシステム編】]
- WordPressにアップロードしますか？:y[x]はいn[]まだしない
- 投稿時:p[x]公開d[]下書き
- カスタムURL:[React-Native-challenge-to-create-text-editor-12]
- カテゴリID:[3,11,12]
- タグID:[]
- 見出し画像のID:[]
- 識別番号[8T2ftVB8l8lH]
>------------<



こんにちは！かたつむり([@Katatumuri_nyan](https://twitter.com/Katatumuri_nyan))です！

Reactを触ってみて、サイト的なものは作れるようになりました(*´ω｀)
そこで、次はReactNativeを触ってみようと思い、簡単なテキストエディタを作成しようと企んでおります(笑)


[GitHub](https://github.com/katatumuri-maimai/snail_Markdown_TextEditor)でソースコードを管理しています！

**最初から見る↓**
[kanren id="557"]

**前回を見る↓**
[kanren id="634"]


## ファイルシステムの導入・データの読み書き
マークダウンファイルやプロジェクトフォルダを保存して一覧に反映できるようにします。
既に、アプリの設定を保存・取得するためにファイルシステムは導入しているので、それを使っていきます！

`controlProjects.js`というファイルを作成し、ここにデータの読み書きの関数を書いていきます。

`FileSystem.documentDirectory`下に`SimpleMarkdown/projects/`というディレクトリを作成し、そこにデータを保存しておくことにします。


### プロジェクトフォルダの作成
↓このような関数を作成し、プロジェクトフォルダを作成できるようにしました。

```javascript
export async function saveProjects(name) {
    const projectName = removeMarks(name)
    
    const Projects = await FileSystem.readDirectoryAsync(directoryUri)
        .then(e => {
            console.log("readDirectoryAsync >>" + e);
            return e
        }).catch(err => {
            console.error(err);
        })

    const newProjectName = Projects.includes(projectName) ? (projectName + "(" + Projects.length + ")" ): projectName
    const projectUri = directoryUri + encodeURIComponent(newProjectName)

    await FileSystem.makeDirectoryAsync(projectUri, { intermediates: true })
        .then(e => {
            console.log("saveProjectsmakeDirectoryAsync" + e);
        }).catch(err => {
            console.error(err);
        })

}

```

```javascript
const newProjectName = Projects.includes(projectName) ? (projectName + "(" + Projects.length + ")" ): projectName
```
↑この部分で、同じ名前で作成した時に別フォルダになるようにしました。


### プロジェクトフォルダ・ファイルの読み取り
プロジェクトフォルダとファイルを読み取って一覧にします。

![picture 5](images/ba71b35b3f2f51e3f4f3e10904b3aa32dbfa44229ff4e7b0deffcbe591098690.png)  
↑このように読み取ることができました。

```javascript
export async function readProjects() {
    let ProjectData=[]
    await FileSystem.makeDirectoryAsync(directoryUri, { intermediates: true })
        .then(e => {
            // console.log("readProjectsmakeDirectoryAsync" + e);
        }).catch(err => {
            console.error(err);
        })

    const Project_List = await FileSystem.readDirectoryAsync(directoryUri)
        .then(e => {
            // console.log("Project_ListreadDirectoryAsync >>" + e);
            return e
        }).catch(err => {
            console.error(err);
        })

    if (!Project_List){
        console.log("Project_List" + Project_List);
        return null
    }
```
↑このような関数を作成し、↓のように反映しています。


```javascript
{Project_List.map(e=>{
    let projectName;
    for(let key in e){
        projectName=key
    }
    const fileList = e[projectName]

    return(
        <Project
            project={{
                projectName: projectName,
                fileList: fileList
            }}
        />
    )
})}
```

### 新規ファイルの作成
新規ファイルは、プロジェクトの中に作成することにします。
なので、格納先のプロジェクトフォルダを選んでもらうか、新規作成できるようにしないといけません。
む、むずかしいｗ

![picture 6](images//b8503217ad23c14037d98718c728aaded303185cbd92fcf7a73972a31adc0386.png)  
↑結局こんな感じにフォルダを選択して↓の様な感じで表示できるようにしました✨

![picture 7](images//d96e6c1cf62f65c77f4e6b3910188f2edbd1a508b4779996fc7065b12ec28ff5.png)  

あちこちコード書いたので、コードは載せません💦

### ファイル・プロジェクトフォルダ作成時に更新する
ファイルやプロジェクトフォルダを作成した時に、一覧を更新します。
今は、アプリ全体のマウント時に一括で一覧を取得しているのですが、毎回一括で取得すると動作が重たくなるのでこまりました💦

そこで、作成したプロジェクトフォルダやファイルのみを取得するようにしたいと思います。

```javascript
// Modal.js
const {
    Project_List
} = useContext(ContextObject)
//省略
const new_ProjectName =await saveProject(newProjectName)
setSetDataNameModalOpen(false)
Project_List.push({ [new_ProjectName]:undefined})
```
↑プロジェクトフォルダの取得はこのようにしました。


```javascript
// Modal.js
const new_Filelist= await saveFile(projectName, newFileName)
for (let i in Project_List) {
    for (const key in Project_List[i]) {
        console.log(key);
        if (key == projectName){
            Project_List.splice(i, 1, new_Filelist)
        }
    }
}}
```
↑ファイルの取得はこのようにしました。

`saveProject`や`saveFile`で保存し、その返り値を`Project_List`に追加・置きかえしています。


### 選択したファイルの色を変える
今までは、選択していないファイルも色が変わるようになっていました。
ここで、選択中のファイルだけのの色を変えて、選択しているファイルを分かりやすくしました。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">選択中のファイルが分かりやすくなるようにしました🥰 <a href="https://t.co/hHgn2Cy4rZ">pic.twitter.com/hHgn2Cy4rZ</a></p>&mdash; Katatumuri (@Katatumuri_nyan) <a href="https://twitter.com/Katatumuri_nyan/status/1413140943142752277?ref_src=twsrc%5Etfw">July 8, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>




## ファイル情報の取得
次は、ファイル情報を取得していきます。
一覧から選択したファイルの情報を取得して画面に反映させます。

```javascript
async function onPressMenuBtnChild(projectName,fileName) {
    const text = await readFileData(projectName, fileName)
    const title = fileName.replace('.md','')

    setTitle(title)
    setText(text)
    setProjectName(projectName)
    setFileName(fileName)
}
```
↑こんな感じで取得しました！

## 編集内容の保存
新規作成したファイルを編集したあとに保存できるようにします。

### 保存ボタンの作成
保存ボタンをデザインしていなかったので、急遽`SaveBtn.js`を作りましたｗ
![picture 8](images//ce913fc38c46b1d86263c58a4b2495a3203e351f3ba3f41fb5b1adb733c7d27b.png)  
↑こんな感じで右上に作成しました。

```javascript
import React, { useContext } from 'react';
import { View } from 'react-native';
import { useTheme ,Icon} from 'react-native-elements';
import { ContextObject } from '../../../modules/context';

export default function SaveBtn() {
    const { theme } = useTheme();
    const {
    } = useContext(ContextObject)

    const styles={
        view:{
            flex: 1,
            justifyContent: 'center',
            position: 'absolute',
            right:20,
            top:10,
            width: 40,
            height:40,
            backgroundColor: theme.main.secondBackgroundColor,
            borderRadius: 20,
        },
        icon:{
            fontSize: 32,
            color: theme.nav.iconColor
        }
    }

    return (
        <View style={styles.view}>
            <Icon
            name='save'
            iconStyle={styles.icon}
            />
        </View>
    )
}
```
↑コードはこちら

### 保存機能の作成
保存ボタンを押したときに、保存されるようにします。

```javascript
export async function saveFile(projectName, fileName,text) {
    const projectUri = directoryUri + encodeURIComponent(removeMarks(projectName))
    const fileUri = projectUri + '/' + encodeURIComponent(removeMarks(fileName).replace('.md','')) + '.md'

    await FS.writeAsStringAsync(fileUri, text, { encoding: FileSystem.EncodingType.UTF8 })
        .then(e => {
        }).catch(err => {
            console.error(err);
        })

    const new_Files = await FileSystem.readDirectoryAsync(projectUri)
        .then(e => {
            return e
        }).catch(err => {
            console.error(err);
        })

}
```
↑このような関数を作成し、書き込むことにしました！


### ファイルを新規作成しないと編集できないようにする
今の状態だと、ファイルを新規作成していなくても無名で保存できるようになっているので、一旦保存できないようにします。

ホントは、テキスト入力からファイル名を取得して保存できるようにしたいのですが、自動保存機能と相性が悪いので、とりあえず、機能を制限しておきます。

```javascript
// InputArea.js
<TextInput
    // 省略
    editable={!fileName ? false: true}
/>
```
↑このように`editable`の条件をつけて、ファイル名がない（既存のファイルを開いていない）時はテキストエリアに入力できないようにしました。

そのうち新規作成していなくても保存できるようにしたいと思います！
そのためには、ファイル名ではなくてIDでファイルを管理するか、ファイルシステムをもう少し理解する必要がありそうです。

### 自動保存機能の作成
ユーザーが決めたタイミングで自動保存できるようにしようと思ったのですが、
保存せずにアプリを閉じた時にデータが保持されなくなってしまうので、即時保存にしました。
（保存ボタンいらなかった…）

```javascript
function onChange(text) {
        setText(text)
        saveFile(projectName, fileName, text)
    }
```
↑このようなコードで、Inputされたtextが変わるたびに保存します。
ほんとはここにタイマーを仕込みたかったのですが、難しかったのと、テキストデータなので、そこまで重くならないかなと思って即時保存にしました。

## 削除機能の追加
プロジェクトフォルダ・ファイルを削除する機能をつけていきます。

![picture 9](images//3ed498683ec55bfb9ed6d9885a873cacab9b2e951fd8f2e7b199021bfec0fac1.png)  

デザインの段階で考えていなかったのですが、フォルダ・ファイルボタンの右側に削除ボタンをつけていこうと思います(^▽^)/

![picture 10](images//58710a21f94e9e7d96c44f9243562b650b370b9e2f0d02d12d96097b162a9ccb.png)  

↑こんな感じで削除ボタンをつけました。

```javascript
// controlProjects.js
export async function removeData(projectName,fileName) {
    const projectUri = directoryUri + encodeURIComponent(projectName)
    let deleteUri;
    let readUri;

    if (!fileName){
        deleteUri = projectUri
        readUri = directoryUri
    }else{
        deleteUri = projectUri + '/' + encodeURIComponent(fileName.replace('.md',''))+'.md'
        readUri = projectUri
    }

    await FileSystem.deleteAsync(deleteUri)

    const deleteData =await FileSystem.readDirectoryAsync(readUri)
        .then(e => {
            console.log("readAsStringAsync" + e);
            return e
        }).catch(err => {
            console.error(err);
        })

    return (!fileName ? projectName:{ [projectName]: deleteData})
}
```
↑こんな感じで、削除する関数をつくりました！
削除する対象がディレクトリかファイルかで条件分岐しています。

リターンは、消したプロジェクトファイルか、消したファイルの配列を返すようにして、`DeleteDataBtn.js`で受け取ります。


```javascript
// DeleteDataBtn.js
async function onLongPressDotIcon() {
    const projectName = props.projectName
    const fileName = props.fileName
    const result= isOnPressDotIcon ? await removeData(projectName, fileName) : console.log('DeleteDataBtn>>削除できませんでした');

    console.log(result);
        for(let i in Project_List){
            for (let key in Project_List[i]) {
                if (key == projectName) {
                    console.log('key>>' + key);
                    !fileName ?
                        Project_List.splice(i, 1)
                        : Project_List.splice(i, 1, result)
            }}}
    }
```
↑`DeleteDataBtn.js`では、こんな感じで、データを受け取って、Project_Listを更新しています。

これで、プロジェクトフォルダ・ファイル一覧が即時更新されると思ったらそうでもありませんでした。

```javascript
// DeleteDataBtn.js
async function onLongPressDotIcon() {
    // 省略
    setIsDelete(true)
    }
```
↑このように`DeleteDataBtn.js`で`isDelete`を更新して、`Folder.js`↓で変化を受け取るようにしました。

```javascript
// Folder.js
useEffect(()=>{
    console.log('useEffect');
    if (isDelete){
    setIsDelete(false)
    }
}, [isDelete])
```
やり方があっているのか疑問ですが、即時更新されるようにはなりました。
Modalの方でプロジェクトフォル・ファイルを追加する時は即時更新されるのに、むずかしいですね！

再レンダリングのタイミングとかも気をつけないと…と思いながら、まだ手が出せてません。


よし！こんな感じで、
プロジェクトフォルダ・ファイルの作成、ファイルの読み書き、削除機能まで完成しました！
次は、テーマ機能の実装をしていきます！

↓続き
[kanren id="646"]