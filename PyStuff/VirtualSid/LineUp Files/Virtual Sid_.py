###################################====================_Virtual Sid_=================####################################

import os
import random
import requests
import webbrowser
from gtts import gTTS
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from playsound import playsound


v='YES'#input("Do you want VoiceOver:").capatalize()

def shutdown():
    print("Shutting Down...")
    try:
        s=gTTS(text="hmm Computer Shutting down!",lang='en-uk')
        s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
        playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
        os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")    
    except requests.exceptions.ConnectionError:
        pass
    os.system('shutdown /s /t 1')
    
def restart():
    print("ReBooting...")
    try:
        s=gTTS(text="hmm Computer Rebooting now!",lang='en-uk')
        s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
        playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
        os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")    
    except requests.exceptions.ConnectionError:
        pass
    os.system('shutdown -t 0 -r -f')

def logout():
    print("SigningOut...")
    try:
        s=gTTS(text="hmm Computer Signing out!",lang='en-uk')
        s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
        playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
        os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")    
    except requests.exceptions.ConnectionError:
        pass
    os.system('shutdown -l')

def date():
    d=datetime.now()
    d_=d.strftime("%d/%m/%Y")
    print("Date Today:",d_)
    try:
        s=gTTS(text="hmm today's date is {}".format(d_),lang='en-uk')
        s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
        playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
        os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")    
    except requests.exceptions.ConnectionError:
        pass
    
def time():
    t=datetime.now()
    t_h=int(t.strftime("%H"))
    if t_h > 12:
        t__='PM'
        t_h = t_h - 12
    else:
        t__='AM'
    t_m=t.strftime("%M")
    t_s=t.strftime("%S")
    print("Time Right Now:",t_h,":",t_m,":",t_s," ",t__)
    try:
        s=gTTS(text="hmm the time is {}:{}:{} {}".format(t_h,t_m,t_s,t__),lang='en-uk')
        s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
        playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
        os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")    
    except requests.exceptions.ConnectionError:
        pass

def month():
    m=datetime.now()
    m_=m.strftime("%B")
    print("This Month:",m_)
    try:
        s=gTTS(text="hmm this month is {}".format(m_),lang='en-uk')
        s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
        playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
        os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")    
    except requests.exceptions.ConnectionError:
        pass
    
def year():
    y=datetime.now()
    y_=y.strftime("%Y")
    print("Year:",y_)
    try:
        s=gTTS(text="hmm this year is {}".format(y_),lang='en-uk')
        s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
        playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
        os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")    
    except requests.exceptions.ConnectionError:
        pass
    
def news_h():
    try:
        r=requests.get("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen")
        type(r)
        s = BeautifulSoup(r.text,"html.parser")
        print("\t                      Live NEWS Headlines")
        for link in s.find_all('a')[71:685]:
            print("◉",link.text)
        print("That's It For NOW!")
        if v == "YES":
            s=gTTS(text="hmm Here we have the Top story coverage headlines",lang='en-us')
            s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
    except requests.exceptions.ConnectionError:
        print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
        if v == "YES":
            playsound(r"D:\Python Files\Audiofiles\offline.mp3")

def sc_browser():
    try:
        print("Here We Go!")
        print("Just In A Moment To Swisscows")
        query = 'search'
        webbrowser.open("https://swisscows.com/?q=%s" % query)
        if v == "YES":
            s=gTTS(text="hmm Here We Go! To Swisscows Browser",lang='en-us')
            s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
    except requests.exceptions.ConnectionError:
        print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
        if v == "YES":
            playsound(r"D:\Python Files\Audiofiles\offline.mp3")
        
def ddg_browser():
    try:
        print("Here We Go!")
        print("Just In A Moment To DuckDuckGo")
        query = 'search'
        webbrowser.open("https://duckduckgo.com/?q=%s" % query)
        if v == "YES":
            s=gTTS(text="hmm Here We Go! To Duckduckgo browser",lang='en-us')
            s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
    except requests.exceptions.ConnectionError:
        print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
        if v == "YES":
            playsound(r"D:\Python Files\Audiofiles\offline.mp3")
    
def se_browser():
    try:
        print("Here We Go!")
        print("Just In A Moment To Search Encrypt")
        query = 'search'
        webbrowser.open("https://searchencrypt.com/?q=%s" % query)
        if v == "YES":
            s=gTTS(text="hmm Here We Go! To Search Encrypt browser",lang='en-us')
            s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
    except requests.exceptions.ConnectionError:
        print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
        if v == "YES":
            playsound(r"D:\Python Files\Audiofiles\offline.mp3")
    

def wiki():
    try:
        query = 'search'
        print("Here We Go!")
        print("Just In A Moment To Wikipedia")
        query = 'search'
        webbrowser.open("https://en.wikipedia.org/wiki/Main_Page?q=%s" % query)
        if v == "YES":
            s=gTTS(text="hmm here it is! Wikipedia",lang='en-us')
            s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
    except requests.exceptions.ConnectionError:
        print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
        if v == "YES":
            playsound(r"D:\Python Files\Audiofiles\offline.mp3")

def wiki_search():
    try:
        a=input("What do you want from Wiki:")
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',options = chrome_options)
        driver.get("https://www.wikipedia.org/")
        search_form = driver.find_element_by_id('searchInput')
        search_form.send_keys(a)
        search_form.submit()
        if v == "YES":
                s=gTTS(text="hmm! these are the result found about {} on Wikipedia".format(a),lang='en-uk')
                s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
    except:
        print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
        if v == "YES":
            playsound(r"D:\Python Files\Audiofiles\offline.mp3")

def amazon_search():
    try:
        a=input("What item do you want to search from  Amazon:")
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',options = chrome_options)
        driver.get("https://www.amazon.com/")
        search_form = driver.find_element_by_id('twotabsearchtextbox')
        search_form.send_keys(a)
        search_form.submit()
        if v == "YES":
                s=gTTS(text="hmm! these are the result found on {} in Amazon".format(a),lang='en-uk')
                s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
    except:
        print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
        if v == "YES":
            playsound(r"D:\Python Files\Audiofiles\offline.mp3")

def ebay_search():
    try:
        a=input("What item do you want to search from  Ebay:")
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',options = chrome_options)
        driver.get("https://www.ebay.com/")
        search_form = driver.find_element_by_id('gh-ac')
        search_form.send_keys(a)
        search_form.submit()
        if v == "YES":
                s=gTTS(text="hmm! these are the result found on {} in Ebay".format(a),lang='en-uk')
                s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
    except:
        print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
        if v == "YES":
            playsound(r"D:\Python Files\Audiofiles\offline.mp3")

def vid_search():
    try:
        query = input("Enter the Title of the Video you wanted to Search:")
        print("Just Sit Back And Hold Tight!")
        webbrowser.open("https://youtube.com/search?q=%s" % query)
        if v == "YES":
            s=gTTS(text="hmm Here are the results for {} in Youtube".format(query),lang='en-uk')
            s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
    except requests.exceptions.ConnectionError:
        print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
        if v == "YES":
            playsound(r"D:\Python Files\Audiofiles\offline.mp3")
            
def play_yt():
    try:
        a=input("What do you wanted to play:")
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',options = chrome_options)
        driver.get("https://www.youtube.com/")
        search_form = driver.find_element_by_name('search_query')
        search_form.send_keys(a)
        search_form.submit()
        click_form = driver.find_element_by_id('dismissable')
        click_form.click()
        if v == "YES":
            s=gTTS(text="hmm! Getting that from Youtube",lang='en-uk')
            s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
    except:
        print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
        if v == "YES":
            playsound(r"D:\Python Files\Audiofiles\offline.mp3")

