>------------<
- タイトル:[【1】React Nativeでテキストエディタを作ってみる！【下調べ編】]
- WordPressにアップロードしますか？:y[x]はいn[]まだしない
- 投稿時:p[x]公開d[]下書き
- カスタムURL:[React-Native-challenge-to-create-text-editor-1]
- カテゴリID:[3,11,12]
- タグID:[]
- 見出し画像のID:[]
- 識別番号[lmEQbAU1Pp1P]
>------------<

こんにちは！かたつむり([@Katatumuri_nyan](https://twitter.com/Katatumuri_nyan))です！

Reactを触ってみて、サイト的なものは作れるようになりました(*´ω｀)
そこで、次はReactNativeを触ってみようと思い、簡単なテキストエディタを作成しようと企んでおります(笑)

そもそもReactを使い始めたきっかけは、こんな感じです。

- フロントエンドでよく使われている（らしい）
- ReactNativeを使うとクロスプラットフォームなアプリ開発ができる（らしい）

iOSとかAndroidのアプリも作れちゃうなんてすごいじゃないですか～！

Reactは使ってみたから、次はNativeやな。
ということで、調べながらやっていきたいと思います(*´ω｀)

この記事のシリーズでは、調べながらやっていく様子をお伝えします。
参考にならない点も多々あるかと思いますが、「密着！駆け出しエンジニアの独学生活！」って感じで見ていただけたら嬉しいです(´∀｀*)ｳﾌﾌ

## テキストエディタを作ろうと思ったきっかけ
ちなみに、テキストエディタを作りたくなったきっかけは、

- iPadでMarkdownエディタを使いたいが、なんとなく手になじむものがない
- 記事をGitで管理したいから、iPadでsourcetreeみたいなアプリ欲しい
- てかほとんどのアプリ英語やんけ！

って思いまして！
ただ、Gitへの理解があまりないので、まずは簡単なテキストエディタを作ってみよう！ってなりました✨

記事には登場していないですが、Reactでwebアプリを作成した時に、壮大な計画を立ててしまい大変過ぎたので(;´･ω･)
というのも、JavaScriptとかほぼ分からない状態だったので、「ミリシラReactアプリ開発」しておりました(笑)

前置きはここまでにして、次のステップに進みたいと思います！


## ひとまず疑問をもとに調べてみた
はじめるにあたって疑問点があったので調べました！

### React Nativeでのアプリ開発について
[React Native](https://reactnative.dev/)  
[【連載】初めてのReact Native + Expo開発環境構築入門(Windowsベース)](https://qiita.com/hitotch/items/5142fff638c7805d84d5)  
[【ReactNative開発】ReactNativeって？今後どうなる？](https://www.simpletraveler.jp/2021/01/10/whatis-reactnative/)

### Expo使わないといけないの？
Expo使わなくてもいいけど、使った方が楽そう  
アプリ開発の知識ないならExpo使おう  

[react nativeで開発する際の環境はどれがいいのって話](https://yuto-m.hatenablog.com/entry/2019/04/30/132644)

### macなくてもできる？
`Expo`があればなくてもできるみたい  
一時的にmac借りてとかでもできるらしい  

[React Native + Expo - WindowsでアプリビルドからAppストア申請まで！【2020年3月時点】](https://tkd708.hatenablog.com/entry/react_native_expo_windows_from_build_to_app_store_application_2020)

### 無料でできる？
Expoなら無料でできるっぽい（2021年6月28日現在）

[expo/pricing](https://expo.io/pricing)


### テキストエディタ作れる？
JSの`ACE.js`っていうテキストエディタライブラリがあるみたい  
自動補完やsyntaxhighlightなどしてくれるみたい（Reactでも使えるのかな？）

[テキストエディターを作ってElectronの基礎を学ぼう！](https://ics.media/entry/8401/)

### Dockerで環境構築できる？
React NativeとExpoつかってもできそう！

[DockerでReact Native環境を構築する](https://px-wing.hatenablog.com/entry/2021/01/29/065249)
[DockerでReact Native(TypeScript)+Expoのプロジェクト構築](https://qiita.com/hidenoritoki/items/9cd972ba102d12faec0e)

と、いうことで、早速作り始めます～！


↓続き
[card2 id="559"]