'''
行見出し　日付　アイテムa　アイテムb　アイテムc　・・・
日付は、1000マイクロセカンド毎に加算（年・月・日　時間:分:秒.000000マイクロセカンド）
アイテム（数値）を辞書に保存するテストデータを作成
date:{a:num1,b:num2,c:nmu3}
2022-03-01 10:00:00.001000:{'a': 0.18047978517289842, 'b': 0.8172327998831116, 'c': 0.2295418854425827}
2022-03-01 10:00:00.002000:{'a': 0.9177572654721937, 'b': 0.5885041904074017, 'c': 0.8743198975605138}

keyのdate(日付）も含めた1行毎のリストオブジェクトを作成して、csv.dictrederで1行ごとに書き出す.
辞書のアイテムをコピーして、新しい辞書に保存。その辞書に、"date":key(日付）の要素を追加するして、リスト化する
date_type_list {'a': 0.13970528755974732, 'b': 0.5404505113984782, 'c': 0.9911711853050291, 'date': '2022-03-01 10:00:00.001000'}

csvwriter field_names = ("date","a","b","c")
writer.writerows(date_type_list)

csv書き出しの場合　時間 .000 数値　小数点１５桁　16桁以降は0埋め　(辞書のキーは小数点１７桁）
テキストで開くと時間.000000 数値　小数点１５桁
csvから読み出してエクセルに転記　時間　.000000 16桁

'''
import csv
import random
from datetime import datetime,timedelta

dic = {}
categories = ["a","b","c"]
dt = datetime(2022,3,1,10,0,0)

# '日時', datetime.date.today(), '時間',
#     "{}:{}:{}".format(for_write_time.hour, for_write_time.minute, for_write_time.second)]
# https://docs.python.org/ja/3/library/datetime.html#strftime-and-strptime-format-codes

#date:{a:num1,b:num2,c:nmu3}
#%f Microsecond as a decimal number, zero-padded to 6 digits
# dates.append(date.strftime('%Y-%m-%d %H:%M'))

for c in range(0,50):

    # dt = dt + timedelta(seconds=1)
    # dt_str = dt.strftime("%Y/%m/%d %H:%M:%S")

    dt = dt + timedelta(microseconds=1000)
    dt_str = dt.strftime("%Y-%m-%d %H:%M:%S.%f")
    dic_num = {}
    for n,ls in enumerate(categories):
        num = random.random()
        #{a:num1,b:num2,c:nmu3}の要素を作成する辞書
        dic_num.update({ls:num})
    # 辞書（キー）date:要素{a:num1,b:num2,c:nmu3}　の辞書を作成する
    dic[dt_str] = dic_num

for k,v in dic.items():
    print(k,v,sep=":")

date_type_list = []
for key,value in dic.items():
    new_dic = value.copy()
    new_dic["date"] = key
    date_type_list.append(new_dic)
for v in date_type_list:
    print(v)
# {'a': 0.13970528755974732, 'b': 0.5404505113984782, 'c': 0.9911711853050291, 'date': '2022-03-01 10:00:00.001000'}

with open("test_data_microsecond.csv",newline="",mode="w",encoding="utf-8") as f:
    field_names = ("date","a","b","c")
    writer = csv.DictWriter(f,fieldnames=field_names)
    writer.writeheader()
    writer.writerows(date_type_list)