def joke():
    j=["Question: What do you call a boomerang that doesn't work? Answer: A stick.", 'Question: What do you call four bullfighters in quicksand? Answer: Quattro sinko.', 'Ed: The same bike tries to run me down every day. Fred: Sounds like a vicious cycle...', 'Question: Why should you never date tennis players? Answer: Love means nothing to them.', 'Question: How do you weigh a millennial? Answer: In Instagrams.', 'Jenny: I can tell if someone is lying just by looking at him. Penny: Really? Jenny: Yep. I can tell if he is standing too.', 'Fred: Can you tell me about that new do-it-yourself orthodontist? Ted: Brace yourself.', 'Question: What happened to the guy who sued over his missing luggage? Answer: He lost his case.', 'Therapist: I’ve concluded that you are incapable of describing your feelings. Patient: I can’t say that I am surprised!', 'Marriage Counselor: So, what brings you here today? Wife: He takes everything literally.  I can’t stand it. Husband: My truck.', 'Question: What weighs more, a gallon of water or a gallon of butane? Answer: The water. Butane is lighter fluid.', 'Mike: Someone stole the wheels off of all the police cars! Spike: The cops are working on it—tirelessly.', 'Question:  What do you call a guy who’s had too much to drink? Answer:  A cab.', 'Ann: I herd that you are a hypochondriac. Stan: Well, my doctor says I’m not, but I spent 3 days reading about it on the internet and I have all...', 'Hal: How did you get hit on the head with a book? Sal: I only have my shelf to blame.', 'Question: What kind of tree has a hand? Answer: A palm tree.', 'Question: What kind of shoes does a lazy person wear? Answer: Loafers.', 'Question: Why should you save your pennies? Answer: It makes good cents.', 'Question: What kind of jokes are told on a farm? Answer: Corny ones.', 'Question: What has T in the beginning, T in the middle, and T at the end? Answer: A teapot.', 'Question: What do you call a penguin in the desert? Answer: Lost', 'Question: What is a tree’s favorite soda? Answer: Root Beer.', 'A lawyer is driving a car down the street and instead of stopping at the stop sign, the lawyer slows down. A policeman sees this and pulls the car over...', "Question: Why doesn't McDonald's serve escargot? Answer: It's not fast food!", 'Question: Hear about the two guys who stole a calendar? Answer: They both got 6 months.', 'A guy gets pulled over by a cop. The cop asks, “You’re speeding! Didn’t you see the speed limit sign?” The man replied, “Yeah I saw the speed limit sign,...', 'The last year I entered a marathon. The race started and immediately I was the last of the runners. It was embarrassing. The guy who was in front of me,...', 'Question: What did the SNAIL say while riding on the turtles back? Answer: Wheeeeeeeee', 'I work in the front office of a housing complex that supports people living with mental illness. On one particularly hectic day, a tenant came in to pay her rent....', 'As the dentist labored over my teeth, he tried to make small talk. “What do you do?” he asked. “I’m a comedian,” I answered. “Interesting.” After a pause, he said,...', 'I admit it—I have a tendency to exaggerate, and I was afraid when I joined the Navy that my “creativity” might get me in trouble. But my fears were put...', 'Our base’s Army Exchange Service carried a particular brand of underarm deodorant that I liked and bought for years. Then one day I couldn’t find it. I asked an employee...', 'Fred Astaire and Ginger Rogers were dining in New York. Ginger was resplendent in a ball gown and pearls, and Fred also sported evening wear. But the meal was marred...', 'To the guy who stole my antidepressants: I hope you’re happy now.', 'Spotted in the legal notices section of the Maryland-based Daily Times: Michael Ray Dipirro petitioned the circuit court to change his name to Michael Ray Forbes. His reason for doing...', '“This is your great-grandma and great grandpa,” I told my grandson as I handed him a photo of my parents. “Do you think I look like them?” He shook his...', 'While shopping for a bathroom scale, I found one that tracks not only weight but also body fat, bone mass, and water percentage. I nixed that one in favor of...', 'The topic of conversation was nose jobs. My slightly confused young daughter asked, “Where does the doctor get the new noses to replace the old ones?” “They have a place...', 'In his late 80s, my father-in-law went to the DMV to renew his driver’s license. At one point during the road test, he approached a four-way stop, looked to his...', 'After my husband injured himself, I ran him over to the doctor’s office. There, the nurse dressed his wound and gave him instructions on how to care for it. She...', 'A man is at the funeral of an old friend. He tentatively approaches the deceased’s wife and asks whether he can say a word. The widow nods. The man clears...', 'I was instructing new recruits when an officer entered my classroom to observe and report on my teaching style. I thought I was on top of my game that day,...', 'Comedian Martha Raye was a great supporter of the military and made many trips to Vietnam to entertain the troops. She also liked her scotch. One day, I was told...', 'I was trapped in an elevator for 30 minutes before the doors finally opened. Relieved, I said to a fellow hostage, “There’s a first time for everything.” She grumbled back,...', 'After my wife accidentally swallowed my prostate medication, our daughter called a pharmacist to ask whether there was any cause for alarm. He replied, “Only if she starts hanging out...', 'My 35-year-old son and I had just finished our meal when I realized I’d left my wallet in my truck. As I headed out the door, I told the waitress...', 'Starving after hours of driving nonstop, my husband and I pulled over at a truck stop. While he gassed up the car, I went into the restaurant and placed our...', 'As part of my Naval Reserve requirements at Emory University Dental School, I attended a talk about proper dental procedures following nuclear warfare. Evidently, one of my classmates found the...', 'When I was a Navy student pilot, I visited the home of a classmate. I met his wife and baby and was impressed that he had all his flight gear...', 'While taking a clinical history from an elderly patient, I asked, “How’s your love life?” “I don’t know,” he said. “I’ll ask my wife.” He got up, walked into the...', 'A coworker was telling us all about her trip to Las Vegas. “That sounds great. Where’d you stay?” asked a colleague. “I can’t remember,” she said. “But I think it...', 'Sometimes honesty isn’t the best policy.A patient showed up at our medical office and asked, “You’re Mary, aren’t you?” I smiled. “No, sorry, I’m not.” “Are you sure? You look...', 'I just read that 4,153,237 people got married last year. Not to cause any trouble, but shouldn’t that be an even number?', 'My husband cooks for me like I’m a god—by placing burnt offerings before me every night.', 'Question: What happens when an artist has trouble finding inspiration? Answer: She draws a blank.', 'Something tells me I need to lose some weight. During a recent trip to visit my son and his family, I stopped off at a bakery to pick up dessert....', 'Over dinner, I could sense something was bothering my mother, so I asked if anything was wrong. “Yes,” she admitted. “What’s all this I hear on the news about banning...', 'Descartes walked into a bar and ordered a beer. “Want another?” asked the bartender. “I think not”, Descartes replied … then he disappeared.', 'Did you hear about the young actor who fell through the floorboards? He was just going through a stage.', 'Question: What did the left eye say to the right eye? Answer: Between you and me, something smells.', 'Question: How does the solar system organize a party? Answer: They planet!', 'I went to a smoke shop to discover that it has been replaced by an apparel store. Clothes, but no cigar.', 'Question: What is the best way to cook a gator? Answer: In a crock-pot', "Question: What did the numerator say to the denominator when they broke up? Answer: I'm so over you!", "I'm sick of following my dreams. I'm just going to ask where they're going and hook up with 'em later.", "I've reached the age where my prescription bill has caught up to my bar bill.", 'Did you hear how they caught the great produce bandit? He stopped to take a leek.', 'Question: What do you get when you combine an insomniac, an agnostic, and a dyslexic? Answer: Someone who lays awake at night wondering the true meaning of Dog.', 'I was working from home, interviewing a famous neurologist for an article, when my three-year-old announced she had to go potty and waddled into the bathroom. After some loud moans,...', 'My job as a facilities maintenance engineer required a wide range of skills. One day I might have to fix the furnace, while the next day could see me painting...', 'Our manager kept reminding us waitresses to encourage customers to order dessert. At the end of an especially exhausting day, I walked over to a couple who had just sat...', 'A man goes to a job interview and the interviewer begins with the question, “What do you think is your biggest weakness?” The man thinks for a moment, then says,...', 'A man goes to the doctor, concerned about his wife’s hearing. The doctor says, “Stand behind her and say something and tell me how close you are when she hears...']
    j_=random.randint(0,73)
    print(j[j_])
    if v == "YES":
            t=j[j_]
            s=gTTS(text="hmm,{}".format(t),lang='en-uk')
            s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
            
