import os
import requests
import pprint
import webbrowser
#import urllib.request
import requests
from bs4 import BeautifulSoup

q_="cat"
r = requests.get("https://www.google.com/search?q={}&tbm=isch&source=hp&biw=1284&bih=722&ei=i6hsY8nTLoKaseMP8KC8qAc&iflsig=AJiK0e8AAAAAY2y2m1b1e-E3X9GCHmFV5LvC6JR4yQs-&ved=0ahUKEwiJxbr2i6P7AhUCTWwGHXAQD3UQ4dUDCAY&uact=5&oq=cat&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMgUIABCABDIICAAQgAQQsQM6CwgAEIAEELEDEIMBOggIABCxAxCDAVAAWLkDYMwGaABwAHgAgAFSiAHqAZIBATOYAQCgAQGqAQtnd3Mtd2l6LWltZw&sclient=img".format(q_))
s = BeautifulSoup(r.content, 'html.parser')

e=[]
for a_ in s.find_all('a', href=True):
    try:
        if a_.find('img')!=None:
            e.append(a_.find('img'))
    except:
        pass
pprint.pprint(e)

for url in e:
    u=url.get('src')
    #r_=requests.get("https:"+u).content
    webbrowser.open('https:'+u)
    '''os.chdir('T:\\Python Files\\Jus learning stuff\\img')
    imgfile=open(os.path.join(os.path.basename(url)),'wb')
    for i in r_.iter_content():
        imgfile.write(i)
    imgfile.close()'''

'''
s=BeautifulSoup(r.text,'html.parser')
pic=s.select('img')
print(pic)
for i in pic:
    url=i.get('src')
    print(url)
    try:
        r_=requests.get(url)
    except:
        r_=requests.get("http:"+url)
    print(r_)
    os.chdir('T:\\Python Files\\Jus learning stuff\\img')
    imgfile=open(os.path.join(os.path.basename(url)),'wb')
    for i in r_.iter_content():
        imgfile.write(i)
    imgfile.close()
'''
