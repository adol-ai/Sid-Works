import os
import glob

os.chdir("textLabels/")
x = glob.glob("*.txt")

for i in x:
    print(i)
    f = open(str(i),'r')
    data = f.readlines()
    print(data)
    f.close()
    new_data = []
    for j in data:
        j = list(j)
        j[0]="0"
        j = ''.join(j)
        new_data.append(j)
    f = open(str(i),'w')
    f.writelines(''.join(new_data))
    f.close()
