import requests
from datetime import *
from bs4 import BeautifulSoup
import math
import os

w='1234'+'5678'
__f__=open("SidData.txt",'w+')
__f__.write(w)
_p_=__f__.read()
__f__.close()
#os.remove('SidData.txt')

'''r=requests.get("https://www.daysoftheyear.com/")
s=BeautifulSoup(r.content,"html.parser")
n=s.find(class_='card__title heading')
t=datetime.now()
d=n.text
d_=t.strftime("%H")
print(d_)
d_=t.strftime("%A")
print(d_)'''

'''while True:
    q_=str(input("qwerty:"))
    l=q_.split()
    _x_=[]
    x_=[]
    y_=[]
    z_=[]
    if ("min" in q_ and "sec" in q_) and (" h" not in q_ and "day" not in q_ and "week" not in q_ and "month" not in q_ and "year" not in q_):
        for x in q_:
            for y in x:
                if y.isdigit():
                    x_.append(y)
        n=int(''.join(x_))
        for i in l:
            if "min" in i:
                j=l.index(i)
            elif "sec" in i:
                k=l.index(i)
        if k>j:
            p=n*60
        elif j>k:
            p=n/60
        print(p)
    if ("h" in q_ and "sec" in q_) and ("min" not in q_ and "day" not in q_ and "week" not in q_ and "month" not in q_ and "year" not in q_):
        for x in q_:
            for y in x:
                if y.isdigit():
                    x_.append(y)
        n=int(''.join(x_))
        for i in l:
            if "h" in i:
                j=l.index(i)
            elif "sec" in i:
                k=l.index(i)
        if k>j:
            p=n*60*60
        elif j>k:
            p=n/(60*60)
            if n%(60*60)!=0:
                if p>1:
                    p_=math.ceil(p)-1
                    d=round((p-p_)*(60))
                else:
                    p_=p
                    d=round((p_)*(60))
                print(d)
                print(p_,"Hours &",d,"Minutes, But to be Accurate",p,"Hours")
            else:
                print(int(p))
    if ("day" in q_ and "sec" in q_) and ("min" not in q_ and " h" not in q_ and "week" not in q_ and "month" not in q_ and "year" not in q_):
        for x in q_:
            for y in x:
                if y.isdigit():
                    x_.append(y)
        n=int(''.join(x_))
        for i in l:
            if "day" in i:
                j=l.index(i)
            elif "sec" in i:
                k=l.index(i)
        if k>j:
            p=n*60*60*24
        elif j>k:
            p=n/(60*60*24)
            if n%(60*60*24)!=0:
                if p>1:
                    p_=math.ceil(p)-1
                    d=round((p-p_)*(24))
                else:
                    p_=p
                    d=round((p_)*(24))
                print(d)
                print(p_,"Days &",d,"Hours, But to be Accurate",p,"Days")
            else:
                print(int(p))
        print(p)
    if ("month" in q_ and "sec" in q_) and ("min" not in q_ and " h" not in q_ and "day" not in q_ and "week" not in q_ and "year" not in q_):
        for x in q_:
            for y in x:
                if y.isdigit():
                    x_.append(y)
        n=int(''.join(x_))
        for i in l:
            if "month" in i:
                j=l.index(i)
            elif "sec" in i:
                k=l.index(i)
        if k>j:
            p=n*60*60*24*30
        elif j>k:
            p=n/(60*60*24*30)
            print(p)
            if n%(60*60*24*30)!=0:
                if p>1:
                    p_=math.ceil(p)-1
                    d=round((p-p_)*(30))
                else:
                    p_=p
                    d=round(p_*(30))
                print(d)
                print(p_,"Months &",d,"Days, But to be Accurate",p,"Months")
            else:
                print(int(p))
        print(p)
    if ("year" in q_ and "sec" in q_) and ("min" not in q_ and " h" not in q_ and "day" not in q_ and "week" not in q_ and "month" not in q_):
        for x in q_:
            for y in x:
                if y.isdigit():
                    x_.append(y)
        n=int(''.join(x_))
        for i in l:
            if "year" in i:
                j=l.index(i)
            elif "sec" in i:
                k=l.index(i)
        if k>j:
            p=n*60*60*24*30*365
        elif j>k:
            p=n/(60*60*24*30*365)
            print(p)
            if n%(60*60*24*30*365)!=0:
                if p>1:
                    p_=math.ceil(p)-1
                    d=round((p-p_)*(365))
                else:
                    p_=p
                    d=round(p_*(365))
                print(d)
                print(p_,"Years &",d,"Months, But to be Accurate",p,"Years")
            else:
                print(int(p))
        print(p)
    elif ("min" in q_ and "h" in q_) and ("sec" not in q_ and "day" not in q_ and "week" not in q_ and "month" not in q_ and "year" not in q_):
        for x in q_:
            for y in x:
                if y.isdigit():
                    x_.append(y)
        n=int(''.join(x_))
        for i in l:
            if " h" in i:
                j=l.index(i)
            elif "min" in i:
                k=l.index(i)
        if k>j:
            p=n*60
        elif j>k:
            p=n/60
        print(p)
    if ("day" in q_ and "min" in q_) and ("sec" not in q_ and " h" not in q_ and "week" not in q_ and "month" not in q_ and "year" not in q_):
        for x in q_:
            for y in x:
                if y.isdigit():
                    x_.append(y)
        n=int(''.join(x_))
        for i in l:
            if "day" in i:
                j=l.index(i)
            elif "min" in i:
                k=l.index(i)
        if k>j:
            p=n*60*24
        elif j>k:
            p=n/(60*24)
            if n%(60*24)!=0:
                if p>1:
                    p_=math.ceil(p)-1
                    d=round((p-p_)*(24))
                else:
                    p_=p
                    d=round((p_)*(24))
                print(d)
                print(p_,"Days &",d,"Hours, But to be Accurate",p,"Days")
            else:
                print(int(p))
        print(p)
    if ("month" in q_ and "min" in q_) and ("sec" not in q_ and " h" not in q_ and "day" not in q_ and "week" not in q_ and "year" not in q_):
        for x in q_:
            for y in x:
                if y.isdigit():
                    x_.append(y)
        n=int(''.join(x_))
        for i in l:
            if "month" in i:
                j=l.index(i)
            elif "min" in i:
                k=l.index(i)
        if k>j:
            p=n*60*24*30
        elif j>k:
            p=n/(60*24*30)
            print(p)
            if n%(60*24*30)!=0:
                if p>1:
                    p_=math.ceil(p)-1
                    d=round((p-p_)*(30))
                else:
                    p_=p
                    d=round(p_*(30))
                print(d)
                print(p_,"Months &",d,"Days, But to be Accurate",p,"Months")
            else:
                print(int(p))
        print(p)
    if ("year" in q_ and "min" in q_) and ("sec" not in q_ and " h" not in q_ and "day" not in q_ and "week" not in q_ and "month" not in q_):
        for x in q_:
            for y in x:
                if y.isdigit():
                    x_.append(y)
        n=int(''.join(x_))
        for i in l:
            if "year" in i:
                j=l.index(i)
            elif "min" in i:
                k=l.index(i)
        if k>j:
            p=n*60*24*30*365
        elif j>k:
            p=n/(60*24*30*365)
            print(p)
            if n%(60*24*30*365)!=0:
                if p>1:
                    p_=math.ceil(p)-1
                    d=round((p-p_)*(365))
                else:
                    p_=p
                    d=round(p_*(365))
                print(d)
                print(p_,"Years &",d,"Months, But to be Accurate",p,"Years")
            else:
                print(int(p))
        print(p)
    elif ("h" in q_ and "day" in q_) and ("sec" not in q_ and "min" not in q_ and "week" not in q_ and "month" not in q_ and "year" not in q_):
        for x in q_:
            for y in x:
                if y.isdigit():
                    x_.append(y)
        n=int(''.join(x_))
        for i in l:
            if "day" in i:
                j=l.index(i)
            elif " h" in i:
                k=l.index(i)
        if k>j:
            p=n*24
        elif j>k:
            p=n/24
        print(p)
    if ("month" in q_ and "h" in q_) and ("sec" not in q_ and "min" not in q_ and "day" not in q_ and "week" not in q_ and "year" not in q_):
        for x in q_:
            for y in x:
                if y.isdigit():
                    x_.append(y)
        n=int(''.join(x_))
        for i in l:
            if "month" in i:
                j=l.index(i)
            elif "hr" in i or "ho" in i:
                k=l.index(i)
        if k>j:
            p=n*24*30
        elif j>k:
            p=n/(24*30)
            print(p)
            if n%(24*30)!=0:
                if p>1:
                    p_=math.ceil(p)-1
                    d=round((p-p_)*(30))
                else:
                    p_=p
                    d=round(p_*(30))
                print(d)
                print(p_,"Months &",d,"Days, But to be Accurate",p,"Months")
            else:
                print(int(p))
        print(p)
    if ("year" in q_ and "h" in q_) and ("sec" not in q_ and " h" not in q_ and "day" not in q_ and "week" not in q_ and "month" not in q_):
        for x in q_:
            for y in x:
                if y.isdigit():
                    x_.append(y)
        n=int(''.join(x_))
        for i in l:
            if "year" in i:
                j=l.index(i)
            elif "h" in i:
                k=l.index(i)
        if k>j:
            p=n*60*24*30*365
        elif j>k:
            p=n/(60*24*30*365)
            print(p)
            if n%(60*24*30*365)!=0:
                if p>1:
                    p_=math.ceil(p)-1
                    d=round((p-p_)*(365))
                else:
                    p_=p
                    d=round(p_*(365))
                print(d)
                print(p_,"Years &",d,"Months, But to be Accurate",p,"Years")
            else:
                print(int(p))
        print(p)
    elif ("sec" in q_ and "week" in q_) and ("min" not in q_ and "h" not in q_ and "day" not in q_ and "month" not in q_ and "year" not in q_):
        for x in q_:
            for y in x:
                if y.isdigit():
                    x_.append(y)
        n=int(''.join(x_))
        for i in l:
            if "week" in i:
                j=l.index(i)
            elif "sec" in i:
                k=l.index(i)
        if k>j:
            p=n*7*24*60*60
            print(p)
        elif j>k:
            p=n/(7*24*60*60)
            if n%(7*24*60*60)!=0:
                if p>1:
                    p_=math.ceil(p)-1
                    d=round((p-p_)*7)
                else:
                    p_=p
                    d=round((p_)*7)
                print(d)
                print(p_,"Weeks &",d,"Days, But to be Accurate",p,"Weeks")
            else:
                print(int(p))
    elif ("min" in q_ and "week" in q_) and ("sec" not in q_ and "h" not in q_ and "day" not in q_ and "month" not in q_ and "year" not in q_):
        for x in q_:
            for y in x:
                if y.isdigit():
                    x_.append(y)
        n=int(''.join(x_))
        for i in l:
            if "week" in i:
                j=l.index(i)
            elif "min" in i:
                k=l.index(i)
        if k>j:
            p=n*7*24*60
            print(p)
        elif j>k:
            p=n/(7*24*60)
            if n%(7*24*60)!=0:
                if p>1:
                    p_=math.ceil(p)-1
                    d=round((p-p_)*7)
                else:
                    p_=p
                    d=round((p_)*7)
                print(d)
                print(p_,"Weeks &",d,"Days, But to be Accurate",p,"Weeks")
            else:
                print(int(p))
    elif ("h" in q_ and "week" in q_) and ("sec" not in q_ and "min" not in q_ and "day" not in q_ and "month" not in q_ and "year" not in q_):
        for x in q_:
            for y in x:
                if y.isdigit():
                    x_.append(y)
        n=int(''.join(x_))
        for i in l:
            if "week" in i:
                j=l.index(i)
            elif "h" in i:
                k=l.index(i)
        if k>j:
            p=n*7*24
            print(p)
        elif j>k:
            p=n/(7*24)
            if n%(7*24)!=0:
                if p>1:
                    p_=math.ceil(p)-1
                    d=round((p-p_)*7)
                else:
                    p_=p
                    d=round((p_)*7)
                print(d)
                print(p_,"Weeks &",d,"Days, But to be Accurate",p,"Weeks")
            else:
                print(int(p))
    elif ("day" in q_ and "week" in q_) and ("sec" not in q_ and "min" not in q_ and " h" not in q_ and "month" not in q_ and "year" not in q_):
        for x in q_:
            for y in x:
                if y.isdigit():
                    x_.append(y)
        n=int(''.join(x_))
        for i in l:
            if "week" in i:
                j=l.index(i)
            elif "day" in i:
                k=l.index(i)
        if k>j:
            p=n*7
            print(p)
        elif j>k:
            p=n/7
            if n%7!=0:
                if p>1:
                    p_=math.ceil(p)-1
                    d=round((p-p_)*7)
                else:
                    p_=p
                    d=round((p_)*7)
                print(d)
                print(p_,"Weeks &",d,"Days, But to be Accurate",p,"Weeks")
            else:
                print(int(p))
    elif ("week" in q_ and "month" in q_) and ("sec" not in q_ and "min" not in q_ and " h" not in q_ and "day" not in q_ and "year" not in q_):
        for x in q_:
            for y in x:
                if y.isdigit():
                    x_.append(y)
        n=int(''.join(x_))
        for i in l:
            if "month" in i:
                j=l.index(i)
            elif "week" in i:
                k=l.index(i)
        if k>j:
            p=n*4
            print(p)
        elif j>k:
            p=n/4
            if n%4!=0:
                if p>1:
                    p_=math.ceil(p)-1
                    d=round((p-p_)*4)
                else:
                    p_=p
                    d=round((p_)*4)
                print(d)
                print(p_,"Months &",d,"Weeks, But to be Accurate",p,"Months")
            else:
                print(int(p))
    elif ("week" in q_ and "year" in q_) and ("sec" not in q_ and "min" not in q_ and " h" not in q_ and "day" not in q_ and "month" not in q_):
        for x in q_:
            for y in x:
                if y.isdigit():
                    x_.append(y)
        n=int(''.join(x_))
        for i in l:
            if "year" in i:
                j=l.index(i)
            elif "week" in i:
                k=l.index(i)
        if k>j:
            p=n*4*12
            print(p)
        elif j>k:
            p=n/(4*12)
            if n%(4*12)!=0:
                if p>1:
                    p_=math.ceil(p)-1
                    d=round((p-p_)*12)
                else:
                    p_=p
                    d=round((p_)*12)
                print(d)
                print(p_,"Years &",d,"Months, But to be Accurate",p,"Months")
            else:
                print(int(p))
    elif ("month" in q_ and "year" in q_) and ("sec" not in q_ and "min" not in q_ and " h" not in q_ and "day" not in q_ and "week" not in q_):
        print("QWERT")
        for x in q_:
            for y in x:
                y_.append(y)
                if y.isdigit():
                    x_.append(y)
        for z in x_:
            z_.append(y_.index(z))
        e=-1
        for u in z_:
            e+=1
            if u==e:
                _x_.append(y_[u])
            else:
                break
        print(y_)
        print(x_)
        print(z_)
        n=int(''.join(_x_))
        for i in l:
            if "year" in i:
                j=l.index(i)
            elif "month" in i:
                k=l.index(i)
        if k>j:
            p=n*12
            print(p)
        elif j>k:
            p=n/12
            if n%12!=0.0:
                if p>1:
                    p_=math.ceil(p)-1
                    d=round((p-p_)*12)
                else:
                    p_=p
                    d=round((p_)*12)
                print(d)
                print(p_,"Years &",d,"Months, But to be Accurate",p,"Years")
            else:
                print(int(p))'''

