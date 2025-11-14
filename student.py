from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recoginiton System")

        #=====variables======
        self.var_Dep=StringVar()
        self.var_Course=StringVar()
        self.var_Year=StringVar()
        self.var_Semester=StringVar()
        self.var_Student_id=StringVar()
        self.var_Name=StringVar()
        self.var_Division=StringVar()
        self.var_Roll=StringVar()
        self.var_Gender=StringVar()
        self.var_Dob=StringVar()
        self.var_Email=StringVar()
        self.var_Phone=StringVar()
        self.var_Address=StringVar()
        self.var_Teacher=StringVar()

        #first img
        img=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\0_5HCXXlt_5G9Qhd3H.jpg")
        img=img.resize((510,170))
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=510,height=170)

        #secong img
        img1=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\student.jpg")
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
        img3=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\bgimg.jpg")
        img3=img3.resize((1530,620))
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=170,width=1540,height=620)

        #title
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1521,height=600)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=770,height=540)

        #current course
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=8,width=755,height=120)

        #department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Dep,font=("times new roman",12),width=25,state="read only")
        dep_combo['values']=("Select Department","Computer Science","Information Technology","Meachanical","Electronic Communication")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Course,font=("times new roman",12),width=25,state="read only")
        course_combo['values']=("Select Course","B. Tech","BE","BCA","M. Tech","ME","MCA")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Year,font=("times new roman",12),width=25,state="read only")
        year_combo['values']=("Select Year","1st Year","2nd Year","3rd Year","4th Year")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Semester,font=("times new roman",12),width=25,state="read only")
        semester_combo['values']=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class student information
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=140,width=755,height=370)

        #student id
        studentId_label=Label(class_student_frame,text="Student ID :",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_Student_id,width=25,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        #student name
        studentName_label=Label(class_student_frame,text="Student Name :",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_Name,width=25,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        #roll number
        rollnumber_label=Label(class_student_frame,text="Roll Number :",font=("times new roman",12,"bold"),bg="white")
        rollnumber_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        rollnumber_entry=ttk.Entry(class_student_frame,textvariable=self.var_Roll,width=25,font=("times new roman",12,"bold"))
        rollnumber_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #class division
        classdiv_label=Label(class_student_frame,text="Class Division :",font=("times new roman",12,"bold"),bg="white")
        classdiv_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        division_combo=ttk.Combobox(class_student_frame,textvariable=self.var_Division,font=("times new roman",12),width=23,state="read only")
        division_combo['values']=("A","B","C")
        division_combo.current(0)
        division_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        #gender
        gender_label=Label(class_student_frame,text="Gender :",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_Gender,font=("times new roman",12),width=23,state="read only")
        gender_combo['values']=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #dob
        dob_label=Label(class_student_frame,text="Date Of Birth :",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_Dob,width=25,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        #email
        email_label=Label(class_student_frame,text="E-mail :",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_Email,width=25,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=10,sticky=W)

        #mobile no
        mob_no_label=Label(class_student_frame,text="Mobile Number :",font=("times new roman",12,"bold"),bg="white")
        mob_no_label.grid(row=3,column=2,padx=10,pady=10,sticky=W)

        mob_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_Phone,width=25,font=("times new roman",12,"bold"))
        mob_no_entry.grid(row=3,column=3,padx=10,pady=10,sticky=W)

        #address
        address_label=Label(class_student_frame,text="Address :",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=10,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_Address,width=25,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=10,sticky=W)

        #teacher name
        teacher_label=Label(class_student_frame,text="Professor Name :",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=10,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_Teacher,width=25,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=10,sticky=W)

        #radio buttons
        self.var_PhotoSample=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_PhotoSample,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_PhotoSample,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)

        #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=260,width=740,height=42)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",12,"bold"),bg="grey",fg="white",cursor="hand2")
        save_btn.grid(row=0,column=0,padx=10,pady=3)

        update_btn=Button(btn_frame,text="Update",width=17,command=self.update_data,font=("times new roman",12,"bold"),bg="grey",fg="white",cursor="hand2")
        update_btn.grid(row=0,column=1,padx=10,pady=3)

        delete_btn=Button(btn_frame,text="Delete",width=17,command=self.delete_data,font=("times new roman",12,"bold"),bg="grey",fg="white",cursor="hand2")
        delete_btn.grid(row=0,column=2,padx=10,pady=3)

        reset_btn=Button(btn_frame,text="Reset",width=17,command=self.reset_data,font=("times new roman",12,"bold"),bg="grey",fg="white",cursor="hand2")
        reset_btn.grid(row=0,column=3,padx=10,pady=3)

        #button frame1
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=5,y=300,width=740,height=42)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=30,font=("times new roman",12,"bold"),bg="grey",fg="white",cursor="hand2")
        take_photo_btn.grid(row=0,column=0,padx=40,pady=2)

        upd_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=30,font=("times new roman",12,"bold"),bg="grey",fg="white",cursor="hand2")
        upd_photo_btn.grid(row=0,column=1,padx=40,pady=2)



        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=790,y=10,width=710,height=540)

        # =======search system======
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=10,width=695,height=110)

        search_label=Label(search_frame,text="Search By :",font=("times new roman",12,"bold"),bg="beige")
        search_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12),width=25,state="read only")
        search_combo['values']=("Select","Roll Number","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=25,font=("times new roman",12,"bold"))
        search_entry.grid(row=1,column=0,padx=10)

        search_btn=Button(search_frame,text="Search",width=14,font=("times new roman",12,"bold"),bg="grey",fg="white",cursor="hand2")
        search_btn.grid(row=1,column=1)

        showall_btn=Button(search_frame,text="Show All",width=14,font=("times new roman",12,"bold"),bg="grey",fg="white",cursor="hand2")
        showall_btn.grid(row=1,column=2)

        # table frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=130,width=695,height=380)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("Dep","Course","Year","Semester","Student_id","Name","Division","Roll","Gender","Dob","Email","Phone","Address","Teacher","PhotoSample"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semeter")
        self.student_table.heading("Student_id",text="Student Id")
        self.student_table.heading("Name",text="Student Name")
        self.student_table.heading("Division",text="Division")
        self.student_table.heading("Roll",text="Roll No")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Dob",text="Date of Birth")
        self.student_table.heading("Email",text="E-Mail")
        self.student_table.heading("Phone",text="Phone No.")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("PhotoSample",text="Photo Sample Status")
        self.student_table["show"]="headings"

        self.student_table.column("Dep",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("Student_id",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Division",width=100)
        self.student_table.column("Roll",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Dob",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("PhotoSample",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        # ==========function declaration=========
    def add_data(self):
    # Check for required fields
        if self.var_Dep.get()=="Select Department" or self.var_Name.get()=="" or self.var_Student_id.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
            return

        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Mysql@14",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                self.var_Dep.get(),
                                                                                                self.var_Course.get(),
                                                                                                self.var_Year.get(),
                                                                                                self.var_Semester.get(),
                                                                                                self.var_Student_id.get(),
                                                                                                self.var_Name.get(),
                                                                                                self.var_Division.get(),
                                                                                                self.var_Roll.get(),
                                                                                                self.var_Gender.get(),
                                                                                                self.var_Dob.get(),
                                                                                                self.var_Email.get(),
                                                                                                self.var_Phone.get(),
                                                                                                self.var_Address.get(),
                                                                                                self.var_Teacher.get(),
                                                                                                self.var_PhotoSample.get()


                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Sucess","Student Detail has been added successfully")
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}")

    # ======fetch data=======
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Mysql@14",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # ======get cursor======
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_Dep.set(data[0])
        self.var_Course.set(data[1]),
        self.var_Year.set(data[2]),
        self.var_Semester.set(data[3]),
        self.var_Student_id.set(data[4]),
        self.var_Name.set(data[5]),
        self.var_Division.set(data[6]),
        self.var_Roll.set(data[7]),
        self.var_Gender.set(data[8]),
        self.var_Dob.set(data[9]),
        self.var_Email.set(data[10]),
        self.var_Phone.set(data[11]),
        self.var_Address.set(data[12]),
        self.var_Teacher.set(data[13]),
        self.var_PhotoSample.set(data[14])

    # =======UPDATE FUNCTION=======
    def update_data(self):
        if self.var_Dep.get()=="Select Department" or self.var_Name.get()=="" or self.var_Student_id.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)

        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="Mysql@14",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                                        self.var_Dep.get(),
                                                                                                                                                                                                        self.var_Course.get(),
                                                                                                                                                                                                        self.var_Year.get(),
                                                                                                                                                                                                        self.var_Semester.get(),                                                                                                                                                                                    
                                                                                                                                                                                                        self.var_Name.get(),
                                                                                                                                                                                                        self.var_Division.get(),
                                                                                                                                                                                                        self.var_Roll.get(),
                                                                                                                                                                                                        self.var_Gender.get(),
                                                                                                                                                                                                        self.var_Dob.get(),
                                                                                                                                                                                                        self.var_Email.get(),
                                                                                                                                                                                                        self.var_Phone.get(),
                                                                                                                                                                                                        self.var_Address.get(),
                                                                                                                                                                                                        self.var_Teacher.get(),
                                                                                                                                                                                                        self.var_PhotoSample.get(),
                                                                                                                                                                                                        self.var_Student_id.get()                                                                                                                                                                                                  
                                                                                                                                                                                                            ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student detail successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    # ======delete function=======
    def delete_data(self):
        if self.var_Student_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student data",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="Mysql@14",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_Student_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #=======reset function=====
    def reset_data(self):
        self.var_Dep.set("Select Department")
        self.var_Course.set("Select Course")
        self.var_Year.set("Select Year")
        self.var_Semester.set("Select Semester")
        self.var_Student_id.set("")
        self.var_Name.set("")
        self.var_Division.set("A")
        self.var_Roll.set("")
        self.var_Gender.set("Male")
        self.var_Dob.set("")
        self.var_Email.set("")
        self.var_Phone.set("")
        self.var_Address.set("")
        self.var_Teacher.set("")
        self.var_PhotoSample.set("")

    #====== generate data set or take photo sample========
    def generate_dataset(self):
        if self.var_Dep.get()=="Select Department" or self.var_Name.get()=="" or self.var_Student_id.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Mysql@14",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                                        self.var_Dep.get(),
                                                                                                                                                                                                        self.var_Course.get(),
                                                                                                                                                                                                        self.var_Year.get(),
                                                                                                                                                                                                        self.var_Semester.get(),                                                                                                                                                                                    
                                                                                                                                                                                                        self.var_Name.get(),
                                                                                                                                                                                                        self.var_Division.get(),
                                                                                                                                                                                                        self.var_Roll.get(),
                                                                                                                                                                                                        self.var_Gender.get(),
                                                                                                                                                                                                        self.var_Dob.get(),
                                                                                                                                                                                                        self.var_Email.get(),
                                                                                                                                                                                                        self.var_Phone.get(),
                                                                                                                                                                                                        self.var_Address.get(),
                                                                                                                                                                                                        self.var_Teacher.get(),
                                                                                                                                                                                                        self.var_PhotoSample.get(),
                                                                                                                                                                                                        self.var_Student_id.get()==id+1                                                                                                                                                                                                
                                                                                                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ========= load predefined data on face frontals from opencv =========
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break 
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")
            
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


                


            






        



    


if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()