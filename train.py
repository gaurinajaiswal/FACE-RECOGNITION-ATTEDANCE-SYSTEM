from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recoginiton System")

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        train_bg=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\trainback.jpg")
        train_bg=train_bg.resize((1540,800))
        self.photo_bg=ImageTk.PhotoImage(train_bg)
        train_bg_img=Label(self.root,image=self.photo_bg)
        train_bg_img.place(x=0,y=45,width=1540,height=800)

        top_img=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\topimg00.png")
        top_img=top_img.resize((1540,345))
        self.photoimg_top=ImageTk.PhotoImage(top_img)
        top_lbl=Label(self.root,image=self.photoimg_top)
        top_lbl.place(x=0,y=45,width=1540,height=345)

        # button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("Sans serif fonts",30,"bold"),bg="white",fg="midnight blue")
        b1_1.place(x=0,y=380,width=1540,height=60)

        bottom_img=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\botimg.png")
        bottom_img=bottom_img.resize((1540,360))
        self.photoimg_bottom=ImageTk.PhotoImage(bottom_img)
        bot_lbl=Label(self.root,image=self.photoimg_bottom)
        bot_lbl.place(x=0,y=440,width=1540,height=360)

    
    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []
        for image_path in path:
            try:
                img = Image.open(image_path).convert('L')  # Convert to grayscale
                imagenp = np.array(img, 'uint8')

                # Extract ID from file name like "user.1.jpg"
                id = int(os.path.split(image_path)[1].split(".")[1])

                faces.append(imagenp)
                ids.append(id)

                cv2.imshow("Training", imagenp)
                cv2.waitKey(1)

            except Exception as e:
                print(f"Skipped file {image_path} due to error: {e}")

        if len(faces) == 0 or len(faces) != len(ids):
            messagebox.showerror("Error", "No valid training data found!")
            return
        ids = np.array(ids)

        # Train the classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!!")


           

       









if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
        