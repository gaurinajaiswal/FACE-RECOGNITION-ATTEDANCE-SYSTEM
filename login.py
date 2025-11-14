from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()


class Login_window:
    def __init__(self,root):
        self.root= root
        self.root.title("login")
        self.root.geometry("1530x790+0+0")

        login_bg=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\backgroundimg.jpg")
        login_bg=login_bg.resize((1540,800))
        self.photo_bg=ImageTk.PhotoImage(login_bg)
        login_bg_img=Label(self.root,image=self.photo_bg)
        login_bg_img.place(x=0,y=0,width=1540,height=800)

        #title
        title_lbl=Label(self.root,text="FACE ID ATTENDANCE",font=("Sans serif fonts",40,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=60)

        frame=Frame(self.root,bg="white",bd=1,relief=SOLID)
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\loginlogo.jpg")
        img1=img1.resize((100,100))
        self.photoimg1=ImageTk.PhotoImage(img1)
        lb_img1=Label(image=self.photoimg1,)
        lb_img1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="GET STARTED", font=("Sans serif fonts",15,"bold"),fg="black",bg="white")
        get_str.place(x=95,y=100)

        # LABELS
        username_lbl=Label(frame,text="Username",font=("Sans serif fonts",12,"bold"),fg="black",bg="white")
        username_lbl.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("Sans serif fonts",10))
        self.txtuser.place(x=40,y=180,width=270)

        password_lbl=Label(frame,text="Password",font=("Sans serif fonts",12,"bold"),fg="black",bg="white")
        password_lbl.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("Sans serif fonts",10),show="*")
        self.txtpass.place(x=40,y=250,width=270)

        # icon
        img2=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\userlogo.jpg")
        img2=img2.resize((25,25))
        self.photoimg2=ImageTk.PhotoImage(img2)
        lb_img1=Label(image=self.photoimg2,)
        lb_img1.place(x=655,y=327,width=25,height=25)

        img3=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\passlogo.png")
        img3=img3.resize((25,25))
        self.photoimg3=ImageTk.PhotoImage(img3)
        lb_img1=Label(image=self.photoimg3, bg="white")
        lb_img1.place(x=655,y=397,width=25,height=25)

        # login btn
        loginbtn=Button(frame,command=self.login,text="Login",font=("Sans serif fonts",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="light blue",activeforeground="white",activebackground="light blue")
        loginbtn.place(x=110,y=300,width=120,height=35)

        # register btn
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("Sans serif fonts",10),borderwidth=0,fg="black",bg="white",activeforeground="black",activebackground="white")
        registerbtn.place(x=15,y=360,width=160)

        # forget password btn
        forpassbtn=Button(frame,text="Forget Password",command=self.forgot_pass_win,font=("Sans serif fonts",10),borderwidth=0,fg="black",bg="white",activeforeground="black",activebackground="white")
        forpassbtn.place(x=10,y=380,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Success","Welcome to FaceID Attendance")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Mysql@14",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                                                                                    ))
            row=my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Invalid username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recoginition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close

        self.var_secquestion=StringVar()
        self.var_secanswer=StringVar()
        self.var_password=StringVar()

    def reset(self):
        if self.combo_secque.get()=="Select":
            messagebox.showerror("Error","Select the security question")
        elif self.var_secanswer.get()=="":
            messagebox.showerror("Error","Please enter the security answer")
        elif self.var_password.get()=="":
            messagebox.showerror("Error","Please enter the new password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Mysql@14",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and secquestion=%s and secanswer=%s")
            value=(self.txtuser.get(),self.combo_secque.get,self.var_secanswer.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer")
            else:
                qury=("update register set password=%s where email=&s")
                values=(self.var_password.get(),self.txtuser.get())
                my_cursor.execute(qury,values)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your new password has reset, please login with new password")


    def forgot_pass_win(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Mysql@14",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("Error","Please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("Sans serif fonts",15,"bold"),fg="black",bg="white")
                l.place(x=0,y=10,relwidth=1)

                secquestion=Label(self.root2,text="Select Security Question",textvariable=self.var_secquestion,font=("Sans serif fonts",12,"bold"),bg="white",fg="midnight blue")
                secquestion.place(x=50,y=80)

                self.combo_secque=ttk.Combobox(self.root2,font=("Sans serif fonts",12),state="readonly")
                self.combo_secque["values"]=("Select","Your Birth Place","Your Pet Name","Your Favourite Color")
                self.combo_secque.place(x=50,y=110,width=250)
                self.combo_secque.current(0)

                secanswer=Label(self.root2,text="Security Answer",textvariable=self.var_secanswer,font=("Sans serif fonts",12,"bold"),bg="white",fg="midnight blue")
                secanswer.place(x=50,y=150)
                secanswer_entry=ttk.Entry(self.root2,font=("Sans serif fonts",12))
                secanswer_entry.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",textvariable=self.var_password,font=("Sans serif fonts",12,"bold"),bg="white",fg="midnight blue")
                new_password.place(x=50,y=220)
                new_password_entry=ttk.Entry(self.root2,font=("Sans serif fonts",12),show="*")
                new_password_entry.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",font=("Sans serif fonts",12,"bold"),bg="white",fg="black")
                btn.place(x=150,y=290)




class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1530x790+0+0")

        # =======variables=====
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_secquestion=StringVar()
        self.var_secanswer=StringVar()
        self.var_password=StringVar()
        self.var_conpassword=StringVar()
        self.var_checkbtn=IntVar()

        register_bg=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\backgroundimg.jpg")
        register_bg=register_bg.resize((1540,800))
        self.photo_bg=ImageTk.PhotoImage(register_bg)
        register_bg_img=Label(self.root,image=self.photo_bg)
        register_bg_img.place(x=0,y=0,width=1540,height=800)

        #title
        title_lbl=Label(self.root,text="FACE ID ATTENDANCE",font=("Sans serif fonts",40,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=60)

        leftreg_bg=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\regleft.jpg")
        leftreg_bg=leftreg_bg.resize((470,550))
        self.photoleft_bg=ImageTk.PhotoImage(leftreg_bg)
        leftreg_bg_img=Label(self.root,image=self.photoleft_bg)
        leftreg_bg_img.place(x=130,y=130,width=470,height=550)

        frame=Frame(self.root,bg="white",bd=1,relief=SOLID)
        frame.place(x=600,y=130,width=800,height=550)

        reg_lbl=Label(frame,text="REGISTER HERE",font=("Sans serif fonts",25,"bold"),bg="white",fg="black")
        reg_lbl.place(x=20,y=20)

# ===== row 1
        fname=Label(frame,text="First Name",font=("Sans serif fonts",12,"bold"),bg="white",fg="midnight blue")
        fname.place(x=50,y=100)
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("Sans serif fonts",12))
        fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("Sans serif fonts",12,"bold"),bg="white",fg="midnight blue")
        lname.place(x=370,y=100)
        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("Sans serif fonts",12))
        lname_entry.place(x=370,y=130,width=250)

