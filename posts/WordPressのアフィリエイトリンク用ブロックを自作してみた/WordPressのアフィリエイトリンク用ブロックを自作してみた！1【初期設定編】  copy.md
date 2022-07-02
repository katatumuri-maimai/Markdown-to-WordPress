>------------<
- タイトル:[【1】WordPressのアフィリエイトリンク用ブロックを自作してみた！【初期設定編】 ]
- WordPressにアップロードしますか？:y[]はいn[x]まだしない
- 投稿時:p[]公開d[x]下書き
- カスタムURL:[made-block-for-affiliate-link-of-WordPress-1]
- カテゴリID:[2,12]
- タグID:[]
- 見出し画像のID:[]
- 識別番号[AWiXnaI4x9gR]
>------------<

<!-- ↓続き
[kanren id=""] -->

こんにちは！かたつむり([@Katatumuri_nyan](https://twitter.com/Katatumuri_nyan))です！

最近、WordPressのアフィリエイトリンクを貼るのってめんどくさいなぁと思いまして、、、。

カッテネなどのプラグインを使って、ショートコードでリンクを貼るのもいいんですが、ショートコードめっちゃめんどくさい…
しかもミスる可能性が上がるので、ブロックで対応することにしました。

**最初から見る↓**
[kanren id=""]

<!-- **前回を見る↓**
[kanren id=""] -->

## 環境
[こちら](https://www.webdesignleaves.com/pr/wp/wp_block_basic.html)のサイトを参考に、プラグインを作成していきます。

すでにWordPressが本番環境にあるのと、ローカルで開発するのがめんどくさいので←
今回は、本番環境で開発することにしました。（ぉぃ）

## afi-link-block.php と block.jsの作成

```php
// afi-link-block.php
<?php
/*
Plugin Name: Afi Link Block
*/
 
defined( 'ABSPATH' ) || exit; 

//ブロック用のスクリプトの読み込み
function afi_link_block_enqueue() {
  //ブロック用のスクリプトを登録し、出力用のキューに入れる
  wp_enqueue_script(
    'afi-link-block-script', //スクリプトを識別するためのハンドル名
    plugins_url( 'block.js', __FILE__ )  //スクリプトの URL
  );
}
add_action( 'enqueue_block_editor_assets', 'afi_link_block_enqueue' );
```

```javascript
// block.js
console.log('Hello from my first block!');
```

とりあえずこちらを作成し、アップロードしてみました！
![picture 2](/6ee60e4e9dbfd7242e70da9197b1228d5cca373c9486d05e473089bec34685b3.png)  
いるいる！


有効化すると、以下のように投稿画面のコンソールで表示されました！成功
![picture 1](/a7eb9e49faf2e82e48a32692af032e52bee76d044394a495b9cb985772b995b3.png)  


## 依存するスクリプトの追加
```php
// afi-link-block.php
array( 'wp-blocks', 'wp-element', 'wp-components' ) 
```

とりあえず、関連しそうなスクリプトを追加しておきました。

## フロントエンドのCSSの適応
フロントエンド側のCSSは異なるものを使うので、`style.css`を追加して、以下も追加しました。

```php
// afi-link-block.php
function my_block_enqueue() {
  //管理画面（エディタ画面）以外では
  if(! is_admin()) {
    wp_enqueue_style(
      'afi-link-block-front-only',
      plugins_url( 'style.css', __FILE__ ),
      array(),
      filemtime( plugin_dir_path( __FILE__ ) . 'style.css' )
    );
  }
}
add_action( 'enqueue_block_assets', 'afi_link_block_enqueue');    
```

## register_block_typeでの書き換え
```php
// afi-link-block.php
function my_first_block_enqueue() {
  //ブロック用のスクリプトを wp_register_script で登録
  wp_register_script(
    //スクリプトを識別するためのハンドル名
    'afi-link-block-script',
    //スクリプトの URL
    plugins_url( 'block.js', __FILE__ ),
    //依存するスクリプト
    array( 'wp-blocks', 'wp-element', 'wp-components' ) 
  );
  
  //ブロックタイプの登録
  register_block_type( 
    //namespace を含むブロックタイプの名前
    'afi-link-blocks/afi-link-block', 
    array(   
      //ブロックのスクリプト block.js をエディタ用スクリプトとして関連付け
      //上記 wp_enqueue_script で登録したハンドル名 afi-link-block-script を指定
      'editor_script' => 'afi-link-block-script', 
    ) 
  );
}
add_action( 'init', 'afi_link_block_enqueue' );
```

## 試行錯誤
[こちら] (https://zooan.net/wordpress-gutenberg-customblock-link/)を参考にしながら試行錯誤します。

```javascript
// block.js
```