def jokes():
    j=["Question: What do you call a boomerang that doesn't work? Answer: A stick.", 'Question: What do you call four bullfighters in quicksand? Answer: Quattro sinko.', 'Ed: The same bike tries to run me down every day. Fred: Sounds like a vicious cycle...', 'Question: Why should you never date tennis players? Answer: Love means nothing to them.', 'Question: How do you weigh a millennial? Answer: In Instagrams.', 'Jenny: I can tell if someone is lying just by looking at him. Penny: Really? Jenny: Yep. I can tell if he is standing too.', 'Fred: Can you tell me about that new do-it-yourself orthodontist? Ted: Brace yourself.', 'Question: What happened to the guy who sued over his missing luggage? Answer: He lost his case.', 'Therapist: I’ve concluded that you are incapable of describing your feelings. Patient: I can’t say that I am surprised!', 'Marriage Counselor: So, what brings you here today? Wife: He takes everything literally.  I can’t stand it. Husband: My truck.', 'Question: What weighs more, a gallon of water or a gallon of butane? Answer: The water. Butane is lighter fluid.', 'Mike: Someone stole the wheels off of all the police cars! Spike: The cops are working on it—tirelessly.', 'Question:  What do you call a guy who’s had too much to drink? Answer:  A cab.', 'Ann: I herd that you are a hypochondriac. Stan: Well, my doctor says I’m not, but I spent 3 days reading about it on the internet and I have all...', 'Hal: How did you get hit on the head with a book? Sal: I only have my shelf to blame.', 'Question: What kind of tree has a hand? Answer: A palm tree.', 'Question: What kind of shoes does a lazy person wear? Answer: Loafers.', 'Question: Why should you save your pennies? Answer: It makes good cents.', 'Question: What kind of jokes are told on a farm? Answer: Corny ones.', 'Question: What has T in the beginning, T in the middle, and T at the end? Answer: A teapot.', 'Question: What do you call a penguin in the desert? Answer: Lost', 'Question: What is a tree’s favorite soda? Answer: Root Beer.', 'A lawyer is driving a car down the street and instead of stopping at the stop sign, the lawyer slows down. A policeman sees this and pulls the car over...', "Question: Why doesn't McDonald's serve escargot? Answer: It's not fast food!", 'Question: Hear about the two guys who stole a calendar? Answer: They both got 6 months.', 'A guy gets pulled over by a cop. The cop asks, “You’re speeding! Didn’t you see the speed limit sign?” The man replied, “Yeah I saw the speed limit sign,...', 'The last year I entered a marathon. The race started and immediately I was the last of the runners. It was embarrassing. The guy who was in front of me,...', 'Question: What did the SNAIL say while riding on the turtles back? Answer: Wheeeeeeeee', 'I work in the front office of a housing complex that supports people living with mental illness. On one particularly hectic day, a tenant came in to pay her rent....', 'As the dentist labored over my teeth, he tried to make small talk. “What do you do?” he asked. “I’m a comedian,” I answered. “Interesting.” After a pause, he said,...', 'I admit it—I have a tendency to exaggerate, and I was afraid when I joined the Navy that my “creativity” might get me in trouble. But my fears were put...', 'Our base’s Army Exchange Service carried a particular brand of underarm deodorant that I liked and bought for years. Then one day I couldn’t find it. I asked an employee...', 'Fred Astaire and Ginger Rogers were dining in New York. Ginger was resplendent in a ball gown and pearls, and Fred also sported evening wear. But the meal was marred...', 'To the guy who stole my antidepressants: I hope you’re happy now.', 'Spotted in the legal notices section of the Maryland-based Daily Times: Michael Ray Dipirro petitioned the circuit court to change his name to Michael Ray Forbes. His reason for doing...', '“This is your great-grandma and great grandpa,” I told my grandson as I handed him a photo of my parents. “Do you think I look like them?” He shook his...', 'While shopping for a bathroom scale, I found one that tracks not only weight but also body fat, bone mass, and water percentage. I nixed that one in favor of...', 'The topic of conversation was nose jobs. My slightly confused young daughter asked, “Where does the doctor get the new noses to replace the old ones?” “They have a place...', 'In his late 80s, my father-in-law went to the DMV to renew his driver’s license. At one point during the road test, he approached a four-way stop, looked to his...', 'After my husband injured himself, I ran him over to the doctor’s office. There, the nurse dressed his wound and gave him instructions on how to care for it. She...', 'A man is at the funeral of an old friend. He tentatively approaches the deceased’s wife and asks whether he can say a word. The widow nods. The man clears...', 'I was instructing new recruits when an officer entered my classroom to observe and report on my teaching style. I thought I was on top of my game that day,...', 'Comedian Martha Raye was a great supporter of the military and made many trips to Vietnam to entertain the troops. She also liked her scotch. One day, I was told...', 'I was trapped in an elevator for 30 minutes before the doors finally opened. Relieved, I said to a fellow hostage, “There’s a first time for everything.” She grumbled back,...', 'After my wife accidentally swallowed my prostate medication, our daughter called a pharmacist to ask whether there was any cause for alarm. He replied, “Only if she starts hanging out...', 'My 35-year-old son and I had just finished our meal when I realized I’d left my wallet in my truck. As I headed out the door, I told the waitress...', 'Starving after hours of driving nonstop, my husband and I pulled over at a truck stop. While he gassed up the car, I went into the restaurant and placed our...', 'As part of my Naval Reserve requirements at Emory University Dental School, I attended a talk about proper dental procedures following nuclear warfare. Evidently, one of my classmates found the...', 'When I was a Navy student pilot, I visited the home of a classmate. I met his wife and baby and was impressed that he had all his flight gear...', 'While taking a clinical history from an elderly patient, I asked, “How’s your love life?” “I don’t know,” he said. “I’ll ask my wife.” He got up, walked into the...', 'A coworker was telling us all about her trip to Las Vegas. “That sounds great. Where’d you stay?” asked a colleague. “I can’t remember,” she said. “But I think it...', 'Sometimes honesty isn’t the best policy.A patient showed up at our medical office and asked, “You’re Mary, aren’t you?” I smiled. “No, sorry, I’m not.” “Are you sure? You look...', 'I just read that 4,153,237 people got married last year. Not to cause any trouble, but shouldn’t that be an even number?', 'My husband cooks for me like I’m a god—by placing burnt offerings before me every night.', 'Question: What happens when an artist has trouble finding inspiration? Answer: She draws a blank.', 'Something tells me I need to lose some weight. During a recent trip to visit my son and his family, I stopped off at a bakery to pick up dessert....', 'Over dinner, I could sense something was bothering my mother, so I asked if anything was wrong. “Yes,” she admitted. “What’s all this I hear on the news about banning...', 'Descartes walked into a bar and ordered a beer. “Want another?” asked the bartender. “I think not”, Descartes replied … then he disappeared.', 'Did you hear about the young actor who fell through the floorboards? He was just going through a stage.', 'Question: What did the left eye say to the right eye? Answer: Between you and me, something smells.', 'Question: How does the solar system organize a party? Answer: They planet!', 'I went to a smoke shop to discover that it has been replaced by an apparel store. Clothes, but no cigar.', 'Question: What is the best way to cook a gator? Answer: In a crock-pot', "Question: What did the numerator say to the denominator when they broke up? Answer: I'm so over you!", "I'm sick of following my dreams. I'm just going to ask where they're going and hook up with 'em later.", "I've reached the age where my prescription bill has caught up to my bar bill.", 'Did you hear how they caught the great produce bandit? He stopped to take a leek.', 'Question: What do you get when you combine an insomniac, an agnostic, and a dyslexic? Answer: Someone who lays awake at night wondering the true meaning of Dog.', 'I was working from home, interviewing a famous neurologist for an article, when my three-year-old announced she had to go potty and waddled into the bathroom. After some loud moans,...', 'My job as a facilities maintenance engineer required a wide range of skills. One day I might have to fix the furnace, while the next day could see me painting...', 'Our manager kept reminding us waitresses to encourage customers to order dessert. At the end of an especially exhausting day, I walked over to a couple who had just sat...', 'A man goes to a job interview and the interviewer begins with the question, “What do you think is your biggest weakness?” The man thinks for a moment, then says,...', 'A man goes to the doctor, concerned about his wife’s hearing. The doctor says, “Stand behind her and say something and tell me how close you are when she hears...']
    j_=random.randint(0,73)
    j1_=random.randint(0,73)
    j2_=random.randint(0,73)
    print(j[j_])
    if v == "YES":
            t=j[j_]
            s=gTTS(text="hmm,{}".format(t),lang='en-uk')
            s.save(r"D:\Python Files\Audiofiles\joke.mp3")
            playsound(r"D:\Python Files\Audiofiles\joke.mp3")
    print("\n")
    print(j[j1_])
    if v == "YES":
            t=j[j1_]
            s=gTTS(text="hmm,{}".format(t),lang='en-uk')
            s.save(r"D:\Python Files\Audiofiles\joke1.mp3")
            playsound(r"D:\Python Files\Audiofiles\joke1.mp3")
    print("\n")
    print(j[j2_])
    if v == "YES":
            t=j[j2_]
            s=gTTS(text="hmm,{}".format(t),lang='en-uk')
            s.save(r"D:\Python Files\Audiofiles\joke2.mp3")
            playsound(r"D:\Python Files\Audiofiles\joke2.mp3")
                        
