#[1]シート「元データ」にある表で残業時間が100時間を超えている人の情報を、シート「要注意リスト」に書きこむマクロを作りなさい

import openpyxl

ph = "../5bai/ks005.xlsx"
mod_ph = "../5bai/ks005_mod.xlsx"
#計算式をCellオブジェクトから取得したい時は、引数　data_only=Trueを追加する
wb = openpyxl.load_workbook(ph,data_only=True)
shFm = wb["元データ"]
shTo = wb["要注意リスト"]

attention_lst = []
#合計が１００時間以上の場合は、要注意リストに格納する
for row in shFm.iter_rows(min_row=4,max_row=13,max_col=9):
    goukei = row[8].value
    if goukei > 100:
        attention_lst.append([row[0].value,row[1].value,row[8].value])
        print(attention_lst)

#要注意リストに格納したリストを転記する 開始行はインデックス9
r_idx = 9　
for lst in attention_lst:
    shTo.cell(row=r_idx,column=3).value = lst[0]
    shTo.cell(row=r_idx,column=4).value = lst[1]
    shTo.cell(row=r_idx,column=5).value = lst[2]
    r_idx = r_idx + 1

wb.save(mod_ph)
