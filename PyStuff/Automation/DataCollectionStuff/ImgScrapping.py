import io
import time
import requests
import datetime
import threading
from PIL import Image
from selenium import webdriver
from colorama import Fore,Style
from selenium.webdriver.common.by import By

t1 = time.time()
a = 0
b = -1
imgSet = set()
xximgTempVal = 0
driver = webdriver.Firefox()
q = ['people', 'people in the streets', 'people vlogging', 'children playing', 'kids with pets', 'children group photo', 'children crowd', 'children school', 'teen students', 'children classroom', 'high school class', 'play school students', 'children park playing', 'walking in the streets', 'crowd area', 'crowd street', 'walking in crowd street', 'busy morning street', 'busy crowd', 'busy people', 'people partying', 'people dancing', 'people watching match', 'people in stadium', 'students group photo','vlogging in night street', 'crowd vlogging', 'people competition', 'people marathon', 'people in wwe', 'crowd in a meeting', 'night street', 'walking in the crowd', 'crowd in the forest', 'group photo', 'group dance', 'group selfie', 'children dancing']
f = open("LinkSet.txt", "a")
f.write("\n\n\n\n\n\n\n\n\n\n")
f.write(str(datetime.datetime.now())+'\n')
f.close()
for q_ in q:
    b+=1
    skip = 0
    max_ = 150
    imgTempVal = 1
    imgTemp = set()
    driver.get("https://www.google.com/search?q={}&tbm=isch&source=hp&biw=1873&bih=969&ei=jX1tY83SF87az7sPwKO68AY&iflsig=AJiK0e8AAAAAY22LnaUQStNMEm2fk8dCGptfVOdHqY1D&ved=0ahUKEwiNzZqI16T7AhVO7XMBHcCRDm4Q4dUDCAc&uact=5&oq=cat&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzILCAAQgAQQsQMQgwEyCAgAEIAEELEDMggIABCABBCxAzIFCAAQgAQ6CAgAELEDEIMBUABYrQFgvgdoAHAAeACAAU-IAewBkgEBM5gBAKABAaoBC2d3cy13aXotaW1n&sclient=img".format(q_))
    while len(imgTemp)<max_:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        if skip>100:
            break
        p = 0
        try:
            comPics = driver.find_elements(By.CLASS_NAME,"Q4LuWd")
            for img in comPics[len(imgTemp)+skip:max_]:
                p+=1
                if p%10==0:
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(5)
                if skip>100:
                    break
                img.click()
                time.sleep(1)
                orgPics = driver.find_elements(By.CSS_SELECTOR, ".r48jcc.pT0Scc.iPVvYb")
                try:
                    morePics_btn = driver.find_element(By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div[2]/input")
                    morePics_btn.click()
                    time.sleep(1)
                    print(Fore.RED+Style.BRIGHT+"~~~Yoooooo !")
                except:
                    pass
                for pic in orgPics:
                    if pic.get_attribute('src') in imgTemp or 'encrypted' in pic.get_attribute('src'):
                        print(Fore.YELLOW+Style.BRIGHT+pic.get_attribute('src'))
                        skip+=1
                        max_+=1
                        break
                    if 'http' in pic.get_attribute('src') and 'encrypted' not in pic.get_attribute('src') and pic.get_attribute('src') not in imgTemp:
                        x = len(imgSet)+b*imgTempVal
                        y = len(imgTemp)+b*imgTempVal
                        imgTemp.add(pic.get_attribute('src'))
                        print(Fore.BLUE+Style.BRIGHT+"\tScrapped Img{}~Img{} Url...".format(str(x+y),str(y)))
                        print(Fore.GREEN+Style.BRIGHT+pic.get_attribute('src'))
                        f = open("LinkSet.txt", "a")
                        f.write(str(pic.get_attribute('src'))+"\n")
                        f.close()
        except:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            pass
        imgTempVal = len(imgTemp)
        imgSet = imgSet.union(imgTemp)
        break

t2 = time.time()
print("\n\n\nFetchingExecTime:", t2-t1)


t1 = time.time()
def saving(img_):
    try:
        global a
        t1_ = time.time()
        r = requests.get(img_).content
        f = io.BytesIO(r)
        imgf = Image.open(f)
        imgf.save("ImgSet/"+str(a)+'.png')
        t2_ = time.time()
        if a%2==0:
            print(Fore.MAGENTA+Style.BRIGHT+str(a)+'.png in! ~ '+Fore.BLUE+Style.BRIGHT+str(t2_-t1_)+' Secs')
        else:
            print(Fore.CYAN+Style.BRIGHT+'\t\t'+str(a)+'.png in! ~ '+Fore.BLUE+Style.BRIGHT+str(t2_-t1_)+' Secs')
        a+=1
    except:
        print(Fore.RED+Style.BRIGHT+"~~~|",i)
        pass

for i in imgSet:
    ThreadObj = threading.Thread(target=saving, args =(i,))
    ThreadObj.start()
    ThreadObj.join(timeout=60)
              
t2 = time.time()
print("\n\n\nExecTime:", t2-t1)

