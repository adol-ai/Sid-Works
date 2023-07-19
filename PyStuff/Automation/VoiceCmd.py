import os
from gtts import gTTS
from playsound import playsound
from datetime import datetime

true=True
print("...~...~...V~V...~...~...~...")
while true==True:
    td=datetime.now()
    h_=td.strftime("%H")
    if len(h_)==1:
        h_='0'+h_
    m_=td.strftime("%M")
    if h_=='02' and m_=='30':
        game='start'
        s=gTTS(text="Siddiq Initiating lap 1 right now!"*15,lang='en-uk')
        s.save(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
        playsound(r"D:\Python Files\Audiofiles\VoiceOver.mp3")
        os.remove("D:\Python Files\Audiofiles\VoiceOver.mp3")
    elif h_=='08' and m_=='30':
        game='start'
    elif h_=='10' and m_=='00':
        game='start'
    elif h_=='11' and m_=='15':
        game='start'
    try:
        if game=='start':
            break
    except:
        pass
