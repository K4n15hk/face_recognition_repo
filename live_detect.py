import cv2
import face_recognition as facrec
import os
encodings={}
directory='/home/robot/Documents/face_detect/images'
for filename in os.listdir(directory):
    name=filename.split('.')[0]
    img=cv2.imread(directory+'/'+filename)
    rgb_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img_encoding=facrec.face_encodings(rgb_img)[0]
    encodings[name]=img_encoding
cam=cv2.VideoCapture(0)
check=1
while check==1:
    ret,frame=cam.read()
    cv2.imshow('frame',frame)
    rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    if cv2.waitKey(1) ==  ord('q'):
            break   
    try:

        encode=facrec.face_encodings(rgb)[0]
        for e in encodings:
            result=facrec.compare_faces([encodings[e]],encode)
            if result == [True]:
                print(e)
                check =0
            else:
                continue
    except:
        pass

cam.release()
cv2.destroyAllWindows()
