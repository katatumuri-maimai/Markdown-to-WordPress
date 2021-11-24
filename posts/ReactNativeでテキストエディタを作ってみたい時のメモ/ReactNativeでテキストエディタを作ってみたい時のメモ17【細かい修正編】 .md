>------------<
- タイトル:[【17】React Nativeでテキストエディタを作ってみる！【細かい修正編】]
- WordPressにアップロードしますか？:y[x]はいn[]まだしない
- 投稿時:p[x]公開d[]下書き
- カスタムURL:[React-Native-challenge-to-create-text-editor-17]
- カテゴリID:[3,11,12]
- タグID:[]
- 見出し画像のID:[]
- 識別番号[aH1inE3QlBS9]
>------------<



こんにちは！かたつむり([@Katatumuri_nyan](https://twitter.com/Katatumuri_nyan))です！

Reactを触ってみて、サイト的なものは作れるようになりました(*´ω｀)
そこで、次はReactNativeを触ってみようと思い、簡単なテキストエディタを作成しようと企んでおります(笑)

もうそろそろアプリとして配信できるくらいになってきた！
いま見つかっている細かいバグや、もう少し改良したい点などを修正していきます😊

[GitHub](https://github.com/katatumuri-maimai/snail_Markdown_TextEditor)でソースコードを管理しています！

**最初から見る↓**
[kanren id="557"]

**前回を見る↓**
[kanren id="656"]


## 修正したいところ

1. PDF出力時に画像があると反映されない
2. プレビュー画面の一番下が見切れてしまう
3. プレビュー画面のスクロール位置が入力のたびにトップに戻ってしまう


## 1. PDF出力時に画像があると反映されない
![picture 17](../../images/5df58ec5d0b7143c306ed7665c6d93939846d4990e31b972f3eb693156b2279b.png)  

↑左ように入力すると、右のようにプレビューされます。
しかし、PDF出力結果は↓です。

![picture 16](../../images/e32b296325c61dc818f25aabe1b0935527ef3957ade4c6e8dad1977ec48e5b97.png)  

PDF出力に試用している`Print`ライブラリの仕様で、PDFに出力する際に、ローカルの画像はbase64に変換する必要があります。

base64に変換するのは大変なので、ローカルのファイルはbase64で再読み込みすることにしました。


```javascript
async function convertImage(html) {
    // imgタグの取得
    const imageTag = /(<img src=)["|'](.*?)["|']+/gi
    const imageTagList = html.match(imageTag)

    // imgタグがあるとき
    if (imageTagList.length != 0) {
        let imageSrcList = []
        // imgタグを削除してsrcを取り出す
        imageTagList.forEach(imageTag => {
            const imageSrc = imageTag.replace(/<img src=["|'](.*?)["|']+/i, "$1")
            imageSrcList.push(../../imagesrc)
        })

        // base64に置換が必要なsrcリスト
        let needReaplace_imageSrcList = [...imageSrcList]

        // base64に置換不要なsrcを取り除く
        allowImageHandlers.forEach(imageHandler => {
            needReaplace_imageSrcList =
                needReaplace_imageSrcList
                    .filter(../../imagesrc => { return filterByImageHandler(../../imagesrc, imageHandler) })
        })


        // base64に置換が必要なsrcリストをbase64に変換

        for (const imageSrc of needReaplace_imageSrcList) {
            let before_imageSrc = imageSrc
            let imageUri = imagePickerUri + imageSrc
            let after_imageSrc = ''

            needAddHeaderImageHandlers.forEach(imageHandler => {
                const matchData = imageSrc.match(imageHandler)
                if (!!matchData) {
                    imageUri = localDefaltImageHandler + { ...matchData }.input
                }
            })

            const matchData = imageSrc.match(localDefaltImageHandler)
            if (!!matchData) {
                imageUri = { ...matchData }.input
            }

            const ext = imageUri.match(/.*\.(.*$)/)[1].toLowerCase()
            const fileType = ext == 'jpeg' ? 'jpg' : ext

            after_imageSrc =
                `data:image/${fileType};base64,` +
                await FileSystem.readAsStringAsync(imageUri, { encoding: FileSystem.EncodingType.Base64 })

            html = html.replace(before_imageSrc, after_imageSrc)

        }
        
        const imgStyle = `<img style="max-width:20%;max-height;50%;"`

        html = html.replace(/<img /g, imgStyle)
    }
    return html
}
```
↑このような関数を作成して、画像をPDFでも表示させることができました。

画像のサイズを個々に変えたいところですが、難しそうなのでとりあえず固定の大きさにしています。



## 2. プレビュー画面の一番下が見切れてしまう
![picture 18](../../images/ca30e64cfa7c01c3180cb89af5ef8977eb9058bbc041a25f43bba324c07d4df4.png)  

↑右側のプレビュー画面、下までスクロールしているのですが、一番下が見えていないですね。

スタイル調節していきます。

## 3. プレビュー画面のスクロール位置が入力のたびにトップに戻ってしまう
![picture 19](../../images/b039e03dd08446ceba675e7cec2c6f17da9bb0c23185364e3b3b717ab0dd1dad.gif)  
↑こんな風に、プレビュー画面を下までスクロールしても、入力を始めると上まで戻ってしまいます。

`Markdown`の再レンダリングのせいみたいですね。
`Markdown`に渡すテキストが更新されるたびに`Markdown`が更新されるので、プレビューコンポーネントを修正していきます。

```javascript
function toArrayText(){
  const ArrayText = text.split(/(!\[.*\]\(.*\))/)
  return ArrayText
}

// 省略
{toArrayText().map(e=>{
  return <Markdown>{e}</Markdown>
})}
```
↑このように、`Markdown`に挿入するテキストを配列にすることで、すでに読み込まれている`Markdown`が更新されるのを防ぎました。



今回はこのあたりで終わりにします！
あとは、細かい修正を沢山していくことになると思います。

なので、ここで一旦「React Nativeでテキストエディタを作ってみる！」シリーズの開発編は終了です。
次回以降の記事では、アプリの公開申請と、成果のまとめをしていきます😊

大きめの修正や重要な修正などがありましたら、別途記事にするかもです！


それでは！

↓続き
[kanren id=""]