import time
import webbrowser
import selenium
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdrivers

print("~~Things Are Going Smoothly~~ \n Time-")
d_=td.strftime("%d-%m-%Y")
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path='T:\Python Files\Automation\chromedriver.exe',options = chrome_options)
driver.get("https://kvm.edusollearning.com/")
driver.maximize_window()
username = driver.find_element_by_name('username')
username.send_keys('EDS200015')
time.sleep(1)
password = driver.find_element_by_name('password')
password.send_keys('EDS200015')
btn=driver.find_element_by_xpath('//*[@id="form-signin"]/section[3]/button')
btn.submit()
time.sleep(1)
#driver.execute_script("window.open('https://kvm.edusollearning.com/student/online-classes', 'new window')")
driver.get('https://kvm.edusollearning.com/student/online-classes')
r=driver.page_source
type(r)
s = BeautifulSoup(r,"html.parser")
y=[]
for a in s.find_all('a', href=True):
    y.append(a['href'])
z=[]
for t in y:
    if "https://kvm.edusollearning.com/student/online-classes/" in t:
        z.append(t)
for j in range(0,20,2):
    time.sleep(1)
    driver.get(z[j])
    r_=driver.page_source
    type(r_)
    s_=BeautifulSoup(r_,"html.parser")
    i=s_.find(class_='tile-body')
    p=[]
    for l in i.find_all():
        p.append(l.text)
    _s_ = BeautifulSoup(r_,"html.parser")
    y_=[]
    for a in _s_.find_all('a', href=True):
        y_.append(a['href'])
    if td.strftime("%d-%m-%Y") in p[4]:
        if int(h_)>12:
            h_=int(h_)-12
            h_='0'+str(h_)
        else:
            pass
        if "Bio" not in p[0] and p[4][11:13]==h_:
            time.sleep(420)
            driver.refresh()
            driver.get(y_[len(y_)-1])
            driver.refresh()
            time.sleep(3600)
            print("Session Hour ",h_," Accomplished")
            driver.close()
            break
        time.sleep(1)
        driver.back()
    else:
        break
driver.close()

