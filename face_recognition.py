from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recoginiton System")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("Sans Serif fonts",40,"bold"),bg="white",fg="midnight blue")
        title_lbl.place(x=0,y=0,width=1530,height=60)

        face_bg=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\backgroundimg.jpg")
        face_bg=face_bg.resize((1540,800))
        self.photoface_bg=ImageTk.PhotoImage(face_bg)
        bg_img=Label(self.root,image=self.photoface_bg)
        bg_img.place(x=0,y=60,width=1540,height=800)

        face_det=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\facedetect.webp")
        face_det=face_det.resize((690,400))
        face_det_with_border = ImageOps.expand(face_det, border=4, fill="black")
        self.photoface_det=ImageTk.PhotoImage(face_det_with_border)
        top_lbl=Label(self.root,image=self.photoface_det)
        top_lbl.place(x=425,y=170,width=698,height=408)

        # button
        b1_1=Button(self.root,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("Sans serif fonts",25,"bold"),bg="white",fg="midnight blue")
        b1_1.place(x=425,y=580,width=698,height=50)

    # ===============attendance=================
    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            mydatalist=f.readlines()
            name_list=[]
            for line in mydatalist:
                entry=line.split((","))
                name_list.append(entry[0])
            if i not in [line.split(',')[0] for line in mydatalist]:
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},Present")



    # =============face recognition===============
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence = min(100, int(100 * (1 - predict / 300)))

                conn=mysql.connector.connect(host="localhost",user="root",password="Mysql@14",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("SELECT Student_id, Roll, Name, Dep FROM student WHERE Student_id=%s", (id,))
                result = my_cursor.fetchone()
                if result and confidence > 77:
                    i, r, n, d = map(str, result)
                    cv2.putText(img,f"Id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,255),3)
                    cv2.putText(img,f"Roll No:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)
        if not video_cap.isOpened():
            messagebox.showerror("Error","Cannot open webcam")
            return

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1) & 0xFF == 27:
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()