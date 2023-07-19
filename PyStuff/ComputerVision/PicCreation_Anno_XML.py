import os
import cv2
import glob
import pprint
import xml.etree.ElementTree as et

os.chdir("F:\\Python Files\\Computer Vision\\Yooooo")
l=glob.iglob("*.xml")
l=list(l)
l_=[]

for i in l:
    l_.append(i.rstrip(".xml")+".png")

x=list(zip(l_,l))

print(x)

file=x[0]
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

dp=[['referee', '73', '261', '206', '656', 139, 458, 133, 395],
 ['player', '364', '66', '685', '768', 584, 407, 201, 662],
 ['player', '698', '53', '927', '715', 826, 384, 201, 662],
 ['face', '505', '71', '619', '196', 567, 133, 104, 125],
 ['face', '780', '76', '884', '180', 832, 138, 104, 125],
 ['b_ball', '354', '243', '474', '379', 414, 311, 120, 136],
 ['face', '97', '261', '172', '340', 134, 300, 75, 79],
 ['basket', '1096', '213', '1140', '283', 1119, 248, 67, 70]]
#rec
for y in dp:
    #rec
    if y[0]=="face":        
        min_point=(int(y[1]), int(y[2]))
        max_point=(int(y[3]), int(y[4]))
        cv2.rectangle(img,min_point,max_point,(255,0,0), thickness=3, lineType=cv2.LINE_8)
    if y[0]=="player":        
        min_point=(int(y[1]), int(y[2]))
        max_point=(int(y[3]), int(y[4]))
        cv2.rectangle(img,min_point,max_point,(0,255,0), thickness=3, lineType=cv2.LINE_8)
    if y[0]=="b_ball":        
        min_point=(int(y[1]), int(y[2]))
        max_point=(int(y[3]), int(y[4]))
        cv2.rectangle(img,min_point,max_point,(0,0,255), thickness=3, lineType=cv2.LINE_8)
    if y[0]=="basket":        
        min_point=(int(y[1]), int(y[2]))
        max_point=(int(y[3]), int(y[4]))
        cv2.rectangle(img,min_point,max_point,(0,255,255), thickness=3, lineType=cv2.LINE_8)
cv2.imshow("LabelledPic", img)
cv2.imwrite("LabelledLayer.png",img)
cv2.waitKey(500)
