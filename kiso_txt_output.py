#pyファイルの内、kisoの文字列のファイル名だけを格納したリストを作り、txtファイルに保存する
#ファイル全般操作はpathlib
#改行するためには、リストの文字列に ".\n"　を追加するのがポイント

import os
from pathlib import Path

#書き出して保存するファイルパス
output_path = Path("../learning/kiso_output.txt")

#カレントディレクトリのうち、"kiso"の文字列のファイル名だけ抜き出して、リストに格納
ls = []
for c in os.listdir():
    if "kiso" in c:
        gyo = c + ".\n"
        ls.append(gyo)

for c in ls:
    print(c)

#CSVファイルの書き込み　mode="w" 改行はnewline
with output_path.open(mode="w") as f:
    for i in ls:
        f.write(i)
