#pyファイルを保存しているフォルダから、"kiso"の文字列のテキストファイル名を抜き出す
import os
from pathlib import Path

#カレントディレクトリ内のファイルを表示する os.listdir()
print(os.listdir())

#カレントディレクトリのテキストファイルの最初の文字が"kiso”だったら、リストに格納
lst = [t for t in os.listdir() if t.startswith("kiso")]

#"kiso"から始まるリストだけ書き出されているか
for c in lst:
    print(c)

#"kiso”のファイル名を書き出すテキストファイルパス
save_ph = Path("../learning/dir_output.txt")

#テキストファイルへ保存 モードは"w"　書き込み 改行するには、"\n"”
with save_ph.open(mode="w") as f:
    for c in lst:
        gyo = c + "\n"
        f.write(gyo)
