#pyファイルを保存しているフォルダから、"kiso"の文字列のテキストファイル名を抜き出す
import os

#OSモジュールで、カレントディレクトリを表す
print(os.getcwd())

#カレントディレクトリを変更する
os.chdir("C:/Users/●●/Documents/python/TestDir")
print(os.getcwd())
#元に戻す
os.chdir("C:/Users/●●/Documents/python/py_File")
print(os.getcwd())

#カレントディレクトリ内のファイルを表示する
print(os.listdir())
for c in os.listdir():
    print(c)


