>------------<
- タイトル:[【2】React Nativeでテキストエディタを作ってみる！【環境構築編】]
- WordPressにアップロードしますか？:y[x]はいn[]まだしない
- 投稿時:p[x]公開d[]下書き
- カスタムURL:[React-Native-challenge-to-create-text-editor-2]
- カテゴリID:[3,11,12]
- タグID:[]
- 見出し画像のID:[]
- 識別番号[UWQpLvmyAica]
>------------<

こんにちは！かたつむり([@Katatumuri_nyan](https://twitter.com/Katatumuri_nyan))です！

Reactを触ってみて、サイト的なものは作れるようになりました(*´ω｀)
そこで、次はReactNativeを触ってみようと思い、簡単なテキストエディタを作成しようと企んでおります(笑)

今回は、Dockerで、React Native+Expoの環境構築をしていきます～！


[GitHub](https://github.com/katatumuri-maimai/ReactNative-TextEditer)でソースコードを管理しています！

最初から見る↓
[card2 id="557"]


## 環境

- PC
    - Windows10
    - Docker Desktop
    - docker-compose

-端末
    - iPhone XR
    - iPad 9.7

## 1.Expoアカウントの作成

[Expoアカウントの作成方法](https://qiita.com/hidenoritoki/items/0c5084b84dfc2126d9ec)
[iPhoneでExpo Clientのインストールとセットアップ](https://qiita.com/hidenoritoki/items/afa69ca6ce910ee28cd9)

↑こちらの手順にそって、Expoアカウントを作成、メールが届くのでリンク先にログインして完了。  
iPhoneとiPadでExpo Clientというシミュレーターみたいなものを導入。

## 2.Dockerで環境構築

[DockerでReact Native(TypeScript)+Expoのプロジェクト構築](https://qiita.com/hidenoritoki/items/9cd972ba102d12faec0e)

↑こちらの手順とファイルを参考に作成　　

### `docker-compose build`でエラーがでた！
![picture 1](images/2021/06/860e1bbc3dbf9a59713e1f7e7d8601b42059509f40b34e5d69178b32a391054e.png)  
`pywintypes.error: (2, 'CreateFile', '指定されたファイルが見つかりません。')`

↑DockerDesktopを起動していないだけだった

↓またエラー
![picture 2](images/2021/06/6959d88234340008928ce20ff97aab50cffade3dc12756ca005144caa8c0247c.png)  

```
Building react_native
[+] Building 0.1s (2/2) FINISHED
 => [internal] load build definition from Dockerfile                                                             0.1s 
 => => transferring dockerfile: 2B                                                                               0.0s 
 => CANCELED [internal] load .dockerignore                                                                       0.0s 
 => => transferring context:                                                                                     0.0s 
failed to solve with frontend dockerfile.v0: failed to read dockerfile: open /var/lib/docker/tmp/buildkit-mount883823841/Dockerfile: no such file or directory
ERROR: Service 'react_native' failed to build : Build failed
```

`dockerfile`の名前を`DockerFile`と間違えていました(;´･ω･)
無事ビルドできました～！

記事にしたがってセットアップしていきます。

### プロジェクトのセットアップ
TypeScriptを使っていないので`blank`を選択しました。

### コンテナの起動とアプリでの確認
参考記事にしたがって、起動していきます！  

![picture 3](images/2021/06/f780cac06c0227063e60e572e6500238246f2d51f238b0d6603b4aacf47d6020.png)  

読むとるも起動せず…  

![picture 5](images/2021/06/9650ab1202c8d06c78d4b863dd70a905bcf72d99973409a03785b721510a3d09.png)  


Expoのデベロッパーツールが起動する`http://localhost:19002/`にも接続できませんでした(;´･ω･)

もしかして、ローカルホストの`192.168.0.2`が違うかも！と思い、`.env`を変更　　
（`ipconfig`で分かるIPアドレスに変更）

```
REACT_NATIVE_PACKAGER_HOSTNAME=192.168.0.19
```

`docker-compose up`しなおしました。

が、**同エラー**(;´･ω･)

ポートが他のプロセスと被っているのかと思い、ホストマシンで`netstat -nao | find`するも特に何もなく…

~~~`.env`への変更を`192.168.0.2`に戻しました。~~~
~~~`http://localhost:19000/`では、`192.168.0.19`でも`192.168.0.2`でもJSONが表示されているので、`192.168.0.2`の変更は関係ないと判断しました！~~~


iPhone側から`http://192.168.0.19:19000/`にアクセスできないので、ポートの設定か何かがうまくいっていないのかもしれないですね。

```
EXPOSE 19000
EXPOSE 19001
EXPOSE 19002
```

ポートが解放されていないのかなぁと思い、`dockerfile`に上記を足してみました。
buildしなおすも特にかわらずｗ

おかしいなと思って、以前つくったReactアプリを立ち上げてみると、全滅していました。  
パソコンではアクセスできるものの、iPhoneからは難しく…こまったｗ
どこかでパソコンかDockerとかの設定が変わってしまったんでしょう…

![picture 6](images/2021/06/0163eb8144d2a3a9e08acd5bb4bef3dbb8a3dde844d03d94b6bb3528c7d7e989.png)  

このポートのところ、`0.0.0.0:3030`ですよね。
以前は`localhost:3030`だったんです…。
何が起きたんだろうｗ

#### 解決！
![picture 7](images/2021/06/730fefc190d143b24925aeffa312d061bf595d7282d6813221078b53d7def411.png)  

パソコンのネットワークがパブリックの設定になっていました。
プライベートに設定しなおすと、iPhoneからも接続できるようになりました(*´ω｀)

やっと実機確認終了です～！

`http://localhost:19001/`と`http://localhost:19002/`にはまだ接続できませんが…

> http://localhost:19002
> アクセスすると、Expo DevToolが使用できます。
> ここからシミュレータを起動したりできるみたいです。
> （X Code、Android Studioのインストールや設定が別途必要になるようです）
> 後述していますが、自分はうまくいきませんでした...。
引用:[DockerでReact Native環境作成から、Expo Clientで実機確認するまで](https://qiita.com/h-yoshikawa44/items/51b631ec0a6beabdce2d#httplocalhost19002)

とのことなので、とりあえず無しで進めてみます。

### ホットリロードされない問題
> ホットリロードによって末尾の☺️がiPhone上の検証画面へ自動的に反映されます。
[DockerでReact Native(TypeScript)+Expoのプロジェクト構築](https://qiita.com/hidenoritoki/items/9cd972ba102d12faec0e)

と書いてありますが、私の実機では無理でしたｗ

[Expoのドキュメント](https://docs.expo.io/get-started/create-a-new-app/)を参考に、作業してみました。

> 変更がデバイスに表示されていませんか？
> Expo Goはデフォルトで、ファイルが変更されるたびにアプリを自動的にリロードするように構成されていますが、何らかの理由で機能しない場合に備えて、アプリを有効にする手順を確認してください。
> まず、ExpoCLIで開発モードが有効になっていることを確認します。
> 次に、アプリを閉じて再度開きます。
> アプリが再び開いたら、デバイスを振って開発者メニューを表示します。エミュレーターを使用している場合は⌘+d、iOSまたはctrl+mAndroidの場合はを押します。
> が表示されたらEnable Fast Refresh、それを押します。が表示された場合はDisable Fast Refresh、開発者メニューを閉じます。次に、別の変更を加えてみてください。  


> ExpoCLIで開発モードが有効になっていることを確認します


ここなんですが、[公式ドキュメント](https://docs.expo.io/workflow/development-mode/#toggling-development-mode-in-expo-dev-tools)によると、、  `http://localhost:19002/`（Expo開発ツール）には接続必要って事みたいですね、、、。  
ターミナルデモできる様な気もしますが、今後のために`Expo開発ツール`を使えるように試行錯誤します！


#### とりあえずデバッグしてみた
![picture 8](images/2021/06/29a43cb4726072ae2c0090c3017a1fc91980b32642672ca3b29e89cd111d9613.png)  
![picture 9](images/2021/06/b9fb50b189a6ba4e4bd015a41fdf725ed01bef48ffa2e10dcadc6d5c85c997e2.png)  
![picture 10](images/2021/06/4504e32c63ef253dc111b752ba613d41a8abd46fe8ecf626cc5273813693b7ad.png)  

```
Runtime is not ready for debugging.
 - Make sure Packager server is running.
- Make sure the JavaScript Debugger is running and not paused on a breakpoint or exception and try reloading again.
```
> ランタイムはデバッグの準備ができていません。
> -Packagerサーバーが実行されていることを確認します。
> -JavaScriptデバッガーが実行中であり、ブレークポイントまたは例外で一時停止していないことを確認して、再ロードを再試行してください。

…謎


#### 1つ解決
[Metro bundler with Expo dockerized app is not working](https://stackoverflow.com/questions/59638451/metro-bundler-with-expo-dockerized-app-is-not-working)

↑こちらを参考に、`.env`に以下を追加

`EXPO_DEVTOOLS_LISTEN_ADDRESS=0.0.0.0`

`docker-compose up`しなおしてみます。

![picture 11](images/2021/06/a6be0f0f535b1b8dc182c3d38df3e404d2f908fbd91626b87f2ceee5491da2d2.png)  

真っ暗だけど開きました！
コンテナ内のlocalhostに繋がっていたのですね。
なるほど！


でも、真っ暗だしホットリロードできないですね。

[]()
↑こちらを参考に、`npm install -g expo-cli`と`npm start`してみたら良いのかもしれません。
`yarn`を使っているので、まずは`yarn`でアップデートしてみます。

一旦`Ctrl+C`でコンテナを落として、
`docker-compose.yml`に`yarn upgrade --latest`を追加しました。

```yml
version: "3"
services:
  react_native:
    build: ./docker/react_native
    volumes:
      - ./react_native/:/usr/src/app
    env_file: .env
    command: sh -c 'yarn upgrade --latest && yarn start'
    ports:
      - "19000:19000"
      - "19001:19001"
      - "19002:19002"
```

再び`docker-compose up`しなおしてみます。  
が、真っ黒のままでした(;´･ω･)

`docker-compose.yml`を元に戻しました。

コンテナを起動したまま別のターミナルを開いて、`yarn global upgrade`してみます。

`yarn`遅いから苦手😢

再び`docker-compose up`しなおしてみます。  

![picture 12](images/2021/06/1fc19756e525f291c511536c2eb810512efafcca10f8a114cfc2d0801c2e10a5.png)  

あ`http://192.168.0.19:19002/`でアクセスできました！
ありゃ～、もしかしたら`yarn`のくだりは必要ないかもですね(笑)

#### ホットリロードはうまくいかなかった
ただし、ホットリロードうまくいかないので、実機でのリアルタイム確認はできなさそうです(;´･ω･)


#### 代替え案-webブラウザで確認する
![picture 13](images/2021/06/1599fa88e2d6ff117d983dd9be386996cff4ea396311d992361d01415c9df0d9.png)  
ここ押すとインストールが勝手に始まります。

![picture 14](images/2021/06/a7d2ea1ca38f44cc24b5a36f7ce5f5ca9970bef54a52b4db23ea6b9832ee5104.png)  

ポート`19006`で動くみたいなので、`docker-compose.yml`にポートを追加しました。
```yml
version: "3"
services:
  react_native:
    build: ./docker/react_native
    volumes:
      - ./react_native/:/usr/src/app
    env_file: .env
    command: yarn start
    ports:
      - "19000:19000"
      - "19001:19001"
      - "19002:19002"
      - "19006:19006"
```

再び`docker-compose up`しなおしてみます。
![picture 13](images/2021/06/1599fa88e2d6ff117d983dd9be386996cff4ea396311d992361d01415c9df0d9.png)  
ここをもう一度押すと、勝手にWebpackが起動。
`http://localhost:19006/`にアクセスすると、、、

![picture 15](images/2021/06/80c7aa001aa8f2706eefb3d0cca5abd8fd2b77bef3d7e1b0cddbe55b8cd59ee4.png)  

できました～！

でもやっぱりホットリロードできないｗ(´;ω;｀)


#### 解決：`.env`に`CHOKIDAR_USEPOLLING=true`を追加
そういえば以前、Reactアプリを作成した時はホットリロードできてたので、その方法を試してみます。
`.env`に`CHOKIDAR_USEPOLLING=true`を追加。

再び`docker-compose up`しなおしてみます。


webブラウザの方ではできました～！！！！！！
やった～！
コードを更新すると、リロードしてくれるようになりました✨

iPhoneの方は、ホットリロードしてくれませんね(;´･ω･)
とりあえず、webブラウザでリアルタイムに確認して、iPhoneは時々確認しようと思います！



いちおう`expo update`をしておきました～！


と、いうことで、環境構築は終わりです(*´ω｀)
ありがとうございました～！


↓続き
[card2 id=""]