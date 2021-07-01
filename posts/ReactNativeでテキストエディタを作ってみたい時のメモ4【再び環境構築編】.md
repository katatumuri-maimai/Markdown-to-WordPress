>------------<
- タイトル:[【4】React Nativeでテキストエディタを作ってみる！【再び環境構築編】]
- WordPressにアップロードしますか？:y[x]はいn[]まだしない
- 投稿時:p[x]公開d[]下書き
- カスタムURL:[React-Native-challenge-to-create-text-editor-4]
- カテゴリID:[3,11,12]
- タグID:[]
- 見出し画像のID:[]
- 識別番号[HqhCf4zbGThO]
>------------<

<!-- ↓続き
[kanren id="575"] -->

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



Windows+DockerDesktopでのReact Native+Expoでは、仕様上ホットリロード効かないことが分かったので、WSLを使って環境構築をしていきます！
（ホストマシンに環境構築しないのは、ただのこだわり。）

[DockerでReact Native環境作成から、Expo Clientで実機確認するまで](https://qiita.com/h-yoshikawa44/items/51b631ec0a6beabdce2d)
↑こちらの方が↓のような記事も書いてくださってるので、参考に環境構築していきます！
[WSLでReact Native + Expo環境を作ろう](https://qiita.com/h-yoshikawa44/items/610ffea888f13275cde8)


## WSLのインストール
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

## Node.jsのインストール
[Windows に WSL を使って Node 環境を構築する](https://qiita.com/nekonekonekosan/items/61a6b9d4da6bdfd1d0bb)
↑こちらを参考にインストールしていきます！

## ReactNative+Expo環境構築
やっとここまできました！
[WSLでReact Native + Expo環境を作ろう](https://qiita.com/h-yoshikawa44/items/610ffea888f13275cde8)



### 疑問メモ
ここでちょっと疑問：VScodeでコード編集できるんだろうか…？
[VSCodeをWSLで使用する設定](https://infltech.com/articles/N0jUEQ)
↑でいけるっぽい。試してみよう。

いけたけど、せっかくつくったリポジトリ…はどうなるのかなｗ

うまくいきました～！
sourcetreeにも作業ディレクトリ登録できたので、いい感じですね。


## 環境変数の設定がよくわからない
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


## Android Studioのインストール
[WSLでReact Native + Expo環境を作ろう](https://qiita.com/h-yoshikawa44/items/610ffea888f13275cde8)
↑こちらを参考にインストールしていきます。

### 環境変数の追加
[Windows10でTempやPathなどの環境変数を設定する方法](https://proengineer.internous.co.jp/content/columnfeature/5205)
[Windowsの環境パスを通す(path)](http://realize.jounin.jp/path.html)
↑こちらを参考に追加していきます。コントロールパネルから行いました。

うまくいかないので、↓。
[[Android] adb コマンドを利用するために PATHを切る、PATHを通す](https://akira-watson.com/android/path-environment.html)

これでいけました！PATHの最後に\が足りなかったみたいですね。


### Android Studioでのシミュレーション
```
Couldn't start project on Android: No Android connected device found, and no emulators could be started automatically.
Please connect a device or create an emulator (https://docs.expo.io/workflow/android-studio-emulator).
Then follow the instructions here to enable USB debugging:
https://developer.android.com/studio/run/device.html#developer-device-options. If you are using Genymotion go to Settings -> ADB, select "Use custom Android SDK tools", and point it at your Android SDK directory.
```

できませんｗｗｗ
なんで？


[WSL2のadbコマンドでWindowsホストのadb-serverに接続する](https://blog.takeyuweb.co.jp/entry/2021/04/17/152724)
↑を参考にやってみます。


[Using the Android emulator on Windows 10 with WSL2](https://pellea.medium.com/using-the-android-emulator-on-windows-10-with-wsl2-39c2bae30c49)
↑を見ながらubuntu用のAndroid SDK / platform-tools をインストール


```
sudo apt install openjdk-8-jdk

wget https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip
unzip sdk-tools-linux-4333796.zip
```
`unzip`がないので入れます。`sudo apt install unzip`

```
unzip sdk-tools-linux-4333796.zip
mv tools android-sdk-tools
cd android-sdk-tools

sdkmanager "system-images;android-28;google_apis_playstore;x86_64" "build-tools;28.0.3" "platforms;android-28" --sdk_root="$ANDROID_SDK_ROOT"
sdkmanager "platform-tools" --sdk_root="$ANDROID_SDK_ROOT"
sdkmanager --licenses
```

`sdkmanager`入ってない😢
[SDKToolsだけでコマンドラインからエミュレータを設定 起動](https://qiita.com/SeijiNishiwaki/items/09ee4f50011ca825610d)
これみたら、Command line toolsだけダウンロードできるらしいので、やってみます。

同じディレクトリで

```
wget https://dl.google.com/android/repository/commandlinetools-win-7302050_latest.zip
unzip commandlinetools-win-7302050_latest.zip
```

`cmdline-tools`が増えました。


なんか使えないｗｗｗ
`sdkmanager: command not found`

解凍からやり直します。ubuntuも再起動したもののできないので、、、。

あ、パスが通ってないだけかもしれない！
[カレントディレクトリのスクリプト実行で「Command not found」と表示される](https://www.itmedia.co.jp/help/tips/linux/l0255.html)
`sdkmanager`の存在するディレクトリで`./`をつけて実行したらできたので、パスの問題ですね。
`bin/`つけてやってみます。

```
cd android-sdk-tools

bin/sdkmanager "system-images;android-28;google_apis_playstore;x86_64" "build-tools;28.0.3" "platforms;android-28" --sdk_root="$ANDROID_SDK_ROOT"
bin/sdkmanager "platform-tools" --sdk_root="$ANDROID_SDK_ROOT"
bin/sdkmanager --licenses

touch ~/.android/repositories.cfg

cd ~/.android/platform-tools
```

むむむ。`bash: cd: /home/mymai/.android/platform-tools: No such file or directory`
たしかにない。

rootに入っていましたｗ

![picture 1](images/234b3811c62e3cdc86f4ffc09e79ab6cc9a4ed0a704f85adf267d454eb662d92.png)  

ファイル移動させますｗ

```
mv build-tools licenses platform-tools tools emulator patcher platforms system-images .android
```

もう一度以下を試します。`abd`使えなかったので`./adb`で
```
cd ~/.android/platform-tools
./adb --version
./adb kill-server
./adb devices

```


できたので、`.profile`に以下を追記

```
# JDK
if [[ -e /usr/lib/jvm/java-8-openjdk-amd64 ]]; then
  export JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"
  export PATH="$PATH:$JAVA_HOME/bin"
fi
# Android tools
if [[ -e $HOME/android-sdk-tools ]]; then
    export PATH="$HOME/android-sdk-tools:$HOME/android-sdk-tools/bin:$PATH"
    export PATH="$HOME/.android/platform-tools:$PATH"
    export ANDROID_HOME="$HOME/.android"
    export ANDROID_SDK_ROOT="$HOME/.android"
    export REPO_OS_OVERRIDE="linux"
    adb kill-server 2> /dev/null
    export ADB_SERVER_SOCKET=tcp:$(cat /etc/resolv.conf | grep nameserver | cut -d' ' -f2):5037
fi
```

ubuntu再起動。

[WSL2でのADBの使用](https://pellea.medium.com/using-adb-with-wsl2-7aebbb070a47)も参考に↓

[start-adb.ps1](https://gist.github.com/pellea/9d1c39bbc561f781d4190f1d1439f653#file-start-adb-ps1)という名前でWindows上に保存する（リンク先にコードあります。）

> $adbPath は "C:\Users\ユーザー名\AppData\Local\Android\Sdk\platform-tools"

あとは、
[【PowerShell】PowerShellを管理者権限で実行したい！ソースの先頭に埋め込むだけで自動で管理者権限に昇格するスクリプト！](https://correct-log.com/powershell_auto_admin/)
↑を参考に、冒頭に以下を追加します。

```
if (!([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole("Administrators")) { Start-Process powershell.exe "-File `"$PSCommandPath`"" -Verb RunAs; exit }
```

`start-adb.ps1`を右クリックして、`PowerShellで実行`を押す。

うーん。いけない。
パソコンごと再起動してみます。

3.Expoサーバを起動し、Expo DevTools（localhost:19002）の「Run on Android device/emulator」を選択すると以下のエラーが出ます。

```
Couldn't start project on Android: adb W 06-30 18:23:15   678   678 network.cpp:149] failed to connect to '172.25.112.1:5037': Connection timed out
* cannot start server on remote host
error: cannot connect to daemon at tcp:172.25.112.1:5037: failed to connect to '172.25.112.1:5037': Connection timed out
```


```
# JDK
if [[ -e /usr/lib/jvm/java-8-openjdk-amd64 ]]; then
  export JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"
  export PATH="$PATH:$JAVA_HOME/bin"
fi
# Android tools
if [[ -e $HOME/android-sdk-tools ]]; then
    export PATH="$HOME/android-sdk-tools:$HOME/android-sdk-tools/bin:$PATH"
    export PATH="$HOME/.android/platform-tools:$PATH"
    export ANDROID_HOME="$HOME/.android"
    export ANDROID_SDK_ROOT="$HOME/.android"
    export REPO_OS_OVERRIDE="linux"
    adb kill-server 2> /dev/null
    export ADB_SERVER_SOCKET=tcp:$(cat /etc/resolv.conf | grep nameserver | cut -d' ' -f2):5037
fi
```
↑これ、`export ADB_SERVER_SOCKET=tcp:$(cat /etc/resolv.conf | grep nameserver | cut -d' ' -f2):5037`だけでいい気が。
`.profile`を編集して`source ~/.profile`

関係なかったし、必要でした。

たぶんだけど、ポートの設定がうまくいっていないらしい。
`source ~/.profile`で`adb kill-server 2> /dev/null`までしか読み込まれていない。

![picture 1](images/c342f227d8f42477e1b509d7c7b233f3ca4bffb5aeb6637f4be0ac0556c970f8.png)  

WindowsとWSLの`adb`んｐバージョンが違うとうまくいかないみたいだけど、同じでした。

`adb -a nodaemon server start`


~~~ためしにWindows側で`adb kill-server`すると`cannot connect to daemon at tcp:5037: cannot connect to 127.0.0.1:5037: 対象のコンピューターによって拒否されたため、接続できませんでした。 (10061)`と出ました。~~~
~~~[「対象のコンピューターによって拒否されたため、接続できませんでした」VisualStudioのclient.Connectのlocalhost 80でエラー出たときの対処法](https://selife5.com/visualstudio-localhost80-error/)~~~
~~~↑を参考に、「Windows Communication Foundation HTTP アクティブ化」「Windows Communication Foundation 非HTTP アクティブ化」にチェックを入れました。~~~

ubuntu再起動。


`adb.exe devices`ならできそう！ということは…


↑の長いの消して、`.bashrc`に以下を追加
```
alias adb='adb.exe'
```

もダメ。

[ADB tool in WSL cannot identify device solution](https://www.programmersought.com/article/30543551648/)
↑より↓
`sudo apt-get update && sudo apt-get install android-tools-adb`

WindowsとWSLのadbが一緒のバージョンじゃないといけないらしいので、
`sudo cp adb /usr/lib/android-sdk/platform-tools/adb -i`で前の方でインストールしていたadbを今インストールしたadbに上書きしました。


`export ADB_SERVER_SOCKET=tcp:$(cat /etc/resolv.conf | grep nameserver | cut -d' ' -f2):5037`を`.profile`に追記




できない＼(^o^)／ｵﾜﾀ


## AndroidデバイスでのUSBデバッグの有効化
[ReactNative-EXPOでAndroidエミュレータでアプリ起動するまでにはまったところ](https://qiita.com/ageage-hamsters/items/c5dd95c9f6dc87dac298)
[AndroidデバイスでのUSBデバッグの有効化](https://www.embarcadero.com/starthere/xe5/mobdevsetup/android/en/enabling_usb_debugging_on_an_android_device.html)
![picture 1](images/dbc1b6541b34fd6e330f3ff7fe7122ca00293238980a8fe76b3db160b241adfa.png)  

![picture 2](images/6715bc6b335fc02f49d3969bcc46fb4d432ae6a3e279ac462227cd852f64d8ee.png)  

![picture 5](images/b6b9608691a535f5b892508259a02b23fec17e76de9080cc38bd8f70f42f7509.png)  

![picture 7](images/604a88db79de4a32dec8f8f003e176f1bece9342dacfa32427d1fb63786761a7.png)  

![picture 6](images/4dc24d4aef1b9031745eed0f7c7444c8f94565f085e7bbab9672e0d8d39c06fe.png)  

![picture 8](images/0c9ce5376d456be4091f78f8339fb3788a567c044cc42adda90f49e91ec1bdcf.png)  


できない！！！



## socatのインストール
[Building a react native app in WSL2](https://gist.github.com/bergmannjg/461958db03c6ae41a66d264ae6504ade)
↑より。`sudo apt-get install socat`

`socat -d -d TCP-LISTEN:5037,reuseaddr,fork TCP:$(cat /etc/resolv.conf | tail -n1 | cut -d " " -f 2):5037`


手順にそって、ファイアウォール設定しなおすとつなげた！
でもエラーが出る😢

```
Couldn't start project on Android: could not connect to TCP port 5554: Connection refused
```


[TCPポートに接続できませんでした：WSL2のAndroidエミュレーターでExpoアプリを開こうとすると接続が拒否されました](https://tech.wayne-chu.com/archives/10527)
↑を見ながらPowerShellで`Set-NetFirewallProfile -DisabledInterfaceAliases "vEthernet (WSL)"`（管理者権限で実行）

```
$WSL_CLIENT = bash.exe -c "ip addr show eth0 | grep -oP '(?<=inets)d+(.d+){3}'";
$WSL_CLIENT -match 'd{1,3}.d{1,3}.d{1,3}.d{1,3}';
$WSL_CLIENT = $matches[0];
iex "netsh interface portproxy add v4tov4 listenport=5554 listenaddress=127.0.0.1 connectport=5554 connectaddress=$WSL_CLIENT"
```

できないのでパソコンごと再起動。





`ip addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'`

```
iex "netsh interface portproxy delete v4tov4 listenport=8081 listenaddress=127.0.0.1" | out-null;
$WSL_CLIENT = bash.exe -c "ip addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'";
$WSL_CLIENT -match '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}';
$WSL_CLIENT = $matches[0];
iex "netsh interface portproxy add v4tov4 listenport=8081 listenaddress=127.0.0.1 connectport=8081 connectaddress=$WSL_CLIENT"
```

androidエミュレーターでの確認は無理でした！！！＼(^o^)／ｵﾜﾀ

もうiPadだけでいいや！
！

[Androidでプロジェクトを開始できませんでした：TCPポート5580に接続できませんでした：127.0.0.1：5580に接続できません：](https://forums.expo.io/t/couldnt-start-project-on-android-could-not-connect-to-tcp-port-5580-cannot-connect-to-127-0-0-1/44593)


`.expo`削除して見ましただめだ！


[[WSL 2] NIC Bridge mode 🖧 (Has TCP Workaround🔨)](https://github.com/microsoft/WSL/issues/4150)
↑よりPowerShellのタスクを使ってみる。

できない


### そもそもLANでExpoに接続できないのが原因では？

[wsl2でsshサーバを起動し、外部からそこに接続](https://qiita.com/yabeenico/items/15532c703974dc40a7f5)
↑よりPowerShellでポートフォワード`netsh.exe interface portproxy add v4tov4 listenaddress=localhost listenport=19000 connectaddress=127.0.1.1 connectport=19000`


できぬ！

[Windows WSL2に外部から直接アクセスするための設定](https://rcmdnk.com/blog/2021/03/01/computer-windows-network/)

これもできないなぁ


```
ipv4 をリッスンする:         ipv4 に接続する:

Address         Port        Address         Port
--------------- ----------  --------------- ----------
0.0.0.0         19000       127.0.0.1       19000
*               19000       192.168.0.19    19000
localhost       19000       127.0.1.1       19000
```

```
iex "netsh interface portproxy add v4tov4 listenport=5554 listenaddress=127.0.0.1 connectport=5554 connectaddress=172.22.185.61"
iex "netsh interface portproxy add v4tov4 listenport=5037 listenaddress=127.0.0.1 connectport=5037 connectaddress=172.22.185.61"
iex "netsh interface portproxy add v4tov4 listenport=5037 listenaddress=127.0.0.1 connectport=5037 connectaddress=172.22.176.1"
```

てかてか、ポートフォワードとかリッスンとかコネクトとか分からないｗ
[ポートフォワード](https://ikatakos.com/pot/software/windows/network/routing)


うーん…
[WSL2 環境で Windows 側の adb.exe を使うといろいろ楽](https://scrapbox.io/hotchpotch/WSL2_%E7%92%B0%E5%A2%83%E3%81%A7_Windows_%E5%81%B4%E3%81%AE_adb.exe_%E3%82%92%E4%BD%BF%E3%81%86%E3%81%A8%E3%81%84%E3%82%8D%E3%81%84%E3%82%8D%E6%A5%BD)
↑これやってみよう

C:\Users\mymai\AppData\Local\Android\Sdk\platform-tools\adb.exe


`/usr/bin`にadbがあったので、削除して`/usr/bin`で↓
`sudo ln -s /mnt/c/Users/mymai/AppData/Local/Android/Sdk/platform-tools/adb.exe adb`

```
cd /usr/lib/android-sdk/platform-tools/
sudo rm adb
```
もしました。

あ、Expo側で`Run on Android device/emulator`選択すると、Expoクライアントをandroidの仮想デバイスにインストールするのははいけました！
めっちゃ簡単だった！

しかし以下のエラーが…

![picture 1](images/ca08a986deb5253a35a1aebe118e64dfe019f40aa25814a9e0f8da1a6719c924.png)  


`192.168.0.19:19000`にLAN接続できないので、しょうがないですね。
`tunnel`にしてみます。

もう一度`Run on Android device/emulator`！！！！
いけた！！！！！！
やった！！！！！！

![picture 2](images/b60903185f855ac13010dbaefc00be0f89d328ed2339879222e7166f45929cca.png)  


長かったｗｗｗ


原因はあまりよくわかりませんが…
おそらくポートの解放問題と、adbの設定の仕方ですね。
Windows側のadbとWSL2側のadbの兼ね合いというか…
WSL2側でadbがうまく使えないので、Windows側のadbを使ったらうまくいったって言う話に落ち着きました。

あとLANがうまく使えないので、tuunelで行けたということですね。

よかったｗ


パソコンごと再起動すると、tuunelが使えなくなりました😢
なんでや…
```
Tunnel URL not found (it might not be ready yet), falling back to LAN URL.
Error starting tunnel protocol fault (couldn't read status): connection reset
```

ポートプロキシの設定いじってたのがダメだったみたい。PowerShellで管理者権限で`netsh int portproxy reset all`したらいけました。


ちなみに、最初のandroidにクライアントをExpoインストールする時は、`LAN`、そのあとの接続は`tunnel`でできます。

![picture 1](images/3f448e8c51b378af9b5d09eccd2d0f3c87cb4c969c0ac18e13a937c2ad0ffb83.png)  

Pixel Xにしてみてもできました！


これで、AndroidStudio、iPhone、iPadでの確認ができるー！
しかも、ホットリロードも効くようになりました(*´ω｀)（Dockerの時より早い）
LANの方がホットリロード速いらしいけど、ちょっとLANはあきらめてもよさそう！

これでやっと環境構築完了です！お疲れ様でした！ここからが本題です(*´ω｀)