#図表1-1-1 ふだんの食生活で特に力を入れたい食育の内容
#http://www.maff.go.jp/j/syokuiku/wpaper/h28/h28_h/book/other/z1_1_01.csv
#https://docs.python.org/ja/3/library/csv.html

import csv
from pathlib import Path

#読み込み専用のパス
csv_path = Path("../learning/z1_1_01.csv")
print(csv_path.is_file())

#行番号はreader.line_numで先頭に行数を表示
with csv_path.open(encoding="cp932") as f:
    #cCSVファイルの読み込み（入力）にはcsv.readerクラスを使う。
    # 第一引数にopen()で開いたファイルオブジェクト＝fを指定
    reader = csv.reader(f)
    for row in reader:
        # csvreader.line_num ソースイテレータから読んだ行数です。この数は返されるレコードの数とは、レコードが複数行に亘ることがあるので、一致しません。
        if reader.line_num < 3:
            #1,2行目だったら、contineでループの先頭に戻る
            continue
        print(row)
        print(row[0],row[3],sep="☆")

#もう一度csvを読み込んで、3行目以降をリストに格納する
ls = []
with csv_path.open(encoding="cp932") as f:
    reader = csv.reader(f)
    ls = [row for row in reader if reader.line_num >=3]

#書き込み用のパス
write_path = Path("../learning/output_z1.csv")

#　書き込み用のファイル.open (mode="w" ,改行にはnewline=""の引数を加える) as f:
with write_path.open(mode="w",newline="") as f:
    #CSVファイルの書き込み（出力）にはcsv.writerクラスを使う。 第一引数はopen()で開いたファイルオブジェクトfを指定
    writer = csv.writer(f)
    #データの書き込みは、writerow()メソッドを使い、1行ずつ書き込む　引数はリスト
    for c in ls:
        writer.writerow(c)



