from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
from gtts import gTTS
import os
from playsound import playsound
from tkinter import colorchooser
from selenium import webdriver
import time
import keyboard
import random
import smtplib
import webbrowser
import speech_recognition as sr
import pyaudio
from subprocess import *
import os
from signal import *
import time
#Popen('python sidbrain.py')
def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        said=''
        try:
            said=r.recognize_google(audio)
            print(said)
        except Exception as e:
            pass
root=Tk()
root.title("online Shopping")
root.config(bg='#9b9b9b')
root.resizable(height=0,width=0)
speakerstatus='speakeron'
f=open('sidmic.txt','w')
f.write(speakerstatus)
f.close()
bgp1=ImageTk.PhotoImage(Image.open('bgp1.jpg'))
bgp2=ImageTk.PhotoImage(Image.open('bgp2.jpg'))
bgp3=ImageTk.PhotoImage(Image.open('bgp3.jpg'))
bgp4=ImageTk.PhotoImage(Image.open('bgp4.jpg'))
bgp5=ImageTk.PhotoImage(Image.open('bgp5.jpg'))
bgp6=ImageTk.PhotoImage(Image.open('bgp6.jpg'))

bgpl=[bgp1,bgp2,bgp3,bgp4,bgp5,bgp6]

def background():
    global bgp
    root_=Toplevel()
    root_.geometry('800x600+300+100')
    #create a mainframe
    main_frame_=LabelFrame(root_)
    main_frame_.pack(fill='both',expand=1)
    #create a canvas
    canvas_=Canvas(main_frame_)
    canvas_.pack(side='left',fill='both',expand=1)
    #add a scrollbar to canvas
    scroll_=ttk.Scrollbar(main_frame_,orient='vertical',command=canvas_.yview)
    scroll_.pack(side='right',fill='y')
    #configure the canvas
    canvas_.configure(yscrollcommand=scroll_.set)
    canvas_.bind('<Configure>',lambda e:canvas_.configure(scrollregion=canvas_.bbox('all')))

    #create another frame inside the canvas
    frame2_=LabelFrame(canvas_)
    #add that new frame to a window in the canvas
    canvas_.create_window((0,0),window=frame2_,anchor='nw')
    def selectedbg(i):
        global bgp
        global canvas
        bgp=i
        canvas.create_image(0,0,image=bgp,anchor='nw')
        root_.quit
    b1=Button(frame2_,image=bgp1,command=lambda:selectedbg(bgp1))
    b2=Button(frame2_,image=bgp2,command=lambda:selectedbg(bgp2))
    b3=Button(frame2_,image=bgp3,command=lambda:selectedbg(bgp3))
    b4=Button(frame2_,image=bgp4,command=lambda:selectedbg(bgp4))
    b5=Button(frame2_,image=bgp5,command=lambda:selectedbg(bgp5))
    b6=Button(frame2_,image=bgp6,command=lambda:selectedbg(bgp6))
    
    bg=[b1,b2,b3,b4,b5,b6]
    h=1
    for j in bg:
        try:
            j.grid(row=h,column=1)
        except:
            break
        h+=1
        
my_menu=Menu(root)
root.config(menu=my_menu)
file_menu=Menu(my_menu)
my_menu.add_cascade(label='file',menu=file_menu)
file_menu.add_command(label='select background',command=background)
file_menu.add_command(label='quit program',command=root.quit)

speakeroff=ImageTk.PhotoImage(Image.open('speakeroff.png'))
speakeron=ImageTk.PhotoImage(Image.open('speakeron.png'))
mute=ImageTk.PhotoImage(Image.open('mute.png'))
unmute=ImageTk.PhotoImage(Image.open('unmute.png'))

def munm(i):
    global micstatus
    if i=='unmute':
        micbtn.config(image=mute,command=lambda:munm('mute'),bd=0)
        micstatus='mute'
    if i=='mute':
        micbtn.config(image=unmute,command=lambda:munm('unmute'),bd=0)
        micstatus='unmute'
def sonoff(i):
    global speakerstatus
    if i=='speakeron':
        speakerbtn.config(image=speakeroff,command=lambda:sonoff('speakeroff'),bd=0)
        speakerstatus='speakeroff'
        f=open('sidmic.txt','w')
        f.write(speakerstatus)
        f.close()
    if i=='speakeroff':
        speakerbtn.config(image=speakeron,command=lambda:sonoff('speakeron'),bd=0)
        speakerstatus='speakeron'
        f=open('sidmic.txt','w')
        f.write(speakerstatus)
        f.close()
        
panel_1=PanedWindow(bd=4,relief='groove',bg='red')
panel_1.pack(fill=BOTH,expand=1)
panel_2=PanedWindow(panel_1,orient='vertical',bd=4,relief='groove',bg='blue')
panel_2.pack(fill=BOTH,expand=1)

frame1=LabelFrame(panel_1,relief='raised')
frame2=LabelFrame(panel_2,relief='raised')
panel_2.add(frame2)
frame3=LabelFrame(panel_2,relief='raised')
panel_2.add(frame3)

speakerbtn=Button(frame3,image=speakeron,relief='groove',command=lambda:sonoff('speakeron'),bd=0)
speakerbtn.grid(row=1,column=5)
micbtn=Button(frame3,image=unmute,relief='groove',command=lambda:munm('unmute'),bd=0)
micbtn.grid(row=1,column=2)

bgp=bgp1

def custom_yview(*args,**kwargs):
    canvas.yview(*args,**kwargs)
    y=canvas.canvasy(0)    
    canvas.create_image(0,y,image=bgp,anchor='nw')    
#create a mainframe
main_frame=LabelFrame(frame2)
main_frame.pack(fill='both',expand=1)
#create a canvas
canvas=Canvas(main_frame,width=800,height=500)
canvas.pack(side='left',fill='both',expand=1)

#add a scrollbar to canvas
scroll=ttk.Scrollbar(main_frame,orient='vertical',command=custom_yview)
scroll.pack(side='right',fill='y')
#configure the canvas
canvas.configure(yscrollcommand=scroll.set)
canvas.bind('<Configure>',lambda e:canvas.configure(scrollregion=canvas.bbox('all')))
canvas.create_image(0,0,image=bgp,anchor='nw')
#create another frame inside the canvas
frame2sub=LabelFrame(canvas)
#add that new frame to a window in the canvas
canvas.create_window((0,0),window=frame2sub,anchor='nw')
for i in range(30):
    Label(frame2sub,text='hi').pack()

#myc=Canvas(canvas,width=800,height=500)
#myc.pack(fill='both',expand='true')
#canvas.create_image(0,0,image=bgp,anchor='nw')

root.mainloop()
