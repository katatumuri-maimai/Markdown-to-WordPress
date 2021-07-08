>------------<
- タイトル:[【12】React Nativeでテキストエディタを作ってみる！【ファイルシステム編】]
- WordPressにアップロードしますか？:y[]はいn[x]まだしない
- 投稿時:p[]公開d[x]下書き
- カスタムURL:[React-Native-challenge-to-create-text-editor-12]
- カテゴリID:[3,11,12]
- タグID:[]
- 見出し画像のID:[]
- 識別番号[8T2ftVB8l8lH]
>------------<

<!-- ↓続き
[kanren id=""] -->

こんにちは！かたつむり([@Katatumuri_nyan](https://twitter.com/Katatumuri_nyan))です！

Reactを触ってみて、サイト的なものは作れるようになりました(*´ω｀)
そこで、次はReactNativeを触ってみようと思い、簡単なテキストエディタを作成しようと企んでおります(笑)


[GitHub](https://github.com/katatumuri-maimai/snail_Markdown_TextEditor)でソースコードを管理しています！

**最初から見る↓**
[kanren id="557"]

<!-- **前回を見る↓**
[kanren id=""] -->


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

### 

```javascript
```

```javascript
```


```javascript
```


```javascript
```


```javascript
```

