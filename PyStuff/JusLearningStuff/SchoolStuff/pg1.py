'''#temp. conversion
c=eval(input("enter cel.:"))
f=(c*1.8)+32
print("temp. in faren.",f)'''

'''#grade
s1=int(input("enter marks;"))
s2=int(input("enter marks;"))
s3=int(input("enter marks;"))
s4=int(input("enter marks;"))
s5=int(input("enter marks;"))
t=s1+s2+s3+s4+s5
avg=t/5
print("total",t)
if(s1<50)or(s2<50)or(s3<50)or(s4<50)or(s5<50):
    print("fail")
    quit()
if (avg>90):
    print("grade a")
if (avg>80)and(avg<=90):
    print("grade b")
if (avg>70)and(avg<=80):
    print("grade c")
if (avg>60)and(avg<=70):
    print("grade d")
if (avg>50)and(avg<=60):
    print("grade e")'''
'''#fiboacci series
print("fibonacci series")
f=0
s=1
print(f)
print(s)
for i in range(1,6):
    t=f+s
    print(t)
    f=s
    s=t'''

'''#prime no.
n=int(input("num:"))
l=int(n/2)+1
for i in range(2,l):
    r=n%i
    if r==0:
        print("not p.no.")
        break
else:
    print("p.no.")'''

#lcm&hcf
'''x=input("ent:")
y=input("ent:")
if x>y:
    s=y
else:
    s=x
for i in range(1,s+1):
    if((x%i==0)and(y%i==0)):
        hcf=i
lcm=(x*y)/hcf
print("hcf",hcf)
print("lcm",lcm)'''

def fibonacci(num):
    num1 = 0
    num2 = 1
    series = 0
    for i in range(num):
        print(series, end=' ');
        num1 = num2;
        num2 = series;
        series = num1 + num2;


# running function after takking user input
num = int(input('Enter how many numbers needed in Fibonacci series- '))
fibonacci(num)
