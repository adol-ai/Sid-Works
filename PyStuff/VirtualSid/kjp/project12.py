'''from tkinter import *
root=Tk()
#creating label widget
mylabel=Label(root,text='world')
#showing label widget
mylabel.pack()
root.mainloop()'''

'''from tkinter import *
root=Tk()
mylabel1=Label(root,text='hey there')
mylabel2=Label(root,text="i'm bk eshwaran")
mylabel3=Label(root,text="          ")
mylabel1.grid(row=1,column=1)
mylabel2.grid(row=1,column=5)
mylabel3.grid(row=1,column=2)
root.mainloop()'''

'''from tkinter import *
root=Tk()
mylabel1=Label(root,text='hey there').grid(row=0,column=2)
mylabel2=Label(root,text="i'm bk eshwaran").grid(row=1,column=1)
mylabel3=Label(root,text="          ").grid(row=1,column=2)
root.mainloop()'''


'''from tkinter import *
root=Tk()
mybutton=Button(root,text='click me',state='disabled')
mybutton.pack()
root.mainloop()'''

'''from tkinter import *
root=Tk()
mybutton=Button(root,text='click me',padx=50,pady=50)
mybutton.pack()
root.mainloop()'''

'''from tkinter import *
root=Tk()
def myclick():
    mylabel=Label(root,text='you are a david')
    mylabel.pack()
    return

mybutton=Button(root,text='click me',padx=50,pady=50,command=myclick,fg='orange',bg='black')
mybutton.pack()
root.mainloop()'''

'''from tkinter import *
root=Tk()
e=Entry(root,width=50,borderwidth=50,bg='black',fg='red')
e.pack()
e.get()
e.insert(2,'k')

def myclick():
    a='hello '+e.get()
    mylabel=Label(root,text=a)
    mylabel.pack()
    return

mybutton=Button(root,text='click me',padx=50,pady=50,command=myclick,fg='orange',bg='black')
mybutton.pack()

root.mainloop()'''


'''
from tkinter import *
root=Tk()

e=Entry(root,width=20,borderwidth=10,fg='orange',bg='black')
e.grid(row=1,column=1,columnspan=4,padx=30,pady=10)

def buttonclick(n):
    first=e.get()
    a=len(e.get())
    e.delete(0,a)
    e.insert(0,str(first)+str(n))
    return
def buttonclear():
    e.delete(0,END)
    return

def buttonadd():
    f=e.get()
    global f_num
    global math
    math='addition'
    f_num=f
    e.delete(0,END)    
    return
def buttonsubtract():
    f=e.get()
    global f_num
    global math
    math='subtraction'
    f_num=f
    e.delete(0,END)    
    return
def buttonmultiply():
    f=e.get()
    global f_num
    global math
    math='multiplication'
    f_num=f
    e.delete(0,END)    
    return
def buttondivide():
    f=e.get()
    global f_num
    global math
    math='division'
    f_num=f
    e.delete(0,END)    
    return
def buttonequal():
    secondnumber=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,int(f_num)+int(secondnumber))
    if math=="subtraction":
        e.insert(0,int(f_num)-int(secondnumber))
    if math=="multiplication":
        e.insert(0,int(f_num)*int(secondnumber))
    if math=="division":
        e.insert(0,int(f_num)/int(secondnumber))
    return

button_1=Button(root,text="1",padx=20,pady=10,command=lambda:buttonclick('1')).grid(row=4,column=1)
button_2=Button(root,text="2",padx=20,pady=10,command=lambda:buttonclick('2')).grid(row=4,column=2)
button_3=Button(root,text="3",padx=20,pady=10,command=lambda:buttonclick('3')).grid(row=4,column=3)

button_4=Button(root,text="4",padx=20,pady=10,command=lambda:buttonclick('4')).grid(row=3,column=1)
button_5=Button(root,text="5",padx=20,pady=10,command=lambda:buttonclick('5')).grid(row=3,column=2)
button_6=Button(root,text="6",padx=20,pady=10,command=lambda:buttonclick('6')).grid(row=3,column=3)

button_7=Button(root,text="7",padx=20,pady=10,command=lambda:buttonclick('7')).grid(row=2,column=1)
button_8=Button(root,text="8",padx=20,pady=10,command=lambda:buttonclick('8')).grid(row=2,column=2)
button_9=Button(root,text="9",padx=20,pady=10,command=lambda:buttonclick('9')).grid(row=2,column=3)

button_0=Button(root,text="0",padx=45,pady=10,command=lambda:buttonclick(0)).grid(row=5,column=1,columnspan=2)
button_dot=Button(root,text=".",padx=20,pady=10,command=lambda:buttonclick('.')).grid(row=5,column=3,columnspan=1)

button_clear=Button(root,text="clear",padx=60,pady=10,command=buttonclear).grid(row=6,column=1,columnspan=3)

button_add=Button(root,text="+",padx=20,pady=10,command=buttonadd).grid(row=2,column=4,columnspan=1)
button_sub=Button(root,text="-",padx=20,pady=10,command=buttonsubtract).grid(row=3,column=4,columnspan=1)
button_mul=Button(root,text="*",padx=20,pady=10,command=buttonmultiply).grid(row=4,column=4,columnspan=1)
button_div=Button(root,text="/",padx=20,pady=10,command=buttondivide).grid(row=5,column=4,columnspan=1)
button_equal=Button(root,text="=",padx=20,pady=10,command=buttonequal).grid(row=6,column=4,columnspan=1)




root.mainloop()'''