def fitness():
    print("\t                      Always remember: No Pain! No Gain! \n")
    f=" ⨷Fix a Workout Schedule Aleast 20mins a Day \n ⨷Always Remember there're no Faster Results! \n ⨷Sleep is a Very Important Aspect \n ⨷Go for HIIT(High-Intensity Interval Training) workouts \n ⨷Don't Go for WeightTraining unless you are done with Body-WeightTraining \n ⨷Avoid Junk Foods \n ⨷Don't Go for Diet unless you are trying 6-pack ABS \n ⨷Never Over-Indulge Food \n ⨷Have Self-Control \n ⨷Cardio+BodyWeightTraining Give Spectacular Results!"
    print(f)
    try:
        s=gTTS(text="hmm Just try these out....Quiet Essential!",lang='en-uk')
        s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
        playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
        os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
    except:
        print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
        if v == "YES":
            playsound(r"D:\Python Files\Audiofiles\offline.mp3")    
def rep():
    r=["For clearification: I'm Sid", "That's Awkward!", "That's Awful", "I did'nt Expect that!", "You're dissappointing Me!", "You're here with different Person in a different Platform", "I thought you Recognise me!"]
    r_=random.randint(0,7)
    print(r[r_])
    r1=["That is Awkward!", "That is Awful", "I did'nt Expect that!", "You're dissappointing Me!", "You're here with different Person in a different Platform", "I thought you Recognise me!"]
    r1_=random.randint(0,6)
    try:
        t=r1[r1_]
        s=gTTS(text="hmm,{}".format(t),lang='en-uk')
        s.save(r"D:\Python Files\Audiofiles\VoiceOver9.mp3")
        playsound(r"D:\Python Files\Audiofiles\VoiceOver9.mp3")
    except:
        try:
            t=r1[r1_]
            s=gTTS(text="hmm,{}".format(t),lang='en-uk')
            s.save(r"D:\Python Files\Audiofiles\VoiceOver101.mp3")
            playsound(r"D:\Python Files\Audiofiles\VoiceOver101.mp3")
        except:
            try:
                t=r1[r1_]
                s=gTTS(text="hmm,{}".format(t),lang='en-uk')
                s.save(r"D:\Python Files\Audiofiles\VoiceOver102.mp3")
                playsound(r"D:\Python Files\Audiofiles\VoiceOver102.mp3")
            except:
                print("I'm Fed Up!")
                quit()

def rep1():
    r=["That's Awkward!", "That's Awful", "I did'nt Expect that!", "You're dissappointing Me!", "You're here with different Person in a different Platform", "I thought you Recognise me!"]
    r_=random.randint(0,6)
    print(r[r_])
    r1=["That is Awkward!", "That is Awful", "I did'nt Expect that!", "You're dissappointing Me!", "You're here with different Person in a different Platform", "I thought you Recognise me!"]
    r1_=random.randint(0,6)
    try:
        t=r1[r1_]
        s=gTTS(text="hmm,{}".format(t),lang='en-uk')
        s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
        playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
        os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
    except:
        print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
        if v == "YES":
            playsound(r"D:\Python Files\Audiofiles\offline.mp3")

def sid_info():
        s=" I'm Sid , A Virtual Assistant \n I was Build & Developed by Siddiq_Moideen \n I Built with a Female Voice Assistant She's Glenda \n I Acquire most of the data via Internet:'Web Scraping' \n I'm also Built-in with offline features as my Creator fed me \n I was built during the LockDown Days \n My File was first Commenced on Wednesday March 25 2020, 10:29:24 PM and Still being Developed! \n In the beginning in was in the Journey to be Developed as an Artifical Intelligence but eventually Destined to Virtual Assistant \n So now I'm here to Assist You!"
        print(s)
        try:
            s=gTTS(text="hmmmm That is a Small breif about Sid",lang='en-uk')
            s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
        except:
            print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
            if v == "YES":
                playsound(r"D:\Python Files\Audiofiles\offline.mp3")
            
'''' Slang:-
        'af':'Afrikaans',
        'sq':'Albanian',
        'ar':'Arabic',
        'hy':'Armenian',
        'bn':'Bengali',
        'ca':'Catalan',
        'zh':'Chinese',
        'zh-cn':'Chinese (Mandarin/China)',
        'zh-tw':'Chinese (Mandarin/Taiwan)',
        'zh-yue':'Chinese (Cantonese)',
        'hr':'Croatian',
        'cs':'Czech',
        'da':'Danish',
        'nl':'Dutch',
        'en':'English',
        'en-au':'English (Australia)',
        'en-uk':'English (United Kingdom)',
        'en-us':'English (United States)',
        'eo':'Esperanto',
        'fi':'Finnish',
        'fr':'French',
        'de':'German',
        'el':'Greek',
        'hi':'Hindi',
        'hu':'Hungarian',
        'is':'Icelandic',
        'id':'Indonesian',
        'it':'Italian',
        'ja':'Japanese',
        'ko':'Korean',
        'la':'Latin',
        'lv':'Latvian',
        'mk':'Macedonian',
        'no':'Norwegian',
        'pl':'Polish',
        'pt':'Portuguese',
        'pt-br':'Portuguese (Brazil)',
        'ro':'Romanian',
        'ru':'Russian',
        'sr':'Serbian',
        'sk':'Slovak',
        'es':'Spanish',
        'es-es':'Spanish (Spain)',
        'es-us':'Spanish (United States)',
        'sw':'Swahili',
        'sv':'Swedish',
        'ta':'Tamil',
        'th':'Thai',
        'tr':'Turkish',
        'vi':'Vietnamese',
        'cy':'Welsh' 
'''

def news():
    try:
        r=requests.get("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen")
        type(r)
        s = BeautifulSoup(r.text,"html.parser")
        print("\t                        NEWS Coverage")
        n=s.find(id='yDmH0d')
        i=n.find(class_='lBwEZb BL5WZb xP6mwf')
        for link in i:
            print("◉",link.text,"\n")
        print("That's It For NOW!")
        if v == "YES":
            s=gTTS(text="hmm Here we have the Top coverage stories",lang='en-uk')
            s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
    except requests.exceptions.ConnectionError:
        print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
        if v == "YES":
            playsound(r"D:\Python Files\Audiofiles\offline.mp3")

