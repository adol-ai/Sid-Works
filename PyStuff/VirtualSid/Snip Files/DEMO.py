'''from selenium import webdriver

driver = webdriver.Chrome()
driver.get("ttps://www.wikipedia.org/")
content = driver.page_source
print(content)

#AI Sid
print("Hi I'm Sid")
print("\n")

import random

q_1=input("HOW COULD I HELP YOU?")

import os

def shutdown():
    os.system('shutdown /s /t 1')

def restart():
    os.system('shutdown /r /t 1')

for i in q_1:
    if i=="RESTART":
        restart()
    if i=="SHUTDOWN":
        shutdown()
    if i=="HI":
        print("Hi")

'''

'''string = input("Enter any string to remove particular word: ")
word = input("Enter word to be delete/remove: ")
print("\nDeleting given word from the given string...")
print("New String after successfully deleting",word)
word_list = string.split()
print(word_list)
print(' '.join([i for i in word_list if i in word]))
'''

'''l=['q','w','e','r','t','y','u']
w=l.index('t')
a=l[2:]
print(w)
print(a)'''
from bs4 import BeautifulSoup
import requests

'''try:
    r=requests.get("https://en.wikipedia.org/wiki/John_Cabot")
    type(r)
    s = BeautifulSoup(r.text,"html.parser")
    print("\t                      Live NEWS Headlines")
    i=s.find(class_='infobox biography vcard')
    for link in i.find():
        print("◉",link.text)
    print("That's It For NOW!")
except:
    pass'''


#i=l.index("Jump to search")
#j=l.index("Contents")
#u=' '.join([x for x in l if x in l[i:j]])
'''r=requests.get("https://en.wikipedia.org/wiki/John_Cabot")
type(r)
s = BeautifulSoup(r.text,"html.parser")
print("\t                      Live NEWS Headlines")
i=s.find(class_='infobox biography vcard')
#for link in s.find_all():
    #print("◉",link.text)
l_=(s.find().text).split()
i=l_.index("search")+1
j=l_.index("Contents")-1
print(l_[i:j])
print(i ,"&", j)
u=' '.join([x for x in l_ if x in l_[i:j]])
print(u,sep=" ")
    #for l in s.find_all()[i:j]:
        #print("◉",link.text)
print("That's It For NOW!")
p=s.select('p')
i='\n'.join([o.text for o in p])
print(i)

try:
    i_=s.find(class_='infobox')
except:
    try:
        i_=s.find(class_='infobox vcard')
    except:
        i=s.find(class_='infobox biography vcard')
for link in i_.find():
    print("₪",link.text)
print("That's It For NOW!")'''

'''a="qwerty"
r=requests.get("https://google.com/search?q={}".format(a))
s = BeautifulSoup(r.text,"html.parser")
q=s.select(class_='h3.r',selector='a')
print(q)'''
'''for link in q:
    print(link.get('href'))'''

'''import requests
from bs4 import BeautifulSoup

r = requests.get("https://google.com/search?q=time wiki")
soup = BeautifulSoup(r.content, "html.parser")
for link in soup.find_all("a"):
    link.get("href")
'''


import requests
import webbrowser
from bs4 import BeautifulSoup

