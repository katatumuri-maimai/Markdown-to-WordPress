# Reactでモーダルの外をクリックするとモーダルが閉じる機能を作ったときに困ったことと対処法メモ
## 困ったこと
Reactでモーダルの外をクリックするとモーダルが閉じる機能をつけたいのに、ほかのページをクリックしてもその関数が動くので困ったんですよ。

（解決したけどあってるのか分からないので、間違ってたらすみません。）

## 原因
```javascript
// モーダルをモーダル外をクリックしても閉じる
LinkShareClose2(){
  const TTK = window.addEventListener('click', (e) => {
    if(!e.target.closest('.modal')) {
     if(!e.target.closest('.btn_square')) {
       //ここに外側をクリックしたときの処理
       this.mounted && this.setState({isLinkShareOpen: false})
       this.mounted && this.setState({iscopyToClipboard: false});
       window.removeEventListener('click',TTK);
     }
   }
 })
}
```
クラスコンポーネントの中で定義していた↑の関数を`render`の中で`this.LinkShareClose2();`して実行していたのが問題っぽい。


## 解決方法
`render`の中の`this.LinkShareClose2();`を消して、以下を追加しました。
```javascript
// モーダルをモーダル外をクリックしても閉じる
LinkShareClose2(){
  const TTK = window.addEventListener('click', (e) => {
    if(!e.target.closest('.modal')) {
     if(!e.target.closest('.btn_square')) {
       //ここに外側をクリックしたときの処理
       this.mounted && this.setState({isLinkShareOpen: false})
       this.mounted && this.setState({iscopyToClipboard: false});
       window.removeEventListener('click',TTK);
     }
   }
 })
}

// ↓↓↓↓以下を追加↓↓↓↓
// マウント時、アンマウント時に実行させる。
componentDidMount() {
  this.mounted = true;
  this.mounted && this.LinkShareClose2();
}

componentWillUnmount() {
  this.mounted = false;
}

```

マウントがよくわからないけど←。
とりあえず、`componentDidMount(){}`の中に関数を書くと、勝手に実行してくれるみたい。
  `componentWillUnmount(){}`の中に書くと、ほかのページに行った時に実行しないようにしてくれる。ありがたや～



## 参考サイト
[React.jsのEventについて](https://qiita.com/koba04/items/bf8d02a2d0589e9247a7)
[React コンポーネントのアンマウント時のエラーを修正する方法(componentWillUnmount)](https://alpacat.com/blog/react-unmount-error)
