>------------<
- タイトル:[【2】Laravelでコーディングテストサービスを共同開発した際のメモ【フロントエンド編】 ]
- WordPressにアップロードしますか？:y[]はいn[x]まだしない
- 投稿時:p[]公開d[x]下書き
- カスタムURL:[joint-development-Laravel-coding-tester-2]
- カテゴリID:[12,15,16]
- タグID:[]
- 見出し画像のID:[]
- 識別番号[b085KWHwJt5n]
>------------<

<!-- ↓続き
[kanren id=""] -->

こんにちは！かたつむり([@Katatumuri_nyan](https://twitter.com/Katatumuri_nyan))です！

今回は、[とらちゃん](https://github.com/dt-torachan)と共同開発した際の開発メモを書いていきます！
コーディングの問題を登録できるサービスを作成しています。

今回は、デザインをもとにコーディングしていきます。

[GitHub](https://github.com/dt-torachan/CodingTester)でソースコードを管理しています！

**最初から見る↓**
[kanren id="723"]

<!-- **前回を見る↓**
[kanren id=""] -->


ディレクトリ構造とファイル
[【Laravel】Bladeテンプレートでレイアウトを共通化する](https://nodoame.net/archives/10756)
[LaravelのBladeについての備忘録](https://qiita.com/sakashin10291029/items/27220f443d550338d347)

[カーソルを指マークにするためだけにaタグを利用するのをやめよう](https://zenn.dev/yukito0616/articles/c956de73b02ed8)

[【laravelでの実装例付き】フッターを常にページ最下部に表示する方法](https://note.com/kishiyyyyy/n/n56e2c3b0ba07)


## Gitの運用



## HTML
[form内のbuttonとform外のbuttonの違い](https://webbeginner.hatenablog.com/entry/2014/11/01/172318)


## cssをscssに変換
cssでデザインをしていたのですが、scssでの記述に変えたいので逆コンパイルしました。

[CSS 2 SASS/SCSS CONVERTER](http://css2sass.herokuapp.com/)


## scssをcssに変換
VScodeで自動コンパイルされるように設定していきます。

### 新バージョンの拡張機能「Live Sass Compiler」を導入

[こちら](https://github.com/glenn2223/vscode-live-sass-compiler/blob/HEAD/docs/settings.md)を参考に設定

```json
#.vscode/setting.json
{
    "liveSassCompile.settings.formats": [
        {
            "savePath": "/src/codingtester/public/css"
        }
    ],
    "liveSassCompile.settings.generateMap":false,
    "liveSassCompile.settings.excludeList":[
        "**/node_modules/**",
        ".vscode/**",
        "**/bootstrap-stubs/app.scss",
        "**/codechecker/**"
    ]
}
```

### 使用方法
Watch my Sass でコンパイルの監視を開始