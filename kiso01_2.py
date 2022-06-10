#合計が100点超えたら〇、そうでないなら×を転記
#＃100時間超えたフラグ判定の関数　returneで戻り値を返す
# kiso01_judge.pyのover_time_judge関数を呼び出す工夫をした

import openpyxl
import kiso01_Judge
from openpyxl.styles import Font

wbPath = "../learning/kiso001_kaito.xlsx"
svPath = "../learning/kiso001_kaito_mod_2.xlsx"
wb = openpyxl.load_workbook(wbPath)
ws = wb["Mondai2"]

r_idx = 4
for r in ws["B4:J13"]:#J列へ書き込むため、J列のインデックス番号を取得するため

    # kiso01_judge.pyのover_time_judge関数を呼び出す
    ans = kiso01_Judge.over_time_judge(r[7].value)

    #ws.cell(row=r_idx,column=10).value = ans
    r[8].value =ans
    r[8].font = Font(bold=True,italic=True)
    r_idx = r_idx + 1

wb.save(svPath)