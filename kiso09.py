#苗字と名前の間の文字列で分割して書き出す　split()メソッド
import openpyxl
ph = "../learning/ks009.xlsx"
mod_ph = "../learning/ks009_mod2.xlsx"
wb = openpyxl.load_workbook(ph)
sh1 = wb["問題１"]
sh2 = wb["問題２"]
sh3 = wb["問題３"]

#苗字と名前を split()メソッド　引数"/"で分割したリストを作り、C/D列に書き出し　
for row in sh1.iter_rows(min_row=2,max_row=11):
    namae = row[1].value
    sp_list = []
    sp_list = namae.split("/")
    print(sp_list[0],sp_list[1],sep=":")
    row[2].value = sp_list[0]
    row[3].value = sp_list[1]

#苗字と名前を split()メソッド　引数" "で分割したリストを作り、C/D列に書き出し　
for row in sh2.iter_rows(min_row=2,max_row=11):
    namae = row[1].value
    sp_list = []
    sp_list = namae.split(" ")
    print(sp_list[0],sp_list[1],sep=":")
    row[2].value = sp_list[0]
    row[3].value = sp_list[1]

#苗字と名前を split()メソッド　引数"/" " " で分割したリストを作り、C/D列に書き出し　
for row in sh3.iter_rows(min_row=2,max_row=11):
    namae = row[1].value
    sp_list = []
    if "/" in namae:
        st = "/"
    else:
        st = " "
    sp_list = namae.split(st)
    row[2].value = sp_list[0]
    row[3].value = sp_list[1]

wb.save(mod_ph)