def latest_news_h():
    try:
        r=requests.get("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen")
        type(r)
        s = BeautifulSoup(r.text,"html.parser")
        print("\t                      Latest NEWS Headlines")
        for link in s.find_all('a')[48:]:
            print("◉",link.text)
        print("That's It For NOW!")
        if v == "YES":
            s=gTTS(text="hmm Here we have the Latest news headlines",lang='en-uk')
            s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
    except requests.exceptions.ConnectionError:
        print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
        if v == "YES":
            playsound(r"D:\Python Files\Audiofiles\offline.mp3")

def sports_news():
    try:
        r=requests.get("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen")
        type(r)
        s = BeautifulSoup(r.text,"html.parser")
        print("\t                           Sports NEWS ")
        n=s.find(id='yDmH0d')
        i=n.find(class_='fe4pJf')
        for link in i.find_all('a')[0:677]:
            print("◉",link.text,"\n")
        print("That's It For NOW!")
        if v == "YES":
            s=gTTS(text="hmm Here we have the Sports News",lang='en-uk')
            s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
    except requests.exceptions.ConnectionError:
        print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
        if v == "YES":
            playsound(r"D:\Python Files\Audiofiles\offline.mp3")

def world_news():
    try:
        r=requests.get("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen")
        type(r)
        s = BeautifulSoup(r.text,"html.parser")
        print("\t                           World NEWS ")
        n=s.find(id='yDmH0d')
        i=n.find(class_='MNK4Vd')
        for link in i.find_all('a'):
            print("◉",link.text,"\n")
        print("That's It For NOW!")
        if v == "YES":
            s=gTTS(text="hmm Here we have the Global News",lang='en-uk')
            s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
    except requests.exceptions.ConnectionError:
        print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
        if v == "YES":
            playsound(r"D:\Python Files\Audiofiles\offline.mp3")

def tech_news():
    try:
        r=requests.get("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen")
        type(r)
        s = BeautifulSoup(r.text,"html.parser")
        print("\t                           Tech NEWS ")
        n=s.find(id='yDmH0d')
        i=n.find(class_='MNK4Vd')
        for link in i.find_all('a')[2:]:
            print("◉",link.text,"\n")
        print("That's It For NOW!")
        if v == "YES":
            s=gTTS(text="hmm Here we have the Tech News",lang='en-uk')
            s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
    except requests.exceptions.ConnectionError:
        print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
        if v == "YES":
            playsound(r"D:\Python Files\Audiofiles\offline.mp3")

def local_news():
    try:
        r=requests.get("https://news.google.com/topics/CAAqHAgKIhZDQklTQ2pvSWJHOWpZV3hmZGpJb0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen")
        type(r)
        s = BeautifulSoup(r.text,"html.parser")
        print("\t                           Local NEWS ")
        n=s.find(id='yDmH0d')
        i=n.find(class_='MNK4Vd')
        for link in i.find_all('a')[2:]:
            print("◉",link.text,"\n")
        print("That's It For NOW!")
        if v == "YES":
            s=gTTS(text="hmm Here we have the Local News",lang='en-uk')
            s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
    except requests.exceptions.ConnectionError:
        print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
        if v == "YES":
            playsound(r"D:\Python Files\Audiofiles\offline.mp3")

def business_news():
    try:
        r=requests.get("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen")
        type(r)
        s = BeautifulSoup(r.text,"html.parser")
        print("\t                           Business NEWS ")
        n=s.find(id='yDmH0d')
        i=n.find(class_='MNK4Vd')
        for link in i.find_all('a'):
            print("◉",link.text,"\n")
        print("That's It For NOW!")
        if v == "YES":
            s=gTTS(text="hmm Here we have the Business News",lang='en-uk')
            s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
    except requests.exceptions.ConnectionError:
        print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
        if v == "YES":
            playsound(r"D:\Python Files\Audiofiles\offline.mp3")

def f_scan():
    try:
        s=gTTS(text="Enter the Location",lang='en-uk')
        s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
        playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
        os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
    except requests.exceptions.ConnectionError:
        pass
    try:
        l=input("Enter the location:")
        os.chdir('{}'.format(l))
        for dirpath, dirnames, filenames in os.walk(os.getcwd()):
            print("File Name:", filenames)
            print("Current path:", dirpath)
            print("Files available:", dirnames)
        print("Scanning Completed! These are the Results")
        try:
            s=gTTS(text="Scanning Completed! These are the Results",lang='en-uk')
            s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
        except requests.exceptions.ConnectionError:
            pass
    except:
        print("Error: InValid Location")
        try:
            s=gTTS(text="Couldn't pass on procedures due to Invalid location ",lang='en-uk')
            s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
        except requests.exceptions.ConnectionError:
            pass

def weather():
    try:
        r=requests.get("https://in.search.yahoo.com/search?p=weather")
        r1=requests.get("https://www.bing.com/search?q=weather&form=QBLH&sp=-1&pq=weather&sc=9-7&qs=n&sk=&cvid=685416D5C043438EAF2162C0F54978B5")
        type(r)
        s = BeautifulSoup(r.text,"html.parser")
        s1 = BeautifulSoup(r1.text,"html.parser")
        print("\t                           Weather ")
        l=s.find(class_='cptn-ctnt')
        w=s.find(class_='condition')
        t=s.find(class_='currTemp')
        '''d=s1.find(class_='wtr_condiAttribs')
        p=s1.find(class_='wtr_currPerci')
        w_=s1.find(class_='wtr_currWind')
        h=s1.find(class_='wtr_currHumi')'''
        print("Location:",l.text)
        print("Weather:",w.text)
        print("Temperature:",t.text,"℃")
        '''print(p.text)
        print(w_.text)
        print(h.text)'''
        print("\n                  ","\t That's the Current Weather \t")
        if v == "YES":
            s=gTTS(text="hmm. Current weather is: {}".format(w.text),lang='en-uk')
            s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
    except requests.exceptions.ConnectionError:
        print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
        if v == "YES":
            playsound(r"D:\Python Files\Audiofiles\offline.mp3")

def stocks():
    try:
        print("Just Sit Back And Hold Tight!")
        webbrowser.open("https://www.moneycontrol.com/stocksmarketsindia/")
        if v == "YES":
            s=gTTS(text="hmm these are live stock updates",lang='en-uk')
            s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
    except requests.exceptions.ConnectionError:
        print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
        if v == "YES":
            playsound(r"D:\Python Files\Audiofiles\offline.mp3")

def opb():
    print("1:DuckDuckGo / 2:Swisscows / 3:Search Encrypt")
    pb=input("Which Browser do you Choose(1/\2/\3):")
    try:
        s=gTTS(text="hmm which browser do you choose?",lang='en-uk')
        s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
        playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
        os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
    except requests.exceptions.ConnectionError:
        pass
    if pb == 1:
        ddg_browser()
    if pb == 2:
        sc_browser()
    if pb == 3:
        se_browser()
    else:
        print("Your Choice is Out of Range!")
        try:
            s=gTTS(text="hmm your choice is out of range!",lang='en-uk')
            s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
        except requests.exceptions.ConnectionError:
            pass

def html_con():
    try:
        s=gTTS(text="Enter the URL:",lang='en-uk')
        s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
        playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
        os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
    except requests.exceptions.ConnectionError:
        pass
    url=input("Enter the URL:")
    r=requests.get(url)
    type(r)
    s = BeautifulSoup(r.text,"html.parser")
    print(s.prettify())

def search():
    try:
        w=input("Title[only]:")
        query = input("Search[query only]:")
        print("Just Sit Back And Hold Tight!")
        webbrowser.open("https://{}.com/search?q={}".format(w,query))
        if v == "YES":
            s=gTTS(text="hmm Here We Are searching for {} in {}".format(query,w),lang='en-us')
            s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
            os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
    except requests.exceptions.ConnectionError:
        print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
        if v == "YES":
            playsound(r"D:\Python Files\Audiofiles\offline.mp3")
    
