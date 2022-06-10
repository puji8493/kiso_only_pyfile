#No.002 - 問題
#[1]昭和生まれ、平成生まれの各受講生について、西暦での生年を求めてG列に記入するマクロを作りなさい。
#[2]男性の場合は80点以上、女性の場合は70点以上を合格とする。H列に、合否の結果を記入するマクロを作りなさい。
import openpyxl
fPath = ("../5bai/ks002.xlsx")
mod_Path = ("../5bai/ks002_mod.xlsx")
wb = openpyxl.load_workbook(fPath)
sh = wb["Sheet1"]

def hantei(gender,tokuten):
    if gender == "男性" and tokuten >= 80:
        gouhi = "合格"
    elif gender == "女性" and tokuten >= 70:
        gouhi = "合格"
    else:
        gouhi =""
    return gouhi

def trans_seireki(gengo,birth_year):
    if gengo == "昭和":
        ad = 1925 + birth_year
    else:
        ad = 1988 + birth_year
    return ad
#iter_rows()メソッドで範囲を指定してループ2行目から11行目　1列目から8列目まで
for row in sh.iter_rows(min_row=2,max_row=11,min_col=1,max_col=8):
    gender = row[2].value
    tokuten = row[3].value
    gouhi_hantei = hantei(gender,tokuten)
    print(gouhi_hantei)
    gengo = row[4].value
    birth_year = row[5].value
    print(gengo,birth_year,sep=";")
    seireki = trans_seireki(gengo,birth_year)
    print(seireki)
    row[6].value = seireki
    row[7].value = gouhi_hantei

wb.save(mod_Path)