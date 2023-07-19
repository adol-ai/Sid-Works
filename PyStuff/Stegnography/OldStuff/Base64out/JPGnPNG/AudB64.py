import time
import math
import base64
import numpy as np

f = open("Aud.mp3", 'rb')
b64_str = f.read()
aud_data = base64.urlsafe_b64encode(b64_str)
aud_b64 = aud_data.decode('ascii').replace("_","/").replace("-","+")


f = open("wavAud.wav", "wb")
decoded_b64 = base64.b64decode(aud_b64)
f.write(decoded_b64)
f.close()
