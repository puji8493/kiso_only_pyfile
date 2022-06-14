#キャンペーン応募状況を配列に読み込み、顧客リストのIDと一致したら、Ｃ列にキャンペーンタイプを書き出す
#　numpy をインポート
#https://numpy.org/doc/stable/reference/generated/numpy.append.html
# numpyで空配列の末尾に行を追加して2次元配列を作る https://qiita.com/fist0/items/d0779ff861356dafaf95
# numpyの配列で読み込んだキャンペーンIDの型は、<class 'numpy.str_'> だったので、顧客リストのIDをstr関数にした それでいいのか不明

import numpy as np
import openpyxl

ph = "../learning/ks013.xlsx"
mod_ph = "../learning/ks013_arry_mach.xlsx"
wb = openpyxl.load_workbook(ph)
sh = wb["キャンペーン名簿"]

#顧客リスト（ID）のリスト
id_list = []
for i in sh["A4:A29"]:
    id_list.append(i[0].value)
#print(id_list)

#配列　arr  を初期化　分かりやすいようにＧ列に任意の文字列を追加　列方向３列の配列にする
#追加する配列の要素数は初期化した行の長さ(今回は3)と一致させる
arr = np.empty((0,3),int)

for row in sh["E11:G22"]:
    #１行のセルの集まりは、Tuple
    ##1行毎のタプルの要素をセルの値row[インデックス番号].valueの値でlsというリストに追加
    ls = []
    ls.append([row[0].value, row[1].value, row[2].value])
    #print(ls)
    # 実行結果　
    #[[12, 'かんぴょう巻き無料', 'test']]
    #[[17, 'しそ巻き無料', 'aaa']]
    #・・・[[13, '飲みもの無料', 'kkk']]

    #配列 arry に格納　np.append
    #第一引数に元の配列ndarray、第二引数に追加する要素を指定する。元の配列はそのままで、新たな配列が返される。
    #axisは軸　次元を保ったまま配列を追加するには引数axisを指定する。
    # axis=0で新たな行として追加（縦に連結）、axis=1で新たな列として追加（横に連結）される。存在しない次元（軸）を指定するとエラー。

    arr = np.append(arr,np.array(ls),axis=0)

for row in range(len(arr)):
    print(type(arr[row][0]))
    for c,v in enumerate(id_list):
        if str(v) == arr[row][0]:
            sh.cell(row=c+4,column=3).value = arr[row][1]
            break

wb.save(mod_ph)


print(arr[11,2])
print(len(arr))
print(len(arr[10]))

