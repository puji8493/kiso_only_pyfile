#[1]フリガナの文字列の長さが10文字を超える場合、J列に「フリガナが長すぎます」と表示するマクロを作りなさい。
#[2]所属の文字列に「都島」を含むものについて、J列に「都島グループです」と表示するマクロを作りなさい。
import openpyxl
ph = "../5bai/ks014.xlsx"
mod_ph = "../5bai/ks014_mod.xlsx"
wb = openpyxl.load_workbook(ph)
sh = wb["IfThenEndIf"]

#J列ひとことにコメントする戻り値を求める関数
def Hitokoto(syozoku,furigana):
    if syozoku[:2] == "都島" and len(furigana) >= 10:
        coment = "都島グループです フリガナが長すぎます"
    elif syozoku[:2] == "都島":
        coment = "都島グループです"
    elif len(furigana) >= 10:
        coment = "フリガナが長すぎます"
    else:
        coment =""
    return coment

#２行目からシートのデータをリストに格納
ls = []
for row in sh.iter_rows(min_row=2,max_row=11):
    ls.append(row)

#リストの値とインデックス番号を書き出す
for c,v in enumerate(ls):
    #所属はB列　フリガナはD列（インデックス番号3)
    syozoku = v[1].value
    furigana = v[3].value
    ans = Hitokoto(syozoku,furigana)
    print(ans,c)
    sh.cell(row=c+2,column=10).value = ans

wb.save(mod_ph)