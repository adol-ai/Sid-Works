import time
import threading
import keyboard

'''def thread_():
    time.sleep(5)
    print("Running WoooooAaaaH")
print("Yoooooo Vrooooo")
ThreadObj=threading.Thread(target=thread_)
ThreadObj.start()
print("Uh huh")'''

def input_():
    time.sleep(3)
    keyboard.write("'WooooW'")
    keyboard.press_and_release('enter')
    

print("VCoooooooL")
ThreadObj=threading.Thread(target=input_)
ThreadObj.start()
x=eval(input("Enter Yo: "))
time.sleep(4)
print("data Vroo: ", x)


'''x=str(input("Enter: "))
time.sleep(1)
keyboard.write("qwertyui")
time.sleep(1)
print("data: ",x)'''
