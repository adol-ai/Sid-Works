import cv2
import time

vid=cv2.VideoCapture('matchAud.mp4')

if (vid.isOpened() == False):
  print("Error opening the video file")
else:
  # Get frame rate information
 
  fps = int(vid.get(5))
  print("Frame Rate : ",fps,"frames per second")  
 
  # Get frame count
  frame_count = vid.get(7)
  print("Frame count : ", frame_count)

for i in range(0,105):
    try:
        print(i,"---->",vid.get(i))
    except:
        pass
a=0
b=0
while vid.isOpened():
    ret, frame=vid.read()
    if ret is True:
        #cv2.imshow('Vid',frame)
        #key=cv2.waitKey(1)
        if b%fps==0:
          cv2.imwrite("frames/"+str(a)+".png",frame)
          a+=1
          print(str(a)+".png")
        b+=1
        if key==ord(' '):
            time.sleep(2)
    else:
        break

cv2.destroyAllWindows()
