#テキストファイル open()メソッド as キーワード　変数 f
#ファイルを開く時は、with　ファイルパス型変数.open() as f
#ファイルの読みこみ　変数f.read()メソッド
#変数fをfor文でループして1行ずつ処理できる
#末尾改行マークまで読み込まれるので、実行すると、一行空行ができる
#そのため、end=""オプションを追加する

#指定したパスのファイルを開く
import os
from pathlib import Path

#ファイルパス
f_path = Path("../learning/mondai014.txt")

#ファイルのPath変数.open()メソッドをwith文を使用して書く
#as キーワードに紐づけ、fにアクセス
#テキストを読み込むには変数fにアクセスしてread()メソッドで読み出し

with f_path.open() as f:
    gyo = f.read()
    print(gyo,end="")

'''
end=""オプション入れないと、実行結果1行空行がはいる
実行結果

kiso01.py

kiso01_2.py

kiso01_3.py

'''