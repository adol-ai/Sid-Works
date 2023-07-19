'''import requests
from bs4 import BeautifulSoup

r=requests.get("https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen")
s=BeautifulSoup(r.text,"html.parser")

for i in s.find_all("a"):
    if "watch" in (i.text).casefold():
        print("--->",(i.text))'''


import requests
import json
from bs4 import BeautifulSoup

r=requests.get("https://news.google.com/topstories?pz=1&cf=all&topic=n&hl=en-IN&gl=IN&ceid=IN:en")
data=(r.text)
print(data)


'''s=BeautifulSoup(r.text,"html.parser")
c=s.find(id="daylink-0")
print(c.text)
for i in c:
    print(i.text)'''

print("completed")
