>------------<
- タイトル:[【19】React Nativeでテキストエディタを作ってみる！【リーダブルコードの学習】]
- WordPressにアップロードしますか？:y[]はいn[x]まだしない
- 投稿時:p[]公開d[x]下書き
- カスタムURL:[React-Native-challenge-to-create-text-editor-19]
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


[GitHub](https://github.com/katatumuri-maimai/snail_Markdown_TextEditor)でソースコードを管理しています！

**最初から見る↓**
[kanren id="557"]

<!-- **前回を見る↓**
[kanren id=""] -->


## 共通のステート名の変更
色んなコンポーネントで使うステートを、コンテキストバリューとして定義しています。
名前の付け方が悲惨なので、変えていきます。

かっこ悪いけどコード見せます！
```javascript
const [appTheme, setAppTheme] = useState("Night")
const [title, setTitle] = useState("")
const [text, setText] = useState("")
const [isPreviewOpen, setIsPreviewOpen] = useState(false)
const [absoluteX, setAbsoluteX] = useState(useWindowDimensions().width)
const [isMenuOpen, setIsMenuOpen] = useState(false)
const [whichMenuOpen, setWhichMenuOpen] = useState('none')
const [isSetDataNameModalOpen, setSetDataNameModalOpen] = useState(false)
const [whichSetDataNameModalOpen, setWhichDataNameModalOpen] = useState('')
const [isSelectProjectModalOpen, setSelectProjectModalOpen] = useState(false)
const [isDataChange, setDataChange] = useState('')
const [projectName, setProjectName] = useState('')
const [fileName, setFileName] = useState('')
const [newProjectName, setNewProjectName] = useState('')
const [newFileName, setNewFileName] = useState('')
const [newText, setNewText] = useState('')
const [Project_List, setProject_List] = useState([])
const [Image_List, setImage_List] = useState([])
const [isDelete, setIsDelete] = useState(false)
const [whichMenuChidOpen, setWhichMenuChidOpen] = useState('')
const [selectedPreviewtheme, setSelectedPreviewtheme] = useState('theme')
const [keyboardScreenY, setKeyboardScreenYd] = useState(0)
```
↑色々ツッコミどころがあると思いますが…。
自分で分かる範囲で編集していきます。

ついでに、コンテキストファイルを分けたいので、どれがどのファイルで使っているかも見ていきます。

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



```javascript
```

```javascript
```