'''w=input("Search:")
r = requests.get("https://google.com/search?q={} wikipedia".format(w))
s = BeautifulSoup(r.content, 'html.parser')
e=[]
for a_tag in s.find_all('a', href=True):
    e.append(a_tag['href'])
x=[]
for t in e:
    if "/url?q=https://en.wikipedia.org/wiki/" in t:
        x.append(e.index(t))
l=e[x[0]]
i=l.index('&')
q=l[37:i]

if ("List_" in q or "_of_" in q) and ("who" in w and "list" in w):
    l=e[x[1]]
    i=l.index('&')
    q=l[37:i]
    if ("List_" in q or "_of_" in q) and ("who" in w and "list" in w):
        print("@@#@")
        l=e[x[2]]
        i=l.index('&')
        q=l[37:i]
        if ("List_" in q or "_of_" in q) and ("who" in w and "list" in w):
            l=e[x[3]]
            i=l.index('&')
            q=l[37:i]
            if ("List_" in q or "_of_" in q) and ("who" in w and "list" in w):
                print("@@#@")
                l=e[x[4]]
                i=l.index('&')
                q=l[37:i]
                if ("List_" in q or "_of_" in q) and ("who" in w and "list" in w):
                    l=e[x[5]]
                    i=l.index('&')
                    q=l[37:i]
                    if ("List_" in q or "_of_" in q) and ("who" in w and "list" in w):
                        print("@@#@")
                        l=e[x[6]]
                        i=l.index('&')
                        q=l[37:i]
                        if ("List_" in q or "_of_" in q) and ("who" in w and "list" in w):
                            print("@@#@")
                            webbrowser.open("https://google.com/search?q=%s" % w)
                            q==""

else:
    pass

print(q)

if q != "":
    r=requests.get("https://en.wikipedia.org/wiki/{}".format(q))
    type(r)
    s = BeautifulSoup(r.text,"html.parser")

    try:
        print('\t InfoBox')
        i_=s.find(class_='infobox biography vcard')
        try:
            for link in i_.find():
                print("₪",link.text)
        except:
            i=s.find(class_='infobox biography vcard')
            for link in i.findAll('td'):
                print("₪",link.text)
    except:
        try:
            i_=s.find(class_='infobox vcard')
            try:
                for link in i_.find():
                    print("₪",link.text)
            except:
                i=s.find(class_='infobox vcard')
                for link in i.findAll('td'):
                    print("₪",link.text)
        except:
            try:
                i=s.find(class_='infobox')
                try:
                    for link in i_.find():
                        print("₪",link.text)
                except:
                    i=s.find(class_='infobox')
                    for link in i.findAll('td'):
                        print("₪",link.text)
            except:
                try:
                    i=s.find(class_='infobox geography vcard')
                    try:
                        for link in i.find():
                            print("₪",link.text)
                    except:
                        i=s.find(class_='infobox geography vcard')
                        for link in i.findAll('td'):
                            print("₪",link.text)
                except:
                    try:
                        i=s.find(class_='infobox vevent')
                        
                        try:
                            for link in i_.find():
                                print("₪",link.text)
                        except:
                            i=s.find(class_='infobox vevent')
                            for link in i.findAll('td'):
                                print("₪",link.text)
                    except:
                        try:
                            i=s.find(class_='vertical-navbox nowraplinks')
                            for link in i.find():
                                print("↴",link.text)
                        except:
                            pass
        
    print("\t Para's")

    p=s.select('p')
    i='\n'.join([o.text for o in p])
    print(i)

'''
'''w=input("meaning:")

g = requests.get("https://google.com/search?q={} cambridge dictionary".format(w))
_s_ = BeautifulSoup(g.content, 'html.parser')
y=[]
for a in _s_.find_all('a', href=True):
    y.append(a['href'])
z=[]
for t in y:
    if "/url?q=https://dictionary.cambridge.org/dictionary/english/" in t:
        z.append(y.index(t))
l=y[z[0]]
j=l.index('&')
k=l[59:j]
print(k)
if k == "":
    print("ERROR 404:Not Found!")
    
r = requests.get("https://dictionary.cambridge.org/dictionary/english/{}".format(k))
s = BeautifulSoup(r.content, 'html.parser')
i= s.find(class_="ddef_h")
e=[]
try:
    for b in i.findAll():
        e.append(b.text)
    x=[]
    for h in e:
        if ":" in h:
            x.append(e.index(h))
    try:
        p=e[x[0]]
        print(p)
    except:
        print("##")
        print(e[1])
except:
    pass

try:
    r_ = requests.get("https://www.oxfordlearnersdictionaries.com/definition/english/{}".format(k))
    s_ = BeautifulSoup(r_.content, 'html.parser')
    i_= s_.find(class_="def")
    print((i_.extract()).text)
except:
    pass
'''