'''for x in q_:
                        for y in x:
                            y_.append(y)
                            if y.isdigit():
                                x_.append(y)
                    for z in x_:
                        z_.append(y_.index(z))
                    e=-1
                    for u in z_:
                        e+=1
                        if u==e:
                            _x_.append(y_[u])
                        else:
                            break
                    n=int(''.join(_x_))'''

'''while True:
    q_=str(input("qwerty:"))
    l=q_.split()
    x_=[]
    y_=[]
    if ("bin" in q_ and "oct" in q_) and ("dec" not in q_ and "hex" not in q_):
        for x in q_:
            for y in x:
                if y.isdigit():
                    x_.append(y)
        n=int(''.join(x_))
        for i in l:
            if "bin" in i:
                j=l.index(i)
            elif "oct" in i:
                k=l.index(i)
        if k>j:
            p=oct(int(str(n), 2))
            print("Octal Value:",p[2:])
        elif j>k:
            p=bin(int(str(n), 8))
            print("Binary Value:",p[2:])
    elif ("bin" in q_ and "hex" in q_) and ("dec" not in q_ and "oct" not in q_):
        for x in q_:
            for y in x:
                y_.append(y)
                if y.isdigit():
                    x_.append(y)
        h=(y_.index(x_[0]))+len(x_)
        if y_[h]=='a' or y_[h]=='b' or y_[h]=='c' or y_[h]=='d' or y_[h]=='e' or y_[h]=='f':
            x_.append(y_[h])
        n=''.join(x_)
        for i in l:
            if "bin" in i:
                j=l.index(i)
            elif "hex" in i:
                k=l.index(i)
        if k>j:
            p=hex(int(str(n), 2))
            print("Hexadecimal Value:",p[2:])
        elif j>k:
            p=bin(int(str(n), 16))
            print("Binary Value:",p[2:])
    elif (("bin" in q_ and "dec" in q_) or ("bin" in q_ and "dec" not in q_)) and ("oct" not in q_ and "hex" not in q_):
        for x in q_:
            for y in x:
                if y.isdigit():
                    x_.append(y)
        n=int(''.join(x_))
        if ("bin" in q_ and "dec" in q_):
            for i in l:
                if "bin" in i:
                    j=l.index(i)
                elif "dec" in i:
                    k=l.index(i)
            if k>j:
                p=int(str(n), 2)
                print("Decimal Value:",p)
            elif j>k:
                p=bin(int(n))
                print("Binary Value:",p[2:])
        else:
            p=bin(int(n))
            print("Binary Value:",p[2:])
    elif (("dec" in q_ and "oct" in q_) or ("oct" in q_ and "dec" not in q_)) and ("bin" not in q_ and "hex" not in q_):
        for x in q_:
            for y in x:
                if y.isdigit():
                    x_.append(y)
        n=int(''.join(x_))
        if "dec" in q_ and "oct" in q_:
            for i in l:
                if "dec" in i:
                    j=l.index(i)
                elif "oct" in i:
                    k=l.index(i)
            if k>j:
                p=oct(int(n))
                print("Octal Value:",p[2:])
            elif j>k:
                p=int(str(n), 8)
                print("Decimal Value:",p)
        else:
            p=oct(int(n))
            print("Octal Value:",p[2:])
    elif ("dec" in q_ and "hex" in q_) or ("dec" not in q_ and "hex" in q_) and ("bin" not in q_ and "oct" not in q_):
        for x in q_:
            for y in x:
                y_.append(y)
                if y.isdigit():
                    x_.append(y)
        h=(y_.index(x_[0]))+len(x_)
        if y_[h]=='a' or y_[h]=='b' or y_[h]=='c' or y_[h]=='d' or y_[h]=='e' or y_[h]=='f':
            x_.append(y_[h])
        n=''.join(x_)
        if " dec" in q_ and "hex" in q_:
            for i in l:
                if "dec" in i:
                    j=l.index(i)
                elif "hex" in i:
                    k=l.index(i)
            if k>j:
                p=hex(int(n))
                print("Hexadecimal Value:",p[2:])
            elif j>k:
                p=int(str(n), 16)
                print("Decimal Value:",p)
        else:
            p=hex(int(n))
            print("Hexadecimal Value:",p[2:])
    elif ("oct" in q_ and "hex" in q_) and ("dec" not in q_ and "bin" not in q_):
        for x in q_:
            for y in x:
                y_.append(y)
                if y.isdigit():
                    x_.append(y)
        h=(y_.index(x_[0]))+len(x_)
        if y_[h]=='a' or y_[h]=='b' or y_[h]=='c' or y_[h]=='d' or y_[h]=='e' or y_[h]=='f':
            x_.append(y_[h])
        n=''.join(x_)
        for i in l:
            if "oct" in i:
                j=l.index(i)
            elif "hex" in i:
                k=l.index(i)
        if k>j:
            p=hex(int(str(n), 8))
            print("Hexadecimal Value:",p[2:])
        elif j>k:
            p=oct(int(str(n), 16))
            print("Octal Value:",p[2:])
'''
'''
while True:
    q_=str(input("qwerty:"))
    l=q_.split()
    x_=[]
    elif ("faren" in q_ and "cel" in q_) and "kel" not in q_:
        for x in q_:
            for y in x:
                if y.isdigit():
                    x_.append(y)
        n=float(''.join(x_))
        for i in l:
            if "faren" in i:
                j=l.index(i)
            elif "cel" in i:
                k=l.index(i)
        if k>j:
            p=(n-32)*(5/9)
            print(p,"°Celsius")
        elif j>k:
            p=((n)*(9/5))+32
            print(p,"°Farenheit")
    elif ("kel" in q_ and "cel" in q_) and "faren" not in q_:
        for x in q_:
            for y in x:
                if y.isdigit():
                    x_.append(y)
        n=float(''.join(x_))
        for i in l:
            if "kel" in i:
                j=l.index(i)
            elif "cel" in i:
                k=l.index(i)
        if k>j:
            p=n-273.15
            print(p,"°Celsius")
        elif j>k:
            p=n+273.15
            print(p,"Kelvin")
    elif ("kel" in q_ and "faren" in q_) and "cel" not in q_:
        for x in q_:
            for y in x:
                if y.isdigit():
                    x_.append(y)
        n=float(''.join(x_))
        for i in l:
            if "faren" in i:
                j=l.index(i)
            elif "kel" in i:
                k=l.index(i)
        if k>j:
            p=(n-32)*(5/9)
            p_=p+273.15
            print(p_,"Kelvin")
        elif j>k:
            p=n-273.15
            p_=((p)*(9/5))+32
            print(p_,"°Farenheit")'''


