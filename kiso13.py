#キャンペーン名簿表を元に、転記リストと一致したものを書き出す
#キャンペーン応募状況のIDは一意＝重複しないので、辞書でkey=ID value=キャンペーンタイプの値を取得する
import openpyxl
ph = "../learning/ks013.xlsx"
mod_ph = "../learning/ks013_mod.xlsx"
wb = openpyxl.load_workbook(ph)
sh = wb["キャンペーン名簿"]

#キャンペン応募状況の辞書を作る　key=ID value=キャンペンタイプ
dic = {}
for row in sh["E11:F22"]:
    ind = row[0].value
    dic[ind] = row[1].value

#Ａ列のＩＤと、キャンペン応募状況の辞書のkey(ID)が一致したらＣ列に書き出す
#辞書の値と一致、セルへ書き出したらbreak文でfor文を抜ける
for r in sh["A4:C29"]:
    idx = r[0].value
    for k,v in dic.items():
        if idx == k:
            print(k,v)
            r[2].value = v
            break

wb.save(mod_ph)