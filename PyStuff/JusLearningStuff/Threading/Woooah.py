import sys
import time
import threading

def stop(a):
    if a%2==0:
        time.sleep(10)
        print(a)
    else:
        print(a)
    

for i in range(1,24):
    ThreadObj=threading.Thread(target=stop, args=(i,))
    ThreadObj.start()
    print("wooooaaaaH")
    ThreadObj.join(timeout=5)
    