'''while True:
    q_=input("qwerty:")
    if "+" not in q_ or "-" not in q_ or "/" in not q_ or "*" not in q_ or "plus" not in q_ or "add" not in q_ or "sub" not in q_ or "minus" not in q_ or "multi" not in q_ or "into" not in q_ or "div" not in q_ or "by" not in q_ or "x" not in q_: 
        l=q_.split()
        x_=[]
        y_=[]
        _x_=[]
        if ("what" in q_ or "value" in q_) and "factorial" in q_:
            for x in q_:
                for y in x:
                    if y.isdigit():
                        x_.append(y)
            n=eval(''.join(x_))
            print("The Factorial of",n,"is",math.factorial(n))
        elif ("what" in q_ or "value" in q_) and ("log" in q_ or ("natural" in q_ and "log" in q_)) and "base" not in q_:
            for x in q_:
                for y in x:
                    if y.isdigit():
                        x_.append(y)
            n=eval(''.join(x_))
            print("The Logarithm of",n,"is",math.log(n))
        elif ("what" in q_ or "value" in q_) and ("log" in q_ and "base" in q_):
            if "base e" in q_ or ("natural" in q_ and "base" in q_):
                for x in q_:
                    for y in x:
                        if y.isdigit():
                            _x_.append(y)
                n=eval(''.join(_x_))
                print("The Logarithm of",n,"is",math.log(n))
            else:
                for i in l:
                    if "base" in i:
                        j=l.index(i)
                    elif "log" in i:
                        k=l.index(i)
                if k>j:
                    w_=''.join(l[k:])
                    _w_=''.join(l[:k])
                    for x in w_:
                        for y in x:
                            if y.isdigit():
                                x_.append(y)
                    for x in _w_:
                        for y in x:
                            if y.isdigit():
                                y_.append(y)
                    n=eval(''.join(x_))
                    n_=eval(''.join(y_))
                    print("The Logarithm of",n,"to the Base",n_,"is",math.log(n,n_))
                elif j>k:
                    w_=''.join(l[:j])
                    _w_=''.join(l[j:])
                    for x in w_:
                        for y in x:
                            if y.isdigit():
                                x_.append(y)
                    for x in _w_:
                        for y in x:
                            if y.isdigit():
                                y_.append(y)
                    n=eval(''.join(x_))
                    n_=eval(''.join(y_))
                    print("The Logarithm of",n,"to the Base",n_,"is",math.log(n,n_))
        elif ("what" in q_ or "value" in q_) and "root" in q_ and "square" in q_:
            for x in q_:
                for y in x:
                    if y.isdigit():
                        x_.append(y)
            n=eval(''.join(x_))
            for i in l:
                if "square" in i:
                    j=l.index(i)
                elif "root" in i:
                    k=l.index(i)
            if j>k:
                print("The SquareRoot value is",math.sqrt(n))
            else:
                print("The SquareRoot of",n,"is",math.sqrt(n))
        elif ("what" in q_ or "value" in q_) and "square" in q_ and ("area" not in q_ or "volume" not in q_ and "root" not in q_ and "form" not in q_):
            for x in q_:
                for y in x:
                    if y.isdigit():
                        x_.append(y)
            n=eval(''.join(x_))
            print("The Square of",n,"is",math.pow(n,2))
        elif ("what" in q_ or "value" in q_) and "cube" in q_ and ("area" not in q_ or "volume" not in q_ and "root" not in q_ and "form" not in q_):
            for x in q_:
                for y in x:
                    if y.isdigit():
                        x_.append(y)
            n=eval(''.join(x_))
            print("The Cube of",n,"is",math.pow(n,3))
        elif ("what" in q_ or "value" in q_) and "power" in q_:
            w=l.index("power")
            w_=''.join(l[w:])
            _w_=''.join(l[:w])
            for x in _w_:
                for y in x:
                    if y.isdigit():
                        x_.append(y)
            for x in w_:
                for y in x:
                    if y.isdigit():
                        y_.append(y)
            n=eval(''.join(x_))
            n_=eval(''.join(y_))
            print("The Value of",n,"Power",n_,"is",math.pow(n,n_))
        elif ("what" in q_ or "value" in q_) and "sin" in q_:
            for x in q_:
                for y in x:
                    if y.isdigit():
                        x_.append(y)
            n=eval(''.join(x_))
            if "rad" not in q_:
                n_=math.radians(n)
            else:
                n_=n
            print("The Value of Sine",n_,"radians is",math.sin(n_))
        elif ("what" in q_ or "value" in q_) and "cosec" in q_:
            for x in q_:
                for y in x:
                    if y.isdigit():
                        x_.append(y)
            n=eval(''.join(x_))
            if "rad" not in q_:
                n_=math.radians(n)
            else:
                n_=n
            print("The Value of Cosecant",n_,"radians is",1/math.sin(n_))
        elif ("what" in q_ or "value" in q_) and "cos" in q_:
            for x in q_:
                for y in x:
                    if y.isdigit():
                        x_.append(y)
            n=eval(''.join(x_))
            if "rad" not in q_:
                n_=math.radians(n)
            else:
                n_=n
            print("The Value of Cosine",n_,"radians is",math.cos(n_))
        elif ("what" in q_ or "value" in q_) and "tan" in q_:
            for x in q_:
                for y in x:
                    if y.isdigit():
                        x_.append(y)
            n=eval(''.join(x_))
            if "rad" not in q_:
                n_=math.radians(n)
            else:
                n_=n
            print("The Value of Tan",n_,"radians is",math.tan(n_))
        elif ("what" in q_ or "value" in q_) and "sec" in q_:
            for x in q_:
                for y in x:
                    if y.isdigit():
                        x_.append(y)
            n=eval(''.join(x_))
            if "rad" not in q_:
                n_=math.radians(n)
            else:
                n_=n
            print("The Value of Secant",n_,"radians is",1/math.cos(n_))
        elif ("what" in q_ or "value" in q_) and "cot" in q_:
            for x in q_:
                for y in x:
                    if y.isdigit():
                        x_.append(y)
            n=eval(''.join(x_))
            if "rad" not in q_:
                n_=math.radians(n)
            else:
                n_=n
            print("The Value of Cotan",n_,"radians is",1/math.tan(n_))'''