'''q_=input("w:")
l= q_.split()
try:
    try:
        i=l.index("the")+1
        j=l.index("of")
        w=' '.join([x for x in l if x in l[i:j]])
    except:
        i=l.index("the")+1
        j=l.index("in")
        w=' '.join([x for x in l if x in l[i:j]])
except:
    try:
        i=l.index("is")+1
        j=l.index("of")
        w=' '.join([x for x in l if x in l[i:j]])
    except:
        i=l.index("is")+1
        j=l.index("in")
        w=' '.join([x for x in l if x in l[i:j]])
w_ = str(w).casefold()
try:
    i=l.index("of")+1
    u=' '.join([x for x in l if x in l[i:]])
except:
    i=l.index("in")+1
    u=' '.join([x for x in l if x in l[i:]])
            
r = requests.get("https://google.com/search?q={} wikipedia".format(u))
s = BeautifulSoup(r.content, 'html.parser')
e=[]
for a_ in s.find_all('a', href=True):
    e.append(a_['href'])
x=[]
for t in e:
    if "/url?q=https://en.wikipedia.org/wiki/" in t:
        x.append(e.index(t))
l=e[x[0]]
i=l.index('&')
q=l[37:i]
if len(q) > 20:
    print("\t                                 ",q)
else:
    print("\t                                        ",q)
if q != "":
    print("\t                       ʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭ")
r=requests.get("https://en.wikipedia.org/wiki/{}".format(q))
type(r)
s = BeautifulSoup(r.text,"html.parser")
i_=s.find(class_='infobox geography vcard')
_l_=[]
for link in i_.find():
    _l_.append(link.text)
    if w_ in (link.text).casefold():
        z=link.text
print(_l_)
_i_= (_l_).index(z)
print(_i_)
print(z)
for i__ in _l_[_i_:_i_+2]:
        if "•" in i__:
            print("utfuf")
            z_=link.text
            print(z_)
'''
from datetime import datetime

'''u=input("input:")
r = requests.get("https://bing.com/search?q={}".format(u))
s = BeautifulSoup(r.content, 'html.parser')
e=[]
for a_ in s.find_all('a', href=True):
    print(a_['href'])
    e.append(a_['href'])'''
    
'''x=[]
for t in e:
    if "/url?q=https://en.wikipedia.org/wiki/" in t:
        x.append(e.index(t))'''

#t=datetime.now()
#h=int(t.strftime("%H"))
#print(h)

'''if h==  and h== :
    l=s.find(class_='cptn-ctnt')
    w=s.find(class_='condition')
    t=s.find(class_='currTemp')
    d=s1.find(class_='wtr_condiAttribs')
    p=s1.find(class_='wtr_currPerci')
    w_=s1.find(class_='wtr_currWind')
    h=s1.find(class_='wtr_currHumi')
    print("Location:",l.text)
    print("Weather:",w.text)
    print("Location:",l.text)
    print("Weather:",w.text)
    print("Location:",l.text)
    print("Weather:",w.text)
    print("Temperature:",t.text,"℃")
'''

'''def weather():
    try:
        r=requests.get("https://www.msn.com/en-in/weather/today/")
        type(r)
        s = BeautifulSoup(r.text,"html.parser")
        print("\t                           Weather ")
        w=s.find(class_='weather-info')
        t=s.find(class_='current-info')
        t_=(t.text).split()
        w_=(w.text).split()
        print("Temperature:",t_[0],t_[1])
        print('\n')
        print("Weather ⤵",w.text)
        print("\n                  ","\t That's the Current Weather \t")
        if v == "YES":
            s=gTTS(text="hmm. Current weather is: {}".format(w.text),lang='en-uk')
            s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
    except requests.exceptions.ConnectionError:
        print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
        if v == "YES":
            playsound(r"D:\Python Files\Audiofiles\offline.mp3")'''

'''print('\n')
u=input("input:")
r = requests.get("https://google.com/search?q={} msn weather".format(u))
s = BeautifulSoup(r.content, 'html.parser')
e=[]
for a_ in s.find_all('a', href=True):
    e.append(a_['href'])
x=[]
for t in e:
    if "/url?q=https://www.msn.com/en" in t:
        x.append(e.index(t))
l=e[x[0]]
i=l.index('&')
q=l[7:i]
r=requests.get("{}".format(q))
type(r)
s = BeautifulSoup(r.text,"html.parser")
print("\t                                 Weather Forecast Report ")
w=s.find(class_='weather-info')
t=s.find(class_='current-info')
t_=(t.text).split()
w_=(w.text).split()
j=l.index('%')-8
c=l[47:j]
if "F" in t_[1]:
    _t_= (int(t_[0])-32)*(5/9)
else:
    _t_= (int(t_[0])*(9/5))+32
print("Location:",c,"\n")
print("Temperature:",t_[0],t_[1],"/////",round(_t_),t_[2])
print('\n')
print("Weather ⤵",w.text)
print("\n                  ","\t That's the Current Weather \t")
'''
###########################################