'''from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title('icons,images,exit buttons')
root.iconbitmap('c:/#1eScanProtected.docx')

img=ImageTk.PhotoImage(Image.open(''))



button_quit=Button(root,text='exit program',command=root.quit)
button_quit.pack()


root.mainloop()'''
'''
from tkinter import *
from PIL import ImageTk,Image
import time
root=Tk()
root.title('icons,images,exit buttons')


img1=ImageTk.PhotoImage(Image.open('tkimages/picture168.jpg'))
img2=ImageTk.PhotoImage(Image.open('tkimages/picture169.jpg'))
img3=ImageTk.PhotoImage(Image.open('tkimages/picture170.jpg'))
imglist=[img1,img2,img3]
label=Label(image=img1)
label.grid(row=1,column=1,columnspan=3)
def forward(imagenumber):
    global label
    global buttonforward
    global buttonback
    label.grid_forget()
    label=Label(image=imglist[imagenumber+1])
    label.grid(row=1,column=1,columnspan=3)
    buttonforward=Button(root,text='>>',command=lambda:forward(imagenumber+1))
    buttonforward.grid(row=2,column=3)
    buttonback=Button(root,text='<<',command=lambda:back(imagenumber+1))
    buttonback.grid(row=2,column=1)
    if imagenumber==1:
        buttonforward=Button(root,text='>>',command=lambda:forward(imagenumber+1),state=DISABLED)
        buttonforward.grid(row=2,column=3)

def back(imagenumber):
    global label
    global buttonforward
    global buttonback
    label.grid_forget()
    label=Label(image=imglist[imagenumber-1])
    label.grid(row=1,column=1,columnspan=3)
    buttonforward=Button(root,text='>>',command=lambda:forward(imagenumber-1))
    buttonforward.grid(row=2,column=3)
    buttonback=Button(root,text='<<',command=lambda:back(imagenumber-1))
    buttonback.grid(row=2,column=1)
    if imagenumber==1:
        buttonback=Button(root,text='<<',state='disabled')
        buttonback.grid(row=2,column=1)
    
        
buttonback=Button(root,text='<<',command=back,state='disabled')
buttonforward=Button(root,text='>>',command=lambda:forward(0))

button_quit=Button(root,text='exit program',command=root.quit)
buttonback.grid(row=2,column=1)
button_quit.grid(row=2,column=2)
buttonforward.grid(row=2,column=3)

root.mainloop()'''
'''
from tkinter import *
from PIL import ImageTk,Image
import time
root=Tk()
root.title('icons,images,exit buttons')


img1=ImageTk.PhotoImage(Image.open('tkimages/1.jpg'))
img2=ImageTk.PhotoImage(Image.open('tkimages/2.jpg'))
img3=ImageTk.PhotoImage(Image.open('tkimages/3.jpg'))
img4=ImageTk.PhotoImage(Image.open('tkimages/4.jpg'))
img5=ImageTk.PhotoImage(Image.open('tkimages/5.jpg'))
img6=ImageTk.PhotoImage(Image.open('tkimages/6.jpg'))
img7=ImageTk.PhotoImage(Image.open('tkimages/7.jpg'))
img8=ImageTk.PhotoImage(Image.open('tkimages/8.jpg'))
img9=ImageTk.PhotoImage(Image.open('tkimages/9.jpg'))


imglist=[img1,img2,img3,img4,img5,img6,img7,img8,img9]
a=len(imglist)
label=Label(image=img1)
label.grid(row=1,column=1,columnspan=3)
status=Label(root,text='image 1 out of 5',relief='sunken',anchor=E)
status.grid(row=3,column=1,columnspan=3,sticky=W+E)

def forward(imagenumber):
    global label
    global buttonforward
    global buttonback
    label.grid_forget()
    label=Label(image=imglist[imagenumber+1])
    label.grid(row=1,column=1,columnspan=3)
    buttonforward=Button(root,text='>>',command=lambda:forward(imagenumber+1))
    buttonforward.grid(row=2,column=3)
    buttonback=Button(root,text='<<',command=lambda:back(imagenumber+1))
    buttonback.grid(row=2,column=1)
    status=Label(root,text='image '+str(imagenumber+2)+' out of 5',relief='sunken',anchor=E)
    status.grid(row=3,column=1,columnspan=3,sticky=W+E)

    if imagenumber==a-2:
        buttonforward=Button(root,text='>>',command=lambda:forward(imagenumber+1),state=DISABLED)
        buttonforward.grid(row=2,column=3)

def back(imagenumber):
    global label
    global buttonforward
    global buttonback
    label.grid_forget()
    label=Label(image=imglist[imagenumber-1])
    label.grid(row=1,column=1,columnspan=3)
    buttonforward=Button(root,text='>>',command=lambda:forward(imagenumber-1))
    buttonforward.grid(row=2,column=3)
    buttonback=Button(root,text='<<',command=lambda:back(imagenumber-1))
    buttonback.grid(row=2,column=1)
    status=Label(root,text='image '+str(imagenumber)+' out of 5',relief='sunken',anchor=E)
    status.grid(row=3,column=1,columnspan=3,sticky=W+E)

    if imagenumber==1:
        buttonback=Button(root,text='<<',state='disabled')
        buttonback.grid(row=2,column=1)
    
        
buttonback=Button(root,text='<<',command=back,state='disabled')
buttonforward=Button(root,text='>>',command=lambda:forward(0))

button_quit=Button(root,text='exit program',command=root.quit)
buttonback.grid(row=2,column=1)
button_quit.grid(row=2,column=2)
buttonforward.grid(row=2,column=3)

root.mainloop()
'''
#relief maybe flat, groove, raised, ridge, solid, or sunken
#frames
'''from tkinter import *
root=Tk()
frame=LabelFrame(root,text="im",padx=10,pady=10,bg='black',fg='orange',bd=20)
frame.pack()
button=Button(frame,text='yes',padx=50,pady=50,relief='solid').grid(row=1,column=1)
button=Button(frame,text='no',padx=50,pady=50,relief='raised').grid(row=1,column=2)

root.mainloop()
'''

