import cv2
import math
import numpy as np

vid = cv2.VideoCapture('Vid.mp4')
kf = cv2.KalmanFilter(4,2)
kf.measurementMatrix = np.array([[1,0,0,0],[0,1,0,0]], np.float32)
kf.transitionMatrix = np.array([[1,0,1,0],[0,1,0,1],[0,0,1,0],[0,0,0,1]], np.float32)

class EuclideanDistTracker:
    def __init__(self):
        self.center_points = {}
        self.id_count = 0


    def update(self, objects_rect):
        objects_bbs_ids = []
        for rect in objects_rect:
            x, y, w, h = rect
            cx = (x + x + w) // 2
            cy = (y + y + h) // 2
            same_object_detected = False
            for id, pt in self.center_points.items():
                dist = math.hypot(cx - pt[0], cy - pt[1])
                if dist < 25:
                    self.center_points[id] = (cx, cy)
                    print(self.center_points)
                    objects_bbs_ids.append([x, y, w, h, id])
                    same_object_detected = True
                    break
            if same_object_detected is False:
                self.center_points[self.id_count] = (cx, cy)
                objects_bbs_ids.append([x, y, w, h, self.id_count])
                self.id_count += 1
        new_center_points = {}
        for obj_bb_id in objects_bbs_ids:
            _, _, _, _, object_id = obj_bb_id
            center = self.center_points[object_id]
            new_center_points[object_id] = center
        self.center_points = new_center_points.copy()
        return objects_bbs_ids


tracker = EuclideanDistTracker()

def est(x,y):
    m = np.array([[np.float32(x)],[np.float32(y)]])
    kf.correct(m)
    pred = kf.predict()
    return pred

def Contour(frame):
    x,y,w,h=0,0,0,0
    contours,_ = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i in contours:
        ar = cv2.contourArea(i)
        if ar > 500:
            peri = cv2.arc.Length(i,True)
            approx = cv2.approxPolyDP(i, 0.02*peri, True)
            x,y,w,h = cv2.boundRect(approx)
        return x+w/2, y+h/2, w, h

def masking(frame):
    lower = np.array([130,30,0])
    upper = np.array([250,250,90])
    mask = cv2.inRange(frame,lower,upper)
    k = np.ones([10,10])
    mask_d = cv2.dilate(mask, k)
    mask_c = cv2.bitwise_and(frame, frame, mask = mask_d)
    mask_c = cv2.resize(mask_c, (800,800))
    return mask_d, mask_c

def draw(frame, points):
    for i in range(1, len(points)):
        cv2.line(frame, points[i-1], points[i], (0,0,255), 2)

tracker = EuclideanDistTracker()
object_detector = cv2.createBackgroundSubtractorMOG2(history=200, varThreshold=300)

if (vid.isOpened() == False):
  print("Error opening the video file")
else:
  fps = int(vid.get(5))
  print("Frame Rate : ",fps,"frames per second")  
  frame_count = vid.get(7)
  print("Frame count : ", frame_count)

points = []
count = 0
while vid.isOpened():
    ret, frame=vid.read()
    if ret is True:
        ret, frame = vid.read()
        height, width, _ = frame.shape

        mask = object_detector.apply(frame)
        _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        detections = []
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 100:
                cv2.drawContours(frame, [cnt], -1, (0, 255, 0), 2)
                x, y, w, h = cv2.boundingRect(cnt)
                detections.append([x, y, w, h])
                
        boxes_ids = tracker.update(detections)
        for box_id in boxes_ids:
            x, y, w, h, id = box_id
            cv2.putText(frame, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        '''mask,_ = masking(frame)
        _, mask_c = masking(frame)
        n_point = []
        if Contour(mask)== None:
            pass
        else:
            x,y,w,h = Contour(mask)
            n_point.append((int(x), int(y)))
            for i in n_point:
                points.append(i)

            if (0,0) in points:
                points.remove((0,0))
            print(points)
            if len(points)>15:
                del points[0]
            draw(frame, points)

            cv2.circle(frame, (int(x), int(y)), 20, [0,0,255], 2,7)
            cv2.line(frame, (int(x), int(y+20)), (int(x+50), int(y+20)), [0,0,0], 2, 7)'''
        cv2.imshow('Vid',frame)
        key=cv2.waitKey(1)
        if key==ord(' '):
            time.sleep(2)
        if key==ord('q'):
            cv2.destroyAllWindows()
            break
    else:
        break

cv2.destroyAllWindows()