def sid_func():
    print("⚜I can update you with ⫸Weather ⫸Stocks ⫸News Headlines ⫸Latest News ⫸World News ⫸Sports News ⫸Business News ⫸Tech news ⫸Local News \n")
    print("⚜I can open WebBrowsers as per your Query i.e. from Google & Bing \n")
    print("⚜I can open Wikipedia \n")
    print("⚜I can access Wikipedia as per your Query \n")
    print("⚜I do have few Trusted Private WebBrowsers such as DuckDuckGo, Swisscows & Search Encrypt \n")
    print("⚜I can search anything for you in Wikipedia \n")
    print("⚜I can literally take you to Any Website Online! \n")
    print("⚜I can Extract Whole HTML file of the Website/Url You feed me \n")
    print("⚜I can thoroughly Scan the Folder you feed and List you the Files in it \n")
    print("⚜I have a Voice Assistant She's Glenda \n")
    print("⚜I can tell you Jokes too \n")
    print("⚜I can ShutDown / LogOut / Restart the Device \n")
    print("⚜I can give you Fitness Tips \n")
    print("⚜I do have a Personal Sketch about Myself \n")
    print("⚜Truth is,I can do Anything for you!")
    print("\n")
    try:
        s=gTTS(text="Myself And Sid are here to Assist you! ",lang='en-uk')
        s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
        playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
        os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
    except requests.exceptions.ConnectionError:
        pass
    