#radiobutton
'''
from tkinter import *
root=Tk()
#defining tkintervariable
k=IntVar()
k.set(2)

def clicked(value):
    global label
    label.pack_forget()
    label=Label(root,text=value)
    label.pack()

Radiobutton(root,text='option 1',variable=k,value=1,command=lambda:clicked(k.get())).pack()
Radiobutton(root,text='option 2',variable=k,value=2,command=lambda:clicked(k.get())).pack()

label=Label(root,text=k.get())
label.pack()



root.mainloop()
'''
'''
from tkinter import *
root=Tk()
#defining tkintervariable
k=StringVar()
modes=[('michael','m'),('david','d'),('phillips','p'),('bela','b')]
k.set('m')

for i in modes:
    Radiobutton(root,text=i[0],variable=k,value=i[1]).pack(anchor=W)

root.mainloop()
'''
#messagebox
'''
from tkinter import *
from tkinter import messagebox

root=Tk()
#showinfo,showwarning,showerror,askquestion,askokcancel,askyesno
def popup():
    response=messagebox.askokcancel('this my popup','are you a david')
    label=Label(root,text=response).pack()
    if response=='yes':
        label=Label(root,text='you are a shameless fellow').pack()
    else:
        label=Label(root,text='you have some sense').pack()
        

Button(root,text='popup',command=popup).pack()
root.mainloop()'''

