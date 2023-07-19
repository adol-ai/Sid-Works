import os
import cv2
import glob
import pprint
import xml.etree.ElementTree as et

os.chdir("K:\\Python Files\\Computer Vision\\picNxml")
l=glob.iglob("*.xml")
l=list(l)
l_=[]

for i in l:
    l_.append(i.rstrip(".xml")+".png")

x=list(zip(l_,l))

print(x)

file=x[17]
tree=et.parse(file[1])
root=tree.getroot()
print(root.findall('object'))

datapoints=[]
for k in root.findall('object'):
    print(k[0].text)
    print("xMin --> ", k[4][0].text)
    print("yMin --> ", k[4][1].text)
    print("xMax --> ", k[4][2].text)
    print("yMax --> ", k[4][3].text)
    img_w=int(root.find("size")[0].text)
    img_h=int(root.find("size")[1].text)
    w=int((int(k[4][2].text)-int(k[4][0].text)))
    h=int((int(k[4][3].text)-int(k[4][1].text)))
    print(w,h)
    x_cen= int((int(k[4][0].text)+(int(k[4][2].text)-int(k[4][0].text))/2))
    y_cen= int((int(k[4][1].text)+(int(k[4][3].text)-int(k[4][1].text))/2))
    print(x_cen,y_cen)
    value=[k[0].text,
           k[4][0].text,
           k[4][1].text,
           k[4][2].text,
           k[4][3].text,
           x_cen,
           y_cen,
           w,
           h]
    datapoints.append(value)

pprint.pprint(datapoints)


img=cv2.imread(file[0])
cv2.imshow("Pic", img)
cv2.waitKey(500)

#rec
for y in datapoints:
    #rec
    min_point=(int(y[1]), int(y[2]))
    max_point=(int(y[3]), int(y[4]))
    cv2.rectangle(img,min_point,max_point,(0,0,255), thickness=3, lineType=cv2.LINE_8)
    #cir
    cen=(int(y[5]), int(y[6]))
    rad_w=int(y[7])-50
    rad_h=int(y[8])-50
    cv2.circle(img, cen, rad_w, (255,0,0), thickness=2, lineType=cv2.LINE_AA)
    #elli
    axis = (rad_w,rad_h)
    if rad_w<rad_h:
        cv2.ellipse(img, cen, axis,0 ,0, 360, (0,255,0),thickness=1) 
    else:
        cv2.ellipse(img, cen, axis,90 ,0, 360, (0,255,0),thickness=1)
cv2.imshow("LabelledPic", img)
cv2.waitKey(500)
