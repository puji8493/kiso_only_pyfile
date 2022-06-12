#pyファイルの内、kisoの文字列のファイル名だけを格納したリストを作り、csvファイルに保存する
#ファイル全般操作はpathlib
#改行するためには、リストの文字列に ".\n"　を追加するのがポイント

import os
from pathlib import Path

#書き出して保存するファイルパス
output_path = Path("../learning/kiso_output_3.txt")

#カレントディレクトリのうち、"kiso"の文字列のファイル名だけ抜き出して、リストに格納
#1行毎に t + "\n"の改行マークを入れる

ls = [t + "\n" for t in os.listdir() if "kiso" in t]
for c in ls:
    print(c)

#CSVファイルの書き込み　mode="w" 改行はnewline
with output_path.open(mode="w") as f:
    for i in ls:
        f.write(i)


'''
ls = []
for c in os.listdir():
    if "kiso" in c:
        gyo = c + "\n"
        ls.append(gyo)

'''
