import sys
import os
import markdown

def convertMarkdownToHTML(mdString):
  htmlString = markdown.markdown(mdString, extensions=['tables'])
  htmltemplate = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
{htmlString}
</body>
</html>
'''
  return htmltemplate

# check argument count
def checkArgumentCount(args, targetCount = 4):
  if len(args) != targetCount:
    print(f"エラー: 不適切な引数の数です。正しい引数の数は{targetCount}です。")
    print("使用法: python file_converter.py markdown sample.md sample.html")
    sys.exit(1)

# command check
def checkCommand(command):
  if command != "markdown":
    print(f"エラー：コマンド {command} は存在しません。使用できるコマンドはmarkdownです。")
    print("使用法: python file_converter.py markdown sample.md sample.html")
    sys.exit(1)

# file existance check
def checkFilepathExists(filepath):
  if not os.path.exists(filepath):
    print(f"エラー：ファイル {filepath} は存在しません。正しいファイルパスを指定してください。")
    print("使用法: python file_converter.py markdown sample.md sample.html")
    sys.exit(1)

# file extension check
def checkFileExtension(filepath, targetExtension):
  _, ext = os.path.splitext(filepath)
  if ext != targetExtension:
    print(f"エラー：ファイル {filepath} の拡張子が適切ではありません。使用できる拡張子は{ext}です。")
    print("使用法: python file_converter.py markdown sample.md sample.html")
    sys.exit(1)
  
# ファイルのディレクトリが存在しない場合にディレクトリを作成する
def ensureDirectoryExists(file_path):
  directory = os.path.dirname(file_path)
  if not os.path.exists(directory):
    os.makedirs(directory, exist_ok=True)

def validateFiles(command, inputfilePath, outputfilePath):
  # command check
  checkCommand(command)
  # filepath check
  checkFilepathExists(inputfilePath)
  # fileextension check
  checkFileExtension(inputfilePath, ".md")
  checkFileExtension(outputfilePath, ".html")

def main(args):
  checkArgumentCount(args)
  
  [_, command, inputfilePath, outputfilePath] = args

  validateFiles(command, inputfilePath, outputfilePath)
  
  mdContent = ""
  # read md
  try:
    with open(inputfilePath, "r", encoding="utf-8") as f:
      mdContent = f.read()
  except FileNotFoundError:
      print(f"エラー: ファイル '{inputfilePath}' が見つかりませんでした。")
  except IOError:
      print(f"エラー: ファイル '{inputfilePath}' の読み取り中にエラーが発生しました。")
  except Exception as e:
      print(f"予期せぬエラーが発生しました: {e}")
      
  # write html
  try:
    ensureDirectoryExists(outputfilePath)
    with open(outputfilePath, "w", encoding="utf-8") as f:
      htmlstring = convertMarkdownToHTML(mdContent)
      f.write(htmlstring)
  except FileNotFoundError:
      print(f"エラー: ファイル '{outputfilePath}' のパスに存在しないフォルダが含まれています。")
  except IOError:
      print(f"エラー: ファイル '{outputfilePath}' の書き込み中にエラーが発生しました。")
  except Exception as e:
      print(f"予期せぬエラーが発生しました: {e}")
  
if __name__ == "__main__":
  main(sys.argv)

