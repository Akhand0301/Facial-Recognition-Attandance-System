from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("icon.png")

        # Variable initialization
        self.ver_department = StringVar()
        self.ver_course = StringVar()
        self.ver_year = StringVar()
        self.ver_semester = StringVar()
        self.ver_id = StringVar()
        self.ver_name = StringVar()
        self.ver_div = StringVar()
        self.ver_roll = StringVar()
        self.ver_gender = StringVar()
        self.ver_dob = StringVar()
        self.ver_email = StringVar()
        self.ver_phone = StringVar()
        self.ver_address = StringVar()
        self.ver_teacher = StringVar()
        self.ver_radio1 = StringVar()




        # First Image
        img_path1 = r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro\4.png"  # Ensure this path is correct
        try:
            img1 = Image.open(img_path1)
            img1 = img1.resize((500, 130), Image.LANCZOS)
            self.photoimg1 = ImageTk.PhotoImage(img1)
        except Exception as e:
            print(f"Error loading image: {e}")
            return

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=500, height=130)

        # Second Image
        img_path2 = r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro\5.png"  # Ensure this path is correct
        try:
            img2 = Image.open(img_path2)
            img2 = img2.resize((500, 130), Image.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)
        except Exception as e:
            print(f"Error loading image: {e}")
            return

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=500, y=0, width=500, height=130)

        # Third Image
        img_path3 = r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro\6.png"  # Ensure this path is correct
        try:
            img3 = Image.open(img_path3)
            img3 = img3.resize((500, 130), Image.LANCZOS)
            self.photoimg3 = ImageTk.PhotoImage(img3)
        except Exception as e:
            print(f"Error loading image: {e}")
            return

        f_lbl3 = Label(self.root, image=self.photoimg3)
        f_lbl3.place(x=1000, y=0, width=500, height=130)

        # BG Image
        img_path_bg = r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro\bg.jpg"  # Ensure this path is correct
        try:
            img_bg = Image.open(img_path_bg)
            img_bg = img_bg.resize((1530, 710), Image.LANCZOS)
            self.photoimg_bg = ImageTk.PhotoImage(img_bg)
        except Exception as e:
            print(f"Error loading image: {e}")
            return

        bg_img = Label(self.root, image=self.photoimg_bg)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"),
                          bg="red", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2, bg="White")
        main_frame.place(x=5, y=55, width=1470, height=600)

        # Left side label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="White", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=690, height=580)

        # Insert Image in Left Frame
        img_path_left = r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro\7.jpg"  # Ensure this path is correct
        try:
            img_left = Image.open(img_path_left)
            img_left = img_left.resize((680, 100), Image.LANCZOS)
            self.photoimg_left = ImageTk.PhotoImage(img_left)
        except Exception as e:
            print(f"Error loading image: {e}")
            return
        f_lbl_left = Label(Left_frame, image=self.photoimg_left)
        f_lbl_left.place(x=5, y=0, width=680, height=100)

        # Current course
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="White", relief=RIDGE, text="Current Course Information",
                                          font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=110, width=680, height=130)

        # Department
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"))
        dep_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.ver_department, font=("times new roman", 12, "bold"), width=17, state="readonly")
        dep_combo["values"] = ("Select Department", "Computer Science", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"))
        course_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.ver_course, font=("times new roman", 12, "bold"), width=17, state="readonly")
        course_combo["values"] = ("Select Course", "B.Tech", "M.Tech", "MBA", "BCA")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"))
        year_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.ver_year, font=("times new roman", 12, "bold"), width=17, state="readonly")
        year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"))
        semester_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.ver_semester, font=("times new roman", 12, "bold"), width=17, state="readonly")
        semester_combo["values"] = ("Select Semester", "Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5", "Semester 6", "Semester 7", "Semester 8")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class Student Information
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="White", relief=RIDGE, text="Class Student Information",
                                         font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=240, width=680, height=270)

        # Student ID
        studentid_label = Label(class_student_frame,  text="StudentID", font=("times new roman", 12, "bold"), bg="white")
        studentid_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        studentid_entry = ttk.Entry(class_student_frame, textvariable=self.ver_id, width=20, font=("times new roman", 12, "bold"))
        studentid_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # Student name
        studentname_label = Label(class_student_frame, text="Student Name", font=("times new roman", 12, "bold"), bg="white")
        studentname_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        studentname_entry = ttk.Entry(class_student_frame, textvariable=self.ver_name, width=20, font=("times new roman", 12, "bold"))
        studentname_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # Class Division
        studentdiv_label = Label(class_student_frame, text="Class Division", font=("times new roman", 12, "bold"), bg="white")
        studentdiv_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        studentdiv_entry = ttk.Entry(class_student_frame, textvariable=self.ver_div, width=20, font=("times new roman", 12, "bold"))
        studentdiv_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Create a combo box for class division
        studentdiv_combo = ttk.Combobox(class_student_frame, textvariable=self.ver_div, width=20,
                                        font=("times new roman", 12, "bold"))
        studentdiv_combo['values'] = ('A', 'B', 'C')  # Set the available options
        studentdiv_combo.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        studentdiv_combo.current(0)  # Set the default selection to the first option


        # Roll No
        rollno_label = Label(class_student_frame, text="Roll No", font=("times new roman", 12, "bold"), bg="white")
        rollno_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        rollno_entry = ttk.Entry(class_student_frame, textvariable=self.ver_roll, width=20, font=("times new roman", 12, "bold"))
        rollno_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # Gender
        gender_label = Label(class_student_frame, text="Gender", font=("times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.ver_gender, font=("times new roman", 12, "bold"), width=18, state="readonly")
        gender_combo["values"] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        # DOB
        dob_label = Label(class_student_frame, text="DOB", font=("times new roman", 12, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame, textvariable=self.ver_dob, width=20, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        # Email
        email_label = Label(class_student_frame, text="Email", font=("times new roman", 12, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.ver_email, width=20, font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        # Phone no
        phone_label = Label(class_student_frame, text="Phone", font=("times new roman", 12, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=5, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_student_frame, textvariable=self.ver_phone, width=20, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=5, pady=5, sticky=W)

        # Address
        address_label = Label(class_student_frame, text="Address", font=("times new roman", 12, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=5, pady=5, sticky=W)

        address_entry = ttk.Entry(class_student_frame, textvariable=self.ver_address, width=20, font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        # Teacher name
        teacher_label = Label(class_student_frame, text="Teacher Name", font=("times new roman", 12, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=5, pady=5, sticky=W)

        teacher_entry = ttk.Entry(class_student_frame, textvariable=self.ver_teacher, width=20, font=("times new roman", 12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=5, pady=5, sticky=W)

        # Radio buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take Photo Sample", value="yes")
        radiobtn1.grid(row=5, column=0, padx=5, pady=5, sticky=W)


        radiobtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No Photo Sample", value="no")
        radiobtn2.grid(row=5, column=1, padx=5, pady=5, sticky=W)

        # Buttons frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=205, width=680, height=37)

        # Save Button
        save_btn = Button(btn_frame, text="Save", command=self.add_data, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        # Update Button
        update_btn = Button(btn_frame,  text="Update", command=self.update_data, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # Delete Button
        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        # Reset Button
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # take photo Button
        takephoto_btn = Button(btn_frame, text="Take Photo Sample", command=self.generate_dataset, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        takephoto_btn.grid(row=0, column=4, padx=5, pady=5, sticky=W)

        # Update photo Button
        updatephoto_btn = Button(btn_frame, text="Update Photo Sample", font=("times new roman", 12, "bold"), bg="blue", fg="white")
        updatephoto_btn.grid(row=0, column=5, padx=5, pady=5, sticky=W)

        # Right side label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="White", relief=RIDGE, text="Student Details",
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=710, y=10, width=730, height=580)

        # Insert Image in Right Frame
        img_path_right = r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro\8.jpeg"
        try:
            img_right = Image.open(img_path_right)
            img_right = img_right.resize((680, 100), Image.LANCZOS)
            self.photoimg_right = ImageTk.PhotoImage(img_right)
        except Exception as e:
            print(f"Error loading image: {e}")
            return
        f_lbl_right = Label(Right_frame, image=self.photoimg_right)
        f_lbl_right.place(x=5, y=0, width=680, height=100)

        # Search system
        search_frame = LabelFrame(Right_frame, bd=2, bg="White", relief=RIDGE, text="Search System",
                                  font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=100, width=715, height=70)

        search_label = Label(search_frame, text="Search By:", font=("times new roman", 12, "bold"), bg="white")
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), width=15, state="readonly")
        search_combo["values"] = ("Select", "StudentID", "Phone", "Roll No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        search_entry = ttk.Entry(search_frame, width=15, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", font=("times new roman", 12, "bold"), bg="blue", fg="white",
                            width=10)
        search_btn.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        showall_btn = Button(search_frame, text="Show All", font=("times new roman", 12, "bold"), bg="blue", fg="white",
                             width=10)
        showall_btn.grid(row=0, column=4, padx=5, pady=5, sticky=W)

        # Table frame
        table_frame = Frame(Right_frame, bd=2, bg="White", relief=RIDGE)
        table_frame.place(x=5, y=180, width=715, height=330)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=(
            "department","course", "year", "semester", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("department", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("semester", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")

        self.student_table["show"] = "headings"

        self.student_table.column("department", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("semester", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    import mysql.connector
    from mysql.connector import Error
    import cv2
    from tkinter import messagebox, END

    def add_data(self):
        if self.ver_department.get() == "Select Department" or not self.ver_name.get() or not self.ver_id.get():
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        try:
            with mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="12345@123",
                    database="face_recognizer"
            ) as conn:
                with conn.cursor() as my_cursor:
                    my_cursor.execute(
                        """INSERT INTO student (department, course, year, semester, StudentId, Name, Division, Roll, Gender, 
                        Dob, Email, phone, Address, Teacher, PhotoSample) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                        %s, %s, %s, %s, %s)""",
                        (
                            self.ver_department.get(),
                            self.ver_course.get(),
                            self.ver_year.get(),
                            self.ver_semester.get(),
                            self.ver_id.get(),
                            self.ver_name.get(),
                            self.ver_div.get(),
                            self.ver_roll.get(),
                            self.ver_gender.get(),
                            self.ver_dob.get(),
                            self.ver_email.get(),
                            self.ver_phone.get(),
                            self.ver_address.get(),
                            self.ver_teacher.get(),
                            self.ver_radio1.get()
                        )
                    )
                    conn.commit()
                    self.fetch_data()
                    messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
        except Error as e:
            messagebox.showerror("Database Error", f"Due to: {str(e)}", parent=self.root)

    def fetch_data(self):
        try:
            with mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="12345@123",
                    database="face_recognizer"
            ) as conn:
                with conn.cursor() as my_cursor:
                    my_cursor.execute("SELECT * FROM student")
                    data = my_cursor.fetchall()

                    self.student_table.delete(*self.student_table.get_children())  # Clear existing data

                    for record in data:
                        self.student_table.insert("", END, values=record)
        except Error as e:
            messagebox.showerror("Database Error", f"Error fetching data: {str(e)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        if data:
            self.ver_department.set(data[0])
            self.ver_course.set(data[1])
            self.ver_year.set(data[2])
            self.ver_semester.set(data[3])
            self.ver_id.set(data[4])
            self.ver_name.set(data[5])
            self.ver_div.set(data[6])
            self.ver_roll.set(data[7])
            self.ver_gender.set(data[8])
            self.ver_dob.set(data[9])
            self.ver_email.set(data[10])
            self.ver_phone.set(data[11])
            self.ver_address.set(data[12])
            self.ver_teacher.set(data[13])
            self.ver_radio1.set(data[14])

    def update_data(self):
        if self.ver_department.get() == "Select Department" or not self.ver_name.get() or not self.ver_id.get():
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        try:
            if messagebox.askyesno("Update", "Do you want to update this student's details?", parent=self.root):
                with mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="12345@123",
                        database="face_recognizer"
                ) as conn:
                    with conn.cursor() as my_cursor:
                        my_cursor.execute(
                            """UPDATE student SET department=%s, course=%s, year=%s, semester=%s, Name=%s, Division=%s, 
                            Roll=%s, Gender=%s, Dob=%s, Email=%s, phone=%s, Address=%s, Teacher=%s, PhotoSample=%s 
                            WHERE StudentId=%s""",
                            (
                                self.ver_department.get(), self.ver_course.get(), self.ver_year.get(),
                                self.ver_semester.get(), self.ver_name.get(), self.ver_div.get(), self.ver_roll.get(),
                                self.ver_gender.get(), self.ver_dob.get(), self.ver_email.get(), self.ver_phone.get(),
                                self.ver_address.get(), self.ver_teacher.get(), self.ver_radio1.get(), self.ver_id.get()
                            )
                        )
                        conn.commit()
                        self.fetch_data()
                        messagebox.showinfo("Success", "Student details have been updated successfully",
                                            parent=self.root)
        except Error as e:
            messagebox.showerror("Database Error", f"Error occurred while updating data: {str(e)}", parent=self.root)

    def delete_data(self):
        if not self.ver_id.get():
            messagebox.showerror("Error", "Student ID must be provided", parent=self.root)
            return

        try:
            if messagebox.askyesno("Student Delete Page", "Do you want to delete this student?", parent=self.root):
                with mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="12345@123",
                        database="face_recognizer"
                ) as conn:
                    with conn.cursor() as my_cursor:
                        my_cursor.execute("DELETE FROM student WHERE StudentId=%s", (self.ver_id.get(),))
                        conn.commit()
                        self.fetch_data()
                        messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
        except Error as e:
            messagebox.showerror("Database Error", f"Error during deletion: {str(e)}", parent=self.root)

    def reset_data(self):
        self.ver_department.set("Select Department")
        self.ver_course.set("Select Course")
        self.ver_year.set("Select Year")
        self.ver_semester.set("Select Semester")
        self.ver_id.set("")
        self.ver_name.set("")
        self.ver_div.set("Select Division")
        self.ver_roll.set("")
        self.ver_gender.set("Male")
        self.ver_dob.set("")
        self.ver_email.set("")
        self.ver_phone.set("")
        self.ver_address.set("")
        self.ver_teacher.set("")
        self.ver_radio1.set("")

    def generate_dataset(self):
        if self.ver_department.get() == "Select Department" or not self.ver_name.get() or not self.ver_id.get():
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="12345@123",
                database="face_recognizer"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT MAX(StudentId) FROM student")
            result = my_cursor.fetchone()
            student_id = result[0] if result and result[0] is not None else 1

            my_cursor.execute(
                """UPDATE student SET department=%s, course=%s, year=%s, semester=%s, Name=%s, Division=%s, Roll=%s, 
                Gender=%s, Dob=%s, Email=%s, phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE StudentId=%s""",
                (
                    self.ver_department.get(), self.ver_course.get(), self.ver_year.get(), self.ver_semester.get(),
                    self.ver_name.get(), self.ver_div.get(), self.ver_roll.get(), self.ver_gender.get(),
                    self.ver_dob.get(),
                    self.ver_email.get(), self.ver_phone.get(), self.ver_address.get(), self.ver_teacher.get(),
                    self.ver_radio1.get(), student_id
                )
            )
            conn.commit()

            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    return img[y:y + h, x:x + w]
                return None

            cap = cv2.VideoCapture(0)
            img_id = 0
            while True:
                ret, my_frame = cap.read()
                if not ret:
                    messagebox.showerror("Error", "Failed to capture video", parent=self.root)
                    break

                face = face_cropped(my_frame)
                if face is not None:
                    img_id += 1
                    face_resized = cv2.resize(face, (450, 450))
                    face_gray = cv2.cvtColor(face_resized, cv2.COLOR_BGR2GRAY)
                    file_name_path = f"data/user.{student_id}.{img_id}.jpg"
                    cv2.imwrite(file_name_path, face_gray)
                    cv2.putText(face_resized, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                    cv2.imshow("Cropped Face", face_resized)

                if cv2.waitKey(1) == 13 or img_id == 100:
                    break

            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Generating datasets completed!")

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {str(err)}", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"An error occurred: {str(ex)}", parent=self.root)
        finally:
            if 'my_cursor' in locals() and my_cursor.is_connected():
                my_cursor.close()
            if 'conn' in locals() and conn.is_connected():
                conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()

