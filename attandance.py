from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import csv
import os

mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("icon.png")

        #===================variable===================================================
        self.var_atten_id=StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # =======1st Image============================================================================
        img_path_top = r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro\10.png"  # Ensure this path is correct
        try:
            img_top = Image.open(img_path_top)
            img_top = img_top.resize((800, 200), Image.LANCZOS)
            self.photoimg_top = ImageTk.PhotoImage(img_top)
        except Exception as e:
            print(f"Error loading image: {e}")
            messagebox.showerror("Image Error", f"Failed to load image: {e}")
            return

        f_lbl_top = Label(self.root, image=self.photoimg_top)
        f_lbl_top.place(x=0, y=0, width=800, height=200)

        # =======2nd Image============================================================================
        img_path_bott = r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro\12.png"  # Ensure this path is correct
        try:
            img_bott = Image.open(img_path_bott)
            img_bott = img_bott.resize((800, 200), Image.LANCZOS)
            self.photoimg_bott = ImageTk.PhotoImage(img_bott)
        except Exception as e:
            print(f"Error loading image: {e}")
            messagebox.showerror("Image Error", f"Failed to load image: {e}")
            return

        f_lbl_bott = Label(self.root, image=self.photoimg_bott)
        f_lbl_bott.place(x=800, y=0, width=800, height=200)

        # Title of page
        title_lbl = Label(self.root, text="ATTENDANCE MANAGEMENT SYSTEM", font=("Comic Sans MS", 35, "bold"),
                          bg="red", fg="white")
        title_lbl.place(x=0, y=200, width=1530, height=45)

        # Main frame of page
        main_frame = Frame(self.root, bd=2, bg="White")
        main_frame.place(x=0, y=245, width=1530, height=600)

        # Left side label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="White", relief=RIDGE, text="Student Attendance Details",
                                font=("Comic Sans MS", 12, "bold"))
        Left_frame.place(x=0, y=0, width=750, height=580)

        # Insert Image in Left Frame
        img_path_left = r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro\11.jpeg"  # Ensure this path is correct
        try:
            img_left = Image.open(img_path_left)
            img_left = img_left.resize((750, 100), Image.LANCZOS)
            self.photoimg_left = ImageTk.PhotoImage(img_left)
        except Exception as e:
            print(f"Error loading image: {e}")
            return
        f_lbl_left = Label(Left_frame, image=self.photoimg_left)
        f_lbl_left.place(x=0, y=0, width=740, height=100)

        # Left Inside frame of page
        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=100, width=740, height=460)

        # Label and Entry

        # Attendance ID
        attendance_id_label = Label(left_inside_frame, text="Attendance ID", font=("Comic Sans MS", 11, "bold"), bg="white")
        attendance_id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        self.attendance_id_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_id, font=("Comic Sans MS", 11, "bold"))
        self.attendance_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Roll No
        roll_no_label = Label(left_inside_frame, text="Roll No", font=("Comic Sans MS", 11, "bold"), bg="white")
        roll_no_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        self.roll_no_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_roll, font=("Comic Sans MS", 11, "bold"))
        self.roll_no_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Name
        name_label = Label(left_inside_frame, text="Name", font=("Comic Sans MS", 11, "bold"), bg="white")
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        self.name_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_name, font=("Comic Sans MS", 11, "bold"))
        self.name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Department
        department_label = Label(left_inside_frame, text="Department", font=("Comic Sans MS", 11, "bold"), bg="white")
        department_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        self.department_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_dep, font=("Comic Sans MS", 11, "bold"))
        self.department_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Time
        time_label = Label(left_inside_frame, text="Time", font=("Comic Sans MS", 11, "bold"), bg="white")
        time_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        self.time_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_time, font=("Comic Sans MS", 11, "bold"))
        self.time_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Date
        date_label = Label(left_inside_frame, text="Date", font=("Comic Sans MS", 11, "bold"), bg="white")
        date_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        self.date_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_date, font=("Comic Sans MS", 11, "bold"))
        self.date_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Attendance Status
        attendance_label = Label(left_inside_frame, text="Attendance Status", font=("Comic Sans MS", 11, "bold"), bg="white")
        attendance_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        self.attendance_status = ttk.Combobox(left_inside_frame, width=20, textvariable=self.var_atten_attendance, font=("Comic Sans MS", 11, "bold"), state="readonly")
        self.attendance_status["values"] = ("Status", "Present", "Absent")
        self.attendance_status.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        self.attendance_status.current(0)

        # Buttons frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=330, width=740, height=37)

        # Import Button
        import_btn = Button(btn_frame, text="Import CSV", command=self.importCsv, font=("Comic Sans MS", 11, "bold"), bg="blue", fg="white")
        import_btn.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        # Export Button
        export_btn = Button(btn_frame, text="Export CSV", command=self.exportCsv, font=("Comic Sans MS", 11, "bold"), bg="blue", fg="white")
        export_btn.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Update Button
        update_btn = Button(btn_frame, text="Update", command=self.updateData, font=("Comic Sans MS", 11, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        # Reset Button
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, font=("Comic Sans MS", 11, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Right side label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="White", relief=RIDGE, text="Attendance Details",
                                 font=("Comic Sans MS", 12, "bold"))
        Right_frame.place(x=760, y=0, width=750, height=580)

        # Insert Image in Right Frame
        img_path_right = r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro\13.jpeg"
        try:
            img_right = Image.open(img_path_right)
            img_right = img_right.resize((740, 100), Image.LANCZOS)
            self.photoimg_right = ImageTk.PhotoImage(img_right)
        except Exception as e:
            print(f"Error loading image: {e}")
            return
        f_lbl_right = Label(Right_frame, image=self.photoimg_right)
        f_lbl_right.place(x=0, y=0, width=740, height=100)

        # Right inside frame of page
        right_inside_frame = Frame(Right_frame, bd=2, bg="white")
        right_inside_frame.place(x=2, y=100, width=740, height=400)

        # ============Scroll Bar====================================
        scroll_x = ttk.Scrollbar(right_inside_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(right_inside_frame, orient=VERTICAL)

        self.AttandanceReportTable = ttk.Treeview(right_inside_frame,
                                                  column=("id", "roll", "name", "department", "time", "date", "attendance"),
                                                  xscrollcommand=scroll_x.set,
                                                  yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttandanceReportTable.xview)
        scroll_y.config(command=self.AttandanceReportTable.yview)

        self.AttandanceReportTable.heading("id", text="Attendance ID")
        self.AttandanceReportTable.heading("roll", text="Roll No")
        self.AttandanceReportTable.heading("name", text="Name")
        self.AttandanceReportTable.heading("department", text="Department")
        self.AttandanceReportTable.heading("time", text="Time")
        self.AttandanceReportTable.heading("date", text="Date")
        self.AttandanceReportTable.heading("attendance", text="Attendance")

        self.AttandanceReportTable["show"] = "headings"

        self.AttandanceReportTable.column("id", width=100)
        self.AttandanceReportTable.column("roll", width=100)
        self.AttandanceReportTable.column("name", width=100)
        self.AttandanceReportTable.column("department", width=100)
        self.AttandanceReportTable.column("time", width=100)
        self.AttandanceReportTable.column("date", width=100)
        self.AttandanceReportTable.column("attendance", width=100)

        self.AttandanceReportTable.pack(fill=BOTH, expand=1)
        self.AttandanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    # ===============fetch data=================================================
    def fetchData(self, rows):
        self.AttandanceReportTable.delete(*self.AttandanceReportTable.get_children())
        for i in rows:
            self.AttandanceReportTable.insert("", END, values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="open CSV",
                                         filetypes=(("CSV File", "*.csv"), ("All files", "*.*")),
                                         parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data Found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="open CSV",
                                               filetypes=(("CSV File", "*.csv"), ("All files", "*.*")),
                                               parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", f"Your data exported to {os.path.basename(fln)} successfully")
        except Exception as e:
            print(f"Error Export data: {e}")

    def updateData(self):
        pass

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")

    def get_cursor(self,event=""):
        cursor_row=self.AttandanceReportTable.focus()
        content=self.AttandanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
