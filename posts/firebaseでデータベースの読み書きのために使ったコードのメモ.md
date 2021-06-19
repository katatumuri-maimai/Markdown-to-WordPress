# React×firebaseでデータベースの読み書きのために使ったコードのメモ
ReactでfirebaseのCloud FireStoreやRealtime Databaseと接続して、データを追加したり取得したりしたいときに使ったコードとかをメモしておきます。
HTML/CSSしか分からない駆け出しエンジニア（仮）なので、よくわかってない部分もあるけど。。。ｗ
もしアドバイスとかあればコメントによろしくお願いいたします(*´ω｀)
説明とか使用例書いてほしいとかあったら追加します。

## 使ってるもの
- Node.js
- React
- firebase
- firebase emulators (firebase-toolsをインストールする)
- Docker

（何書いたらいいんだろｗ）

## 前提
どのサイトを見ても、コードの使い方が分からんのじゃ！ってなってたプログラミング初心者なので、前提書いときますね。
- Reactっていうライブラリでサイト作ってます。
- firebase関連のものはサーバーにインストール（もしくは[firebaseのドキュメント](https://firebase.google.com/docs)に従って導入）
- コードを使いたい.jsファイルにの頭に↓は絶対かく。
- 紹介しているコードは関数の中で使ってね。


### Reactっていうライブラリでサイト作ってます。
Reactって、Javascriptのライブラリらしい。
ライブラリってなんだよって思いながら使ってます。
サーバーもレンタルサーバーじゃなくて、自分のパソコンにDockerってやつをインストールして、そこでサーバーをたてて。。。ってやってるので、なんかよくわかりませんが、すごいことしてます。

※DockerやReactの導入の仕方とかはまた今度。

### firebase関連のものはサーバーにインストールしておく
※今回は、ローカル（自分のパソコン）にサーバーを構築して、そこにサイトとかをのせてるので、サーバーにfirebaseをインストールして使ってます。（レンタルサーバーでやる方法は分からないお）
※ローカルでfirebaseを実行しているので、エミュレーターってのを使っていますが、ウェブ上のfirebaseにデータを送る場合は、エミュレーター要らないと思う。たぶん。

- firebase
- firebase-tools　（これがエミュレーター）
- firebase-app
- firebase-firestore
- firebase-database

※導入の仕方は、[firebaseのドキュメント](https://firebase.google.com/docs)を参考にしました。



### コードを使いたい.jsファイルにの頭に↓は絶対かく。
```Javascript
// Reactのインポート
import React from 'react';
// firebaseのインポート
import "firebase";
import firebase from "firebase/app"; // firebase/appのインポート
import "../../firebase/config.js"; // config.jsのインポート

```
これかくの忘れてると、データベースと接続できない。
※`config.js`のパスは、ご自身の使ってる環境に合わせて書いてください。（書き方わからんって人はごめん）
※`config.js`の名前は`firebase.js`とかだったりするから分からんちんなので、一番下の方に一応中身こんなのだよってのを書いておきました。

### 紹介しているコードは関数の中で使ってね。
#### Reactのコンポーネントとして普通に書くならこう
```Javascript
function Sample(){ //Sampleのとこは自分で決めた関数名を書く。最初大文字。
  //
  //ここに使いたいコードを書く
  //
}
```
####Reactのクラスコンポーネントのなかで書くならこう
```Javascript
class MainColorBtn extends React.Component {
  /// …
  //省略
  //…

  function Sample(){ //Sampleのとこは自分で決めた関数名を書く。最初大文字。
    //
    //ここに使いたいコードを書く
    //
  }

  render(){
    /// …
    //省略
    //…

}

```

### ※関数の実行の仕方
これわからなくて困ったんだけど、その辺はおいおい書きます。
ググってm(__)m



## FireStore関連
### データを追加する
`collectionName`って名前のデータの中に送りたいデータを送る。
`.set({"送りたいデータ"})`で送れる。

```Javascript
firebase.firestore().collection("collectionName").doc().set({
  roomid: "RoomID",
  name: "gest",
  people: "People",
  gamelaps:"GameLaps",
  created: firebase.firestore.FieldValue.serverTimestamp(),
});
```

ちなみに↓これは、その時の時間を出力してくれるfirebaseの機能をつかうコード。
```Javascript
firebase.firestore.FieldValue.serverTimestamp()
```


### データをとってくる

```Javascript
const documentSnapshot =  firebase.firestore().collection('CreateGameRoom').doc("DocId")

documentSnapshot.get().then((doc)=>{
   if (doc.exists) {
     const DocData = doc.data();
     const RoomPeople = DocData["people"];
     console.log(RoomPeople)
   }})

```

## Realtime Database関連
### データを追加する
`users`というデータの中に`userId`というデータを作って、`userId`と`userName`を登録する例です。
```Javascript
firebase.database().ref('users/' + userId).set({
  // 追加するデータをJSON形式で書く。
  userId:"TestID",
  userName:"TestName"
});

```
#### 実際に関数の中で使用した例
```Javascript
// Reactのインポート
import React from 'react';
// firebaseのインポート
import "firebase";
import firebase from "firebase/app";
import "../../firebase/config.js";

// SetData関数を作ります。
function SetData(userId, userName){
  // Realtime Databaseに接続して、userIdとuserNameを追加する
  firebase.database().ref('users/' + userId).set({
    userId:userId,
    userName:userName
  });
}

```

### データをとってくる
`users`という名前のデータ中の`userId`という名前のデータなかにある`userName`の項目にはなにが登録されてるかなってとってきてます。

```Javascript
// データをとってくる
firebase.database().ref().child("users").child("userId").get().then((snapshot) => {
  // データがあったらuserNameの項目に登録されているものをとってきて、コンソールに表示する。
  if (snapshot.exists()) {
    console.log(snapshot.val().userName);
  // もしデータが無かったらエラーをコンソールに表示する
  } else {
    console.log("No data available");
  }
}).catch((error) => {
  console.error(error);
});

```

### データをとってきてサイトに表示する
サイトに描画する方法が分からず、結構手間取ったので書いときます。
どこか表示したい場所に↓を書く。

```HTML
<div id="userName"></div>
<div id="userId"></div>
```

↓のコードを使って関数を作って実行する。

```Javascript
const dbRef = firebase.database().ref();
dbRef.child("users").child("userId").get().then((function(snapshot) {
  document.getElementById("userName").innerHTML = snapshot.val().userName;
  document.getElementById("userId").innerHTML = snapshot.val().userId;
})).catch((error) => {
  console.error(error);
});
```


## firebaseを使うためのconfigファイルのimport
firebaseに接続する時に、最初に書かないといけないコードがあるので、それを別ファイル（`config.js`）に書いておきました。
使いたい`.js`ファイルで`import`しておけば、何度も書かなくて良いみたいです。

```Javascript
import "../../firebase/config.js";
```

↑このコードで、↓の`config.js`ファイルをインポート。
（`config.js`ファイル使いたい`.js`ファイルの中で書きます。）
`../../firebase/config.js`の部分は、`config.js`ファイルがあるディレクトリの相対パスを書いています。
なので、階層が異なる場合や`firebase`ディレクトリ名が違う場合は環境に応じて変更してください。

```Javascript
// 以下はfirebaseで使うものをインポートしています。
import firebase from 'firebase/app';

// 以下はfirebaseで自動生成されたものを書き込みます。
let firebaseConfig = {
  apiKey: "",
  authDomain: "",
  databaseURL: "",
  projectId: "",
  storageBucket: "",
  messagingSenderId: "",
  appId: "",
  measurementId: ""
};


// Initialize Firebase　初期化します。書いとかないといけないらしい。
if (firebase.apps.length === 0) {
  firebase.initializeApp(firebaseConfig);
}

// firestoreをローカルのエミュレーターで使う設定。環境に応じて変更の必要あり。
var fs = firebase.firestore();
if (window.location.hostname === "localhost") {
  fs.useEmulator("localhost", 8080);
}

// Realtime Databaseをローカルのエミュレーターで使う設定。環境に応じて変更の必要あり。
var db = firebase.database();
if (window.location.hostname === "localhost") {
  db.useEmulator("localhost", 9000);
}

```
