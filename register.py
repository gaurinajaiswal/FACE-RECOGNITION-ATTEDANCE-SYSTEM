from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

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

        # =====button
        #img=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\regbtn.jpg")
        #img=img.resize((200,80))
        #self.photo_btn=ImageTk.PhotoImage(img)
        #b1=Button(frame,image=self.photo_btn,borderwidth=0,cursor="hand2",bg="white")
        #b1.place(x=10,y=470,width=300)

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










if __name__ == "__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()