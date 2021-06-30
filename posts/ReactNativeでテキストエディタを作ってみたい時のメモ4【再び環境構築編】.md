>------------<
- タイトル:[【4】React Nativeでテキストエディタを作ってみる！【再び環境構築編】]
- WordPressにアップロードしますか？:y[x]はいn[]まだしない
- 投稿時:p[]公開d[x]下書き
- カスタムURL:[React-Native-challenge-to-create-text-editor-4]
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

DockerでReact Nativeを開発すると、ホットリロードが効きません。
一応代替え作もあるのですが…
あまりにもリロードが遅すぎるので、WSLで環境構築しなおします！


[GitHub](https://github.com/katatumuri-maimai/ReactNative-TextEditer)でソースコードを管理しています！

**最初から見る↓**
[kanren id="557"]

**前回を見る↓**
[kanren id="568"]





## 次の日…WSLでの環境構築
Windows+DockerDesktopでのReact Native+Expoでは、仕様上ホットリロード効かないことが分かったので、WSLを使って環境構築をしていきます！
（ホストマシンに環境構築しないのは、ただのこだわり。）

[DockerでReact Native環境作成から、Expo Clientで実機確認するまで](https://qiita.com/h-yoshikawa44/items/51b631ec0a6beabdce2d)
↑こちらの方が↓のような記事も書いてくださってるので、参考に環境構築していきます！
[WSLでReact Native + Expo環境を作ろう](https://qiita.com/h-yoshikawa44/items/610ffea888f13275cde8)


### WSLのインストール
とりあえず、WSLが必要なので、インストールします。

[WSLをインストールする](https://qiita.com/matarillo/items/61a9ead4bfe2868a0b86)
↑こちらを参考にインストールしていきます！
（どこかでDockerとWSLの違いとかそれぞれメリデメとか調べなきゃデスね。）

WSL2の方が新しいみたいなので、WSL2をインストールします。
ついでに[リポジトリ](https://github.com/katatumuri-maimai/ReactNative_TextEditor)を新しくしました。（前回Editorのつづり間違ってた(〃ﾉωﾉ)ｗ）

なじみのUbuntuにしました～！

![picture 1](images/fe0ccf66833c587d34ac20d86c109042d33689065a21bbf2a7044155a4abac1e.png)  

![picture 2](images/f0d22e0f0f1c1e5f39c9c2ce41ca3b4ce1e38914fe4cbee62173da18e89d624f.png)  

```
> WslRegisterDistribution failed with error: 0xc03a001a
```

なぜ…

[failed with error: 0xc03a001a で失敗するときの対処法](https://qiita.com/kuryus/items/27a7206c64eca7ba710b)
↑こちらを参考に直していきます！

無事起動・ログインできました(*´ω｀)

![picture 3](images/b62c08ce44b946a25002a83dbe6c6874d6321263472937057ae760ee79416dfa.png)  

Ubunto久しぶりで嬉しい～（普段Dockerで使っているけどなんとなくｗ）

### Node.jsのインストール
[Windows に WSL を使って Node 環境を構築する](https://qiita.com/nekonekonekosan/items/61a6b9d4da6bdfd1d0bb)
↑こちらを参考にインストールしていきます！

### ReactNative+Expo環境構築
やっとここまできました！
[WSLでReact Native + Expo環境を作ろう](https://qiita.com/h-yoshikawa44/items/610ffea888f13275cde8)



#### 疑問メモ
ここでちょっと疑問：VScodeでコード編集できるんだろうか…？
[VSCodeをWSLで使用する設定](https://infltech.com/articles/N0jUEQ)
↑でいけるっぽい。試してみよう。

いけたけど、せっかくつくったリポジトリ…はどうなるのかなｗ

うまくいきました～！
sourcetreeにも作業ディレクトリ登録できたので、いい感じですね。


### 環境変数の設定がよくわからない
`~/.profile`ってどこ？って思ったので、探してみました。

ubuntuを起動すると最初に表示される画面で、`ls -a`と打ってみます。

![picture 4](images/1c138014db7e979e819b8dc016eb5e38c5f8c2818386b039b2cfaa46010320e0.png)  

`.profile`あった！！！

ここに環境変数を追加します。が、開き方が分からん。。。

`vim .profile`でとりあえず開いてみました。
vimで編集できました。[Vim初心者に捧ぐ実践的入門](https://qiita.com/okamos/items/c97970ab34ff55ff3167)

でも、実機で開けません(´;ω;｀)

`netstat -nao | find "19000"`で確認すると、ほかのプロセスとは被ってないみたいでした。

ファイアウォール切ってみましたが特に何も起こらず。

![picture 5](images/ccb4e6ccc584e31981e02b860b5a27101505a3ddec05a535c639bc394fb43357.png)  

とりあえずTunnelモードで使ってみることにしたら、開けました！
ホットリロードも効くので、実機確認できたあ良かった(*´ω｀)