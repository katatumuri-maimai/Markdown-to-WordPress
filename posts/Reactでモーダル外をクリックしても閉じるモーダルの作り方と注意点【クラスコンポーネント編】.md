>------------<
- タイトル:[]
- WordPressにアップロードしますか？:y[]はいn[]まだしない
- 投稿時:p[]公開d[]下書き
- カスタムURL:[]
- カテゴリID:[]
- タグID:[]
- 見出し画像のID:[]
- 識別番号[ZblAwCRXioLs]
>------------<
# Reactでモーダル外をクリックしても閉じるモーダルの作り方と注意点【クラスコンポーネント編】

こんにちは！かたつむり([@Katatumuri_nyan](https://twitter.com/Katatumuri_nyan))です！

Reactでモーダルウィンドウを作る時に、「閉じるボタンだけじゃなくて、**モーダル外をクリックしても閉じる**ようにしたい」って思ったのですが、なかなか苦戦しましたｗ

他にも同じように困っている方がいるかも！と思い、今回はモーダルの作り方をまとめてみました(*´ω｀)

今回は**クラスコンポーネント**で作成した例です♪
↓クラスコンポーネントで作成したい方はこちらの記事から↓
[Reactでモーダル外をクリックしても閉じるモーダルの作り方と注意点【関数コンポーネント編】](https://katatumuri.xyz/react/357/react-modal-function-component/)


## モーダルのデモ
[html]
<p class="codepen" data-height="348" data-theme-id="dark" data-default-tab="result" data-user="katatumuri-maimai" data-slug-hash="LYWazLm" style="height: 348px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="モーダル＊クラスコンポーネント">
  <span>See the Pen <a href="https://codepen.io/katatumuri-maimai/pen/LYWazLm">
  モーダル＊クラスコンポーネント</a> by katatumuri-maimai (<a href="https://codepen.io/katatumuri-maimai">@katatumuri-maimai</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>
[/html]

このデモで表示されているコードと、実際のコードは少し違います😢
実際のコードを見てみたい方はこちらから↓

[GitHubでコードを見る](https://github.com/katatumuri-maimai/react-code-sample/tree/develop/my-react-app/src/pages/modaltest)
[デモサイト](https://katatumuri-maimai.github.io/ModalPage/Modal_ClassComponent)もあります！

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
import React from 'react';
import './modals.css';

// 子コンポーネント（モーダル）
class Modal extends React.Component {

  render(){
    return(
        <div id="modal" className="modal" onClick={(event)=>{event.stopPropagation()}}>
          <div>
            <p>モーダル</p>
            <button onClick={this.props.onClick}>閉じるボタン</button>
          </div>
        </div>
    )
}}

// 親コンポーネント
class Modal_ClassComponent extends React.Component {
  constructor(props) {
   super(props);
    this.state = {
      isModalOpen: false
    };
    this.closeModal = this.closeModal.bind(this);
  };

  componentWillUnmount(){
    document.removeEventListener('click',this.closeModal)
  }

  openModal(event){
    this.setState({isModalOpen:true})
    document.addEventListener('click',this.closeModal)
    event.stopPropagation()
  }

  closeModal(){
    this.setState({isModalOpen:false})
    document.removeEventListener('click',this.closeModal)
  }

  render(){
      return (
        <div id="modalpage" className="modalpage">
          <h2>クラスコンポーネント</h2>
            <button onClick={(event)=>{this.openModal(event)}}>モーダルを開く</button>

            {this.state.isModalOpen? <Modal onClick={()=>{this.closeModal()}}/> :""}

          </div>
      );
    }
}

export default Modal_ClassComponent;
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
class Modal_ClassComponent extends React.Component {

  render(){
      return (
        <div id="modalpage" className="modalpage">
          <h2>クラスコンポーネント</h2>
          <button>モーダルを開く</button>
          // ここにモーダルコンポーネント（子）を挿入したい。
        </div>
      );
    }
}

// 他のファイルで読み込めるようにexportしている
export default Modal_ClassComponent;
```

このページのコンポーネント（親）をサイト上に表示させる方法は省略します～！


## 2. モーダルコンポーネント（子）を用意
次に、モーダルコンポーネントを作っていきます。
今回は分かりやすく説明するため、親コンポーネントと同じファイルで、親コンポーネントの上に追加で書いています。

```javascript
// MyComponents.js
// 子コンポーネント（モーダル）
class Modal extends React.Component {

  render(){
    return(
        <div id="modal" className="modal">
          <div>
            <p>モーダル</p>
            <button>閉じるボタン</button>
          </div>
        </div>
    )
}}

```

## 3. ページとモーダルをつなげる
次に、ページコンポーネント（親）にモーダルコンポーネント（子）を挿入していきます。

```javascript
// MyComponents.js
// 親コンポーネント
class Modal_ClassComponent extends React.Component {

  render(){
      return (
        <div id="modalpage" className="modalpage">
          <h2>クラスコンポーネント</h2>
          <button>モーダルを開く</button>
          // ↓に挿入
          <Modal />
          // ↑に挿入
          </div>
      );
    }
}

export default Modal_ClassComponent;

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
// ↓に挿入
import './modals.css';
// ↑に挿入
```


## 5. ボタンを押すとモーダルが開く設定
モーダルが浮きましたね～！
それでは、次は、ボタンを押すとモーダルが開くようにします！

```javascript
// MyComponents.js
// 親コンポーネント
class Modal_ClassComponent extends React.Component {
  // -----1------
  // ↓を追加
  constructor(props) {
   super(props);
    this.state = {
      isModalOpen: false
    };
  };
  // ↑を追加

  // -----2------
  // ↓を追加
  openModal(){
    this.setState({isModalOpen:true})
  }
  // ↑を追加

  render(){
      return (
        <div id="modalpage" className="modalpage">
          <h2>クラスコンポーネント</h2>
          // -----3------
          // ↓を修正
          <button onClick={()=>{this.openModal()}}>モーダルを開く</button>
          // ↑を修正

          // -----4------
          // ↓を修正
          {this.state.isModalOpen? <Modal /> :""}
          // ↑を修正
          </div>
      );
    }
}

export default Modal_ClassComponent;
```

コードの説明をしていきます。

### ステートの設定
```javascript
// -----1------
// ↓を追加
constructor(props) {
 super(props);
  this.state = {
    isModalOpen: false
  };
};
// ↑を追加
```
今回は、`isModalOpen`というステートを設定しました。
`isModalOpen`が`true`の時にモーダルが開いて、`false`の時にモーダルが閉じるように作っていきます～！
↑の記述で初期値を`false`にしたので、最初は閉じてることになりますね。

### モーダルを開く関数の作成。
```javascript
// -----2------
// ↓を追加
openModal(){
  this.setState({isModalOpen:true})
}
// ↑を追加
```
`openModal()`という関数を作成しました。
`openModal()`が発動すると、`setState()`関数が発動して、`isModalOpen`ステートを`true`にしてくれます。
（`isModalOpen`が`true`の時にモーダルが開く）


```javascript
// -----3------
// ↓を修正
<button onClick={()=>{this.openModal()}}>モーダルを開く</button>
// ↑を修正
```
`button`タグに`onClick`というイベントハンドラ（クリックされたとき○○をするっていうやつ）を設定します。
クリックされたら`openModal()`が発動するように記述します。


### モーダルコンポーネント（子）がステートによって開閉する設定
```javascript
// -----4------
// ↓を追加
{this.state.isModalOpen? <Modal /> :""}
// ↑を追加
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
class Modal_ClassComponent extends React.Component {
  constructor(props) {
   super(props);
    this.state = {
      isModalOpen: false
    };
  };

  openModal(){
    this.setState({isModalOpen:true})
  }

  // -----1------
  // ↓を追加
  closeModal(){
    this.setState({isModalOpen:false})
  }
  // ↑を追加

  render(){
      return (
        <div className="modalpage">
          <h2>クラスコンポーネント</h2>
            <button onClick={()=>{this.openModal()}}>モーダルを開く</button>
            // -----2------
            // ↓を修正
            {this.state.isModalOpen? <Modal onClick={()=>{this.closeModal()}}/> :""}
            // ↑を修正
          </div>
      );
    }
}

export default Modal_ClassComponent;

```
まずは親コンポーネントへの記述をしていきます！

### モーダルを閉じる関数の作成

```javascript
// -----1------
// ↓を追加
closeModal(){
  this.setState({isModalOpen:false})
}
// ↑を追加
```
`openModal()`の時と同様に、`setState()`関数を使っていきます。
ここでは、閉じる関数なので`isModalOpen`が`false`になるようにします。


### モーダルコンポーネントに`closeModal()`関数を渡す
```javascript
// -----2------
// ↓を修正
{this.state.isModalOpen? <Modal onClick={()=>{this.closeModal()}}/> :""}
// ↑を修正
```
`onClick={()=>{this.closeModal()}}`が増えました！
紛らわしいですが、`onClick`イベントハンドラではないです。
ただ`onClick`って名前をつけてモーダルコンポーネントに関数を渡しています。

モーダルコンポーネントにある閉じるボタンを押すと、親コンポーネントの`closeModal()`関数が実行されるようにしたいんです！
でも、モーダルコンポーネントから直接親コンポーネントの関数を実行できないので、一度`onClick`という名前でモーダルコンポーネントに関数を渡しているって感じです。

### モーダルコンポーネントで関数を受け取る
```javascript
// MyComponents.js
// 子コンポーネント（モーダル）
class Modal extends React.Component {

  render(){
    return(
        <div id="modal" className="modal">
          <div>
            <p>モーダル</p>
            // -----3------
            // ↓を修正
            <button onClick={this.props.onClick}>閉じるボタン</button>
            // ↑を修正
          </div>
        </div>
    )
}}
```
こっちの`buttun`タグについているのは`onClick`イベントハンドラです！
クリックされた時に、`this.props.onClick`を発動するという記述です。

`this.props.onClick`で、親コンポーネント側で設定した`onClick`の中身（`closeModal()`関数）を取り出せます。
これで、モーダルコンポーネント側から、親コンポーネントの`isModalOpen`ステートを更新できます。

## 7. モーダル外を押しても閉じる設定
さて、ここからが本題です！（長かった）
モーダルの外を押してもモーダルが閉じるようにしないといけません。


```javascript
// MyComponents.js
// 親コンポーネント
class Modal_ClassComponent extends React.Component {
  constructor(props) {
   super(props);
    this.state = {
      isModalOpen: false
    };
    // -----1------
    // ↓を追加
    this.closeModal = this.closeModal.bind(this);
    // ↑を追加
  };
  // -----5------
  // ↓を追加
  componentWillUnmount(){
    document.removeEventListener('click',this.closeModal)
  }
  // ↑を追加

  // -----2------
  // ↓を修正
  openModal(event){
    this.setState({isModalOpen:true})
    document.addEventListener('click',this.closeModal)
    event.stopPropagation()
  }
  // ↑を修正

  closeModal(){
    this.setState({isModalOpen:false})
    // -----4------
    // ↓を追加
    document.removeEventListener('click',this.closeModal)
    // ↑を追加
  }

  render(){
      return (
        <div className="modalpage">
          <h2>クラスコンポーネント</h2>
            // -----3------
            // ↓を修正
            <button onClick={(event)=>{this.openModal(event)}}>モーダルを開く</button>
            // ↑を修正
            {this.state.isModalOpen? <Modal onClick={()=>{this.closeModal()}}/> :""}

          </div>
      );
    }
}

export default Modal_ClassComponent;
```
```javascript
// MyComponents.js
// 子コンポーネント（モーダル）
class Modal extends React.Component {

  render(){
    return(
        // -----6------
        // ↓を修正
        <div id="modal" className="modal" onClick={(event)=>{event.stopPropagation()}}>
        // ↑を修正
          <div>
            <p>モーダル</p>
            <button onClick={this.props.onClick}>閉じるボタン</button>
          </div>
        </div>
    )
}}
```
順番ばらばらで見にくいですが、説明していきますね～！


### 画面をクリックしたときにモーダルが閉じるようにする

```javascript
constructor(props) {
   super(props);
    this.state = {
      isModalOpen: false
    };
    // -----1------
    // ↓を追加
    this.closeModal = this.closeModal.bind(this);
    // ↑を追加
  };
```
まずは、`closeModal()`をバインドさせておきます。
こうすることで、この後の説明で登場する`this.closeModal`がすべて同じものになると思っておいてください。

```javascript
// -----2------
// ↓を修正
openModal(event){
  this.setState({isModalOpen:true})
  document.addEventListener('click',this.closeModal)
  event.stopPropagation()
}
// ↑を修正
```
`document.addEventListener('click',this.closeModal)`で、画面のクリックイベントを監視します。
`openModal()`関数が発動すると、画面のクリックを監視しはじめるってわけですね！

でも、このままだと、`openModal()`関数が発動したらすぐにモーダルが閉じてしまいます(´;ω;｀)
`openModal()`はモーダルを開くボタンをクリックすることによって発動するので、`addEventListener`がクリックイベントを受け取ってしまって、モーダルが閉じるというわけですね(;´･ω･)

そこで、`event`引数を追加して、イベント情報を受け取れるようにします。
そして、`event.stopPropagation()`と書きます。
これで、`openModal()`を発動させる時のクリックは、`addEventListener`の適用外になります。


```javascript
render(){
    return (
      <div className="modalpage">
        <h2>クラスコンポーネント</h2>
          // -----3------
          // ↓を修正
          <button onClick={(event)=>{this.openModal(event)}}>モーダルを開く</button>
          // ↑を修正
          {this.state.isModalOpen? <Modal onClick={()=>{this.closeModal()}}/> :""}

        </div>
    );
  }
```
`openModal()`関数にクリックされたときのイベント情報を渡してあげるため、`event`を追加します。


### モーダルが閉じた時に`addEventListener`の監視を止める
```javascript
closeModal(){
  this.setState({isModalOpen:false})
  // -----4------
  // ↓を追加
  document.removeEventListener('click',this.closeModal)
  // ↑を追加
}
```
今のままだと、モーダルが閉じても`document.addEventListener('click',this.closeModal)`の監視が続いてしまいます。
そこで、`document.removeEventListener('click',this.closeModal)`を追加して監視を解除します。

### アンマウント時のメモリリーク対策をする
```javascript
// -----5------
// ↓を追加
componentWillUnmount(){
  document.removeEventListener('click',this.closeModal)
}
// ↑を追加
```
今のままだと、モーダルを開いたまま別のページに遷移した時などに、エラーが起きてしまいます。
どうしてかというと、モーダルを開いた時に発動した`document.addEventListener('click',this.closeModal)`の監視が、別のページでも続くからなんです。

そこで、`componentWillUnmount()`というライフサイクルメソッドとやらを使います。

`componentWillUnmount()`の中に書いたものは、そのコンポーネントがアンマウント（非表示）された直後に発動します。

`componentWillUnmount()`の中に`document.removeEventListener('click',this.closeModal)`を書いておくと、別のページに遷移した時に監視を解除できます。

### モーダルの中をクリックしたときに閉じないようにする。
ここまでで、画面をクリックしたときにモーダルが閉じるようになったと思います(*´ω｀)
だけど、閉じるボタン以外のモーダルの要素をクリックしてもモーダルが閉じてしまいますよね。

そこで、モーダルコンポーネントで以下の処理を行います。
```javascript
// MyComponents.js
// 子コンポーネント（モーダル）
class Modal extends React.Component {

  render(){
    return(
        // -----6------
        // ↓を修正
        <div id="modal" className="modal" onClick={(event)=>{event.stopPropagation()}}>
        // ↑を修正
          <div>
            <p>モーダル</p>
            <button onClick={this.props.onClick}>閉じるボタン</button>
          </div>
        </div>
    )
}}
```
モーダル要素の一番外側に`onClick`イベントハンドラを渡して、`event.stopPropagation()`と書いておきます。
こうすることで、モーダルを開くボタンの時と同様に、`addEventListener`の適用外にできます。


これでモーダルの完成です～！
お疲れ様でした♪

## モーダル作成時の注意点
アンマウント時のメモリリーク対策ができていないと、以下の様なエラーが出ます(´;ω;｀)

![アンマウント時のエラー【クラスコンポーネント】](images/2021/06/アンマウント時のエラー【クラスコンポーネント】.png)
> Warning: Can't perform a React state update on an unmounted component. This is a no-op, but it indicates a memory leak in your application. To fix, cancel all subscriptions and asynchronous tasks in the componentWillUnmount method.
    at Modal_ClassComponent

```javascript
componentWillUnmount(){
  document.removeEventListener('click',this.closeModal)
}
```
↑のように記述することで、対策できるので、気を付けてみてください♪


## 参考

[【JavaScript】クリックイベントで取得したオブジェクトの使い方 まとめ](http://www.hp-stylelink.com/news/2014/04/20140422.php)

[React.Componentで外部要素のevent bind,unbindを正しく行う](https://creators-note.chatwork.com/entry/2017/11/22/113344)

[React Hooksを使ったモーダル実装](https://qiita.com/mt_816/items/961a4faed14d0ce2d3ab)

[安全に React Hooks を使用する](https://qiita.com/kobayang/items/88a104c0be28e16e65e8)

[バブリングによるイベントの伝播](https://www.codegrid.net/articles/addeventlistener-1/#toc-5)

[Event.stopPropagation()](https://developer.mozilla.org/ja/docs/Web/API/Event/stopPropagation)
