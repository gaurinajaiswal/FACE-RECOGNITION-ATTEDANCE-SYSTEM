from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recoginiton System")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        train_bg=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\trainback.jpg")
        train_bg=train_bg.resize((1540,800))
        self.photo_bg=ImageTk.PhotoImage(train_bg)
        train_bg_img=Label(self.root,image=self.photo_bg)
        train_bg_img.place(x=0,y=45,width=1540,height=800)

        main_frame=Frame(train_bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=55,width=500,height=600)




if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()