#new window
'''
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
root=Tk()
def open_():
    global top
    global label
    global img
    top=Toplevel()
    img=ImageTk.PhotoImage(Image.open('tkimages/picture170.jpg'))
    label=Label(top,image=img).pack()
    btn=Button(top,text='close window',command=top.quit).pack()
buttton=Button(root,text='open second window',command=open_).pack()
root.mainloop()
'''
#open files and dialog box
'''
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog

root=Tk()
def open_():
    global myimage
    root.filename=filedialog.askopenfilename(initialdir='gui/images',title='opening files',filetype=(('png files','*.png'),('jpg files','*.jpg')))
    label=Label(root,text=root.filename).pack()
    myimage=ImageTk.PhotoImage(Image.open(root.filename))
    imagelabel=Label(root,image=myimage).pack()

btn=Button(root,text='open file',command=open_).pack()
root.mainloop()
'''

#sliders
'''
from tkinter import *

root=Tk()
root.title('sliders')
root.geometry('220x200+250+250')
vertical=Scale(root,from_=200,to=400)
vertical.pack(side=RIGHT)
horizontal=Scale(root,from_=100,to=400,orient='horizontal')
horizontal.pack(side=BOTTOM)
def slide():
    label=Label(root,text=horizontal.get()).pack()
    root.geometry(str(horizontal.get())+'x'+str(vertical.get()))
    return
label=Label(root,text=horizontal.get()).pack()
btn=Button(root,text='click me',command=slide).pack()

root.mainloop()
'''

'''from tkinter import *
root=Tk()


def show():
    label=Label(root,text=var.get()).pack()

var=StringVar()
c=Checkbutton(root,text='ensure that you are a supporter of david',variable=var,onvalue='david',offvalue='michael')
c.deselect()
c.pack()
button=Button(root,text='show selction',command=show)
button.pack()








root.mainloop()
'''

#drop down menu
'''from tkinter import *
root=Tk()

var=StringVar()
var.set('monday')
d=OptionMenu(root,var,'monday','tuesday','wednesday')

d.pack()





root.mainloop()
'''

'''
#drop down menus using list
from tkinter import *
root=Tk()

var=StringVar()
var.set('d')
options=['monday','tuesday','wednesday','thrusday']
d=OptionMenu(root,var,*options)

d.pack()





root.mainloop()
'''
'''

a=open("customerdetails.txt",'r')
b=a.read()
d_=eval(b)
print(d_)

    
print(l['hari@gmail.com'][2])
'''
'''
#scrollbar
from tkinter import *
from tkinter import ttk
root=Tk()

#create a mainframe
main_frame=LabelFrame(root)
main_frame.pack(fill='both',expand=1)
#create a canvas
canvas=Canvas(main_frame)
canvas.pack(side='left',fill='both',expand=1)
#add a scrollbar to canvas
scroll=ttk.Scrollbar(main_frame,orient='vertical',command=canvas.yview)
scroll.pack(side='right',fill='y')
#configure the canvas
canvas.configure(yscrollcommand=scroll.set)
canvas.bind('<Configure>',lambda e:canvas.configure(scrollregion=canvas.bbox('all')))

#create another frame inside the canvas
frame2=LabelFrame(canvas)
#add that new frame to a window in the canvas
canvas.create_window((0,0),window=frame2,anchor='nw')

frame3=LabelFrame(frame2)
frame3.grid(row=1,column=1)
def k():
    for i in range(1,10):
        Button(frame2,text='button'+str(i)).grid(row=i,column=i)
    for i in range(10,20):
        Button(frame3,text='button'+str(i)).grid(row=i,column=i)
k()
root.mainloop()

'''
'''
from tkinter import *
from tkinter import colorchooser

root=Tk()

color=colorchooser.askcolor()
print(color)

root.mainloop'''

from tkinter import *
from PIL import ImageTk,Image
root=Tk()
login_btn=ImageTk.PhotoImage(Image.open('tkimages/11.jpg'))


def thing():
    print('david')
button=Button(root,image=login_btn,command=thing)
button.pack()




root.mainloop()












