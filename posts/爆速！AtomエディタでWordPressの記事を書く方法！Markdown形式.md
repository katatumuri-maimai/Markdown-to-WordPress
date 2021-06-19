# 爆速！AtomエディタでWordPressの記事を書く方法！Markdown形式
はじめまして♪かたつむりです！

プログラミングにハマってきたので、備忘録としてブログを書くことにしました。
そこで、「いつも使っているAtomエディタで記事をかけたら楽なのに」…と思い、記事をAtomで書く方法を探してみたので、メモとして残しておきたいと思います♪

## Atomエディタで書く意味
そもそもWordPressの投稿画面から書けばいいのに、Atomエディタでかく必要があるのかって言うとこなんですが、、、。

### 1.シンプルに書きたかった
今までWordPressの記事投稿画面で書いてたんですが、なんかちょっと使いにくいんですよね…。
もちろん、文字装飾とかはWordPressの記事投稿画面の方が好きなので、仕上げはWordPressの方でやると思います。

だけど今回のブログは、備忘録として使うので、爆速で書ける必要があったのと、文字装飾はあまり必要なかったので、シンプルに慣れてるテキストエディタでかけちゃった方が楽だと思いました。
（プログラミングでテキストエディタを使うとあるあるになるのかな？）

今まで避けてきた、Markdown形式も、Atomならボタンポチポチでかけるみたいなので、やってみようかなと。
（後で紹介する参考記事の手順に従って設定すると、めっちゃ楽に書ける。）

### 2.Githubと連携して自動で記事投稿できる可能性…
あとは、Githubにプッシュしたら自動で記事投稿してくれないかなぁとか、思っちゃったりして。
AtomでGithub使えるから、テキストエディタ一つで記事投稿できるじゃん！とか思っちゃったり…


## Markdown形式って？
私もよくわからないのですがｗ
簡単な記号を使って、見出しとかを設定できる記法って認識です。

テキストエディタでWordPressの記事を書こうとすると、テキストエディタからコピペするっていうことが多いと思うので、HTMLタグを書きますよね。
具体的には、以下のような感じになります。
`<h2>見出し1だよ</h2>`


Markdown形式で書くなら、以下のように書いたらOKです。
`## 見出しだよ`

今はWordPressでMarkdown形式がサポートされているので、Markdown形式のままコピペしても、記事に反映されます。



## 参考記事
今回は、こちらの記事にしたがってAtomエディタの設定をしました。
[【Atom設定】WordPressの下書きで大活躍するテキストエディタ！爆速！][d8dd553b]

  [d8dd553b]: https://giraffe-media.com/wp-draft "【Atom設定】WordPressの下書きで大活躍するテキストエディタ！爆速！"

もう一つ、似ている記事も見つけましたので貼っておきます。
[Atomを最高のブログエディタにカスタマイズする方法][75bf6342]

  [75bf6342]: https://pooork.com/editor-atom-customize/ "Atomを最高のブログエディタにカスタマイズする方法"

  ちなみに、2記事はWordPressがまだMarkdown形式をサポートしていない時に書かれたみたいなので、「WordPressにHTML形式でコピペしましょう。」って書いてあります。
  今はそのままコピペしてもいけるので、参考までに。
※WordPressの方のエディタは、ブロックエディタで試したので、テキストエディタで使えなかったらごめんなさいｗ

## Markdown

[Qiitaに投稿するマークダウン（Markdown）記法のメモ][249a0451]

  [249a0451]: https://qiita.com/maboy/items/bbfea777544b96b57cda "Qiitaに投稿するマークダウン（Markdown）記法のメモ"

  [  WordPressでMarkdownを使ってみる][75e75510]

  [75e75510]: https://gatespace.jp/2014/07/03/wordpress-markdown/ "WordPressでMarkdownを使ってみる"

[  【cheatsheet】Markdownとは？【使い方/書き方】][a615324a]

  [a615324a]: https://suwaru.tokyo/%E3%80%90cheatsheet%E3%80%91markdown%E3%81%A8%E3%81%AF%EF%BC%9F%E3%80%90%E4%BD%BF%E3%81%84%E6%96%B9-%E6%9B%B8%E3%81%8D%E6%96%B9%E3%80%91/ "【cheatsheet】Markdownとは？【使い方/書き方】"

## ソースコードを綺麗に表示
```html
codeを綺麗に表示したい
```

[wordpressにmarkdown形式で投稿するための設定][a118aa7a]

  [a118aa7a]: https://qiita.com/stmon19/items/77aee1027678755d040f "wordpressにmarkdown形式で投稿するための設定"

↑こちらの記事を参考にCrayon Syntax Highlighterプラグインを入れてみたらエラーがやばかったので、↓の記事を参考に、アップデート版Urvanov Syntax Highlighterを入れました。
[Urvanov Syntax Highlighterに移行しよう（旧：Crayon Syntax Highlighter利用者向け）【簡単解決】][3276e574]

  [3276e574]: https://nkmrdai.com/urvanov-syntax-highlightercrayon_plugin/ "Urvanov Syntax Highlighterに移行しよう（旧：Crayon Syntax Highlighter利用者向け）【簡単解決】"

でも結局、コードブロックをrvanov Syntax Highlighterブロックに変換できなかったので、CodeMirror Blocksを入れました。
これで、マークダウンで書いたコードをWordPressの投稿画面でポチポチするとコードブロックに返還できるようになりました。
（一回変換すると自動で変換してくれるようになるみたいだがはて…？）

[CodeMirror Blocks][867ce99f]

  [867ce99f]: https://ja.wordpress.org/plugins/wp-codemirror-block/ "CodeMirror Blocks"

[Theme Demo][03aa2928]

  [03aa2928]: https://codemirror.net/demo/theme.html "Theme Demo"



## 今後のためのメモ
  Githubと連携して自動で記事投稿できる可能性がある気がするので、後で読みたい記事を貼っておきます。
  何か知ってることがあれば教えてください←
[  WP REST API][ff589429]

  [ff589429]: https://ja.wp-api.org/ "WP REST API"

[  GitでWordPressにPostしたいと思ったけど結局VimRepress導入した][457a7851]

  [457a7851]: http://haya14busa.com/vimrepress-and-wordpress-using-git/ "GitでWordPressにPostしたいと思ったけど結局VimRepress導入した"

[  Gatsbyによるブログ構築][2fde9273]

  [2fde9273]: https://mako-note.com/building-a-blog-with-gatsby/ "Gatsbyによるブログ構築"
