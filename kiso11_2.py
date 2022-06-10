#[1]右の表で、「結婚祝い」として合計いくらの金額が発生したかを調べ、その結果をセルD4に、支払い累計額をセルE4に記入するマクロを書きなさい
#[2]左の表セル「B4からB9」までに登場する各項目について、右の表で合計いくらの金額が発生したかを調べ、その結果をセルD4～D9に、支払い累計額をセルE4～E9に記入するマクロを書きなさい
#[3][2]で作ったマクロを改変し、さらに、セルD10、セルE10に各列の合計額を記入するマクロとしなさい
#4月の支出項目を辞書で登録　キーが重複した時は、値を加算する　連想配列で値の累計を出すイメージ

import openpyxl
ph = "../5bai/ks011.xlsx"
mod_ph = "../5bai/ks011_mod_dic.xlsx"
wb = openpyxl.load_workbook(ph)
sh = wb["Sheet1"]

#4月の支出項目を辞書で登録　キーが重複した時は、値を加算する　連想配列で値の累計を出すイメージ
lst_Aplil = {}
for row in sh["I4:J10"]:
    syousai = row[0].value
    #辞書のキーがすでに存在していたら、valueに金額を加算する
    #新規のキーの時は、金額をvalueに代入する
    if lst_Aplil.get(syousai):
        v = lst_Aplil[syousai] + row[1].value
        lst_Aplil[syousai] = v
    else:
        lst_Aplil[syousai] = row[1].value

#今月支払と支払累計の変数をつくり、値を転記した金額の累計を最後に出力する
pay_thismonth = 0
pay_total = 0

#Ｂ列の項目と一致したら、4月支出金額の値をＤ列今月支払額に転記する
for r in sh["B4:E9"]:
    koumoku = r[0].value
    #項目が辞書に存在しない場合は、総計に転記し、総支払額を追加してbreak文でループを抜ける
    #項目じ辞書に存在する場合は、今月支出額に転記し、今月累計額を加算してbreak文でループを抜ける
    for k,v in lst_Aplil.items():
        if koumoku not in lst_Aplil:
            r[3].value = r[1].value
            pay_total = pay_total + r[3].value
            break
        elif k == koumoku:
            r[2].value = v
            r[3].value = r[1].value + r[2].value
            pay_thismonth = pay_thismonth + r[2].value
            pay_total = pay_total + r[3].value
            break

sh["D10"].value = pay_thismonth
sh["E10"].value = pay_total
wb.save(mod_ph)