'''q_=input("i:")
l= q_.split()
try:
    try:
        i=l.index("the")+1
        j=l.index("of")
        w=' '.join([x for x in l if x in l[i:j]])
    except:
        i=l.index("the")+1
        j=l.index("in")
        w=' '.join([x for x in l if x in l[i:j]])
except:
    try:
        i=l.index("is")+1
        j=l.index("of")
        w=' '.join([x for x in l if x in l[i:j]])
    except:
        i=l.index("is")+1
        j=l.index("in")
        w=' '.join([x for x in l if x in l[i:j]])
w_ = str(w).casefold()
try:
    i=l.index("of")+1
    u=' '.join([x for x in l if x in l[i:]])
except:
    i=l.index("in")+1
    u=' '.join([x for x in l if x in l[i:]])
try:
    r = requests.get("https://google.com/search?q={} wikipedia".format(u))
    s = BeautifulSoup(r.content, 'html.parser')
    e=[]
    for a_ in s.find_all('a', href=True):
        e.append(a_['href'])
    x=[]
    for t in e:
        if "/url?q=https://en.wikipedia.org/wiki/" in t:
            x.append(e.index(t))
    l=e[x[0]]
    i=l.index('&')
    q=l[37:i]
    a=b=0
    for o in range(len(q)):
        if q[o].isalpha():
            a=a+1
        elif q[o].isdigit():
            b=b+1
        else:
            pass
    if a<4 and b>=1:
        l=e[x[1]]
        i=l.index('&')
        q=l[37:i]
    else:
        pass
    if len(q) > 20:
        print("\t                                 ",q)
    else:
        print("\t                                        ",q)
    if q != "":
        print("\t                       ʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭʭ")
    r=requests.get("https://en.wikipedia.org/wiki/{}".format(q))
    type(r)
    s = BeautifulSoup(r.text,"html.parser")
    _w_=w_.split()
    z=[]
    y=[]
    try:
        i_=s.find(class_='infobox geography vcard')
        try:
            for link in i_.find():
                y.append(link.text)
                if w_ in (link.text).casefold():
                    z.append(link.text)
        except:
            try:
                for link in i_.find():
                    y.append(link.text)
                    if _w_[0] in (link.text).casefold():
                        z.append(link.text)
            except:
                for link in i_.find():
                    y.append(link.text)
                    if _w_[1] in (link.text).casefold():
                        z.append(link.text)
    except:
        try:
            i_=s.find(class_='infobox biography vcard')
            try:
                for link in i_.find():
                    y.append(link.text)
                    if w_ in (link.text).casefold():
                        z.append(link.text)
            except:
                try:
                    for link in i_.find():
                        y.append(link.text)
                        if _w_[0] in (link.text).casefold():
                            z.append(link.text)
                except:
                    for link in i_.find():
                        y.append(link.text)
                        if _w_[1] in (link.text).casefold():
                            z.append(link.text)
        except:
            try:
                i_=s.find(class_='infobox vcard')
                try:
                    for link in i_.find():
                        y.append(link.text)
                        if w_ in (link.text).casefold():
                            z.append(link.text)
                except:
                    try:
                        for link in i_.find():
                            y.append(link.text)
                            if _w_[0] in (link.text).casefold():
                                z.append(link.text)
                    except:
                        for link in i_.find():
                            y.append(link.text)
                            if _w_[1] in (link.text).casefold():
                                z.append(link.text)
            except:
                try:
                    i_=s.find(class_='infobox')
                    try:
                        for link in i_.find():
                            y.append(link.text)
                            if w_ in (link.text).casefold():
                                z.append(link.text)
                    except:
                        try:
                            for link in i_.find():
                                y.append(link.text)
                                if _w_[0] in (link.text).casefold():
                                    z.append(link.text)
                        except:
                            for link in i_.find():
                                y.append(link.text)
                                if _w_[1] in (link.text).casefold():
                                    z.append(link.text)
                except:
                    try:
                        i_=s.find(class_='infobox vevent')
                        try:
                            for link in i_.find():
                                y.append(link.text)
                                if w_ in (link.text).casefold():
                                    z.append(link.text)
                        except:
                            try:
                                for link in i_.find():
                                    y.append(link.text)
                                    if _w_[0] in (link.text).casefold():
                                        z.append(link.text)
                            except:
                                for link in i_.find():
                                    y.append(link.text)
                                    if _w_[1] in (link.text).casefold():
                                        z.append(link.text)
                    except:
                        try:
                            i_=s.find(class_='infobox biota')
                            try:
                                for link in i_.findAll('td'):
                                    y.append(link.text)
                                    if w_ in (link.text).casefold():
                                        z.append(link.text)
                            except:
                                try:
                                    for link in i_.findAll('td'):
                                        y.append(link.text)
                                        if _w_[0] in (link.text).casefold():
                                            z.append(link.text)
                                except:
                                    for link in i_.findAll('td'):
                                        y.append(link.text)
                                        if _w_[1] in (link.text).casefold():
                                            z.append(link.text)
                        except:
                            try:
                                i_=s.find(class_='infobox hproduct')
                                try:
                                    for link in i_.findChild():
                                        y.append(link.text)
                                        if w_ in (link.text).casefold():
                                            z.append(link.text)
                                except:
                                    try:
                                        for link in i_.findChild():
                                            y.append(link.text)
                                            if _w_[0] in (link.text).casefold():
                                                z.append(link.text)
                                    except:
                                        for link in i_.findChild():
                                            y.append(link.text)
                                            if _w_[1] in (link.text).casefold():
                                                z.append(link.text)
                            except:
                                try:
                                    i_=s.find(class_='infobox bordered')
                                    try:
                                        for link in i_.findAll('td'):
                                            y.append(link.text)
                                            if w_ in (link.text).casefold():
                                                z.append(link.text)
                                    except:
                                        try:
                                            for link in i_.findAll('td'):
                                                y.append(link.text)
                                                if _w_[0] in (link.text).casefold():
                                                    z.append(link.text)
                                        except:
                                            for link in i_.findAll('td'):
                                                y.append(link.text)
                                                if _w_[1] in (link.text).casefold():
                                                    z.append(link.text)
                                except:
                                    try:
                                        i_=s.find(class_='infobox vcard plainlist')
                                        try:
                                            for link in i_.find():
                                                y.append(link.text)
                                                if w_ in (link.text).casefold():
                                                    z.append(link.text)
                                        except:
                                            try:
                                                for link in i_.find():
                                                    y.append(link.text)
                                                    if _w_[0] in (link.text).casefold():
                                                        z.append(link.text)
                                            except:
                                                for link in i_.find():
                                                    y.append(link.text)
                                                    if _w_[1] in (link.text).casefold():
                                                        z.append(link.text)
                                    except:
                                        try:
                                            i_=s.find(class_='infobox vevent haudio')
                                            try:
                                                for link in i_.find():
                                                    y.append(link.text)
                                                    if w_ in (link.text).casefold():
                                                        z.append(link.text)
                                            except:
                                                try:
                                                    for link in i_.find():
                                                        y.append(link.text)
                                                        if _w_[0] in (link.text).casefold():
                                                            z.append(link.text)
                                                except:
                                                    for link in i_.find():
                                                        y.append(link.text)
                                                        if _w_[1] in (link.text).casefold():
                                                            z.append(link.text)
                                        except:
                                            try:
                                                i_=s.find(class_='vertical-navbox nowraplinks')
                                                try:
                                                    for link in i_.find():
                                                        y.append(link.text)
                                                        if w_ in (link.text).casefold():
                                                            z.append(link.text)
                                                except:
                                                    try:
                                                        for link in i_.find():
                                                            y.append(link.text)
                                                            if _w_[0] in (link.text).casefold():
                                                                z.append(link.text)
                                                    except:
                                                        for link in i_.find():
                                                            y.append(link.text)
                                                            if _w_[1] in (link.text).casefold():
                                                                z.append(link.text)
                                            except:
                                                try:
                                                    i_=s.find(class_='vertical-navbox vcard')
                                                    try:
                                                        for link in i_.find():
                                                            y.append(link.text)
                                                            if w_ in (link.text).casefold():
                                                                z.append(link.text)
                                                    except:
                                                        try:
                                                            for link in i_.find():
                                                                y.append(link.text)
                                                                if _w_[0] in (link.text).casefold():
                                                                    z.append(link.text)
                                                        except:
                                                            for link in i_.find():
                                                                y.append(link.text)
                                                                if _w_[1] in (link.text).casefold():
                                                                    z.append(link.text)
                                                except:
                                                    i_=s.find(class_='vertical-navbox nowraplinks hlist')
                                                    try:
                                                        for link in i_.find():
                                                            y.append(link.text)
                                                            if w_ in (link.text).casefold():
                                                                z.append(link.text)
                                                    except:
                                                        try:
                                                            for link in i_.find():
                                                                y.append(link.text)
                                                                if _w_[0] in (link.text).casefold():
                                                                    z.append(link.text)
                                                        except:
                                                            for link in i_.find():
                                                                y.append(link.text)
                                                                if _w_[1] in (link.text).casefold():
                                                                    z.append(link.text)
    if "president" in w_ and len(z[0]) > 53:
        p=(y).index(z[1])
    else:
       p=(y).index(z[0]) 
    if "•" in y[p]:
        print("〰",y[p],"• 〰")
    elif i_==s.find(class_='vertical-navbox nowraplinks hlist') or i_==s.find(class_='vertical-navbox nowraplinks') or i_==s.find(class_='vertical-navbox vcard'):
        print("⤵",y[p])
    else:
        print(y[p])
    if i_==s.find(class_='infobox bordered'):
        y_=y.index('Chemical formula\n')
        if y_<p:
            print("-⇴►",y[p+1])
        else:
            pass
    elif i_==s.find(class_='infobox biota'):
        print("-⇴►",y[p+1])
    try:
        if "•" in y[p]:
            if "•" in y[p+1]:
                print("\n")
                print(y[p+1])
            if "•" in y[p+2] and "•" in y[p+1]:
                print("\n")
                print(y[p+2])
            if "•" in y[p+3] and ("•" in y[p+1] and "•" in y[p+2]):
                print("\n")
                print(y[p+3])
            if "•" in y[p+4] and ("•" in y[p+1] and "•" in y[p+2] and "•" in y[p+3]):
                print("\n")
                print(y[p+4])
            if "•" in y[p+5] and ("•" in y[p+1] and "•" in y[p+2] and "•" in y[p+3] and "•" in y[p+4]):
                print("\n")
                print(y[p+5])
            if "•" in y[p+6] and ("•" in y[p+1] and "•" in y[p+2] and "•" in y[p+3] and "•" in y[p+4] and "•" in y[p+5]):
                print("\n")
                print(y[p+6])
    except:
        pass
except:
    if "sid" in q_ or "glenda" in q_:
        l= q_.split()
        try:
            l.remove("sid")
            w=' '.join([x for x in l if x in l])
        except:
            l.remove("glenda")
            w=' '.join([x for x in l if x in l])
        else:
            w=q_
    webbrowser.open("https://google.com/search?q={}".format(q_))'''

