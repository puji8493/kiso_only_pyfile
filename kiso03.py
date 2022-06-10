#点数により判定を返す
#関数hanteiで戻り値を返す
import openpyxl

ph = "../learning/ks003_kaito.xlsx"
mod_path = "../learning/ks003_kaito_mod.xlsx"

wb = openpyxl.load_workbook(ph)
sh = wb["Sheet1"]

def Hantei(tokuten):
    if tokuten > 80:
        gouhi = "A判定です"
    elif tokuten > 60:
        gouhi = "B判定です"
    elif tokuten > 40:
        gouhi = "C判定です"
    else:
        gouhi = "D判定です"
    return gouhi

for row in sh.iter_rows(min_row=2,max_row=11):
    tokuten =   row[3].value
    ans = Hantei(tokuten)
    print(ans)
    row[4].value = ans

wb.save(mod_path)