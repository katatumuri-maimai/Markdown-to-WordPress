
ハンズオンでDockerを使用したので、メモを書いていきます(^▽^)/


## Dockerの基本操作
はじめは、Dockerの起動から、コマンドラインでのDockerの操作を学びました。

### お作法！`docker run -d -p 80:80 docker/getting-started`
最初にするお作法。
コマンドの説明をしていただきました。

#### `docker run <指定>`
指定したコマンドを実行する

#### `docker/getting-started`
`docker/getting-started`というイメージを起動。
ない場合はダウンロード
※土台のコンテナの様なもの

#### `-d`
バックグラウンドで。
立ち上がるまでコマンドが打てないのを回避。

#### `-p`
ポート設定
ポートをつなげる
左がHOST、右がコンテナのポート


### 起動しているコンテナの確認`docker container ls`
![picture 22](../images/f9e1d93dbd1cec4246c932f096c5cf17d044ed8ecdb99c2264914e0381032fd4.png)  

### すべてのコンテナの確認`docker container ls -a`
![picture 24](../images/2b0416fe5ea3b07f6ded9c228be9e459a74fdde06e64c611ebb67453762353cf.png)  

`-a`は`all`

### コンテナの停止`docker stop <コンテナID>`
![picture 23](../images/91a5ee37619a83eba7002f154c5232e561af5ac32f642f5294f2defbd63f8aa6.png)  



### メタ情報確認`docker container logs <コンテナID>`
![picture 25](../images/c1ca42c4c17fe6381eebd5f8f5c24aa0092887f358b70e4dadd84eae9ef898df.png)  
Dockerのログが確認できます。

### コンテナの削除`docker rm <ID>`
### すべてのコンテナの削除`docker system prune -a`
`prune`刈り取る
停止中のコンテナがあると、処理スピードは変わらないかもしれないけど、容量を食うので、たまに全消ししたほうが良い
ログの出力がたくさんあったりする。



## その他メモ
情報共有に便利な[HackMD](https://hackmd.io/)
おすすめホラー映画[HOUSE (ハウス)](https://www.amazon.co.jp/HOUSE-%E3%83%8F%E3%82%A6%E3%82%B9-%E6%B1%A0%E4%B8%8A%E5%AD%A3%E5%AE%9F%E5%AD%90/dp/B00FIWA60E)

## 疑問
- お作法！`docker run -d -p 80:80 docker/getting-started`を打ったことがないけどいいのかなぁ
- docker-compose使ってるけど、普通は使うのかなぁ