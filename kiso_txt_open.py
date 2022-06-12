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
    print(gyo)

