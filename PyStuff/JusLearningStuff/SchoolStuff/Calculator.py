from tkinter import *

tk=Tk()
tk.title("Calculator")
operator=""
text_type=StringVar()

def btnclick(num):
    global operator
    operator=operator+ str(num)
    text_type.set(operator)

def btnclear():
    global operator
    operator=""
    text_type.set(operator)

def btnequal():
    global operator
    total=str(eval(operator))
    text_type.set(total)
    operator=total

dis=Entry(tk,font=('Courier New', 20, 'bold'), textvariable=text_type, bd=20,
          insertwidth=4, bg="white", justify="right").grid(columnspan=4)
btn7=Button(tk,padx=16,bd=8,fg="red", font=('Courier New', 20, 'bold'),
            text='7', bg="white",command=lambda: btnclick(7)).grid(row=1,column=0)
btn8=Button(tk,padx=16,bd=8,fg="red", font=('Courier New', 20, 'bold'),
            text='8', bg="white",command=lambda: btnclick(8)).grid(row=1,column=1)
btn9=Button(tk,padx=16,bd=8,fg="red", font=('Courier New', 20, 'bold'),
            text='9', bg="white",command=lambda: btnclick(9)).grid(row=1,column=2)
add=Button(tk,padx=16,bd=8,fg="red", font=('Courier New', 20, 'bold'),
            text='+', bg="white",command=lambda: btnclick('+')).grid(row=1,column=3)

btn4=Button(tk,padx=16,bd=8,fg="red", font=('Courier New', 20, 'bold'),
            text='4', bg="white",command=lambda: btnclick(4)).grid(row=2,column=0)
btn5=Button(tk,padx=16,bd=8,fg="red", font=('Courier New', 20, 'bold'),
            text='5', bg="white",command=lambda: btnclick(5)).grid(row=2,column=1)
btn6=Button(tk,padx=16,bd=8,fg="red", font=('Courier New', 20, 'bold'),
            text='6', bg="white",command=lambda: btnclick(6)).grid(row=2,column=2)
sub=Button(tk,padx=16,bd=8,fg="red", font=('Courier New', 20, 'bold'),
            text='-', bg="white",command=lambda: btnclick('-')).grid(row=2,column=3)

btn1=Button(tk,padx=16,bd=8,fg="red", font=('Courier New', 20, 'bold'),
            text='1', bg="white",command=lambda: btnclick(1)).grid(row=3,column=0)
btn2=Button(tk,padx=16,bd=8,fg="red", font=('Courier New', 20, 'bold'),
            text='2', bg="white",command=lambda: btnclick(2)).grid(row=3,column=1)
btn3=Button(tk,padx=16,bd=8,fg="red", font=('Courier New', 20, 'bold'),
            text='3', bg="white",command=lambda: btnclick(3)).grid(row=3,column=2)
mul=Button(tk,padx=16,bd=8,fg="red", font=('Courier New', 20, 'bold'),
            text='x', bg="white",command=lambda: btnclick('*')).grid(row=3,column=3)

clear=Button(tk,padx=16,bd=8,fg="red", font=('Courier New', 20, 'bold'),
            text='C', bg="white", command=btnclear).grid(row=4,column=0)
btn0=Button(tk,padx=16,bd=8,fg="red", font=('Courier New', 20, 'bold'),
            text='0', bg="white",command=lambda: btnclick(0)).grid(row=4,column=1)
equal=Button(tk,padx=16,bd=8,fg="red", font=('Courier New', 20, 'bold'),
            text='=', bg="white", command=btnequal).grid(row=4,column=2)
div=Button(tk,padx=16,bd=8,fg="red", font=('Courier New', 20, 'bold'),
            text='÷', bg="white",command=lambda: btnclick('/')).grid(row=4,column=3)

tk.mainloop()
    
