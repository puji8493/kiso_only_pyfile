'''
webサイト　日経平均プロファイルページ内のウェート上位10銘柄 順位表をサイトから要素を取得し、csv.Dictwriterでcsvに書き出す。
色々なサイトの中の要素をよく観察して、練習する必要があるかと思いました。
注意した点
・行のクラス名が奇数"list-even" 偶数が"list-odd"と分かれているため、
　予め行のクラス名をリスト(class_name_list)に格納し、順々に行のクラス名を関数 create_listの引数に渡す。
・辞書の要素が　偶数（2位・4位・6位・8位・10位)　奇数（1位・3位・5位・7位・9位)の順で保存されるため、
　順位、コード、銘柄など各要素を辞書に保存した後、最後にsorted関数・引数”順位”で昇順に並べ替える。
要素の取り出し
・HTML要素を取得するメソッドをfind系・select系の２つを試しました。
　検索条件の指定方法が異なるポイントを押さえて練習が必要。
 ・webページのリンクはa要素、href属性の値は、get()メソッドで取得する。
 csv.Dictwriterで書き出し
順位で並べ替えたリストを、csv.Dictwriterで書き出し。csvに書き出す列名は、サイトの列順とは違う順序で指定して、書き込みする
{'順位': 1, 'コード': 'XXXX', '銘柄': '〇', 'リンク': 'http://www.XXX', '社名': '（株）□ △', 'セクター': '消費', '日経業種': '〇業', 'ウェート(%)': '10.37'},
順位	ウェート(%)	コード	銘柄	 リンク	           社名	     セクター	日経業種
1    10.37       XXXX   〇   http://www.XXX   （株）□ △    消費         〇業
2     5.37       ・・・・
'''

from bs4 import BeautifulSoup
import requests
from pathlib import Path
import csv

url = "https://indexes.nikkei.co.jp/nkave/archives/summary"
r = requests.get(url)
soup = BeautifulSoup(r.content,"html.parser")

table = soup.find_all(class_="col-xs-12 col-sm-12")
#ヘッダー名をcsvファイル名にする
title = soup.find("div",class_="row m-title dashed-line list-header info-margin").getText()

# 要素名とclassをselectメソッドで指定する場合
# table = soup.select("col-xs-12 col-sm-12")
# title = soup.select("div.row m-title dashed-line list-header info-margin")

midashi = ["順位","コード","銘柄","リンク","社名","セクター","日経業種","ウェート(%)"]
dic = {}
data_list = []

def create_list(class_name):
    """
    :param class_name:
    :return:
    """
    rows = soup.find_all("div", class_=class_name)
    for row in rows:
        row_list = []
        data_dict = {}
        rank = row.find("div",class_="col-xs-12 col-sm-_5 list-text").getText()
        code = row.find("div",class_="col-xs-8 col-sm-1 list-text").getText()
        # aタグの中のURL(href)と銘柄名(meigara)を取り出す
        a_tag = row.find("a")
        a_tag_text = row.find("a").getText()#銘柄　\n 銘柄 \n  スペース　から銘柄を取り出す
        a_tag_text_re = a_tag_text.replace("\n","")
        meigara = a_tag_text_re.replace("          ","")
        href = a_tag.get("href")
        name = row.find("div",class_="col-xs-8 col-sm-5 list-name").getText()
        sector = row.find("div",class_="col-xs-4 col-sm-1_5 list-name").getText()
        gyousyu = row.find("div",class_="col-xs-4 col-sm-1").getText()
        weight = row.findNext("div",class_="col-xs-8 col-sm-1_5 list-weight").getText()
        #順位(int関数に変換）、コード、銘柄名、url、社名、セクター、業種、ウェートをリストに格納
        row_list =[int(rank),code,meigara,href,name,sector,gyousyu,weight]
        #見出名のリストをkey、スクレイピングした値をvalueの１つの辞書をzip関数で作成する
        data_dict = dict(zip(midashi,row_list))
        data_list.append(data_dict)

# 行のクラス名が奇数"list-even" 偶数が"list-odd"と分かれているため、
# 予め行のクラス名をリスト(class_name_list)に格納し、順々に行のクラス名を関数 create_listの引数に渡す。
class_name_list = []
class_name_list =["row list-row-dashed list-odd","row list-row-dashed list-even"]
for class_name in class_name_list:
    create_list(class_name)

#リストに格納したデータは、順位が昇順ではないため、辞書のキー"順位”を昇順でソートする
#lamda式で、任意の関数を各要素に適用して、結果をソートする
score_sorted = sorted(data_list,key=lambda x:x["順位"])
print(score_sorted)

path = Path(__file__).absolute().parent
csv_path = path / f"{title}.csv"

#csv.Dictwiter 2行目以降はwriterowsメソッドでrowオブジェクトのイテラブルの全ての要素を指定する
with csv_path.open(mode="w",encoding="cp932",newline="") as f:
    field_names = ("順位","ウェート(%)","コード","銘柄","リンク","社名","セクター","日経業種")
    writer = csv.DictWriter(f,fieldnames=field_names)
    writer.writeheader()
    writer.writerows(score_sorted)
