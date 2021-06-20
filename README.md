# MarkdownからWordpressへ自動投稿
Markdown記法で書いた記事をPushすると、自動でワードプレスに投稿される機能を作っています。
今は開発段階です。

## 現在利用できる機能
- Markdown形式のファイルをHTMLへ変換
- `posts`フォルダに`.md`ファイルを入れてpushすると自動的にワードプレスへ投稿（更新したファイルだけ）
- Gutenbergのcodeブロックへの変換（プラグインcodemirror-blocksのブロックになります）
- 一部のcodemirror-blocksのブロックは言語指定可能


## Futures
- 既存の`.md`ファイルが更新されたとき、自動時にワードプレスの既存記事へ反映
（今は更新された記事は新規投稿になります。）
