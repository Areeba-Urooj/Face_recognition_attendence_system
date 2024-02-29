import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video=cv2.VideoCapture(0)

#Load Imagess
A_image=face_recognition.load_image_file('faces/A.jpg')
A_encoding=face_recognition.face_encodings(A_image)[0]


B_image=face_recognition.load_image_file('faces/B.jpg')
B_encoding=face_recognition.face_encodings(B_image)[0]

#storing names
known_face_encoding=[A_encoding,B_encoding]
known_faceNames=['Hatake Kakashi','Osamu Dazai']

#list of expected employees
employees=known_faceNames.copy()
face_locations=[]
face_encodings=[]

#current datetime
now=datetime.now()
current_datetime=now.strftime('%Y-%m-%d')

f=open(f'{current_datetime}.csv','w+',newline='')
lnwriter=csv.writer(f)

while True:
    _,frame=video.read()
    small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame=cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    #recognize faces
    face_locations=face_recognition.face_locations(rgb_small_frame)
    face_encodings=face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches=face_recognition.compare_faces(known_face_encoding, face_encoding)
        face_distance=face_recognition.face_distance(known_face_encoding, face_encoding)
        best_index=np.argmin(face_distance)

        if(matches[best_index]):
            name=known_face_encoding[best_index]
            
    cv2.imshow('Attendence', frame)
    if cv2.waitkey(1) & 0xFF == ord("q"):
        break

    #Add text if a person is present
    if name in known_face_encoding:
        font=cv2.Font_HERSHEYS_SIMPLEX
        bottomLeftCornerOfText=(10, 100)
        fontscale=1.5
        fontcolor=(255, 0, 0)
        thickness=3
        linetype=2
        cv2.putText(frame,name+ "Present",font, bottomLeftCornerOfText, fontscale, fontcolor, thickness, linetype)

        if name in employees:
            employees.remove(name)
            current_datetime=now.strftime("%H,%M,%S")
            lnwriter=writerow([name, current_datetime])

            
video.release()
cv2.destryAllWindows()
f.close()