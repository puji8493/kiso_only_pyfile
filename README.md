# kiso_only_pyfile
**基礎編ベーシックをopenpyxlで操作したpyfileだけ保存しました**

**公式ドキュメント**  

<sub>[openpyxlの公式ドキュメント](https://openpyxl.readthedocs.io/en/stable/)</sub>  
<sub>[pypiのサイト](https://pypi.org/project/openpyxl/)</sub>  

**pipを使用してopenpyxlをインストール**

(1)pipを使用してopenpyxlをインストール  pipを用いたモジュールのインストールは、コマンドプロンプトで行います。   
コマンドプロンプトに、py -m pip install openpyxlと入力してEnterキーを押す。  
「Successfully installed ・・ openpyxl・・」と表示されてインストール完了。  

(2)プログラムを書く時は、openpyxlモジュールをインポートする。  
```
import openpyxl  
```
**エクセル操作をする時のポイント**  

自分がエクセル操作をするときに、理解すればよいと思ったポイントです。  

(1)エクセルシートの繰返（ループ）処理  
・ワークシートを繰返（ループ）処理すると、全行を”１行ずつループ処理”します。
１行分のセルが()=”タプル”で取得されます。
１行分のリストからセルの値を取得したい時は、リスト同様にfor文でインデックス毎の値を取り出すせます。
```
for row in ws["A1:D10"]:
　→（<cell.A1>,<cell.B1>,<cell.C1>,<cell.D1>)
   （<cell.A2>,<cell.B2>,<cell.C2>,<cell.D2>)
```
１行分のリストからセルの値を取得したい時は、リスト同様にfor文でインデックス事の値を取り出せます。
その時、以下のように変数[インデックス番号]と指定することで、セルのオブジェクトを取得できます。
```
    row[0].value・・・cell.A1  
    row[1].value・・・cell.B1  
    row[2].value・・・cell.C1  
    row[3].value・・・cell.D1
```
(2)１行の中のセルの値を、１つずつリストに追加 
```
 for row in sh["A2:D10"]:＃行の指定をセルの番地で直接指定  
     zangyo_list = []#空のリスト  
     for c in row:
         zangyo_list.appned(c.value)
         print(zangyo_list)
```
printで順々に表示させると以下の通り
```
A列  B列　　	   C列　　　　D列  
1    東京研究所　　松本めぐみ  マツモト メグミ  
(実行結果)    
[1]  
[1, '東京研究所']  
[1, '東京研究所', '松本 めぐみ']  
[1, '東京研究所', '松本 めぐみ', 'マツモト メグミ'] 
```
(3)ワークブックを開く  
openpyxl.load_workbook()関数  
()の引数に、開くファイルパスを指定  
```
wb = openpyxl.load_workbook("パス名")  
```
(4)ワークブックを開く（計算式のあるファイル）  
計算式があるブックを開く場合、データ（文字）を読み込むため、SUM関数なら=SUM("A2:B3")など関数の文字がそのまま読み込まれてしまいます。  
計算式の数値を読み込みたいなら、openpyxl.load_workbook()の（）にdata_onlyというオプションをTrueにすればOKです。  
```
wb = openpyxl.load_workbook(xlsxファイルパス, data_only=True)  
```
(5)ワークシートの指定  
wb変数にシート名を入力。エクセルVBAの経験があれば、シートやセルの指定は何ら問題ないかと思います。  
```
shFm = wb["Sheet1"]
```
