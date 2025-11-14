from tkinter import*
from tkinter import ttk,filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import cv2
import os
import csv


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recoginiton System")

        # ===========variables=========
        self.var_Id=StringVar()
        self.var_Roll=StringVar()
        self.var_Name=StringVar()
        self.var_Department=StringVar()
        self.var_Time=StringVar()
        self.var_Date=StringVar()
        self.var_Attendance=StringVar()

        title_lbl=Label(self.root,text="ATTENDANCE MANAGEMENT SYSTEM",font=("Sans serif fonts",40,"bold"),bg="white",fg="midnight blue")
        title_lbl.place(x=0,y=0,width=1540,height=60)

        face_bg=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\backgroundimg.jpg")
        face_bg=face_bg.resize((1540,800))
        self.photoface_bg=ImageTk.PhotoImage(face_bg)
        bg_img=Label(self.root,image=self.photoface_bg)
        bg_img.place(x=0,y=60,width=1540,height=800)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=10,width=1512,height=710)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=740,height=685)

        img_left=Image.open(r"C:\Users\acer\Desktop\Face Recoginition System\images\left.jpg")
        img_left=img_left.resize((720,190))
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=10,y=0,width=720,height=190)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=3,y=195,width=730,height=460)

        #=======labels and entry===========
        # attendance id
        attendanceId_label=Label(left_inside_frame,text="Attendance Id :",font=("comicsansns",11,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        attendanceId_entry=ttk.Entry(left_inside_frame,width=25,textvariable=self.var_Id,font=("comicsansns",11))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        # roll
        roll_label=Label(left_inside_frame,text="Roll No :",font=("comicsansns",11,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        roll_entry=ttk.Entry(left_inside_frame,width=25,textvariable=self.var_Roll,font=("comicsansns",11))
        roll_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        # name
        name_label=Label(left_inside_frame,text="Name :",font=("comicsansns",11,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        name_entry=ttk.Entry(left_inside_frame,width=25,textvariable=self.var_Name,font=("comicsansns",11))
        name_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        # department
        department_label=Label(left_inside_frame,text="Department :",font=("comicsansns",11,"bold"),bg="white")
        department_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        department_entry=ttk.Entry(left_inside_frame,width=25,textvariable=self.var_Department,font=("comicsansns",11))
        department_entry.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        # time
        time_label=Label(left_inside_frame,text="Time :",font=("comicsansns",11,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        time_entry=ttk.Entry(left_inside_frame,width=25,textvariable=self.var_Time,font=("comicsansns",11))
        time_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        # date
        date_label=Label(left_inside_frame,text="Date :",font=("comicsansns",11,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)

        date_entry=ttk.Entry(left_inside_frame,width=25,textvariable=self.var_Date,font=("comicsansns",11))
        date_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        # attendance
        attendance_label=Label(left_inside_frame,text="Attendance Status",font=("comicsansns",11,"bold"),bg="white")
        attendance_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        division_combo=ttk.Combobox(left_inside_frame,font=("comicsansns",11),width=23,textvariable=self.var_Attendance,state="read only")
        division_combo['values']=("Status","Present","Absent")
        division_combo.current(0)
        division_combo.grid(row=3,column=1,padx=10,pady=10,sticky=W)

        #button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=725,height=42)

        import_btn=Button(btn_frame,text="Import CSV",command=self.import_csv,width=17,font=("times new roman",12,"bold"),bg="grey",fg="white",cursor="hand2")
        import_btn.grid(row=0,column=0,padx=7,pady=3)

        export_btn=Button(btn_frame,text="Export CSV",command=self.export_csv,width=17,font=("times new roman",12,"bold"),bg="grey",fg="white",cursor="hand2")
        export_btn.grid(row=0,column=1,padx=10,pady=3)

        update_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",12,"bold"),bg="grey",fg="white",cursor="hand2")
        update_btn.grid(row=0,column=2,padx=10,pady=3)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",12,"bold"),bg="grey",fg="white",cursor="hand2")
        reset_btn.grid(row=0,column=3,padx=10,pady=3)


        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=760,y=10,width=740,height=685)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=727,height=650)

        #=========scroll bar and table==============
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("Id","Roll","Name","Department","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("Id",text="Attendance Id")
        self.AttendanceReportTable.heading("Roll",text="Roll No")
        self.AttendanceReportTable.heading("Name",text="Name")
        self.AttendanceReportTable.heading("Department",text="Department")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("Date",text="Date")
        self.AttendanceReportTable.heading("Attendance",text="Attendance")
        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("Id",width=100)
        self.AttendanceReportTable.column("Roll",width=100)
        self.AttendanceReportTable.column("Name",width=100)
        self.AttendanceReportTable.column("Department",width=100)
        self.AttendanceReportTable.column("Time",width=100)
        self.AttendanceReportTable.column("Date",width=100)
        self.AttendanceReportTable.column("Attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

     #===============fetch data==============
    def fetch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    # import csv
    def import_csv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File",".csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csv_read=csv.reader(myfile,delimiter=",")
            for i in csv_read:
                mydata.append(i)
            self.fetch_data(mydata)

    # export csv
    def export_csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File",".csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_Id.set(rows[0])
        self.var_Roll.set(rows[1])
        self.var_Name.set(rows[2])
        self.var_Department.set(rows[3])
        self.var_Time.set(rows[4])
        self.var_Date.set(rows[5])
        self.var_Attendance.set(rows[6])

    # reset data
    def reset_data(self):
        self.var_Id.set("")
        self.var_Roll.set("")
        self.var_Name.set("")
        self.var_Department.set("")
        self.var_Time.set("")
        self.var_Date.set("")
        self.var_Attendance.set("Status")

if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()