#pyファイルを保存しているフォルダから、"kiso"の文字列のテキストファイル名を抜き出す
import os
from pathlib import Path

#カレントディレクトリ内のファイルを表示する os.listdir()
print(os.listdir())

#カレントディレクトリのテキストファイルの最初の文字が"kiso”だったら、リストに格納
lst = [t for t in os.listdir() if t.startswith("kiso")]

#"kiso”のファイル名を書き出すテキストファイルパス
save_ph = Path("../learning/dir_output.txt")

#テキストファイルへ保存 モードは"w"　書き込み 改行するには、"\n"”
with save_ph.open(mode="w") as f:
    for c in lst:
        gyo = c + "\n"
        f.write(gyo)

#再度読み込んでアウトプットしてみる
open_ph =  Path("../learning/dir_output.txt")
with open_ph.open() as f:
    gyo = f.read()
    print(gyo)