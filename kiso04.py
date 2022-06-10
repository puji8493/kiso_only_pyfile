##100時間残業時間超過の人を要注意リストに格納して、書き出す
import openpyxl
ph = "../learning/ks004.xlsx"
mod_ph = "../learning/ks004_mod.xlsx"
wb = openpyxl.load_workbook(ph)
sh = wb["Sheet1"]

#8行目から１７行目までのＩＤ、名前、合計をリストに格納
lst = []
#データが入力されているセルの最大行は「max_row」最大列は「max_column」で取得
max_row = sh.max_row
print(max_row)

# 範囲指定するセル番地の場合は文字列で変換
for row in sh["A8:C"+str(max_row)]:
    lst.append(row)#リストに格納

attention_lst =[]
#リストを出力し、1行ごとに合計が100時間以上であれば、要注意リストに再格納
for r in lst:
    goukei = r[2].value
    if goukei > 100:
        attention_lst.append(r)
#要注意リストを書き出す
r_idx = 5
for st in attention_lst:
    sh.cell(row=r_idx,column=6).value = st[0].value
    sh.cell(row=r_idx,column=7).value = st[1].value
    sh.cell(row=r_idx,column=8).value = st[2].value
    r_idx = r_idx + 1
wb.save(mod_ph)

