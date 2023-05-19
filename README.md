# Markdown to HTML Converter

## 概要

<p>
  マークダウンを HTML に変換する Python スクリプトです。
  <br>
  python-markdown ライブラリーを使用してマークダウンの文字列を HTML の文字列に変換します。
  <br>
  引数の数及び入力が正しいかどうかをチェックするバリデータを記述しており、不適切な入力がされた場合、エラー内容と使用方法を出力してシステムを終了します。
  <br>
  また、指定したHTMLファイルが既に存在している場合は、上書きされます。
</p>

**変換前**
![sample md - markdown_to_HTML_converter](https://github.com/harutas/Markdown_to_THML_Converter/assets/96802323/e5b8ec8c-f263-4279-9928-349f36be4183)

**変換後**
![sample html - markdown_to_HTML_converter](https://github.com/harutas/Markdown_to_THML_Converter/assets/96802323/fd58dfde-244f-4fa0-b46e-0da7f9c3fc82)

**ブラウザー**
![browser-markdown_to_HTML_converter](https://github.com/harutas/Markdown_to_THML_Converter/assets/96802323/5aaa8383-ebc2-42c6-9b60-5cacd9e1f61a)

**エラー処理**
```
>python file_converter.py markdown
Error!!
エラー: 不適切な引数の数です。正しい引数の数を指定してください。
使用法: python file_converter.py markdown sample.md sample.html

>python file_converter.py Markdown sample.md sample.html
Error!!
エラー：コマンド Markdown は存在しません。使用できるコマンドはmarkdownです。
使用法: python file_converter.py markdown sample.md sample.html

>python file_converter.py markdown sample1.md sample.html
Error!!
エラー：ファイル sample1.md は存在しません。正しいファイルパスを指定してください。
使用法: python file_converter.py markdown sample.md sample.html

>python file_converter.py markdown dummy.html sample.html
Error!!
エラー：ファイルパス dummy.html の拡張子が適切ではありません。
使用法: python file_converter.py markdown sample.md sample.html
```
## 作成目的

- Python でデータストリームを理解する。
- シェルから引数を取得する方法（コマンドライン引数）を理解する。
- ファイルシステムを操作したファイルの読み書き。

## 仕様技術

- Python 3.10.7
- python-markdown 3.4.3

## セットアップ

### 仮想化
```shell
python -m venv .venv
```

```shell
.venv\Scripts\activate.bat
```

### pip install
```shell
pip install -r requirements.txt
```

## 使用方法
```shell
python file_converter.py markdown inputfile outputfile
```

- markdown 実行するコマンド(現在はmarkdownのみ)
- inputfile .md ファイルへのパス
- outputfile プログラムを実行した後に作成される.html ファイルのパス

具体的な使用例
```shell
python file_converter.py markdown sample.md sample.html
```
