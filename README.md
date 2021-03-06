# kiso_only_pyfile
**基礎編ベーシックをopenpyxlで操作したpyfileだけ保存しました**

**公式ドキュメント**  

<sub>[openpyxlの公式ドキュメント](https://openpyxl.readthedocs.io/en/stable/)</sub>  
<sub>[pypiのサイト](https://pypi.org/project/openpyxl/)</sub>  

**pipを使用してopenpyxlをインストール**

(1)windowの場合  
pipを使用してopenpyxlをインストール  pipを用いたモジュールのインストールは、コマンドプロンプトで行います。   
コマンドプロンプトに、py -m pip install openpyxlと入力してEnterキーを押す。  
「Successfully installed ・・ openpyxl・・」と表示されてインストール完了。  

Macの場合　インストールの説明のリンクのご参考です  
(https://aiacademy.jp/media/?p=2905)

(2)プログラムを書く時は、openpyxlモジュールをインポートする。  
```
import openpyxl  
```
**エクセル操作をする時のポイント**  

データ構造 (https://docs.python.org/ja/3/tutorial/datastructures.html#)  

自分がエクセル操作をするときに、理解すればよいと思ったポイントです。  

(1)エクセルシートの繰返（ループ）処理  
ワークシートを繰返（ループ）処理すると、全行を”１行ずつループ処理”します。  
１行分のセルが()=”タプル”で取得されます。  
１行分のリストからセルの値を取得したい時は、リスト同様にfor文でインデックス毎の値を取り出せます。  
```
for row in ws["A1:D10"]:
　→（<cell.A1>,<cell.B1>,<cell.C1>,<cell.D1>)
   （<cell.A2>,<cell.B2>,<cell.C2>,<cell.D2>)
```
以下のように変数[インデックス番号]と指定することで、セルの値を取得したり、セルに値を書き込みできます。
```
    row[0].value・・・cell.A1  
    row[1].value・・・cell.B1  
    row[2].value・・・cell.C1  
    row[3].value・・・cell.D1
```
(2)１行の中のセルの値を、１つずつリストに追加 
```
 for row in sh["A2:D10"]:＃行の指定をセルの番地で直接指定  
     id_list = []#空のリスト  
     for c in row:
         id_list.appned(c.value)
         print(id_list)
```
printの実行結果は以下の通り(インデントを1段あげないでfor文の中でprintを繰り返す)　　
```

A列  B列　　	   C列　　　　D列  
1    東京研究所　　松本めぐみ  マツモト メグミ  
(実行結果)    
[1]  
[1, '東京研究所']  
[1, '東京研究所', '松本 めぐみ']  
[1, '東京研究所', '松本 めぐみ', 'マツモト メグミ'] 
```
(3)残業時間100時間以上を警告するフラグ(〇をつける）とき、リストの判定と書き出し
```
 A       B           C  
警告信号 名前         合計  
      	米子 美和    227.0  
	呉 早希	    65.0  
	五日市 加奈子 139.0  
	静岡 威宏    133.5  
```
リストに保存する　row(1行分）をさらにfor文でまわして、ループをぬけたときの実行結果  
```
lst_total = []#1行ごとの名前、残業時間のセルの値を入れる変数　最初に空リストをつくっておく
for row in ws["B2:C11"]:
    lst = []#行を入れる空リスト
    for r in row:
        lst.append(r.value)
    lst_total.append(lst)
    # インデントを一段あげてlst_totalのリストに変数lstの要素を追加  
    # リストの要素0 ['米子 美和', 227] リストの要素１ ['呉 早希', 65]と保存されている
```
名前、合計をセットにしたリストをfor文で調査、関数 def Hantei（引数：合計時間）を渡し、判定結果の戻り値をもらう  
書き出す行をcntのカウンターでカウントアップしているが、インデックス番号と値を取り出すenumerate関数もある。  
```
for c,v in enumerate(lst_total): と入力すると、c インデックス番号、v　リストの値がとれる  
enumerate関数で行番号を指定する場合は、sh.cell(row=c+2,column=5).value = ans　R1C1で記述するといいと思う。

cnt = 2
for c in lst_total:
    ans = Hantei(c[1])#合計時間を判定する関数の戻り値を変数ansにいれる
    print(ans,c[0],c[1],sep=":")#引数　リスト[要素の番号]
    ws["A"+ str(cnt)].value = ans#セルの番地は文字列str関数で文字列に変換
    cnt = cnt + 1

printの実行結果  
〇:米子 美和:227  
×:呉 早希:65  
〇:五日市 加奈子:139  
〇:静岡 威宏:133.5  
```
関数はリスト保存より上に書くこと  
```
def Hantei(overtime):
    if overtime >= 100:
        over = "〇"
    else:
        over = "×"
    return over
```

以下のようにリストに保存するとセルが保存されている  
```
rowの実行結果　(<Cell 'Mondai1'.B2>, <Cell 'Mondai1'.C2>)(<Cell 'Mondai1'.B3>, <Cell 'Mondai1'.C3>)  
ls = []
for row in ws["B2:C11"]:
    ls.append(row)
    #print(row)
```

(4)リスト内包表記  
ループ処理を１行に繋げて書くことができます。  

全員の残業リストから、100時間以上の人を要注意リストに格納するとき、100時間以上の残業対象者をリスト内包表記でリストに格納する    
```
[仮変数を用いた式 for 仮変数 in イテラブルオブジェクト（反復可能なオブジェクト）if 条件式]  

リスト内包表記  
a_list = [t for t in zangyo_list if t[2]>=100]
#print(a_list)

あとは、a_listに入れた要注意リストを書き出せばOK
for c,v in enumerate(a_list):
    #要注意リストの要素を書き出す　v[0]=ID　v[1]=名前 v[2]=合計  
    sh.cell(row=5+c,column=6).value = v[0]
    sh.cell(row=5+c,column=7).value = v[1]
    sh.cell(row=5+c,column=8).value = v[2]

for 文で書く場合は、まずa_listを以下のように保存する
a_list = []
for c in zangyo_list:
    if c[2] >= 100:
        a_list.append(c)

for i in a_list:
    print(i)
```
(5)ワークブックを開く  
openpyxl.load_workbook()関数  
()の引数に、開くファイルパスを指定  
```
wb = openpyxl.load_workbook("パス名")  
```
(6)ワークブックを開く（計算式のあるファイル）  
計算式があるブックを開く場合、データ（文字）を読み込むため、SUM関数なら=SUM("A2:B3")など関数の文字がそのまま読み込まれてしまいます。  
計算式の数値を読み込みたいなら、openpyxl.load_workbook()の（）にdata_onlyというオプションをTrueにすればOKです。  
```
wb = openpyxl.load_workbook(xlsxファイルパス, data_only=True)  
```
(7)ワークシートの指定  
wb変数にシート名を入力。エクセルVBAの経験があれば、シートやセルの指定は何ら問題ないかと思います。  
```
shFm = wb["Sheet1"]
```
以下の練習は完了  
if_else  
def  
for  
iter_rows  
enumerate  
リスト内包表記  
split  
in   
辞書  
辞書get()メソッド  
辞書のitems()メソッドでキーと値の両方を取り出す  
max関数  
numpy  
np.namax  
os.getcwd  
os.listdir()  
Path関数  
textへの書き込みopenメソッド  
