from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

class Face_Recoginition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recoginiton System")

        #first img
        img=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\0_5HCXXlt_5G9Qhd3H.jpg")
        img=img.resize((510,170))
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=510,height=170)

        #secong img
        img1=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\vdfvrve.jpg")
        img1=img1.resize((510,170))
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=510,y=0,width=510,height=170)

        #third img
        img2=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\0_5HCXXlt_5G9Qhd3H.jpg")
        img2=img2.resize((510,170))
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1020,y=0,width=510,height=170)

        #bg img
        img3=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\backgroundimg.jpg")
        img3=img3.resize((1530,620))
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=170,width=1540,height=620)

        #title
        title_lbl=Label(bg_img,text="FACE ID ATTENDANCE",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #student button
        img4=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\face-recognisation-02.webp")
        img4=img4.resize((170,170))
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=170,height=170)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("Sans serif fonts",15,"bold"),bg="white",fg="midnight blue")
        b1_1.place(x=200,y=250,width=170,height=40)

        #detect face button
        img5=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\download1.jpg")
        img5=img5.resize((170,170))
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=650,y=100,width=170,height=170)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("Sans serif fonts",15,"bold"),bg="white",fg="midnight blue")
        b1_1.place(x=650,y=250,width=170,height=40)

        #attandence button
        img6=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\download2.jpg")
        img6=img6.resize((170,170))
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=1100,y=100,width=170,height=170)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("Sans serif fonts",15,"bold"),bg="white",fg="midnight blue")
        b1_1.place(x=1100,y=250,width=170,height=40)

        #helpdesk button
        #img7=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\download.jpg")
        #img7=img7.resize((170,170))
        #self.photoimg7=ImageTk.PhotoImage(img7)

        #b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        #b1.place(x=1100,y=100,width=170,height=170)

        #b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("Sans serif fonts",15,"bold"),bg="white",fg="midnight blue")
        #b1_1.place(x=1100,y=250,width=170,height=40)

        #train button
        img8=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\traindata.webp")
        img8=img8.resize((170,170))
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=400,y=350,width=170,height=170)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("Sans serif fonts",15,"bold"),bg="white",fg="midnight blue")
        b1_1.place(x=400,y=520,width=170,height=40)

        #photo face button
        img9=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\photocollection.jpg")
        img9=img9.resize((170,170))
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=850,y=350,width=170,height=170)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("Sans serif fonts",15,"bold"),bg="white",fg="midnight blue")
        b1_1.place(x=850,y=520,width=170,height=40)

        #developer button
        #img10=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\developer.jpg")
        #img10=img10.resize((170,170))
        #self.photoimg10=ImageTk.PhotoImage(img10)

        #b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        #b1.place(x=800,y=350,width=170,height=170)

        #b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("Sans serif fonts",15,"bold"),bg="white",fg="midnight blue")
        #b1_1.place(x=800,y=520,width=170,height=40)

        #exit button
        #img11=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\exitbutton.webp")
        #img11=img11.resize((170,170))
        #self.photoimg11=ImageTk.PhotoImage(img11)

        #b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        #b1.place(x=1100,y=350,width=170,height=170)

        #b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("Sans serif fonts",15,"bold"),bg="white",fg="midnight blue")
        #b1_1.place(x=1100,y=520,width=170,height=40)

    def open_img(self):
        os.startfile("data")

        # =========function buttons==========
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recoginition_System(root)
    root.mainloop()