######################## 
'''w=input("E:")
r = requests.get("https://google.com/search?q={}".format(w))
s = BeautifulSoup(r.content, 'html.parser')
e=[]
for a_ in s.find_all('a', href=True):
    e.append(a_['href'])
    print(a_['href'])
x=[]
for t in e:
    if "/url?q=https://www." in t:
        x.append(e.index(t))
l=e[x[0]]
j=l[19:].index('.')
w=l[19:19+j]
print(w)'''

'''j=l.index('&')
w=l[7:j]
print(w)'''

'''if w is True:
    pass
elif "amazon" in w:
    webbrowser.open("https://www.amazon.in/s?k={}".format("q"))
elif "snapdeal" in w:
    webbrowser.open("https://www.snapdeal.com/search?keyword={}".format("q"))
elif "ebay" in w:
    webbrowser.open("https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw={}".format("q"))
elif "olx" in w:
    webbrowser.open("https://www.olx.in/items/q-{}?isSearchCall=true".format("q"))
elif "paytm" in w:
    webbrowser.open("https://paytmmall.com/shop/search?q={}".format("q"))
elif "myntra" in w:
    webbrowser.open("https://www.myntra.com/{}".format("q"))
elif "bigbasket" in w:
    webbrowser.open("https://www.bigbasket.com/ps/?q={}".format("q"))
elif "pepperfry" in w:
    webbrowser.open("https://www.pepperfry.com/site_product/search?q={}+&as=0&src=os".format("q"))
elif "alibaba" in w:
    webbrowser.open("https://www.alibaba.com/showroom/{}.html?fsb=y&IndexArea=product_en&CatId=&SearchText={}&isGalleryList=G".format("q","q"))
elif "aliexpress" in w:
    webbrowser.open("https://www.aliexpress.com/premium/{}.html?d=y&origin=y&catId=0&SearchText={}".format("q","q"))
else:
    webbrowser.open("https://www.{}.com/search?q={}".format(w,"q"))'''

