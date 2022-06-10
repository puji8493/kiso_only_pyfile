#合計が100点超えたら〇、そうでないなら×を転記
#＃100時間超えたフラグ判定の関数　returneで戻り値を返す

import openpyxl
wbPath = "../learning/kiso001_kaito.xlsx"
svPath = "../learning/kiso001_kaito_mod.xlsx"
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