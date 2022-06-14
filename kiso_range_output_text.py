#range()関数　開始から終了まで整数繰り返し　終了は番号の一つ手前
#listに変換して、テキストへ書き出し保存

import os
from pathlib import Path

output_path = Path("../learning/output_range.txt")

ls = []
with output_path.open(mode="w",encoding="cp932") as f:

    #range(）関数をリストに変換
    ls = list(range(1,10))
    print(ls)
    #実行結果　[1, 2, 3, 4, 5, 6, 7, 8, 9]

    for c in ls:
        #テキストファイルへの書き込み　改行マークは、￥マーク＋n
        f.write(str(c) + "\n")
        #テキストファイルはsrtの型のみ　TypeError: write() argument must be str, not list　と怒られた


'''
    for c in range(1,100):
        ls.append(str(c) + "\n")

    for i in ls:
        f.write(i)
'''