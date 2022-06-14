#kiso05　sheets("元データ”）の残業時間（1月から6月、合計）までの行を2次元配列で読み込み
#配列の列ごとの数値をsum（配列）で求めた戻り値をぷプリントで表示する

import numpy
import numpy as np
import openpyxl

#配列のテスト
ls = [1,2,3,4,5,6]
id = [12,17,8,2,11,19]

#配列の初期化　列は6列
arr = np.empty((0,6),int)
#配列に追加する
arr = np.append(arr,np.array([ls]),axis=0)
arr = np.append(arr,np.array([id]),axis=0)
print(sum(arr))

#kiso05　元データ　１～合計までの時間をリストで読み込む
ph = "../learning/ks005_mod.xlsx"
mod_ph = "../learning/ks005_mod_arry.xlsx"
wb = openpyxl.load_workbook(ph)

sh = wb["元データ"]
arr_data = np.empty((0,7),int)

data_list = []
for row in sh["C4:I13"]:
    ls = []
    for r in row:
        ls.append(r.value)
    #１行のリストを [ ] で追加する [[[
    data_list.append([ls])
    #print(data_list)
    #実行結果　[[[40, 28, 40, 30, 30, 28.5, 196.5]], [[40, 39.5, 40, 38.5, 29, 40, 227]]]

#配列　arr_dataに、行で読み込んだリストを追加していく
for i in data_list:
    arr_data = np.append(arr_data,np.array(i),axis=0)

#arr_dataの実行結果
print(arr_data)

#sum8arr_data)の実行結果
print(sum(arr_data))
#[ 281.5  170.   196.   164.   179.5  150.5 1141.5]

print(len(sum(arr_data)))
#7
'''
print(sum(arr_data))の実行結果
[ 281.5  170.   196.   164.   179.5  150.5 1141.5]

print(arr_data)の実行結果
[[ 40.   28.   40.   30.   30.   28.5 196.5]
 [ 40.   39.5  40.   38.5  29.   40.  227. ]
 [ 18.    9.    7.    8.    0.    3.   45. ]
 [ 55.   28.   24.   17.   20.   21.  165. ]
 [ 47.5   2.5  19.   31.5  33.    0.  133.5]
 [  0.    0.    0.    0.    0.    0.    0. ]
 [ 51.   28.   31.   17.   24.5  19.  170.5]
 [  0.    0.    0.    0.    0.    0.    0. ]
 [ 30.    0.    0.   22.   13.    0.   65. ]
 [  0.   35.   35.    0.   30.   39.  139. ]]
'''