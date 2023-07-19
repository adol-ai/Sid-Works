import os
import cv2


os.chdir("K:\\Python Files\\Computer Vision\\DataSet")


for i in os.walk(os.getcwd()):
    for j in i[2]:
        print(j)

vid=cv2.VideoCapture("%1d.jpg")

width=int(vid.get(3))
height=int(vid.get(4))
size=(width,height)
writer=cv2.VideoWriter('Output.mp4', cv2.VideoWriter_fourcc(*'MP4V'),20,size)

while vid.isOpened():
    ret,frame=vid.read()
    writer.write(frame)
    if ret is True:
        cv2.imshow('Vid_img',frame)
        cv2.waitKey(2)
    else:
        break
writer.release()

