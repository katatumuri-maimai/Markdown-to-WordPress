# Reactでモーダル外をクリックしても閉じるモーダルの作り方と注意点【関数コンポーネント編】

こんにちは！かたつむり([@Katatumuri_nyan](https://twitter.com/Katatumuri_nyan))です！

Reactでモーダルウィンドウを作る時に、「閉じるボタンだけじゃなくて、**モーダル外をクリックしても閉じる**ようにしたい」って思ったのですが、なかなか苦戦しましたｗ

他にも同じように困っている方がいるかも！と思い、今回はモーダルの作り方をまとめてみました(*´ω｀)


今回は**関数コンポーネント**で作成した例です♪
↓クラスコンポーネントで作成したい方はこちらの記事から↓
[Reactでモーダル外をクリックしても閉じるモーダルの作り方と注意点【クラスコンポーネント編】](https://katatumuri.xyz/react/329/react-modal-class-component/)


## モーダルのデモ
[html]
<p class="codepen" data-height="335" data-theme-id="dark" data-default-tab="result" data-user="katatumuri-maimai" data-slug-hash="XWMGRyV" style="height: 335px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="モーダル＊関数コンポーネント">
  <span>See the Pen <a href="https://codepen.io/katatumuri-maimai/pen/XWMGRyV">
  モーダル＊関数コンポーネント</a> by katatumuri-maimai (<a href="https://codepen.io/katatumuri-maimai">@katatumuri-maimai</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>
[/html]

このデモで表示されているコードと、実際のコードは少し違います😢
実際のコードを見てみたい方はこちらから↓

[GitHubでコードを見る](https://github.com/katatumuri-maimai/react-code-sample/tree/main/my-react-app/src/pages/modaltest)

## モーダルを作る流れ
色んなやり方があると思うのですが、私はこんな流れでモーダルを作ってみました↓
1. モーダルを表示したいページのコンポーネント（親）を作成
2. モーダルコンポーネント（子）を作成
3. ページとモーダルをつなげる
4. CSSの設定
5. ボタンを押すとモーダルが開く設定
6. ボタンを押すとモーダルがとじる設定
7. モーダル外を押しても閉じる設定

ページ用のコンポーネントとモーダルのコンポーネントを分けて作りました。
では、実際にモーダルを作っていきましょう！

ぞれでは、順番に作っていきたいと思います！

## コードの完成形
まずはコードの完成形を見ておきましょう～！
```javascript
 // MyComponents.js
 import React,{ useEffect,useCallback,useState }  from 'react';
 import './modals.css';


 // 子コンポーネント（モーダル）
 function Modal(props){

   return(
       <div id="modal" className="modal" onClick={(event)=>{event.stopPropagation()}}>
         <div>
           <p>モーダル</p>
           <button onClick={props.onClick}>閉じるボタン</button>
         </div>
       </div>
   )
 }


 // 親コンポーネント
 export default function Modal_FunctionComponent(){

   const[isModalOpen,setIsModalOpen]=useState(false)

   const closeModal= useCallback(() =>{
     setIsModalOpen(false)
     document.removeEventListener('click',closeModal)
   },[])

   useEffect(()=>{
     return ()=>{
       document.removeEventListener('click',closeModal)
     }
   },[closeModal])


   function openModal(event){
     setIsModalOpen(true)
     document.addEventListener('click',closeModal)
     event.stopPropagation()
   }


   return (
     <div className="modalpage">
       <h2>関数コンポーネント</h2>
       <button onClick={(event)=>{openModal(event)}}>モーダルを開く</button>

       {isModalOpen? <Modal onClick={(event)=>{closeModal(event)}}/> :""}

     </div>
   );
 }
```


## 1. モーダルを表示したいページのコンポーネント（親）を作成
まずは、ページのコンポーネント（親）を作っていきます！
既にページがある場合は、参考程度に見てみてくださいね♪

ここでは、`MyComponents.js`というファイル名にします。

```javascript
// MyComponents.js
// Reactのインポート
import React from 'react';

// 親コンポーネント
// 他のファイルに読み込んで表示させるためにexportしている。
export default function Modal_FunctionComponent(){

  return (
    <div className="modalpage">
      <h2>関数コンポーネント</h2>
      <button>モーダルを開く</button>
    </div>
  );
}
```

このページのコンポーネント（親）をサイト上に表示させる方法は省略します～！


## 2. モーダルコンポーネント（子）を用意
次に、モーダルコンポーネントを作っていきます。
今回は分かりやすく説明するため、親コンポーネントと同じファイルで、親コンポーネントの上に追加で書いています。

```javascript
// MyComponents.js
// 子コンポーネント（モーダル）
function Modal(){

  return(
      <div id="modal" className="modal">
        <div>
          <p>モーダル</p>
          <button>閉じるボタン</button>
        </div>
      </div>
  )
}
```

## 3. ページとモーダルをつなげる
次に、ページコンポーネント（親）にモーダルコンポーネント（子）を挿入していきます。

```javascript
// MyComponents.js
// 親コンポーネント
export default function Modal_FunctionComponent(){

  return (
    <div className="modalpage">
      <h2>関数コンポーネント</h2>
      <button>モーダルを開く</button>
      <Modal />
    </div>
  );
}
```
これで、モーダルが表示されたんじゃないかと思います～！

## 4. CSSの設定
次は、CSSを設定していきます。
今のままだと、モーダルが変な所に挿入されちゃうので、浮かせますｗ
CSSの説明は飛ばします～！
私は以下のように設定しました！

ここでは、`modal.css`というファイル名にして、`MyComponents.js`と同じディレクトリ（ファイル）に入れています。

```css
/* modal.css */
#modalpage{
  width: 100%;
  height: 100%;
  box-sizing: border-box;
  color: pink;
  background-color: #FFEEF7;
  position: relative;
  margin: 0;
}

#modalpage .modal{
  /* ↓浮かせる設定 */
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  -webkit-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  /* ↑浮かせる設定 */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 300px;
  height:200px;
  background-color: #FFF9F9;
  box-shadow: 0 3px 6px 3px rgba(107,107,107,.10);
  color: #FF9ECA;
  border-radius: 10px;
  text-align: center;
}

#modalpage button{
  width: 100px;
  height: 40px;
  border-radius: 10px;
  color: #FFF;
  background-color: #FBB1BF;
  border: none;
  box-shadow: 0 3px 6px 3px rgba(107,107,107,.10);
  margin: 20px;
}

```

そして、コンポーネントを書いている`MyComponents.js`に以下を追加します。
これでCSSが適応されるはずです！
```javascript
// MyComponents.js
import React from 'react';
// -----ここから-----
import './modals.css';
// -----ここまで-----
```


## 5. ボタンを押すとモーダルが開く設定
モーダルが浮きましたね～！
それでは、次は、ボタンを押すとモーダルが開くようにします！

```javascript
// MyComponents.js
// -----1------
import React,{ useState }  from 'react';
// ---↑修正----
```

```javascript
// MyComponents.js
// 親コンポーネント
export default function Modal_FunctionComponent(){


  // -----2------
  const[isModalOpen,setIsModalOpen]=useState(false)
  // ---↑追加----

  // -----3------
  function openModal(){
    setIsModalOpen(true)
  }
  // ---↑追加----

  return (
    <div className="modalpage">
      <h2>関数コンポーネント</h2>
      // -----4------
      <button onClick={()=>{openModal()}}>モーダルを開く</button>
      // ---↑修正----

      // -----5------
      {isModalOpen? <Modal onClick={()=>{closeModal()}}/> :""}
      // ---↑修正----
    </div>
  );
}
}
```

コードの説明をしていきます。

### ステートの設定
```javascript
// -----1------
import React,{ useState }  from 'react';
// ---↑修正----
```
今回は、モーダルの開閉にステートを使うので、`useState`をインポートします。

```javascript
// -----2------
const[isModalOpen,setIsModalOpen]=useState(false)
// ---↑追加----
```
今回は、`isModalOpen`というステートを設定しました。
`isModalOpen`が`true`の時にモーダルが開いて、`false`の時にモーダルが閉じるように作っていきます～！
↑の記述で初期値を`false`にしたので、最初は閉じてることになりますね。

### モーダルを開く関数の作成。
```javascript
// -----3------
function openModal(){
  setIsModalOpen(true)
}
// ---↑追加----
```
`openModal()`という関数を作成しました。
`openModal()`が発動すると、`setIsModalOpen()`が、`isModalOpen`ステートを`true`にしてくれます。
（`isModalOpen`が`true`の時にモーダルが開く）


```javascript
// -----4------
<button onClick={()=>{openModal()}}>モーダルを開く</button>
// ---↑修正----
```
`button`タグに`onClick`というイベントハンドラ（クリックされたとき○○をするっていうやつ）を設定します。
クリックされたら`openModal()`が発動するように記述します。


### モーダルコンポーネント（子）がステートによって開閉する設定
```javascript
// -----5------
{isModalOpen? <Modal /> :""}
// ---↑修正----
```
さっきまでの状態だと、モーダルは表示されたままですよね。
モーダルを`isModalOpen`の状態によって開閉するように書いていきます。
`（条件）?（trueの時）:（falseの時）`というif文の省略形を使っています。

今回は、`this.state.isModalOpen`が`true`の時` <Modal /> `、`false`の時`""`ということですね。

これでモーダルがボタンを押すと開くようになりましたね(*´ω｀)


## 6.閉じる ボタンを押すとモーダルが閉じる設定
閉じるボタンを押すと、モーダルが閉じるコードを書いていきます。

```javascript
// MyComponents.js
// 親コンポーネント
export default function Modal_FunctionComponent(){

  const[isModalOpen,setIsModalOpen]=useState(false)

  // -----1------
  function closeModal(){
    setIsModalOpen(false)
  }
  // ---↑追加----

  function openModal(){
    setIsModalOpen(true)
  }

  return (
    <div className="modalpage">
      <h2>関数コンポーネント</h2>
      <button onClick={()=>{openModal()}}>モーダルを開く</button>
      // -----2------
      {isModalOpen? <Modal onClick={()=>{closeModal()}}/> :""}
      // ---↑修正----
    </div>
  );
}
```
まずは親コンポーネントへの記述を説明していきます！

### モーダルを閉じる関数の作成

```javascript
// -----1------
function closeModal(){
  setIsModalOpen(false)
}
// ---↑追加----
```
`openModal()`の時と同様に、`setIsModalOpen()`関数を使っていきます。
ここでは、閉じる関数なので`isModalOpen`が`false`になるようにします。


### モーダルコンポーネントに`closeModal()`関数を渡す
```javascript
// -----2------
{isModalOpen? <Modal onClick={()=>{closeModal()}}/> :""}
// ---↑修正----
```
`onClick={()=>{closeModal()}}`が増えました！
紛らわしいですが、`onClick`イベントハンドラではないです。
ただ`onClick`って名前をつけてモーダルコンポーネントに関数を渡しています。

モーダルコンポーネントにある閉じるボタンを押すと、親コンポーネントの`closeModal()`関数が実行されるようにしたいんです！
でも、モーダルコンポーネントから直接親コンポーネントの関数を実行できないので、一度`onClick`という名前でモーダルコンポーネントに関数を渡しているって感じです。

### モーダルコンポーネントで関数を受け取る
```javascript
// MyComponents.js
// 子コンポーネント（モーダル）
// -----3------
function Modal(props){
// ---↑修正----
  return(
      <div id="modal" className="modal">
        <div>
          <p>モーダル</p>
          // -----4------
          <button onClick={props.onClick}>閉じるボタン</button>
          // ---↑修正----
        </div>
      </div>
  )
}
```
次にモーダルコンポーネントでモーダルを閉じるボタンの設定をしていきます！

```javascript
// -----3------
function Modal(props){...}
// ---↑修正----
```
まずは、親コンポーネントの`props`を受け取りたいので、モーダルコンポーネントに`props`引数を設定しておきます。
親コンポーネントから値を引き継ぐことができるおまじないですｗ

```javascript
// -----4------
<button onClick={props.onClick}>閉じるボタン</button>
// ---↑修正----
```

こっちの`buttun`タグについているのは`onClick`イベントハンドラです！
クリックされた時に、`props.onClick`を発動するという記述です。

`props.onClick`で、親コンポーネント側で設定した`onClick`の中身（`closeModal()`関数）を取り出せます。
これで、モーダルコンポーネント側から、親コンポーネントの`isModalOpen`ステートを更新できます。

## 7. モーダル外を押しても閉じる設定1/2
さて、ここからが本題です！（長かった）
モーダルの外を押してもモーダルが閉じるようにしないといけません。

```javascript
// MyComponents.js
// 親コンポーネント
export default function Modal_FunctionComponent(){

  const[isModalOpen,setIsModalOpen]=useState(false)

  // -----3------
  function closeModal(){
    setIsModalOpen(false)
    document.removeEventListener('click',closeModal)
  }
  // ---↑修正----

  // -----1------
  function openModal(event){
    setIsModalOpen(true)
    document.addEventListener('click',closeModal)
    event.stopPropagation()
  }
  // ---↑修正----


  return (
    <div className="modalpage">
      <h2>関数コンポーネント</h2>
      // -----2------
      <button onClick={(event)=>{openModal(event)}}>モーダルを開く</button>
      // ---↑修正----
      {isModalOpen? <Modal onClick={()=>{closeModal()}}/> :""}

    </div>
  );
}
```

順番ばらばらで見にくいですが、説明していきますね～！


### 画面をクリックしたときにモーダルが閉じるようにする

```javascript
// -----1------
function openModal(event){
  setIsModalOpen(true)
  document.addEventListener('click',closeModal)
  event.stopPropagation()
}
// ---↑修正----
```
`document.addEventListener('click',closeModal)`で、画面のクリックイベントを監視します。
画面がクリックされたら、`closeModal`を発動してくれます。
エラーが出るかもですが、後のためにここでは`closeModal`と書いておいてください！

でも、このままだと、`openModal()`関数が発動したらすぐにモーダルが閉じてしまいます(´;ω;｀)
`openModal()`はモーダルを開くボタンをクリックすることによって発動するので、
開くボタンのクリックで`addEventListener`が発動しまって、モーダルが閉じるというわけですね(;´･ω･)

そこで、`event`引数を追加して、イベント情報を受け取れるようにします。
そして、`event.stopPropagation()`と書きます。
これで、`openModal()`を発動させる時のクリックは、`addEventListener`の適用外になります。


```javascript
// -----2------
<button onClick={(event)=>{openModal(event)}}>モーダルを開く</button>
// ---↑修正----
```
`openModal()`関数にクリックされたときのイベント情報を渡してあげるため、`event`を追加します。


### モーダルが閉じた時に`addEventListener`の監視を止める
```javascript
// -----3------
function closeModal(){
  setIsModalOpen(false)
  document.removeEventListener('click',closeModal)
}
// ---↑修正----
```
今のままだと、モーダルが閉じても`document.addEventListener('click',this.closeModal)`の監視が続いてしまいます。
そこで、`removeEventListener`を使って`addEventListener`の監視を解除します。


## 7. モーダル外を押しても閉じる設定2/2
2/2て！長いわ！って感じですが、ここからが大事なのです！
```javascript
// MyComponents.js
// -----1------
import React,{ useEffect,useCallback,useState }  from 'react';
// ---↑修正----
```

```javascript
// 親コンポーネント
export default function Modal_FunctionComponent(){

  const[isModalOpen,setIsModalOpen]=useState(false)

  // -----3------
  const closeModal= useCallback(() =>{
    setIsModalOpen(false)
    document.removeEventListener('click',closeModal)
  },[])
  // ---↑修正----

  // -----2------
  useEffect(()=>{
    return ()=>{
      document.removeEventListener('click',closeModal)
    }
  },[closeModal])
  // ---↑追加----


  function openModal(event){
    setIsModalOpen(true)
    document.addEventListener('click',closeModal)
    event.stopPropagation()
  }


  return (
    <div className="modalpage">
      <h2>関数コンポーネント</h2>
      <button onClick={(event)=>{openModal(event)}}>モーダルを開く</button>

      {isModalOpen? <Modal onClick={()=>{closeModal()}}/> :""}

    </div>
  );
}
```
```javascript
// MyComponents.js
// 子コンポーネント（モーダル）
function Modal(props){

  return(
      // -----4------
      <div id="modal" className="modal" onClick={(event)=>{event.stopPropagation()}}>
      // ---↑修正----
        <div>
          <p>モーダル</p>
          <button onClick={props.onClick}>閉じるボタン</button>
        </div>
      </div>
  )
}
```

### アンマウント時のメモリリーク対策をする
今のままだと、モーダルを開いたまま別のページに遷移した時などに、エラーが起きてしまいます。
どうしてかというと、モーダルを開いた時に発動した`document.addEventListener('click',closeModal)`の監視が、別のページでも続くからなんです。
そこで、メモリリークの対策をしていきます！

```javascript
// MyComponents.js
// -----1------
import React,{ useEffect,useCallback,useState }  from 'react';
// ---↑修正----
```
まずは、`useEffect`と`useCallback`を使うので、インポートしておきます。

```javascript
// -----2------
useEffect(()=>{
  return ()=>{
    document.removeEventListener('click',closeModal)
  }
},[closeModal])
// ---↑追加----
```
`useEffect`は、コンポーネントが表示・非表示になったタイミングで発動してくれます。（厳密には違います。）
`return`として書いたものは、コンポーネントが非表示になった直後に発動します。

そこで今回は、`return`の処理として、`removeEventListener`を使って`addEventListener`を解除しておくわけですね(*´ω｀)
（説明難しい…(;´･ω･)）

`useEffect`の第二引数（`[]`の中）には依存関係を書きます。
今回は`closeModal`に依存しているので、`closeModal`を書いておきます。
（ここ難しいので詳しく知りたい方は調べてみてください！）


```javascript
// -----修正前------
function closeModal(){
  setIsModalOpen(false)
  document.removeEventListener('click',closeModal)
}
// -----修正前------
```
`useEffect`も大事ですが、`useCallback`も大事です。
`useEffect`の中で修正前↑の`closeModal()`関数を呼び出すと、大変なエラーが起きてしまいますｗ

そこで、以下のように修正します。

```javascript
// -----3------
const closeModal= useCallback(() =>{
  setIsModalOpen(false)
  document.removeEventListener('click',closeModal)
},[])
// ---↑修正----
```
`useCallback`で包んであげると、あら不思議、いい感じに動いてくれます。
`useCallback`は、メモ化されたコールバックを返すとか色々あるのですが、ここでは`useEffect`とセットで使うといい感じくらいに思っておいてください。


### モーダルの中をクリックしたときに閉じないようにする。
ここまでで、画面をクリックしたときにモーダルが閉じるようになったと思います(*´ω｀)
だけど、閉じるボタン以外のモーダルの要素をクリックしてもモーダルが閉じてしまいますよね。

そこで、モーダルコンポーネントで以下の処理を行います。
```javascript
// MyComponents.js
// 子コンポーネント（モーダル）
// -----4------
<div id="modal" className="modal" onClick={(event)=>{event.stopPropagation()}}>
// ---↑修正----
```
モーダル要素の一番外側に`onClick`イベントハンドラを渡して、`event.stopPropagation()`と書いておきます。
こうすることで、モーダルを開くボタンの時と同様にモーダルコンポーネントを、`addEventListener`の適用外にできます。


これでモーダルの完成です～！
お疲れ様でした♪

## モーダル作成時の注意点
アンマウント時のメモリリーク対策ができていないと、以下の様なエラーが出ます(´;ω;｀)

![アンマウント時のエラー【関数コンポーネント】](images/2021/06/アンマウント時のエラー【関数コンポーネント】.png)
> Warning: Can't perform a React state update on an unmounted component. This is a no-op, but it indicates a memory leak in your application. To fix, cancel all subscriptions and asynchronous tasks in a useEffect cleanup function.
    at Modal_FunctionComponent

```javascript
const closeModal= useCallback(() =>{
  setIsModalOpen(false)
  document.removeEventListener('click',closeModal)
},[])

useEffect(()=>{
  return ()=>{
    document.removeEventListener('click',closeModal)
  }
},[closeModal])
```
↑のように記述することで、対策できるので、気を付けてみてください♪


## 参考
[React Hooksを使ったモーダル実装](https://qiita.com/mt_816/items/961a4faed14d0ce2d3ab)

[安全に React Hooks を使用する](https://qiita.com/kobayang/items/88a104c0be28e16e65e8)

[バブリングによるイベントの伝播](https://www.codegrid.net/articles/addeventlistener-1/#toc-5)

[Event.stopPropagation()](https://developer.mozilla.org/ja/docs/Web/API/Event/stopPropagation)
