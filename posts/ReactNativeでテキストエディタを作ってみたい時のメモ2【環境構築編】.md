>------------<
- タイトル:[【2】React Nativeでテキストエディタを作ってみる！【環境構築編】]
- WordPressにアップロードしますか？:y[x]はいn[]まだしない
- 投稿時:p[]公開d[x]下書き
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
![picture 1](../../images/860e1bbc3dbf9a59713e1f7e7d8601b42059509f40b34e5d69178b32a391054e.png)  
`pywintypes.error: (2, 'CreateFile', '指定されたファイルが見つかりません。')`

↑DockerDesktopを起動していないだけだった

↓またエラー
![picture 2](../../images/6959d88234340008928ce20ff97aab50cffade3dc12756ca005144caa8c0247c.png)  

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

<!-- ↓続き
[card2 id=""] -->