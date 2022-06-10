#[1]シート「mondai1」で、各行につき、「合計」の値が100を超えていたらA列に「○」そうでなければ「×」をつけるマクロを作りなさい
#'シート「mondai1」で、各行につき、「合計」の値が100を超えていたらA列に「○」そうでなければ「×」をつけるマクロを作りなさい
#＃100時間超えたフラグ判定の関数　returneで戻り値を返す

import openpyxl
wbPath = "../5bai/kiso001_kaito.xlsx"
svPath = "../5bai/kiso001_kaito_mod.xlsx"
wb = openpyxl.load_workbook(wbPath)
ws = wb["Mondai1"]

#＃100時間超えたフラグ判定の関数　returneで戻り値を返す
def Hantei(overtime):
    if overtime >= 100:
        ovfer = "〇"
    else:
        over = "×"
    return  over

for r in ws["A2:C11"]:
    ans = Hantei(r[2].value)
    print(ans)
    r[0].value = ans

wb.save(svPath)