'''while True:
    q_=input("Qwerty:")
    if ("+" in q_ or "plus" in q_ or "add" in q_ or ("add" in q_ and ("and" in q_ or "&" in q_)) and ("-" not in q_ and "/" not in q_ and "*" not in q_ and "sub" not in q_ and "minus" not in q_ and "multi" not in q_ and "into" not in q_ and "div" not in q_ and "by" not in q_ and "x" not in q_)):
        l=q_.split()
        x_=[]
        y_=[]
        _x_=[]
        z='p'
        if "+" in q_:
            for i in l:
                if "+" in i:
                    k=l.index(i)
                else:
                    pass
            if len(l[k])>1:
                k_=l[k]
                if k_[0].isdigit() and k_[len(k_)-1].isdigit():
                    print("It is",eval(k_))
                elif k_[0].isdigit() and not(k_[len(k_)-1].isdigit()):
                    w=l[k+1:]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            y_.append(x)
                    n=eval(''.join(x_))
                    n_=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n+n_)
                elif not(k_[0].isdigit()) and k_[len(k_)-1].isdigit():
                    w=l[:k]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    print(y_)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n+n_)
            else:
                w=l[:k]
                w_=l[k:]
                e=''.join(w)
                e_=''.join(w_)
                for x in e:
                    if "-" in x:
                        z_='n'
                    if x.isdigit():
                        x_.append(x)
                for x in e_:
                    if "-" in x:
                        z='n'
                    if x.isdigit():
                        y_.append(x)
                n_=eval(''.join(x_))
                n=eval(''.join(y_))
                if z=='n':
                    n=-n
                if z_=='n':
                    n_=-n_
                print("It is",n+n_)
        elif "plus" in q_:
            for i in l:
                if "plus" in i:
                    k=l.index(i)
                else:
                    pass
            if len(l[k])>4:
                k_=l[k]
                if k_[0].isdigit() and k_[len(k_)-1].isdigit():
                    o=k_.index('p')
                    w=k_[:o]
                    w_=k_[o:]
                    e=''.join(w)
                    e_=''.join(w_)
                    for x in e:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in e_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n+n_)
                elif k_[0].isdigit() and not(k_[len(k_)-1].isdigit()):
                    w=l[k+1:]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            y_.append(x)
                    n=eval(''.join(x_))
                    n_=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n+n_)
                elif not(k_[0].isdigit()) and k_[len(k_)-1].isdigit():
                    w=l[:k]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n+n_)
            else:
                w=l[:k]
                w_=l[k:]
                e=''.join(w)
                e_=''.join(w_)
                for x in e:
                    if "-" in x:
                        z_='n'
                    if x.isdigit():
                        x_.append(x)
                for x in e_:
                    if "-" in x:
                        z='n'
                    if x.isdigit():
                        y_.append(x)
                n_=eval(''.join(x_))
                n=eval(''.join(y_))
                if z=='n':
                    n=-n
                if z_=='n':
                    n_=-n_
                print("It is",n+n_)
        elif "add" in q_ and "and" in q_:
            for i in l:
                if "and" in i:
                    k=l.index(i)
                else:
                    pass
            if len(l[k])>3:
                k_=l[k]
                if k_[0].isdigit() and k_[len(k_)-1].isdigit():
                    o=k_.index('n')
                    w=k_[:o]
                    w_=k_[o:]
                    e=''.join(w)
                    e_=''.join(w_)
                    for x in e:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in e_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n+n_)
                elif k_[0].isdigit() and not(k_[len(k_)-1].isdigit()):
                    w=l[k+1:]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            y_.append(x)
                    n=eval(''.join(x_))
                    n_=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n+n_)
                elif not(k_[0].isdigit()) and k_[len(k_)-1].isdigit():
                    w=l[:k]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n+n_)
            else:
                w=l[:k]
                w_=l[k:]
                e=''.join(w)
                e_=''.join(w_)
                for x in e:
                    if "-" in x:
                        z_='n'
                    if x.isdigit():
                        x_.append(x)
                for x in e_:
                    if "-" in x:
                        z='n'
                    if x.isdigit():
                        y_.append(x)
                n_=eval(''.join(x_))
                n=eval(''.join(y_))
                if z=='n':
                    n=-n
                if z_=='n':
                    n_=-n_
                print("It is",n+n_)
        elif "add" in q_ and "&" in q_:
            for i in l:
                if "&" in i:
                    k=l.index(i)
                else:
                    pass
            if len(l[k])>1:
                k_=l[k]
                if k_[0].isdigit() and k_[len(k_)-1].isdigit():
                    o=k_.index('&')
                    w=k_[:o]
                    w_=k_[o:]
                    e=''.join(w)
                    e_=''.join(w_)
                    for x in e:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in e_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n+n_)
                elif k_[0].isdigit() and not(k_[len(k_)-1].isdigit()):
                    w=l[k+1:]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            y_.append(x)
                    n=eval(''.join(x_))
                    n_=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n+n_)
                elif not(k_[0].isdigit()) and k_[len(k_)-1].isdigit():
                    w=l[:k]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n+n_)
            else:
                w=l[:k]
                w_=l[k:]
                e=''.join(w)
                e_=''.join(w_)
                for x in e:
                    if "-" in x:
                        z_='n'
                    if x.isdigit():
                        x_.append(x)
                for x in e_:
                    if "-" in x:
                        z='n'
                    if x.isdigit():
                        y_.append(x)
                n_=eval(''.join(x_))
                n=eval(''.join(y_))
                if z=='n':
                    n=-n
                if z_=='n':
                    n_=-n_
                print("It is",n+n_)
    elif ("-" in q_ or "minus" in q_ or "sub" in q_ or ("sub" in q_ and ("and" in q_ or "&" in q_)) and ("+" not in q_ and "/" not in q_ and "*" not in q_ and "add" not in q_ and "plus" not in q_ and "multi" not in q_ and "into" not in q_ and "div" not in q_ and "by" not in q_ and "x" not in q_)):
        l=q_.split()
        x_=[]
        y_=[]
        _x_=[]
        z='p'
        if "-" in q_:
            for i in l:
                if "-" in i:
                    k=l.index(i)
                else:
                    pass
            if len(l[k])>1:
                k_=l[k]
                if k_[0].isdigit() and k_[len(k_)-1].isdigit():
                    print("It is",eval(k_))
                elif k_[0].isdigit() and not(k_[len(k_)-1].isdigit()):
                    w=l[k+1:]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            y_.append(x)
                    n=eval(''.join(x_))
                    n_=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n-n_)
                elif not(k_[0].isdigit()) and k_[len(k_)-1].isdigit():
                    w=l[:k]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n-n_)
            else:
                w=l[:k]
                w_=l[k:]
                e=''.join(w)
                e_=''.join(w_)
                for x in e:
                    if "-" in x:
                        z_='n'
                    if x.isdigit():
                        x_.append(x)
                for x in e_:
                    if "-" in x:
                        z='n'
                    if x.isdigit():
                        y_.append(x)
                n_=eval(''.join(x_))
                n=eval(''.join(y_))
                if z=='n':
                    n=-n
                if z_=='n':
                    n_=-n_
                print("It is",n-n_)
        elif "minus" in q_:
            for i in l:
                if "minus" in i:
                    k=l.index(i)
                else:
                    pass
            if len(l[k])>5:
                k_=l[k]
                if k_[0].isdigit() and k_[len(k_)-1].isdigit():
                    o=k_.index('m')
                    w=k_[:o]
                    w_=k_[o:]
                    e=''.join(w)
                    e_=''.join(w_)
                    for x in e:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in e_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n-n_)
                elif k_[0].isdigit() and not(k_[len(k_)-1].isdigit()):
                    w=l[k+1:]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            y_.append(x)
                    n=eval(''.join(x_))
                    n_=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n-n_)
                elif not(k_[0].isdigit()) and k_[len(k_)-1].isdigit():
                    w=l[:k]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n-n_)
            else:
                w=l[:k]
                w_=l[k:]
                e=''.join(w)
                e_=''.join(w_)
                for x in e:
                    if "-" in x:
                        z_='n'
                    if x.isdigit():
                        x_.append(x)
                for x in e_:
                    if "-" in x:
                        z='n'
                    if x.isdigit():
                        y_.append(x)
                n_=eval(''.join(x_))
                n=eval(''.join(y_))
                if z=='n':
                    n=-n
                if z_=='n':
                    n_=-n_
                print("It is",n-n_)
        elif "sub" in q_ and "and" in q_:
            for i in l:
                if "and" in i:
                    k=l.index(i)
                else:
                    pass
            if len(l[k])>3:
                k_=l[k]
                if k_[0].isdigit() and k_[len(k_)-1].isdigit():
                    o=k_.index('n')
                    w=k_[:o]
                    w_=k_[o:]
                    e=''.join(w)
                    e_=''.join(w_)
                    for x in e:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in e_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n_-n)
                elif k_[0].isdigit() and not(k_[len(k_)-1].isdigit()):
                    w=l[k+1:]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            y_.append(x)
                    n=eval(''.join(x_))
                    n_=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n-n_)
                elif not(k_[0].isdigit()) and k_[len(k_)-1].isdigit():
                    w=l[:k]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n-n_)
            else:
                w=l[:k]
                w_=l[k:]
                e=''.join(w)
                e_=''.join(w_)
                for x in e:
                    if "-" in x:
                        z_='n'
                    if x.isdigit():
                        x_.append(x)
                for x in e_:
                    if "-" in x:
                        z='n'
                    if x.isdigit():
                        y_.append(x)
                n_=eval(''.join(x_))
                n=eval(''.join(y_))
                if z=='n':
                    n=-n
                if z_=='n':
                    n_=-n_
                print("It is",n-n_)
        elif "sub" in q_ and "&" in q_:
            for i in l:
                if "&" in i:
                    k=l.index(i)
                else:
                    pass
            if len(l[k])>1:
                k_=l[k]
                if k_[0].isdigit() and k_[len(k_)-1].isdigit():
                    o=k_.index('&')
                    w=k_[:o]
                    w_=k_[o:]
                    e=''.join(w)
                    e_=''.join(w_)
                    for x in e:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in e_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n_-n)
                elif k_[0].isdigit() and not(k_[len(k_)-1].isdigit()):
                    w=l[k+1:]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            y_.append(x)
                    n=eval(''.join(x_))
                    n_=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n-n_)
                elif not(k_[0].isdigit()) and k_[len(k_)-1].isdigit():
                    w=l[:k]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n-n_)
            else:
                w=l[:k]
                w_=l[k:]
                e=''.join(w)
                e_=''.join(w_)
                for x in e:
                    if "-" in x:
                        z_='n'
                    if x.isdigit():
                        x_.append(x)
                for x in e_:
                    if "-" in x:
                        z='n'
                    if x.isdigit():
                        y_.append(x)
                n_=eval(''.join(x_))
                n=eval(''.join(y_))
                if z=='n':
                    n=-n
                if z_=='n':
                    n_=-n_
                print("It is",n-n_)
    elif ("*" in q_ or "into" in q_ or "x" in q_ or "multi" in q_ or ("multi" in q_ and ("and" in q_ or "&" in q_))) and ("+" not in q_ and "/" not in q_ and "-" not in q_ and "add" not in q_ and "plus" not in q_ and "sub" not in q_ and "minus" not in q_ and "div" not in q_ and "by" not in q_):
        l=q_.split()
        x_=[]
        y_=[]
        _x_=[]
        z='p'
        if "*" in q_:
            for i in l:
                if "*" in i:
                    k=l.index(i)
                else:
                    pass
            if len(l[k])>1:
                k_=l[k]
                if k_[0].isdigit() and k_[len(k_)-1].isdigit():
                    print("It is",eval(k_))
                elif k_[0].isdigit() and not(k_[len(k_)-1].isdigit()):
                    w=l[k+1:]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            y_.append(x)
                    n=eval(''.join(x_))
                    n_=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n*n_)
                elif not(k_[0].isdigit()) and k_[len(k_)-1].isdigit():
                    w=l[:k]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n*n_)
            else:
                w=l[:k]
                w_=l[k:]
                e=''.join(w)
                e_=''.join(w_)
                for x in e:
                    if "-" in x:
                        z_='n'
                    if x.isdigit():
                        x_.append(x)
                for x in e_:
                    if "-" in x:
                        z='n'
                    if x.isdigit():
                        y_.append(x)
                n_=eval(''.join(x_))
                n=eval(''.join(y_))
                if z=='n':
                    n=-n
                if z_=='n':
                    n_=-n_
                print("It is",n*n_)
        elif "into" in q_:
            for i in l:
                if "into" in i:
                    k=l.index(i)
                else:
                    pass
            if len(l[k])>4:
                k_=l[k]
                if k_[0].isdigit() and k_[len(k_)-1].isdigit():
                    o=k_.index('t')
                    w=k_[:o]
                    w_=k_[o:]
                    e=''.join(w)
                    e_=''.join(w_)
                    for x in e:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in e_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n*n_)
                elif k_[0].isdigit() and not(k_[len(k_)-1].isdigit()):
                    w=l[k+1:]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            y_.append(x)
                    n=eval(''.join(x_))
                    n_=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n*n_)
                elif not(k_[0].isdigit()) and k_[len(k_)-1].isdigit():
                    w=l[:k]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n*n_)
            else:
                w=l[:k]
                w_=l[k:]
                e=''.join(w)
                e_=''.join(w_)
                for x in e:
                    if "-" in x:
                        z_='n'
                    if x.isdigit():
                        x_.append(x)
                for x in e_:
                    if "-" in x:
                        z='n'
                    if x.isdigit():
                        y_.append(x)
                n_=eval(''.join(x_))
                n=eval(''.join(y_))
                if z=='n':
                    n=-n
                if z_=='n':
                    n_=-n_
                print("It is",n*n_)
        elif "multi" in q_ and "and" in q_:
            for i in l:
                if "and" in i:
                    k=l.index(i)
                else:
                    pass
            if len(l[k])>3:
                k_=l[k]
                if k_[0].isdigit() and k_[len(k_)-1].isdigit():
                    o=k_.index('n')
                    w=k_[:o]
                    w_=k_[o:]
                    e=''.join(w)
                    e_=''.join(w_)
                    for x in e:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in e_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n_*n)
                elif k_[0].isdigit() and not(k_[len(k_)-1].isdigit()):
                    w=l[k+1:]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            y_.append(x)
                    n=eval(''.join(x_))
                    n_=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n*n_)
                elif not(k_[0].isdigit()) and k_[len(k_)-1].isdigit():
                    w=l[:k]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n*n_)
            else:
                w=l[:k]
                w_=l[k:]
                e=''.join(w)
                e_=''.join(w_)
                for x in e:
                    if "-" in x:
                        z_='n'
                    if x.isdigit():
                        x_.append(x)
                for x in e_:
                    if "-" in x:
                        z='n'
                    if x.isdigit():
                        y_.append(x)
                n_=eval(''.join(x_))
                n=eval(''.join(y_))
                if z=='n':
                    n=-n
                if z_=='n':
                    n_=-n_
                print("It is",n*n_)
        elif "multi" in q_ and "&" in q_:
            for i in l:
                if "&" in i:
                    k=l.index(i)
                else:
                    pass
            if len(l[k])>1:
                k_=l[k]
                if k_[0].isdigit() and k_[len(k_)-1].isdigit():
                    o=k_.index('&')
                    w=k_[:o]
                    w_=k_[o:]
                    e=''.join(w)
                    e_=''.join(w_)
                    for x in e:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in e_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n_*n)
                elif k_[0].isdigit() and not(k_[len(k_)-1].isdigit()):
                    w=l[k+1:]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            y_.append(x)
                    n=eval(''.join(x_))
                    n_=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n*n_)
                elif not(k_[0].isdigit()) and k_[len(k_)-1].isdigit():
                    w=l[:k]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n*n_)
            else:
                w=l[:k]
                w_=l[k:]
                e=''.join(w)
                e_=''.join(w_)
                for x in e:
                    if "-" in x:
                        z_='n'
                    if x.isdigit():
                        x_.append(x)
                for x in e_:
                    if "-" in x:
                        z='n'
                    if x.isdigit():
                        y_.append(x)
                n_=eval(''.join(x_))
                n=eval(''.join(y_))
                if z=='n':
                    n=-n
                if z_=='n':
                    n_=-n_
                print("It is",n*n_)
        elif "x" in q_:
            for i in l:
                if "x" in i:
                    k=l.index(i)
                else:
                    pass
            if len(l[k])>1:
                k_=l[k]
                if k_[0].isdigit() and k_[len(k_)-1].isdigit():
                    o=k_.index('x')
                    w=k_[:o]
                    w_=k_[o:]
                    e=''.join(w)
                    e_=''.join(w_)
                    for x in e:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in e_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n_*n)
                elif k_[0].isdigit() and not(k_[len(k_)-1].isdigit()):
                    w=l[k+1:]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            y_.append(x)
                    n=eval(''.join(x_))
                    n_=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n*n_)
                elif not(k_[0].isdigit()) and k_[len(k_)-1].isdigit():
                    w=l[:k]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n*n_)
            else:
                w=l[:k]
                w_=l[k:]
                e=''.join(w)
                e_=''.join(w_)
                for x in e:
                    if "-" in x:
                        z_='n'
                    if x.isdigit():
                        x_.append(x)
                for x in e_:
                    if "-" in x:
                        z='n'
                    if x.isdigit():
                        y_.append(x)
                n_=eval(''.join(x_))
                n=eval(''.join(y_))
                if z=='n':
                    n=-n
                if z_=='n':
                    n_=-n_
                print("It is",n*n_)
    elif ("/" in q_ or "by" in q_ or "div" in q_ or ("div" in q_ and ("and" in q_ or "&" in q_)) and ("+" not in q_ and "-" not in q_ and "*" not in q_ and "add" not in q_ and "plus" not in q_ and "multi" not in q_ and "into" not in q_ and "sub" not in q_ and "minus" not in q_ and "x" not in q_)):
        l=q_.split()
        x_=[]
        y_=[]
        _x_=[]
        z='p'
        if "/" in q_:
            for i in l:
                if "/" in i:
                    k=l.index(i)
                else:
                    pass
            if len(l[k])>1:
                k_=l[k]
                if k_[0].isdigit() and k_[len(k_)-1].isdigit():
                    print("It is",eval(k_))
                elif k_[0].isdigit() and not(k_[len(k_)-1].isdigit()):
                    w=l[k+1:]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            y_.append(x)
                    n=eval(''.join(x_))
                    n_=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n/n_)
                elif not(k_[0].isdigit()) and k_[len(k_)-1].isdigit():
                    w=l[:k]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n/n_)
            else:
                w=l[:k]
                w_=l[k:]
                e=''.join(w)
                e_=''.join(w_)
                for x in e:
                    if "-" in x:
                        z_='n'
                    if x.isdigit():
                        x_.append(x)
                for x in e_:
                    if "-" in x:
                        z='n'
                    if x.isdigit():
                        y_.append(x)
                n_=eval(''.join(x_))
                n=eval(''.join(y_))
                if z=='n':
                    n=-n
                if z_=='n':
                    n_=-n_
                print("It is",n/n_)
        elif "by" in q_:
            for i in l:
                if "by" in i:
                    k=l.index(i)
                else:
                    pass
            if len(l[k])>2:
                k_=l[k]
                if k_[0].isdigit() and k_[len(k_)-1].isdigit():
                    o=k_.index('y')
                    w=k_[:o]
                    w_=k_[o:]
                    e=''.join(w)
                    e_=''.join(w_)
                    for x in e:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in e_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n/n_)
                elif k_[0].isdigit() and not(k_[len(k_)-1].isdigit()):
                    w=l[k+1:]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            y_.append(x)
                    n=eval(''.join(x_))
                    n_=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n/n_)
                elif not(k_[0].isdigit()) and k_[len(k_)-1].isdigit():
                    w=l[:k]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n/n_)
            else:
                w=l[:k]
                w_=l[k:]
                e=''.join(w)
                e_=''.join(w_)
                for x in e:
                    if "-" in x:
                        z_='n'
                    if x.isdigit():
                        x_.append(x)
                for x in e_:
                    if "-" in x:
                        z='n'
                    if x.isdigit():
                        y_.append(x)
                n_=eval(''.join(x_))
                n=eval(''.join(y_))
                if z=='n':
                    n=-n
                if z_=='n':
                    n_=-n_
                print("It is",n/n_)
        elif "div" in q_ and "and" in q_:
            for i in l:
                if "and" in i:
                    k=l.index(i)
                else:
                    pass
            if len(l[k])>3:
                k_=l[k]
                if k_[0].isdigit() and k_[len(k_)-1].isdigit():
                    o=k_.index('n')
                    w=k_[:o]
                    w_=k_[o:]
                    e=''.join(w)
                    e_=''.join(w_)
                    for x in e:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in e_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n_/n)
                elif k_[0].isdigit() and not(k_[len(k_)-1].isdigit()):
                    w=l[k+1:]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            y_.append(x)
                    n=eval(''.join(x_))
                    n_=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n/n_)
                elif not(k_[0].isdigit()) and k_[len(k_)-1].isdigit():
                    w=l[:k]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n/n_)
            else:
                w=l[:k]
                w_=l[k:]
                e=''.join(w)
                e_=''.join(w_)
                for x in e:
                    if "-" in x:
                        z_='n'
                    if x.isdigit():
                        x_.append(x)
                for x in e_:
                    if "-" in x:
                        z='n'
                    if x.isdigit():
                        y_.append(x)
                n_=eval(''.join(x_))
                n=eval(''.join(y_))
                if z=='n':
                    n=-n
                if z_=='n':
                    n_=-n_
                print("It is",n/n_)
        elif "div" in q_ and "&" in q_:
            for i in l:
                if "&" in i:
                    k=l.index(i)
                else:
                    pass
            if len(l[k])>1:
                k_=l[k]
                if k_[0].isdigit() and k_[len(k_)-1].isdigit():
                    o=k_.index('&')
                    w=k_[:o]
                    w_=k_[o:]
                    e=''.join(w)
                    e_=''.join(w_)
                    for x in e:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in e_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n_/n)
                elif k_[0].isdigit() and not(k_[len(k_)-1].isdigit()):
                    w=l[k+1:]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            y_.append(x)
                    n=eval(''.join(x_))
                    n_=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n/n_)
                elif not(k_[0].isdigit()) and k_[len(k_)-1].isdigit():
                    w=l[:k]
                    _k_=''.join(w)
                    for x in k_:
                        if "-" in x:
                            z_='n'
                        if x.isdigit():
                            x_.append(x)
                    for x in _k_:
                        if "-" in x:
                            z='n'
                        if x.isdigit():
                            y_.append(x)
                    n_=eval(''.join(x_))
                    n=eval(''.join(y_))
                    if z=='n':
                        n=-n
                    if z_=='n':
                        n_=-n_
                    print("It is",n/n_)
            else:
                w=l[:k]
                w_=l[k:]
                e=''.join(w)
                e_=''.join(w_)
                for x in e:
                    if "-" in x:
                        z_='n'
                    if x.isdigit():
                        x_.append(x)
                for x in e_:
                    if "-" in x:
                        z='n'
                    if x.isdigit():
                        y_.append(x)
                n_=eval(''.join(x_))
                n=eval(''.join(y_))
                if z=='n':
                    n=-n
                if z_=='n':
                    n_=-n_
                print("It is",n/n_)
'''
