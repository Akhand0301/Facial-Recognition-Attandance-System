from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import random
import time
import datetime
from main import Face_Recognition_System

def main():
    win = Tk()
    app = Login_window(win)
    win.mainloop()

class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1600x900+0+0")
        self.root.wm_iconbitmap("icon.png")

        # Load and resize the background image
        self.bg = Image.open(r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro/1.jpg")
        self.bg = self.bg.resize((1600, 900), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.bg)

        # Create a label to display the background image
        self.lbl_bg = Label(self.root, image=self.bg)
        self.lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        title_lbl1 = Label(self.root, text="FACIAL RECOGNITION ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"),
                          bg="white", fg="red")
        title_lbl1.place(x=0, y=0, width=1530, height=45)

        # Frame for login elements
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        # Resizing and displaying user image
        img1 = Image.open(r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro\L2.png")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(self.root, image=self.photoimage1, bg='black', borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), bg="black", fg="white")
        get_str.place(x=95, y=100)

        # Label
        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), bg="black", fg="white")
        username.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="black", fg="white")
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show='*')
        self.txtpass.place(x=40, y=250, width=270)

        # Resizing and displaying icon images
        img2 = Image.open(r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro\L3.webp")
        img2 = img2.resize((25, 25), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(self.root, image=self.photoimage2, bg='black', borderwidth=0)
        lblimg2.place(x=650, y=323, width=25, height=25)

        img3 = Image.open(r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro\P.png")
        img3 = img3.resize((25, 25), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(self.root, image=self.photoimage3, bg='black', borderwidth=0)
        lblimg3.place(x=650, y=394, width=25, height=25)

        # Login Button
        loginbtn = Button(frame, text="Login", command=self.login, font=("times new roman", 12, "bold"),
                          bd=3, relief=RIDGE, bg="red", fg="white", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # Register Button
        regbtn = Button(frame, text="New User Register", command=self.register_window, font=("times new roman", 10, "bold"), borderwidth=0,
                        bg="black", fg="white", activeforeground="white", activebackground="black")
        regbtn.place(x=10, y=350, width=160)

        # Forget password Button
        forgetbtn = Button(frame, text="Forget Password",command=self.forgot_password_window, font=("times new roman", 10, "bold"), borderwidth=0,
                           bg="black", fg="white", activeforeground="white", activebackground="black")
        forgetbtn.place(x=10, y=370, width=160)

    #================Function=======================
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    # ================Login Function=======================
    def login(self):
        username = self.txtuser.get()
        password = self.txtpass.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required")
        elif username == "kapu" and password == "ashu":
            messagebox.showinfo("Success", "Welcome to face recognition attendance system application")
            self.new_window = Toplevel(self.root)
            self.app = Face_Recognition_System(self.new_window)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="12345@123", database="mydata")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from users where email=%s and password=%s", (username, password))
                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid username or password")
                else:
                    messagebox.showinfo("Success", "Login Successful")
                    # Ensure open_main is properly checked
                    open_main = True  # Assuming open_main is defined elsewhere in your code
                    if open_main:
                        self.new_window = Toplevel(self.root)
                        self.app = Face_Recognition_System(self.new_window)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}")
            finally:
                conn.close()

    # ================Forget Function=======================
    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter email address to reset password")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="12345@123", database="mydata")
                my_cursor = conn.cursor()
                query = "select * from users where email=%s"
                value = (self.txtuser.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                if row is None:
                    messagebox.showerror("Error", "Please enter a valid username")
                else:
                    self.root2 = Toplevel(self.root)
                    self.root2.title("Forget Password")
                    self.root2.geometry("340x450+610+170")

                    l = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), fg="red", bg="white")
                    l.place(x=0, y=10, relwidth=1)

                    # Security Question
                    sec_question_label = Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"),
                                               fg='black', bg='white')
                    sec_question_label.place(x=50, y=80)
                    self.sec_question_var = StringVar()
                    security_combobox = ttk.Combobox(self.root2, textvariable=self.sec_question_var,
                                                     font=("times new roman", 13, "bold"), state="readonly", width=30)
                    security_combobox['values'] = ("What is your pet's name?", "What is your mother's maiden name?", "What city were you born in?")
                    security_combobox.place(x=50, y=110, width=250)

                    # Security Answer
                    sec_answer_label = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"),
                                             fg='black', bg='white')
                    sec_answer_label.place(x=50, y=150)
                    self.sec_answer_var = StringVar()
                    self.sec_answer_entry = ttk.Entry(self.root2, font=("times new roman", 15, "bold"),
                                                      textvariable=self.sec_answer_var)
                    self.sec_answer_entry.place(x=50, y=180, width=250)

                    # New Password
                    new_password_label = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"),
                                               fg='black', bg='white')
                    new_password_label.place(x=50, y=220)
                    self.new_password_var = StringVar()
                    self.new_password_entry = ttk.Entry(self.root2, font=("times new roman", 15, "bold"), show='*',
                                                        textvariable=self.new_password_var)
                    self.new_password_entry.place(x=50, y=250, width=250)

                    reset_btn = Button(self.root2, text="Reset Password", command=self.reset_password, font=("times new roman", 15, "bold"),
                                       bg="green", fg="white")
                    reset_btn.place(x=90, y=300)

                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}")

    # ================Reset Function=======================
    def reset_password(self):
        if self.sec_question_var.get() == "" or self.sec_answer_var.get() == "" or self.new_password_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="12345@123", database="mydata")
                my_cursor = conn.cursor()
                query = "select * from users where email=%s and securityQ=%s and securityA=%s"
                value = (self.txtuser.get(), self.sec_question_var.get(), self.sec_answer_var.get())
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Please select correct security question / enter answer")
                else:
                    query = "update users set password=%s where email=%s"
                    value = (self.new_password_var.get(), self.txtuser.get())
                    my_cursor.execute(query, value)

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Info", "Your password has been reset, please login with new password")
                    self.root2.destroy()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}")


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # Initialize MySQL connection
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345@123",
            database="mydata"
        )
        self.cursor = self.conn.cursor()

        # StringVars for Entry fields
        self.fname_var = StringVar()
        self.lname_var = StringVar()
        self.email_var = StringVar()
        self.pass_var = StringVar()
        self.cpass_var = StringVar()
        self.contact_var = StringVar()
        self.sec_question_var = StringVar()
        self.sec_answer_var = StringVar()

        # Load and resize the background image
        self.bg = Image.open(r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro\3.jpg")
        self.bg = self.bg.resize((1600, 900), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.bg)

        # Create a label to display the background image
        self.lbl_bg = Label(self.root, image=self.bg)
        self.lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Load and resize the left image
        self.left_img = Image.open(r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro/2.jpg")
        self.left_img = self.left_img.resize((470, 550), Image.LANCZOS)
        self.left_img = ImageTk.PhotoImage(self.left_img)

        # Create a label to display the left image
        self.left_lbl = Label(self.root, image=self.left_img)
        self.left_lbl.place(x=50, y=100, width=470, height=550)

        # Main frame
        frame = Frame(self.root, bg='white')
        frame.place(x=520, y=100, width=800, height=550)

        # Register Label
        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 25, "bold"), fg='green', bg='white')
        register_lbl.place(x=20, y=20)

        # First Name
        fname_label = Label(frame, text="First Name", font=("times new roman", 15, "bold"), fg='black', bg='white')
        fname_label.place(x=50, y=100)
        self.fname_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"), textvariable=self.fname_var)
        self.fname_entry.place(x=50, y=130, width=250)

        # Last Name
        lname_label = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), fg='black', bg='white')
        lname_label.place(x=370, y=100)
        self.lname_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"), textvariable=self.lname_var)
        self.lname_entry.place(x=370, y=130, width=250)

        # Contact Number
        contact_label = Label(frame, text="Contact Number", font=("times new roman", 15, "bold"), fg='black', bg='white')
        contact_label.place(x=50, y=170)
        self.contact_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"), textvariable=self.contact_var)
        self.contact_entry.place(x=50, y=200, width=250)

        # Email
        email_label = Label(frame, text="Email", font=("times new roman", 15, "bold"), fg='black', bg='white')
        email_label.place(x=370, y=170)
        self.email_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"), textvariable=self.email_var)
        self.email_entry.place(x=370, y=200, width=250)

        # Password
        pass_label = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg='black', bg='white')
        pass_label.place(x=50, y=240)
        self.pass_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"), show='*', textvariable=self.pass_var)
        self.pass_entry.place(x=50, y=270, width=250)

        # Confirm Password
        cpass_label = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), fg='black', bg='white')
        cpass_label.place(x=370, y=240)
        self.cpass_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"), show='*', textvariable=self.cpass_var)
        self.cpass_entry.place(x=370, y=270, width=250)

        # Security Question
        sec_question_label = Label(frame, text="Security Question", font=("times new roman", 15, "bold"), fg='black', bg='white')
        sec_question_label.place(x=50, y=310)
        security_combobox = ttk.Combobox(frame, textvariable=self.sec_question_var, font=("times new roman", 13, "bold"), state="readonly", width=40)
        security_combobox['values'] = ("What is your pet's name?", "What is your mother's maiden name?", "What city were you born in?")
        security_combobox.place(x=50, y=340, width=570)

        # Security Answer
        sec_answer_label = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), fg='black', bg='white')
        sec_answer_label.place(x=50, y=380)
        self.sec_answer_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"), textvariable=self.sec_answer_var)
        self.sec_answer_entry.place(x=50, y=410, width=570)

        # Checkbox
        self.var_chk = IntVar()
        chk = Checkbutton(frame, text="I Agree to the Terms & Conditions", variable=self.var_chk, onvalue=1, offvalue=0, font=("times new roman", 13, "bold"), bg="white")
        chk.place(x=50, y=450)

        # Register Button
        reg_btn = Button(frame, text="Register", command=self.register_user, font=("times new roman", 15, "bold"), bg="green", fg="white", bd=0, cursor="hand2")
        reg_btn.place(x=250, y=500, width=150)

        # Login Button
        login_btn = Button(frame, text="Sign In", command=self.go_to_login, font=("times new roman", 15, "bold"), bg="blue", fg="white", bd=0, cursor="hand2")
        login_btn.place(x=410, y=500, width=150)

    def register_user(self):
        fname = self.fname_var.get()
        lname = self.lname_var.get()
        email = self.email_var.get()
        password = self.pass_var.get()
        cpassword = self.cpass_var.get()
        contact = self.contact_var.get()
        security_question = self.sec_question_var.get()
        security_answer = self.sec_answer_var.get()
        agree = self.var_chk.get()

        if fname == "" or lname == "" or email == "" or password == "" or cpassword == "" or contact == "" or security_question == "" or security_answer == "":
            messagebox.showerror("Error", "All fields are required")
        elif password != cpassword:
            messagebox.showerror("Error", "Passwords do not match")
        elif agree == 0:
            messagebox.showerror("Error", "Please agree to the Terms & Conditions")
        else:
            # Check if email already exists
            self.cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            if self.cursor.fetchone():
                messagebox.showerror("Error", "User already exists with this email")
            else:
                # Insert new user into the database
                try:
                    self.cursor.execute(
                        "INSERT INTO users (fname, lname, email, password, contact, securityQ, securityA) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (fname, lname, email, password, contact, security_question, security_answer)
                    )
                    self.conn.commit()
                    messagebox.showinfo("Success", "Registration Successful")
                    self.clear_entries()
                except Exception as e:
                    messagebox.showerror("Error", f"Error due to: {str(e)}")

    def clear_entries(self):
        self.fname_var.set("")
        self.lname_var.set("")
        self.email_var.set("")
        self.pass_var.set("")
        self.cpass_var.set("")
        self.contact_var.set("")
        self.sec_question_var.set("")
        self.sec_answer_var.set("")
        self.var_chk.set(0)

    def go_to_login(self):
        self.root.destroy()
        import Face_Recognition_Software  # Assuming you have a login module

if __name__ == "__main__":
    main()
