#D列に記載された得点が80点以上だったら「A判定です」60点以上だったら「B判定です」40点以上だったら「C判定です」
#それより下だったら「D判定です」と記載するマクロを作りなさい。
#関数hanteiで戻り値を返す
import openpyxl

ph = "../5bai/ks003_kaito.xlsx"
mod_path = "../5bai/ks003_kaito_mod.xlsx"

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