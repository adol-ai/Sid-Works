import time
import os
import keyboard
import requests
import webbrowser
from gtts import gTTS
from playsound import playsound
from bs4 import BeautifulSoup
import speech_recognition
import random

'''r=requests.get("https://en.wikipedia.org/wiki/George_Croghan_Reid")
type(r)
s = BeautifulSoup(r.text,"html.parser")
i_=s.find(class_='infobox')
for link in i_.findAll('tr'):
    g=''
    g_=[]
    for h in (link.text):
        if h.isupper() or h.isdigit():
            if h.isdigit():
                g_.append(((link.text).index(h)))
                if ((link.text).index(h))==g_[0]:
                    g=g+' '+h
                else:
                   g=g+h 
            elif h.isupper():
                g=g+' '+h
            else:
                g=g+h
        else:
            g=g+h
    print("₪",g)
'''

'''keyboard.press_and_release('win')
time.sleep(1)
keyboard.write('steam')
time.sleep(1)
keyboard.press_and_release('Enter')
'''

'''w=input("QWEER:")
g = requests.get("https://google.com/search?q={} in cambridge dictionary".format(w))
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
if k == "" or k == "oxford":
    print("ERROR 404:Not Found!")    
else:
    print(k)
r = requests.get("https://dictionary.cambridge.org/dictionary/english/time")#.format(k))
print("12321556")
s = BeautifulSoup(r.content, 'html.parser')
print(k)
i= s.find(class_="ddef_h")
e=[]
for b in i.findAll():
    print(b.text)
    e.append(b.text)
x=[]
for h in e:
    if ":" in h:
        x.append(e.index(h))
p_=e[x[0]]
try:
    print("\t~~~~",k,"~~~~")
    print("As Per Cambridge Dictionary:",p_)
except:
    pass
try:
    r_ = requests.get("https://www.oxfordlearnersdictionaries.com/definition/english/{}".format(k))
    s_ = BeautifulSoup(r_.content, 'html.parser')
    i_= s_.find(class_="def")
    print("\nAs Per Oxford Dictionary:",(i_.extract()).text)
except:
    pass

r__ = requests.get("https://www.macmillandictionary.com/dictionary/british/{}".format(k))
s__ = BeautifulSoup(r__.content, 'html.parser')
i__= s__.find(class_="DEFINITION")
for b in i__.findAll():
    print(b.text)
print("\nAs Per Macmillan Dictionary:",(i__.extract()).text)
'''

'''p="A magnet is a material or object that produces a magnetic field. This magnetic field is invisible but is responsible for the most notable property of a magnet: a force that pulls on other ferromagnetic materials, such as iron, and attracts or repels other magnets. A permanent magnet is an object made from a material that is magnetized and creates its own persistent magnetic field. An everyday example is a refrigerator magnet used to hold notes on a refrigerator door. Materials that can be magnetized, which are also the ones that are strongly attracted to a magnet, are called ferromagnetic (or ferrimagnetic). These include the elements iron, nickel and cobalt and their alloys, some alloys of rare-earth metals, and some naturally occurring minerals such as lodestone. Although ferromagnetic (and ferrimagnetic) materials are the only ones attracted to a magnet strongly enough to be commonly considered magnetic, all other substances respond weakly to a magnetic field, by one of several other types of magnetism."

s=gTTS(text="hmm. {}".format(p),lang='en-uk',slow=False)
s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")'''

'''time.sleep(1)
keyboard.press_and_release('win + Right')
time.sleep(1)'''


'''_r_=speech_recognition.Recognizer()

with speech_recognition.Microphone() as h:
    print("...")
    playsound(r"D:\Python Files\Audiofiles\On.mp3")
    a=_r_.listen(h)
playsound(r"D:\Python Files\Audiofiles\Off.mp3")
d=_r_.recognize_google(a).casefold()

if "siri" in d or "google" in d or "cortana" in d or "bixby" in d or "alexa" in d:
    r=["For clearification: I'm Sid", "That's Awkward!", "That's Awful", "I did'nt Expect that!", "You're dissappointing Me!", "You're here with different Person in a different Platform", "I thought you Recognise me!"]
    r_=random.randint(0,6)
    t_=r[r_]
    print(t_)
    r1=["That is Awkward!", "That is Awful", "I did'nt Expect that!", "You're dissappointing Me!", "You're here with different Person in a different Platform", "I thought you Recognise me!"]
    r1_=random.randint(0,5)
    t=r1[r1_]
    s=gTTS(text="hmm,{}".format(t),lang='en-uk')
    s.save(r"D:\Python Files\Audiofiles\VoiceOver9.mp3")
    playsound(r"D:\Python Files\Audiofiles\VoiceOver9.mp3")
elif d[0]=='h' or "sid" in d or "glenda" in d:
    with speech_recognition.Microphone() as h_:
        playsound(r"D:\Python Files\Audiofiles\On.mp3")
        a_=_r_.listen(h_)
    playsound(r"D:\Python Files\Audiofiles\Off.mp3")
    d_=_r_.recognize_google(a_)
    print(d_)'''

'''r=requests.get("https://www.google.com/search?q=1%2B9&oq=&aqs=chrome.1.69i57j6j0l6.4594j0j7&sourceid=chrome&ie=UTF-8")
s=BeautifulSoup(r.content,'html.parser')
i=s.find(class_='TIGsTb')
x=[]
for _l_ in i.findAll():
    # print(_l_.text)
    x.append(_l_.text)
p=x.index("All results")
print("@@##@@!!",p)
print("#########:",x[p+23])'''


'''r=requests.get("https://news.google.com/search?q=vaccine&hl=en-US&gl=US&ceid=US%3Aen")
s=BeautifulSoup(r.content,'html.parser')
for _l_ in s.findAll('a')[53:]:
    print(_l_.text)'''
