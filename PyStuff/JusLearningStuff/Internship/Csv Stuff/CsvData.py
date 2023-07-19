import csv
import pandas
from collections import Counter

CompleteDataset=[]

#Day1
data=pandas.read_csv("D:\Python Files\Csv Stuff\DataSet\CSV\Day1.csv")
data_=(data.to_string())
l=data_.split()
l_=[]
u=[]
k=-1
k_=-1
for i in l:
    k+=1
    if i.isdigit() and int(i)<500:
        k_+=1
        if int(i)==k_:
            l_.append(int(k))
        else:
            k_-=1
    elif i.isdigit():
        if int(i) not in u:
            u.append(int(i))

for i in range(0,len(l_)):
    try:
        x=l[l_[i]:l_[i+1]]
        CompleteDataset.append(x)
    except:
        y=l[l_[i]:]
        CompleteDataset.append(y)

#Day2
data=pandas.read_csv("D:\Python Files\Csv Stuff\DataSet\CSV\Day2.csv")
data_=(data.to_string())
l=data_.split()
l_=[]
u_=[]
print(len(l))
k=-1
k_=-1
for i in l:
    k+=1
    if i.isdigit() and int(i)<500:
        k_+=1
        if int(i)==k_:
            l_.append(int(k))
        else:
            k_-=1
    elif i.isdigit():
        if int(i) not in u_:
            u_.append(int(i))

for i in range(0,len(l_)):
    try:
        x=l[l_[i]:l_[i+1]]
        CompleteDataset.append(x)
    except:
        y=l[l_[i]:]
        CompleteDataset.append(y)

#Day3
data=pandas.read_csv("D:\Python Files\Csv Stuff\DataSet\CSV\Day3.csv")
data_=(data.to_string())
l=data_.split()
l_=[]
_u_=[]
k=-1
k_=-1
for i in l:
    k+=1
    if i.isdigit() and int(i)<500:
        k_+=1
        if int(i)==k_:
            l_.append(int(k))
        else:
            k_-=1
    elif i.isdigit():
        if int(i) not in _u_:
            _u_.append(int(i))
        

for i in range(0,len(l_)):
    try:
        x=l[l_[i]:l_[i+1]]
        CompleteDataset.append(x)
    except:
        y=l[l_[i]:]
        CompleteDataset.append(y)

_l_= u + u_ + _u_


d= dict(Counter(_l_))
n=[]
n_=[]
FilteredData=[]
for i in d:
    if d[i]==3:
        n.append(i)
    if d[i]==2:
        n_.append(i)


for x in CompleteDataset:
    for y in n:
        if x[3]=='NaN':
            x.remove(x[3])
        if int(x[8])==y:
            FilteredData.append(x[2:9]+["100%"])
            n.remove(y)

for x in CompleteDataset:
    for y in n_:
        if x[3]=='NaN':
            x.remove(x[3])
        if int(x[8])==y:
            FilteredData.append(x[2:9]+["66.6%"])
            n_.remove(y)

with open("FinalDataset.csv","wt") as f:
    s=csv.writer(f)
    s.writerow(["Email_Address", "NAME", "DESIGNATION", "NAME_OF_THE_INSTITUTE/ORGANIZATION", "DISTRICT", "STATE", "WHATSAPP_NUMBER", "ATTENDANCE PERCENTAGE"])
    s.writerows(FilteredData)
    '''for q in FilteredData:
        s.writerow(q)'''
    
for k in FilteredData:
    print("\n",k)


