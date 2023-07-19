import os
import time
import math
import random
import keyboard
import requests
import webbrowser
from tkinter import *
from gtts import gTTS
from tkinter import ttk
import speech_recognition
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from collections import Counter
from playsound import playsound

'''m_w=Tk()
#m_w.overrideredirect(True)
m_w.geometry("650x730")
m_w.resizable(0,1)
m_w.title("⋎ɨɤŧũāł ₰ɨð")
#⨈⩔⩛⩖⩡₴₷₻▼Ⅴ⋁⋎₫₸₳ɤɨŁɭăāɐđðłĺɬɾŧʈũ
_f=LabelFrame(m_w,text='⩛ɨɤŧũāł ₷ɨð',font=('Comic Sans MS',15),fg='green',bg='alice blue',padx=10,pady=0)
_l=Label(_f,font=('Comic Sans MS',15),fg='green',bg='alice blue',padx=730,pady=0)
_l.pack()
_f.pack()
_f_=LabelFrame(m_w,relief="sunken")
_f_.pack(fill='both',expand=1)
canvas=Canvas(_f_)
canvas.pack(side='left',fill='both',expand=1)
#add a scrollbar to canvas
scroll=ttk.Scrollbar(_f_,orient='vertical',command=canvas.yview)
scroll.pack(side='right',fill='y')
#configure the canvas
canvas.configure(yscrollcommand=scroll.set)
canvas.bind('<Configure>',lambda e:canvas.configure(scrollregion=canvas.bbox('all')))
#create another frame inside the canvas
frame2=LabelFrame(canvas)
#add that new frame to a window in the canvas
canvas.create_window((0,0),window=frame2,anchor='nw')


Label(m_w,text='⩛ɨɤŧũāł ₷ɨð',font=('Comic Sans MS',15),fg='green',bg='alice blue')
_q_=Entry(m_w,width=10,bg='red')
m_w.mainloop()'''

_v_="hi hello",27
try:
    s=gTTS(text="hmm "+str(_v_),lang='en-uk')
    s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
    playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
    os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
except:
    pass