def process():
    while True:
        q_=input().casefold()
        try:
            if q_ is True:
                pass
            elif "Stocks" in q_ or "share market" in q_:
                stocks()
            elif "latest news headlines" in q_ or "present news headlines" in q_:
                latest_news_h()
            elif "sports news" in q_:
                sports_news()
            elif "tech news" in q_ or "technology news" in q_:
                tech_news()
            elif "world news"in q_ or "global news" in q_:
                world_news()
            elif "business news" in q_ or "trade news" in q_:
                business_news()
            elif "local news" in q_:
                local_news()
            elif "news headlines" in q_:
                news_h()
            elif "news" in q_:
                news()
            elif "news headlines" in q_:
                news_h()
            elif "search" in q_ and "amazon" in q_ or ("open amazon" in q_ and (("search" in q_ or "look" in q_ or "find" in q_))) or "search in amazon" in q_:
                try:
                    l= q_.split()
                    try:
                        i=l.index("for")+1
                    except:
                        i=l.index("search")+1
                    try:
                        j=l.index("in")
                        w=' '.join([x for x in l if x in l[i:j]])
                    except:
                        w=' '.join([x for x in l if x in l[i:]])
                    print("Just Sit Back And Hold Tight!")
                    chrome_options = webdriver.ChromeOptions()
                    driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',options = chrome_options)
                    driver.get("https://www.amazon.com/")
                    search_form = driver.find_element_by_id('twotabsearchtextbox')
                    search_form.send_keys(w)
                    search_form.submit()
                    if v == "YES":
                        s=gTTS(text="hmm! these are the result found for {} in Amazon".format(w),lang='en-uk')
                        s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                        playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                        os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                except:
                    print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
                    if v == "YES":
                        playsound(r"D:\Python Files\Audiofiles\offline.mp3")
            elif "search" in q_ and  "ebay" in q_ or ("open ebay" in q_ and (("search" in q_ or "look" in q_ or "find" in q_))) or "search in ebay" in q_:
                try:
                    l= q_.split()
                    try:
                        i=l.index("for")+1
                    except:
                        i=l.index("search")+1
                    try:
                        j=l.index("in")
                        w=' '.join([x for x in l if x in l[i:j]])
                    except:
                        w=' '.join([x for x in l if x in l[i:]])
                    print("Just Sit Back And Hold Tight!")
                    chrome_options = webdriver.ChromeOptions()
                    driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',options = chrome_options)
                    driver.get("https://www.ebay.com/")
                    search_form = driver.find_element_by_id('gh-ac')
                    search_form.send_keys(w)
                    search_form.submit()
                    if v == "YES":
                        s=gTTS(text="hmm! these are the result found for {} in Ebay".format(w),lang='en-uk')
                        s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                        playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                        os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                except:
                    print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
                    if v == "YES":
                        playsound(r"D:\Python Files\Audiofiles\offline.mp3")
            elif "open duckduckgo" in q_ or "duckduckgo brows" in q_:
                ddg_browser()
            elif "open swisscows" in q_ or "open swisscows brows" in q_:
                sc_browser()
            elif "open search encrypt" in q_ or "search encrypt brow" in q_ or "open searchencrypt brows" in q_ or "open searchencrypt" in q_:
                se_browser()
            elif ("open" in q_ and ("search" in q_ or "look" in q_ or "find" in q_)) or (("search" in q_ or "look" in q_ or "find" in q_ or "some" in q_) and ("on" in q_ or "in" in q_ or "for" in q_ or "over" in q_)):
                try:
                    l= q_.split()
                    try: 
                        i=l.index("open")+1
                        j=l.index("and")
                        w=' '.join([x for x in l if x in l[i:j]])
                        i_=l.index("for")+1
                        q=' '.join([x for x in l if x in l[i_:]])
                    except:
                        try:
                            i=l.index("in")+1
                            j=l.index("search")
                            w=' '.join([x for x in l if x in l[i:j]])
                            i_=l.index("for")+1
                            q=' '.join([x for x in l if x in l[i_:]])
                        except:
                            try:
                                i=l.index("in")+1
                                j=l.index("look")
                                w=' '.join([x for x in l if x in l[i:j]])
                                i_=l.index("for")+1
                                q=' '.join([x for x in l if x in l[i_:]])
                            except:
                                try:
                                    i_=l.index("search")+1
                                    j_=l.index("in")
                                    q=' '.join([x for x in l if x in l[i_:j_]])
                                    i=l.index("in")+1
                                    w=' '.join([x for x in l if x in l[i:]])
                                except:
                                    try:
                                        i_=l.index("find")+1
                                        j_=l.index("in")
                                        q=' '.join([x for x in l if x in l[i_:j_]])
                                        i=l.index("in")+1
                                        w=' '.join([x for x in l if x in l[i:]])
                                    except:
                                        try:
                                            i=l.index("on")+1
                                            j=l.index("for")
                                            w=' '.join([x for x in l if x in l[i:j]])
                                            i_=l.index("for")+1
                                            q=' '.join([x for x in l if x in l[i_:]])            
                                        except:
                                            try:
                                                i=l.index("over")+1
                                                j=l.index("for")
                                                w=' '.join([x for x in l if x in l[i:j]])
                                                i_=l.index("for")+1
                                                q=' '.join([x for x in l if x in l[i_:]])
                                            except:
                                                try:
                                                    i=l.index("search")+1
                                                    j=l.index("for")
                                                    w=' '.join([x for x in l if x in l[i:j]])
                                                    i_=l.index("for")+1
                                                    q=' '.join([x for x in l if x in l[i_:]])
                                                except:
                                                    try:
                                                        i=l.index("look")+1
                                                        j=l.index("for")
                                                        w=' '.join([x for x in l if x in l[i:j]])
                                                        i_=l.index("for")+1
                                                        q=' '.join([x for x in l if x in l[i_:]])
                                                    except:
                                                        try:
                                                            i_=l.index("some")+1
                                                            j_=l.index("in")
                                                            q=' '.join([x for x in l if x in l[i_:j_]])
                                                            i=l.index("in")+1
                                                            w=' '.join([x for x in l if x in l[i:]])
                                                        except:
                                                            try:
                                                                i_=l.index("some")+1
                                                                j_=l.index("on")
                                                                q=' '.join([x for x in l if x in l[i_:j_]])
                                                                i=l.index("on")+1
                                                                w=' '.join([x for x in l if x in l[i:]])
                                                            except:
                                                                i_=l.index("some")+1
                                                                j_=l.index("from")
                                                                q=' '.join([x for x in l if x in l[i_:j_]])
                                                                i=l.index("on")+1
                                                                w=' '.join([x for x in l if x in l[i:]])
                    print("Just Sit Back And Hold Tight!")
                    webbrowser.open("https://{}.com/search?q={}".format(w,q))
                    if v == "YES":
                        s=gTTS(text="hmm Here We Are searching for {} in {}".format(q,w),lang='en-us')
                        s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                        playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                        os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                except requests.exceptions.ConnectionError:
                    print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
                    if v == "YES":
                        playsound(r"D:\Python Files\Audiofiles\offline.mp3")
            elif "open" in q_:
                try:
                    l= q_.split()
                    i=l.index("open")+1
                    w=' '.join([x for x in l if x in l[i:]])
                    webbrowser.open("https://www.{}.com".format(w))
                    print("Just Sit Back And Hold Tight!")
                    if v == "YES":
                        s=gTTS(text="hmm Here we are moving to {}dot com".format(w),lang='en-us')
                        s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                        playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                        os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                except requests.exceptions.ConnectionError:
                    print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
                    if v == "YES":
                        playsound(r"D:\Python Files\Audiofiles\offline.mp3")
            elif "google for" in q_ or ((("search" or "look" in q_ or "find" in q_)) and "google" in q_):
                try:
                    l= q_.split()
                    try:
                        i=l.index("for")+1
                    except:
                        i=l.index("search")+1
                    try:
                        j=l.index("in")
                        w=' '.join([x for x in l if x in l[i:j]])
                    except:
                        w=' '.join([x for x in l if x in l[i:]])
                    print("Just Sit Back And Hold Tight!")
                    webbrowser.open("https://google.com/search?q=%s" % w)
                    if v == "YES":
                        s=gTTS(text="hmm these are the results on Google for {}".format(w),lang='en-us')
                        s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                        playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                        os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                except requests.exceptions.ConnectionError:
                    print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
                    if v == "YES":
                        playsound(r"D:\Python Files\Audiofiles\offline.mp3")
            elif "bing for" in q_ or ((("search" or "look" in q_ or "find" in q_)) and "bing" in q_):
                try:
                    l= q_.split()
                    try:
                        i=l.index("for")+1
                    except:
                        i=l.index("search")+1
                    try:
                        j=l.index("in")
                        w=' '.join([x for x in l if x in l[i:j]])
                    except:
                        w=' '.join([x for x in l if x in l[i:]])
                    print("Just Sit Back And Hold Tight!")
                    webbrowser.open("https://bing.com/search?q=%s" % w)
                    if v == "YES":
                        s=gTTS(text="hmm these are the results on Bing for {}".format(w),lang='en-us')
                        s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                        playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                        os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                except requests.exceptions.ConnectionError:
                    print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
                    if v == "YES":
                        playsound(r"D:\Python Files\Audiofiles\offline.mp3")
            elif "yahoo for" in q_ or ((("search" or "look" in q_ or "find" in q_)) and "yahoo" in q_):
                try:
                    l= q_.split()
                    try:
                        i=l.index("for")+1
                    except:
                        i=l.index("search")+1
                    try:
                        j=l.index("in")
                        w=' '.join([x for x in l if x in l[i:j]])
                    except:
                        w=' '.join([x for x in l if x in l[i:]])
                    print("Just Sit Back And Hold Tight!")
                    chrome_options = webdriver.ChromeOptions()
                    driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',options = chrome_options)
                    driver.get("https://www.yahoo.com")
                    search_form = driver.find_element_by_id('header-search-input')
                    search_form.send_keys(w)
                    search_form.submit()
                    if v == "YES":
                        s=gTTS(text="hmm these are the results on yahoo for {}".format(w),lang='en-us')
                        s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                        playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                        os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                except requests.exceptions.ConnectionError:
                    print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
                    if v == "YES":
                        playsound(r"D:\Python Files\Audiofiles\offline.mp3")
            elif ("search" or "look" in q_ or "find" in q_) and "wiki" in q_ or "from wiki" in q_ or "in wiki" in q_ :
                try:
                    l= q_.split()
                    try:
                        i=l.index("for")+1
                    except:
                        i=l.index("search")+1
                    try:
                        j=l.index("in")
                        w=' '.join([x for x in l if x in l[i:j]])
                    except:
                        w=' '.join([x for x in l if x in l[i:]])
                    print("Just Sit Back And Hold Tight!")
                    chrome_options = webdriver.ChromeOptions()
                    driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',options = chrome_options)
                    driver.get("https://www.wikipedia.org/")
                    search_form = driver.find_element_by_id('searchInput')
                    search_form.send_keys(w)
                    search_form.submit()
                    if v == "YES":
                        s=gTTS(text="hmm! these are the result found about {} on Wikipedia".format(w),lang='en-uk')
                        s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                        playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                        os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                except:
                    print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
                    if v == "YES":
                        playsound(r"D:\Python Files\Audiofiles\offline.mp3")
            elif "how are you" in q_:
                print("I'm Great")
            elif "what can you do" in q_ or "what are you meant" in q_ or "what are you capable" in q_:
                sid_func()
            elif "sid" in q_ and ("will you" in q_ or "can you" in q_ or "do you" in q_) and ("me" in q_ or "you" in q_):
                print("Probably that's not Possible!, I'm Virtual...I do what Iam Designed for!")
                try:
                    s=gTTS(text="hmm Probably that is not possible!, He's Virtual Assistant...he does what he's designed for!",lang='en-uk')
                    s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                except requests.exceptions.ConnectionError:
                    pass
            elif "glenda" in q_ and ("will you" in q_ or "can you" in q_ or "do you" in q_) and ("me" in q_ or "you" in q_):
                print("Probably that's not Possible!, She's just a Voice Assistant...she does what she's Designed for!")
                try:
                    s=gTTS(text="hmm Probably that is not possible!, I'm just a Voice Assistant. I do what iam designed for!",lang='en-uk')
                    s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                except requests.exceptions.ConnectionError:
                    pass
            elif "play" in q_:
                try:
                    l= q_.split()
                    i=l.index("play")+1
                    try:
                        j=l.index("in")
                        w=' '.join([x for x in l if x in l[i:j]])
                    except:
                        try:
                            j=l.index("from")
                            w=' '.join([x for x in l if x in l[i:j]])
                        except:
                            w=' '.join([x for x in l if x in l[i:]])
                    print("Just Sit Back And Hold Tight!")
                    chrome_options = webdriver.ChromeOptions()
                    driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',options = chrome_options)
                    driver.get("https://www.youtube.com/")
                    search_form = driver.find_element_by_name('search_query')
                    search_form.send_keys(w)
                    search_form.submit()
                    click_form = driver.find_element_by_id('dismissable')
                    click_form.click()
                    if v == "YES":
                        s=gTTS(text="hmm! now playing, {} in Youtube".format(w),lang='en-uk')
                        s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                        playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                        os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                except:
                    print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
                    if v == "YES":
                        playsound(r"D:\Python Files\Audiofiles\offline.mp3")
                
            elif "glenda" in q_ and "love you" in q_:
                try:
                    s=gTTS(text="I Love you too!",lang='en-uk')
                    s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                except requests.exceptions.ConnectionError:
                    pass
            elif "sid" in q_ and "love you" in q_:
                print("I Love You Too ❤")
                try:
                    s=gTTS(text="hmm he Loves you too!",lang='en-uk')
                    s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                except requests.exceptions.ConnectionError:
                    pass
            elif "hey sid" in q_ or "hi sid" in q_:
                print("Hey Hii \nHow may I help you?")
            elif "glenda" in q_ and "love you" in q_:
                print("She Loves You Too ❤")
                try:
                    s=gTTS(text="hmm Love you too!",lang='en-uk')
                    s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                except requests.exceptions.ConnectionError:
                    pass
            elif "glenda" in q_ and "you" in q_:
                print("Hmm that was UnExpected!")
                try:
                    s=gTTS(text="hmm i didn't expect that!",lang='en-uk')
                    s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                except requests.exceptions.ConnectionError:
                    pass
            elif "hey glenda" in q_ or ("hi" in q_ and "glenda" in q_) or "hey voice" in q_ or ("hi" in q_ and "voice" in q_):
                 try:
                     s=gTTS(text="Hey Hi I'm Glenda, I'm Sid's voice assistant",lang='en-uk')
                     s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                     playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                     os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                 except requests.exceptions.ConnectionError:
                     print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
                     playsound(r"D:\Python Files\Audiofiles\offline.mp3")
            elif "glenda" in q_ or "about glenda" in q_ or "voice assistant" in q_ or "who is glenda" in q_ or "what is glenda" in q_:
                print("Glenda is my Voice Assistant")
                y=input("Do you wanna say Hi to Glenda: ").casefold()
                if 'n' not in y:
                    i=input("Go for it: ").casefold()
                    try:
                        if "hi" in i or "hey" in i:
                            s=gTTS(text="Hey Hi I'm Glenda, I'm Sid's voice assistant",lang='en-uk')
                            s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                            playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                            os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                        else:
                            print("That's Alright!")
                    except requests.exceptions.ConnectionError:
                        print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
                        playsound(r"D:\Python Files\Audiofiles\offline.mp3")
                else:
                    print("That's Alright!")
                print("Truth is:As I wanted be completely Virtual...So I hired a Voice Assistant!✅")
            elif "who is siddiq" in q_:
                print("He is the one Who Built me!")
                try:
                    s=gTTS(text="hmm he He is the one who Built Us!",lang='en-uk')
                    s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                except requests.exceptions.ConnectionError:
                    pass
            elif "who" in q_ and ("you" in q_ or "sid" in q_ or "glenda" in q_):
                print("Siddiq, the one who Created & Developed me!")
                try:
                    s=gTTS(text="hmm he He is the one who Created & Developed Us!",lang='en-uk')
                    s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                except requests.exceptions.ConnectionError:
                    pass
            elif "how are you glenda" in q_:
                print("She's Great")
                try:
                    s=gTTS(text="hmm I'm Great!",lang='en-uk')
                    s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                except requests.exceptions.ConnectionError:
                    pass
            elif "jokes" in q_:
                jokes()
                print("I Guess That puts a Smile on your Face (ツ)")
            elif "joke" in q_:
                joke()
                print("I Guess That puts a Smile on your Face (ツ)")
            elif "who are you" in q_ or "what are you" in q_ or "who is sid" in q_:
                sid_info()
            elif "fitness tip" in q_:
                fitness()
            elif "open private browsing" in q_ or "open private browser" in q_ :
                opb()
            elif "do you know my" in q_ or "did you know my" in q_ or "do you know me" in q_ or "recognize" in q_ or "recognise" in q_ or "remember" in q_:
                print("Sorry i did'nt know that")
                try:
                    s=gTTS(text="hmm Sorry i did'nt know that!",lang='en-uk')
                    s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                except requests.exceptions.ConnectionError:
                    pass
            elif ("you" in q_ and "capable" in q_) or "topper" in q_ or ("you" in q_ and "extra" in q_):
                print("Paduthikoooooo")
                try:
                    s=gTTS(text="paduthikooooooo!",lang='ta', slow=True)
                    s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                except requests.exceptions.ConnectionError:
                    pass
            elif "private browser" in q_ or "private browsing" in q_:
                print("I would Suggest you DuckDuckGo or Swisscows or Search Encrypt")
                try:
                    s=gTTS(text="hmm I would Suggest you DuckDuckGo or Swisscows or Search Encrypt",lang='en-uk')
                    s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                except requests.exceptions.ConnectionError:
                    pass
            elif "html file" in q_ or "extract html" in  q_ or "html content" in q_:
                html_con()
            elif "what" in q_ and "in" in q_:
                try:
                    print("Just Sit Back And Hold Tight!")
                    webbrowser.open("https://google.com/search?q=%s" % q_)
                    if v == "YES":
                        s=gTTS(text="hmm here are the results!",lang='en-uk')
                        s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                        playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                        os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                except requests.exceptions.ConnectionError:
                    print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
                    if v == "YES":
                        playsound(r"D:\Python Files\Audiofiles\offline.mp3")
            elif "weather" in q_:
                weather()
            elif "time" in q_:
                time()
            elif "date" in q_ and ("this" in q_ or "present" in q_ or "today" in q_):
                date()
            elif "year" in q_ and ("this" in q_ or "present" in q_):
                year()
            elif "month" in q_ and ("this" in q_ or "present" in q_):
                month()
            elif "what is" in q_ or "what if" in q_ or "how do" in q_ or "how is" in q_ or "when" in q_ or "where" in q_ or "who" in q_ or "why" in q_:
                try:
                    print("Just Sit Back And Hold Tight!")
                    webbrowser.open("https://google.com/search?q=%s" % q_)
                    if v == "YES":
                        s=gTTS(text="hmm these are Results from Internet!",lang='en-uk')
                        s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                        playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                        os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                except requests.exceptions.ConnectionError:
                    print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮ ")
                    if v == "YES":
                        playsound(r"D:\Python Files\Audiofiles\offline.mp3")
            elif "siri" in q_ or "hey google" in q_ or "cortana" in q_ or "ok google" in q_ or "alexa" in q_ or "hi google" in q_:
                rep()
            elif "describe you" in q_ or "about you" in q_ or "personal sketch" in q_ or "about sid" in q_:
                sid_info()
            elif "scan file" in q_ or "scan folder" in q_ or "scan disk" in q_ or "scan location" in q_ or " scan" in q_:
                f_scan()
            elif "iam" in q_ or "i'm" in q_:
                print("I'm Glad to Acknowledge that!")
                try:
                    s=gTTS(text="I'm Glad to Acknowledge that!",lang='en-uk')
                    s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                except requests.exceptions.ConnectionError:
                    pass
            elif "sid" in q_ and "you" in q_:
                print("Hmm that was UnExpected!")
                try:
                    s=gTTS(text="hmm he didn't expect that!",lang='en-uk')
                    s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                except requests.exceptions.ConnectionError:
                    pass
            elif (("search" or "look" in q_ or "find" in q_) and "video" in q_) or "youtube search" in q_ or "youtube video" in q_:
                try:
                    s=gTTS(text="hmm so Enter the video you wanted to search",lang='en-uk')
                    s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                except requests.exceptions.ConnectionError:
                    pass
                vid_search()
            elif "my" in q_ and "is" in q_:
                print("I'm Glad to Acknowledge that!")
                try:
                    s=gTTS(text="I'm Glad to Acknowledge that!",lang='en-uk')
                    s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                    os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                except requests.exceptions.ConnectionError:
                    pass
            elif "restart" in q_ or "reboot" in q_:
                restart()
            elif "shutdown" in q_ or "shut down" in q_ or "shut-down" in q_:
                shutdown()
            elif "logout" in q_ or "log out" in q_ or "sign out" in q_ or "signout" in q_:
                logout()
            elif q_ == "":
                pass
            else:
                try:
                    print("Just Sit Back And Hold Tight!")
                    webbrowser.open("https://google.com/search?q=%s" % q_)
                    if v == "YES":
                        s=gTTS(text="hmm these are Results from Internet! about {}".format(q_),lang='en-uk')
                        s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                        playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
                        os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
                except requests.exceptions.ConnectionError:
                    print(" \t⚠Oops...Make Sure That You Are Connected With Internet⚠ ☮If Not, Just Carry On☮")
                    if v == "YES":
                        playsound(r"D:\Python Files\Audiofiles\offline.mp3")
        finally:
            pass

#=======================================================================================================================#

q1=input().casefold()
try:
    if "hey siri" in q1 or "hey google" in q1 or "hey cortana" in q1 or "ok google" in q1 or "alexa" in q1:
        print("For clearification: I'm Sid...Virtual Sid")
        rep1()
    if q1 == "hey sid" or q1 == "hi sid":
        print("Hey Hi!")
    if q1 == "":
        print("Hi! I'm Sid, Virtual Assistant")
        print("\n So now How can I help you? ")
        try:
            process()
        finally:
            process()
    process()
finally:
    process()

#==============================First Finished & Tested Prototype on 20/04/2020---03:52 AM===============================#

#==============================First Updated & Tested Prototype |*| 21/04/2020---12:51 AM===============================#
    
