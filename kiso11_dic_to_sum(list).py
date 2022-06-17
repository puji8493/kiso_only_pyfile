# 辞書型（dictionary）の値をvaluesでリスト型にして、まとめて取り出す sum(list名)ことが目標
# enumerate関数のリストの値 = class List、 リスト[0(添え字] = str
# 辞書のvalueを比較する場合、同じstr型出ないと一致しない　よって、リスト[0]（添え字）と辞書の値を比較する
#辞書のアイテムをsum関数で足せる　実行結果　33,100 でOK sh.cell(row=10,column=4).value = sum(dic_spend.values())

import openpyxl
ph = "../learning/ks011.xlsx"
mod_ph = "../learning/ks011_mod06.xlsx"
wb = openpyxl.load_workbook(ph)
sh = wb["Sheet1"]

dic_spend = {}
spend_list = []
for row in sh["I4:J10"]:
    row_list = []
    for r in row:
        row_list.append(r.value)
    spend_list.append(row_list)

#print(spend_list)
#実行結果　[['結婚祝い', 10000], ['お見舞い袋', 100], ['出産祝い', 5000], ['結婚祝い', 5000], ['御霊前', 5000], ['お見舞い', 3000], ['出産祝い', 5000]]

#dicのキーが存在しない場合　if key not in dic.keys() 他にdic.get(key)
#dicの値を取り出すのは　dic[key]
v = 0
for c in spend_list:
    spend_koumoku = c[0]
    #辞書のキーが存在しない場合は、キーを追加
    if spend_koumoku not in dic_spend.keys():
        dic_spend[spend_koumoku] = c[1]
    else:
        #辞書のキーが存在する場合は、アイテムを加算
        dic_spend[spend_koumoku] = dic_spend[spend_koumoku] + c[1]

for c,v in dic_spend.items():
    print(c,v)
#実行結果　結婚祝い 15000　お見舞い袋 100　出産祝い 10000　御霊前 5000　お見舞い 3000

# 辞書型（dictionary）の値をvaluesでリスト型にして、まとめて取り出す sum(list名)
dic_val = dic_spend.values()
#辞書のアイテムをsum関数で足せる　実行結果　33,100 でOK
print(sum(dic_val))

#D,E列に書き出し まずはリストに格納
r_list =[]
for row in sh["B4:B9"]:
    ls =[]
    for r in row:
        ls.append(r.value)
    r_list.append(ls)

#今月支払額に転記
# リストの値 = class List リスト[0] = str
# 辞書のvalueを比較する場合、同じstr型出ないと一致しない　よって、リスト[0]（添え字）と辞書の値を比較する
for cnt,val in enumerate(r_list):
    print(type(val),type(val[0]),sep="*")
    koumoku = val[0]
    for c,v in dic_spend.items():
        print(type(c),type(koumoku),sep="☆")
        if koumoku == c:
            sh.cell(row=4+cnt,column=4).value = v
            print(v,"v",sep=":")

# 辞書型（dictionary）の値をvaluesでリスト型にして、まとめて取り出す sum(list名)
#dic_val = dic_spend.values()
#辞書のアイテムをsum関数で足せる　実行結果　33,100 でOK
sh.cell(row=10,column=4).value = sum(dic_spend.values())


wb.save(mod_ph)