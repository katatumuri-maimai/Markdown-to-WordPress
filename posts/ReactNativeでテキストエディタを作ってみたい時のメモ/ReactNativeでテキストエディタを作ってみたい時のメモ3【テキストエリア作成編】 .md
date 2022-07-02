>------------<
- タイトル:[【3】React Nativeでテキストエディタを作ってみる！【右往左往編】]
- WordPressにアップロードしますか？:y[x]はいn[]まだしない
- 投稿時:p[x]公開d[]下書き
- カスタムURL:[React-Native-challenge-to-create-text-editor-3]
- カテゴリID:[3,11,12]
- タグID:[]
- 見出し画像のID:[]
- 識別番号[pXqDtjJOlfxE]
>------------<


こんにちは！かたつむり([@Katatumuri_nyan](https://twitter.com/Katatumuri_nyan))です！

Reactを触ってみて、サイト的なものは作れるようになりました(*´ω｀)
そこで、次はReactNativeを触ってみようと思い、簡単なテキストエディタを作成しようと企んでおります(笑)

環境構築があらかた終わったので、早速画面を作成してみたいと思います！



**最初から見る↓**
[kanren id="557"]

**前回を見る↓**
[kanren id="559"]



## いきなりエラーから始まります…
![picture 1](/123927f99a07ed87ca0beb39fefd9a2bbb4bd6e4ac201cd1721440248597feaf.png)  

```
/usr/src/app/node_modules/react-native-web/node_modules/fbjs/lib/ExecutionEnvironment.js
Error: ENOENT: no such file or directory, open '/usr/src/app/node_modules/react-native-web/node_modules/fbjs/lib/ExecutionEnvironment.js'
```

これは前回の記事の最後に`expo upgrade`したせいですね…。
これ、`react-native-web`がインストールされてないってことかなぁ…。
と思い、確認するとありました。
でも
`/usr/src/app/node_modules/react-native-web/node_modules/fbjs/lib/ExecutionEnvironment.js`はないですね…。

![picture 2](/ca86bce1f2c68e86f5281730e93a7c858bec2afd910f8c0fd69c1f0888bca77a.png)  

よく見たら、`expo upgrade`のエラーが残っていました。
内容は同じっぽいですね。


![picture 3](/58bfb70e2700a0384218d1d369e42e45497e76e5ead9e3073fa21e7b2cdc03db.png)  
↑一応コンテナ側で確認するも、確かに`/usr/src/app/node_modules/react-native-web/node_modules/fbjs/lib/ExecutionEnvironment.js`はない…。

`react-native-web`を入れなおしてみます。
`yarn add react-native-web`をしてインストール


![picture 4](/6482375d3d2861c8a0c6ef2a6b7b6dd63cb842b94bbabc7f983f16f7f2765cc6.png)  

```
/usr/src/app/node_modules/react-dom/node_modules/scheduler/index.js
Module build failed: Error: ENOENT: no such file or directory, open '/usr/src/app/node_modules/react-dom/node_modules/scheduler/index.js'
```

次はこれ↑

`yarn upgrade`もしてみたけど、とくに変わらないので、Docker imageからbuildしなおすことにしました。`expo`の初期化はなし。


## Google Chromeデベロッパーツールの拡張
やっと開発できるようになったので、デベロッパーツールでiPhoneとiPadの表示を確認しながらやっていきます。

![picture 5](/e44d709426e4cc366f6bf1c48a3aa46b8960aad491e86e8cea17fc3350746d29.png)  

こんなことができたので( ..)φメモメモ

三点マークを押して、`show device frame`で一部のデバイスのフレームが表示されました。

## 今のディレクトリ構成
![picture 6](/987bb665cb2d7fc203b662742be3172ee268680760ec4e024503d1a935f76662.png)  

`App.js`がおそらくメインの枠になるので、これに合わせてコンポーネントを作っていきます。

## ためしにテキストエリアを作成
そもそも、テキストエリアって、Inputエリアでいいのかな…？

とりあえず、`TextArea.js`を作成し、`App.js`に読み込んでみます。
素材は[公式リファレンス](https://docs.expo.io/versions/v41.0.0/react-native/textinput/)から。

```javascript
// App.js
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import UselessTextInput from './components/TextArea';

export default function App() {
  return (
    <View style={styles.container}>
      <UselessTextInput
      value="Hello World!"
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
```

```javascript
// TextArea.js
import React, { Component } from 'react';
import { TextInput } from 'react-native';

export default function UselessTextInput(props) {
  const [value, onChangeText] = React.useState(props.value);

  return (
    <TextInput
      style={{ height: 40, borderColor: 'gray', borderWidth: 1 }}
      onChangeText={text => onChangeText(text)}
      value={value}
    />
  );
};
```

![picture 7](/747a6f470c61e29af107d38340b8995b15e0689caca62b84333a804fca3e5712.png)  

とりあえず、文字は打てるようになりました(*´ω｀)


## テキストエディタパッケージを使用するも断念
[React Native Editor](https://www.npmjs.com/package/react-native-editor)

`npm i react-native-editor`してみる。
互換性があれば使いたい。

ちょっと使ってみたけど、読み込みが遅すぎるので再起動したらエラー…
`yarn install`しろとのことなので、しておきました。


![picture 8](/f1f8c3446b09f79425c29e8356c5ec12e95a2140f2c3b33445dcd8f524df7b83.png)
```  
/usr/src/app/node_modules/react-native-editor/src/RichToolbar.js  
Module not found: Can't resolve '../img/icon_format_bold.png' in '/usr/src/app/node_musr/src/app/node_modules/react-native-editor/src'
```
`RichToolbar.js `の14行目くらいを以下に変更


```javascript
function getDefaultIcon() {
    const texts = {};
    texts[actions.insertImage] = require('../img/icon_format_media@3x.png');
    texts[actions.setBold] = require('../img/icon_format_bold@3x.png');
    texts[actions.setItalic] = require('../img/icon_format_italic@3x.png');
    texts[actions.insertBulletsList] = require('../img/icon_format_ul@3x.png');
    texts[actions.insertOrderedList] = require('../img/icon_format_ol@3x.png');
    texts[actions.insertLink] = require('../img/icon_format_ol@3x.png');
    return texts;
}
```

![picture 9](/36998eb0ca82a7e607ecb573c18670fb0ec962baa715de7fdac052352af0e358.png)  
```
/usr/src/app/node_modules/react-native-editor/src/RichEditor.js    
react_native_1  
Module not found: Can't resolve 'react-native-webview' in '/usr/src/app/node_modules/react-native-editor/src'
```


次はこれなので、`expo install react-native-webview`してみる
[WebView](https://docs.expo.io/versions/latest/sdk/webview/)

やっぱりうまくいかない😢


`react-native-editor`は一旦やめて、自前で作ることにしました。

`npm rm react-native-editor`


## 試しに画面を作ってみる
[React Nativeで任意のReact コンポーネントを使う方法](https://wawoon.dev/posts/react-native-any-component)
↑この方法でできそう…？
ということで、ちょっと自前で色々作ってみます。

![picture 10](/6363fc04307323a7567cc032200e586fdf24cb0460e1831552a02dc3ed081e3e.png)  

とりあえず、こんな感じです！
コードは以下。


```javascript
// App.js
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import MyTextArea from './components/TextArea';
import MyPreview from './components/Preview';
import MyPanel from './components/Panel';
import './styles/style.css'

export default function App() {
  return (
    <View style={styles.container}>
      <div className="main_wrap">
        <MyPanel
        value="panel"
        />
        <MyTextArea
          placeholder="Hello World!"
          className="textarea_main"
        />
        <MyPreview
          value="ぷれびゅ～"
        />
      </div>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
```


```javascript
// Panel.js
import React, { Component } from 'react';
import { StyleSheet, Text} from 'react-native';

export default function MyPanel(props) {
  // const [value, onChangeText] = React.useState(props.value);

  return (
      <Text style={styles.innerText}>
        {props.value}
      </Text>
      
  );
};

const styles = StyleSheet.create({
  baseText: {
    fontWeight: 'bold'
  },
  innerText: {
    color: 'red'
  }
});
```


```javascript
// TextArea.js
import React, { Component } from 'react';
import { StyleSheet, Text} from 'react-native';

export default function MyPanel(props) {
  // const [value, onChangeText] = React.useState(props.value);

  return (
      <Text style={styles.innerText}>
        {props.value}
      </Text>
      
  );
};

const styles = StyleSheet.create({
  baseText: {
    fontWeight: 'bold'
  },
  innerText: {
    color: 'red'
  }
});
```

StyleSheetの扱いが難しいですが、できそうな気がしてきました。



## ホットリロード問題
作業中に`CHOKIDAR_USEPOLLING=true`でのホットリロードが重すぎて悲しくなってきたので、改善したいと思います。


[docker-expo](https://hub.docker.com/r/kerbe/expo)

↑こちらによると、Docker環境ではホットリロードが効かないと書いています。
（そうだと思ってた）
`Watchman`が必要とのことなので、インストールしてみたいと思います。

### `Watchman`をインストール
[公式ドキュメント](https://facebook.github.io/watchman/docs/install.html)を見つつ、`Watchman`をインストールしていきます。

`yarn`を使っているので`yarn add fb-watchman`でインストール。

`CHOKIDAR_USEPOLLING=true`を削除して、`docker-compose up`しなおします。

[公式ドキュメント](https://facebook.github.io/watchman/docs/install.html)からもインストールの必要ありました。


> $ # use the latest stable release
> $ git clone https://github.com/facebook/watchman.git -b v4.9.0 --depth 1
> $ cd watchman 
> $ ./autogen.sh
> $ ./configure
> $ make
> $ sudo make install

↑こちら真似していきます！

`git`がないので`apk add git`します。

```
git clone https://github.com/facebook/watchman.git
cd watchman
./autogen.sh
```

`python3`がないといわれたので`apk add python3`します。

```
./autogen.sh
```

```
Building Boost.Build engine with toolset ...
Failed to build Boost.Build build engine
Consult 'bootstrap.log' for more details
Command '['/tmp/fbcode_builder_getdeps-ZusrZsrcZappZwatchmanZbuildZfbcode_builder-root/extracted/boost-boost_1_69_0.tar.bz2/boost_1_69_0/bootstrap.sh', '--prefix=/tmp/fbcode_builder_getdeps-ZusrZsrcZappZwatchmanZbuildZfbcode_builder-root/installed/boost-EknnPlrWpvg6lQTh9KAzVMJn6jfCvnM2969L_tvo3dg']' returned non-zero exit status 1.
!! Failed
```

エラー(´;ω;｀)
`react_native\watchman\bootstrap.log`を見つけたので見てみます。

```
###
### Using 'cc' toolset.
###
rm -rf bootstrap
mkdir bootstrap
cc -o bootstrap/jam0 command.c compile.c constants.c debug.c execcmd.c frames.c function.c glob.c hash.c hdrmacro.c headers.c jam.c jambase.c jamgram.c lists.c make.c make1.c object.c option.c output.c parse.c pathsys.c regexp.c rules.c scan.c search.c subst.c timestamp.c variable.c modules.c strings.c filesys.c builtins.c class.c cwd.c native.c md5.c w32_getreg.c modules/set.c modules/path.c modules/regex.c modules/property-set.c modules/sequence.c modules/order.c execunix.c fileunix.c pathunix.c
./build.sh: line 17: cc: not found
```

`cc`がないみたいですね。
[alpinelinux: install failed: cc: Command not found](https://github.com/vlang/v/issues/1760)
↑を参考に、`apk add build-base`します。

もう一度↓
```
./autogen.sh
```

```
Command '['/tmp/fbcode_builder_getdeps-ZusrZsrcZappZwatchmanZbuildZfbcode_builder-root/extracted/boost-boost_1_69_0.tar.bz2/boost_1_69_0/b2', '-j4', '--prefix=/tmp/fbcode_builder_getdeps-ZusrZsrcZappZwatchmanZbuildZfbcode_builder-root/installed/boost-eYmU91RK2GtAWHdVNRfDHnGhe-s7cWgFxzY4yPNB4yo', '--builddir=/tmp/fbcode_builder_getdeps-ZusrZsrcZappZwatchmanZbuildZfbcode_builder-root/build/boost-eYmU91RK2GtAWHdVNRfDHnGhe-s7cWgFxzY4yPNB4yo', '--with-atomic', '--with-chrono', '--with-container', '--with-context', '--with-contract', '--with-coroutine', '--with-date_time', '--with-exception', '--with-fiber', '--with-filesystem', '--with-graph', '--with-graph_parallel', '--with-iostreams', '--with-locale', '--with-log', '--with-math', '--with-mpi', '--with-program_options', '--with-python', '--with-random', '--with-regex', '--with-serialization', '--with-stacktrace', '--with-system', '--with-test', '--with-thread', '--with-timer', '--with-type_erasure', '--with-wave', 'link=static', 'runtime-link=shared', 'variant=release', 'threading=multi', 'debug-symbols=on', 'visibility=global', '-d2', 'install']' returned non-zero exit status 1.
!! Failed
```
(´;ω;｀)
試しに`/tmp/fbcode_builder_getdeps-ZusrZsrcZappZwatchmanZbuildZfbcode_builder-root/extracted/boost-boost_1_69_0.tar.bz2/boost_1_69_0/b2`を打ってみます。

```
Unable to load Boost.Build: could not find "boost-build.jam"
---------------------------------------------------------------
BOOST_ROOT must be set, either in the environment, or
on the command-line with -sBOOST_ROOT=..., to the root
of the boost installation.

Attempted search from /usr/src/app/watchman up to the root
at /tmp/fbcode_builder_getdeps-ZusrZsrcZappZwatchmanZbuildZfbcode_builder-root/extracted/boost-boost_1_69_0.tar.bz2/share/boost-build
and in these directories from BOOST_BUILD_PATH and BOOST_ROOT: /usr/share/boost-build.
Please consult the documentation at 'http://www.boost.org'.
```


ついでにDockerfile変えときました。
```
FROM node:14-alpine

WORKDIR /usr/src/app/

RUN apk update && apk add bash &&\
    apk add git &&\
    apk add python3 &&\
    apk add build-base

RUN yarn global add expo-cli
```

イメージからビルドしなおして、以下を再び行います。
（`watchman`ディレクトリを一度消しました。）

```
git clone https://github.com/facebook/watchman.git -b v4.9.0 --depth 1
cd watchman
./autogen.sh
```

```
your system lacks libtoolize
```
↑の様なエラーが出たので、`libtool`を入れないといけないみたいですね。
`apk add libtool`をDockerfileに追加します。

ビルド後、コンテナを起動しなおして、再び以下を行います。


```
cd watchman
./autogen.sh
```

```
libtoolize:   error: One of these is required:
libtoolize:                 gm4 gnum4 m4
libtoolize:   error: Please install GNU M4, or 'export M4=/path/to/gnu/m4'.
```
`GNU M4`をインストールします！
`apk add m4`これもDockerfileに追加します。

↓やりなおし。
```
git clone https://github.com/facebook/watchman.git -b v4.9.0 --depth 1
cd watchman
./autogen.sh
```

```
./autogen.sh: line 16: aclocal: command not found
```
`aclocal`いれます！
[How to install aclocal in ubuntu14.04](https://stackoverflow.com/questions/35221631/how-to-install-aclocal-in-ubuntu14-04)によると、`automake`を入れたらいいみたいなので、rootに戻って`apk add automake`します。

再び…

```
cd watchman
./autogen.sh
```

```
sh: autom4te: not found
aclocal: error: echo failed with exit status: 127
```
`autom4te`ない！入れます！
[autoconf](https://pkgs.alpinelinux.org/package/edge/main/x86/autoconf)に入ってるみたいですね！
`apk add autoconf`


再び…

```
cd watchman
./autogen.sh
```

```
pkg-config appears to be missing (not available to autoconf tools)
please install the pkg-config package for your system.
```
`pkg-config`ないｗｗｗないもの多すぎん？ｗ
[pkgconfig](https://pkgs.alpinelinux.org/package/v3.4/main/x86/pkgconfig)これっぽい。`apk add pkgconfig`入れてみます。


再び…

```
cd watchman
./autogen.sh
```

何も反応がなく、できたっぽいので次に進みます。

```
./configure
make
make install
```

![picture 11](/25dc0746867d641f0297529d354f60b74499a19529c2f5d3457f70b0319bcb8f.png)  
いけたかな？

```
make
```

```
(CDPATH="${ZSH_VERSION+.}:" && cd . && /bin/sh /usr/src/app/watchman/missing autoheader)
rm -f stamp-h1
touch config.h.in
cd . && /bin/sh ./config.status config.h
config.status: creating config.h
config.status: config.h is unchanged
make  all-am
make[1]: Entering directory '/usr/src/app/watchman'
  CXX      watchman-ChildProcess.o
  CXX      watchman-ContentHash.o
ContentHash.cpp:13:10: fatal error: openssl/sha.h: No such file or directory
   13 | #include <openssl/sha.h>
      |          ^~~~~~~~~~~~~~~
compilation terminated.
make[1]: *** [Makefile:3312: watchman-ContentHash.o] Error 1
make[1]: Leaving directory '/usr/src/app/watchman'
make: *** [Makefile:1264: all] Error 2
```

[watchman builds on Linux require OpenSSL, but isn't clearly stated in the docs](https://github.com/facebook/watchman/issues/529)
↑こちらより`apk add libressl-dev`

再度以下を行います！


```
cd watchman
make
```

```
fstype.cpp:18:10: fatal error: linux/magic.h: No such file or directory
   18 | #include <linux/magic.h>
      |          ^~~~~~~~~~~~~~~
compilation terminated.
make[1]: *** [Makefile:3522: watchman-fstype.o] Error 1
make[1]: Leaving directory '/usr/src/app/watchman'
make: *** [Makefile:1264: all] Error 2
```

`linux/magic.h`ないいい！
[fstype.c:18:25: error: linux/magic.h: No such file or directory make[1]: *** [watchman-fstype.o]](https://github.com/facebook/watchman/issues/95)
`kernel-headers`を入れるといいらしい。
[linux-headers](https://pkgs.alpinelinux.org/package/edge/main/x86/linux-headers)ぽいので入れます。`apk add linux-headers`


再度以下を行います！

```
cd watchman
make
```


```
scm/Mercurial.cpp: In constructor 'watchman::Mercurial::infoCache::infoCache(std::string)':
scm/Mercurial.cpp:16:40: error: 'void* memset(void*, int, size_t)' clearing an object of non-trivial type 'struct watchman::FileInformation'; use assignment or value-initialization instead [-Werror=class-memaccess]
   16 |   memset(&dirstate, 0, sizeof(dirstate));
      |                                        ^
In file included from scm/Mercurial.h:10,
                 from scm/Mercurial.cpp:3:
./FileInformation.h:18:8: note: 'struct watchman::FileInformation' declared here
   18 | struct FileInformation {
      |        ^~~~~~~~~~~~~~~
cc1plus: all warnings being treated as errors
make[1]: *** [Makefile:4446: scm/watchman-Mercurial.o] Error 1
make[1]: Leaving directory '/usr/src/app/watchman'
make: *** [Makefile:1264: all] Error 2
```

!?
[v4.9.0 compile failure on Debian unstable](https://github.com/facebook/watchman/issues/638)
↑を参考に`./configure --enable-lenient`してみる。

再度以下

```
make
make install
```

```
gcc -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -Os -fomit-frame-pointer -g -Os -fomit-frame-pointer -g -Os -fomit-frame-pointer -g -DTHREAD_STACK_SIZE=0x100000 -fPIC -I/usr/include/python3.8 -c pywatchman/bser.c -o build/temp.linux-x86_64-3.8/pywatchman/bser.o
pywatchman/bser.c:31:10: fatal error: Python.h: No such file or directory
   31 | #include <Python.h>
      |          ^~~~~~~~~~
compilation terminated.
error: command 'gcc' failed with exit status 1
make[1]: *** [Makefile:5596: py-build] Error 1
make[1]: Leaving directory '/usr/src/app/watchman'
make: *** [Makefile:1264: all] Error 2
```

`./configure --without-python --enable-lenient`してみます！


再度以下

```
make
```
できたっぽいので↓します！
```
make install
```

```
make[1]: Entering directory '/usr/src/app/watchman'
 ./install-sh -c -d '//usr/local/bin'
  /bin/sh ./libtool   --mode=install /usr/bin/install -c watchman '//usr/local/bin'
libtool: install: /usr/bin/install -c watchman //usr/local/bin/watchman
/usr/bin/install -c -d -m 777 //usr/local/var/run/watchman
chmod g+s //usr/local/var/run/watchman
touch //usr/local/var/run/watchman/.not-empty
 ./install-sh -c -d '//usr/local/share/doc/watchman-4.9.0'
 /usr/bin/install -c -m 644 README.markdown '//usr/local/share/doc/watchman-4.9.0'
make[1]: Leaving directory '/usr/src/app/watchman'
```
できたのかな…？

`watchman`ってrootで打ってみた。
```
{
    "cli_validated": true,
    "version": "4.9.0",
    "error": "invalid command (expected an array with some elements!)"
}
```
イケてるっぽい

`.gitignore`に`watchman`を追加しました。



### windowsへ`docker-windows-volume-watcher`を導入
[GAE/GOなdockerを作ろうとしたら１０時間溶けた](https://msitter29.hatenablog.com/entry/2018/05/10/200644)
↑を参考にしました。

windowsのコマンドプロンプトで
```
pip install --upgrade pip
pip install docker-windows-volume-watcher
docker-volume-watcher
```



```
PS D:\ok\プログラミング学習\React-TextEditer> docker-volume-watcher
WARNING:root:Bind of container react-textediter_react_native_1 was skipped since it has invalid source path D:\ok\プログラミング学習\React-TextEditer\react_native
WARNING:root:No mounts match container name pattern * and host directory pattern *
```

ちーん(´;ω;｀)

[WARNING:root:Bind of container was skipped since it has invalid source path](https://github.com/merofeev/docker-windows-volume-watcher/issues/19)

dockerDesktopのせいなのかな…


rootの名前を`React-TextEditer`から`React_TextEditer`に変更


ドッカ―イメージからビルドしなおします。


```
docker-volume-watcher
```

だめでしたー！
名前の問題ではないみたい。

ってか、日本語PATHがダメなのではなかろうか…
と思って`プログラミング学習`を英語に変えたけどダメでした。
こまったな～！

```
pip uninstall docker-windows-volume-watcher
```



[zippoxer/docker-windows-volume-watcher](https://github.com/zippoxer/docker-windows-volume-watcher)
↑こっちも使ってみたいけど、インストールの仕方が分からず💦




## `kerbe/expo`でコンテナ作成・実機確認
[kerbe/expo](https://hub.docker.com/r/kerbe/expo)

こちらを使っていきたいと思います！

[kerbe/docker-expo](https://github.com/kerbe/docker-expo/blob/master/Dockerfile)を参考にDockerfileとdocker-compose.ymlを編集

```yml
FROM kerbe/expo

WORKDIR /usr/src/app
```

```
version: "3"
services:
  react_native:
    build: ./docker/react_native
    volumes:
      - ./react_native:/usr/src/app
    env_file: .env

    command: start

    ports:
      - "19000:19000"
      - "19001:19001"
      - "19002:19002"
      - "19006:19006"
```

`react_native`ディレクトリを削除して、以下を実行しました。
```
docker-compose build
docker-compose run --rm react_native init .
```

templateを`blanck`と入力。
終わったら、`docker-compose up`します。

よくわからなかったので、ファイルの編集とコマンドの編集を何度もチャレンジしましたｗ

成功！
とりあえず、実機確認までできました。

## ホットリロードができるか問題
`CHOKIDAR_USEPOLLING=true`を設定しているので、webブラウザでは一応リロードしてくれます。
iPhoneではホットリロードが効いていません。
[merofeev/docker-windows-volume-watcher](https://github.com/merofeev/docker-windows-volume-watcher)
これが使えないので、
[zippoxer/docker-windows-volume-watcher](https://github.com/zippoxer/docker-windows-volume-watcher)
こっちを使ってみることにしました。

### goをインストール

[WindowsにGo言語開発環境をインストールする](https://qiita.com/suke_masa/items/0c45c92934b9a2807ddb)
↑こちらの手順にしたがって、Goをインストールしました。


[How can I install a package with go get?](https://stackoverflow.com/questions/30295146/how-can-i-install-a-package-with-go-get)
↑　`go get`したらいけるっぽい
Windowsのコマンドプロンプトから、`go get github.com/zippoxer/docker-windows-volume-watcher`をします。

```
go get: github.com/zippoxer/docker-windows-volume-watcher@none updating to
        github.com/zippoxer/docker-windows-volume-watcher@v0.0.0-20190226212435-676f3ba5696c: parsing go.mod:
        module declares its path as: github.com/FrodeHus/docker-windows-volume-watcher
                but was required as: github.com/zippoxer/docker-windows-volume-watcher
```
とのことなので、`go get github.com/FrodeHus/docker-windows-volume-watcher`してみます。

```
docker-windows-volume-watcher -container=[react_textediter_react_native_1]
```
↑をWindowsのコマンドプロンプトから作業ディレクトリに移動してうってみると、いけてる感じがします！

試しにファイルを変更してみると…↓
```
Updating container file react_native/App.js
Error notifying container about file change: exit status 1
Updating container file react_native/.expo/web/cache/development/babel-loader/7c5042ec877f84a9db21a9f6f73ac149.json
Error notifying container about file change: exit status 1
```

もうだめだ！＼(^o^)／ｵﾜﾀ


ホットリロードは諦めます。

そもそもDocker使わない方がいい気しかしないので、明日は違う方法検討しよう！




時間かかるので辞めましたｗ


↓続き
[kanren id="572"]