# ===== row 2
        contact=Label(frame,text="Contact No",font=("Sans serif fonts",12,"bold"),bg="white",fg="midnight blue")
        contact.place(x=50,y=170)
        contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("Sans serif fonts",12))
        contact_entry.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("Sans serif fonts",12,"bold"),bg="white",fg="midnight blue")
        email.place(x=370,y=170)
        email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("Sans serif fonts",12))
        email_entry.place(x=370,y=200,width=250)

# ====== row 3
        secquestion=Label(frame,text="Select Security Question",font=("Sans serif fonts",12,"bold"),bg="white",fg="midnight blue")
        secquestion.place(x=50,y=240)

        self.combo_secque=ttk.Combobox(frame,textvariable=self.var_secquestion,font=("Sans serif fonts",12),state="readonly")
        self.combo_secque["values"]=("Select","Your Birth Place","Your Pet Name","Your Favourite Color")
        self.combo_secque.place(x=50,y=270,width=250)
        self.combo_secque.current(0)

        secanswer=Label(frame,text="Security Answer",textvariable=self.var_secanswer,font=("Sans serif fonts",12,"bold"),bg="white",fg="midnight blue")
        secanswer.place(x=370,y=240)
        secanswer_entry=ttk.Entry(frame,font=("Sans serif fonts",12))
        secanswer_entry.place(x=370,y=270,width=250)

# ====== row4
        password=Label(frame,text="Password",font=("Sans serif fonts",12,"bold"),bg="white",fg="midnight blue")
        password.place(x=50,y=310)
        password_entry=ttk.Entry(frame,textvariable=self.var_password,font=("Sans serif fonts",12))
        password_entry.place(x=50,y=340,width=250)

        conpassword=Label(frame,text="Confirm Password",font=("Sans serif fonts",12,"bold"),bg="white",fg="midnight blue")
        conpassword.place(x=370,y=310)
        conpassword_entry=ttk.Entry(frame,textvariable=self.var_conpassword,font=("Sans serif fonts",12))
        conpassword_entry.place(x=370,y=340,width=250)

# ====== checkbox
        checkbtn=Checkbutton(frame,variable=self.var_checkbtn,text="I agree The Terms & Conditions",font=("Sans serif fonts",12),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        register_btn=Button(frame,text="Register",command=self.register_data,font=("Sans serif fonts",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="white",activeforeground="black",activebackground="white")
        register_btn.place(x=50,y=450,width=150)

        login_btn=Button(frame,text="Login Now",font=("Sans serif fonts",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="white",activeforeground="black",activebackground="white")
        login_btn.place(x=280,y=450,width=150)

    #      function declartion
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_secquestion.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_password.get() != self.var_conpassword.get():
            messagebox.showerror("Error","Password and Confirm Password must be same")
        elif self.var_checkbtn.get()==0:
            messagebox.showerror("Error","Please agree our terms & conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Mysql@14",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error","User already exist, Please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_secquestion.get(),
                                                                                        self.var_secanswer.get(),
                                                                                        self.var_password.get()
                                                                                        ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")


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
    main()