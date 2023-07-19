import base64

f = open("Aud.mp3", 'rb')
b64_str = f.read()

aud_data = base64.urlsafe_b64encode(b64_str)

aud_b64 = aud_data.decode('ascii').replace("_","/").replace("-","+")



