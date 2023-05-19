# Markdown to HTML Converter

## 概要

マークダウンを HTML に変換する Python スクリプト
python-markdown ライブラリーを使用してマークダウンの文字列を HTML の文字列に変換します。
引数の数及び入力が正しいかどうかをチェックするバリデータを記述しており、不適切な入力がされた場合、エラー内容と使用方法を出力しシステムを終了します。
html のファイルが既に存在している場合は、上書きされます。

## 目的

Python でデータストリーム理解する。
シェルから引数を取得する方法（コマンドライン引数）を理解する。
ファイルシステムを操作したファイルの読み書き。

## セットアップ

```shell
pip install -r requirements.txt
```

## 使用方法

```shell
python file_converter.py markdown inputfile outputfile
```

- markdown 実行するコマンド
- inputfile .md ファイルへのパス
- outputfile プログラムを実行した後に作成される.html ファイルのパス

```shell
python file_converter.py markdown sample.md sample.html
```
