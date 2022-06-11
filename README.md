# kiso_only_pyfile
**基礎編ベーシックをopenpyxlで操作したpyfileだけ保存しました**

公式ドキュメント
<sub>[openpyxlの公式ドキュメント](https://openpyxl.readthedocs.io/en/stable/)</sub>

<sub>[pypiのサイト](https://pypi.org/project/openpyxl/)</sub>

**pipを使用してopenpyxlをインストール**

(1)pipを使用してopenpyxlをインストール  pipを用いたモジュールのインストールは、コマンドプロンプトで行う。  
コマンドプロンプトに、py -m pip install openpyxlと入力してEnterキーを押す。  
「Successfully installed ・・ openpyxl・・」と表示されてインストール完了。  

(2)プログラムを書く時は、openpyxlモジュールをインポートする。  
import openpyxl  

**エクセル操作をする時のポイント**

(1)エクセルシートの繰返（ループ）処理  
・ワークシートを繰返（ループ）処理すると、全行を”１行ずつループ処理”します。
１行分のセルは”タプル”で取得される 
```
for row in ws["A1:D10"]:
　→（<cell.A1>,<cell.B1>,<cell.C1>,<cell.D1>)
   （<cell.A2>,<cell.B2>,<cell.C2>,<cell.D2>)
```
 
 ここから１つのセルを取得する場合、for文でインデックス毎の値を取り出せる

　　
 １行の中のセルを取り扱う時は、row[0],row[1],row[3]と変数[インデックス番号]でオブジェクトを取得する
 値を変数に代入したいときは、row[0].valueと操作する

[７]１行の値をリストに格納する時
　ls = []
　for c in row:
      ls.append(c.value)

  1行の中の複数の値を１つのリストで格納したいとき

　for row in sh["B5:C33"]:
  　  zangyo_list.append([row[0].value,row[1].value])
 　　
  list.append([]) []でリストを囲むのをよく忘れるので注意 …自分向けのメモ
  
  以下のように複数の値をリストで保存したい場合は、list.append([a,b]) ()の中に[]を忘れやすい自分は注意
  ['都市名', '数']
　['東京', 38.5]
　['神奈川 ', 17]
　['埼玉', 0]



(3)ワークブックを開く  
openpyxl.load_workbook()関数 （）の引数に、開くファイルパスを指定
wb = openpyxl.load_workbook("パス名")

[４]ワークブックを開く（計算式のあるファイル）
計算式があるブックを開く場合、データ（文字）を読み込むため、SUM関数なら=SUM("A2:B3")など関数の文字がそのまま読み込まれる。
計算式の数値を読み込みたいなら、openpyxl.load_workbook()の（）にdata_onlyというオプションをTrueにする。
wb = openpyxl.load_workbook(xlsxファイルパス, data_only=True)

[５]ワークシートの指定
wb変数にシート名を入力
shFm = wb["Sheet1"]

[８]float型のリストをmax関数で返り値を取得した。(kiso012_1,kiso012_3)


[９]float型で返すnumpyを利用する(kiso012_2)
インストールはコマンドプロンプトでpip install numpy　ＤＬしてから、import numpy
分かりやすい参考リンクhttps://udemy.benesse.co.jp/data-science/ai/python-numpy.html
arry の公式ドキュメント　https://docs.python.org/ja/3/library/array.html
numpyの配列の取り扱い　分かりやすかったリンク　https://python.atelierkobato.com/max/






