#座間市HP ハザードマップPDFをDL href要素のテキスト表示部分を抜き出して保存
#座間市HP　https://www.city.zama.kanagawa.jp/www/contents/1613713435129/index.html
#<a href="/www/contents/1613713435129/files/map1.pdf">1.ハザードマップ（洪水浸水想定区域凡例等）(647KB)(PDF文書)</a>　だったら、
#1.ハザードマップ（洪水浸水想定区域凡例等）(647KB)(PDF文書).pdfで保存する
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pathlib import Path
import time

url = "https://www.city.zama.kanagawa.jp/www/contents/1613713435129/index.html"
request = requests.get(url)
print(request.status_code)

#ハザードマップはa hrefに保存されている
soup = BeautifulSoup(request.content,"html.parser")
a_elments = soup.select("a")
print(a_elments)

#hrefのリンクから、pdfファイルのリンクを抜き出す
pdf_url_list = []
#href文書を抜き出す
dic_txtname = {}

#https://www.twilio.com/blog/web-scraping-and-parsing-html-in-python-with-beautiful-soup-jp
#soup.find_all()はWebスクレイピングで最もよく使われるメソッドです。これによりページのすべてのハイパーリンクを反復してURLを出力できます。
for link in soup.find_all("a"):
    href = link.get("href")
    if href.endswith(".pdf"):
        #print(href)
        pdf_url = urljoin(url,href)
        print(pdf_url)
        pdf_url_list.append(pdf_url)
        lntxt = link.getText()
        dic_txtname[pdf_url] = lntxt

print(dic_txtname)
save_folder_path = Path("../learning/Download_Zama")
save_folder_path.mkdir(exist_ok=True)

for r in pdf_url_list:
    r_file = requests.get(r)
    if r_file.status_code == 200:
        print("yes")
        for k,v in dic_txtname.items():
            if k == r :
                save_file = Path(v + ".pdf")
                print(save_file)
                save_path = save_folder_path / save_file
                with save_path.open("wb") as f:
                    f.write(r_file.content)
    else:
        print("no")

    time.sleep(3)
