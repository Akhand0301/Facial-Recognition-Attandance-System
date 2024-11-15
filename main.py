from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter
from tkinter import messagebox
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attandance import Attendance
from devloper import DeveloperPage
from chatbot import ChatBot

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("icon.png")


        # First Image
        img_path1 = r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro\face3.jpg"  # Ensure this path is correct
        try:
            img1 = Image.open(img_path1)
            img1 = img1.resize((533, 130), Image.LANCZOS)  # Use Image.LANCZOS instead of Image.ANTIALIAS
            self.photoimg1 = ImageTk.PhotoImage(img1)
        except Exception as e:
            print(f"Error loading image: {e}")
            return

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=500, height=130)

        # Second Image
        img_path2 = r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro\face1.jpg"  # Ensure this path is correct
        try:
            img2 = Image.open(img_path2)
            img2 = img2.resize((533, 130), Image.LANCZOS)  # Use Image.LANCZOS instead of Image.ANTIALIAS
            self.photoimg2 = ImageTk.PhotoImage(img2)
        except Exception as e:
            print(f"Error loading image: {e}")
            return

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=500, y=0, width=500, height=130)

        # Third Image
        img_path3 = r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro\face2.jpg"  # Ensure this path is correct
        try:
            img3 = Image.open(img_path3)
            img3 = img3.resize((533, 130), Image.LANCZOS)  # Use Image.LANCZOS instead of Image.ANTIALIAS
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
            img_bg = img_bg.resize((1530, 710), Image.LANCZOS)  # Use Image.LANCZOS instead of Image.ANTIALIAS
            self.photoimg_bg = ImageTk.PhotoImage(img_bg)
        except Exception as e:
            print(f"Error loading image: {e}")
            return

        bg_img = Label(self.root, image=self.photoimg_bg)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="FACIAL RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Add image buttons with names
        self.add_image_button(bg_img, r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro\SD.jpg", "Student Details", 200, 100,
                              self.student_details)
        self.add_image_button(bg_img, r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro\b1.jpg.", "Face Detect", 500, 100, self.face_data)
        self.add_image_button(bg_img, r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro\AT.jpg", "Attendance", 800, 100, self.attandance_data)
        self.add_image_button(bg_img, r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro\CB.png", "ChatBot", 1100, 100, self.chatbo)
        self.add_image_button(bg_img, r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro\TL.png","Train Data", 200, 380, self.train_data)
        self.add_image_button(bg_img, r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro\PT.jpg", "Photos", 500, 380,  self.open_img)
        self.add_image_button(bg_img, r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro\dev.jpg", "Developer", 800, 380, self.dev_data)
        self.add_image_button(bg_img, r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro\Ex.png", "Exit", 1100, 380, self.iExit)

    def add_image_button(self, parent, img_path, button_name, x, y, command=None):
        try:
            img = Image.open(img_path)
            img = img.resize((220, 220), Image.LANCZOS)
            photoimg = ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Error loading image: {e}")
            return

        btn = Button(parent, image=photoimg, text=button_name, compound="top", cursor="hand2",
                     font=("times new roman", 15, "bold"), bg="dark blue", fg="white", command=command)
        btn.image = photoimg  # Keep a reference to avoid garbage collection
        btn.place(x=x, y=y, width=220, height=260)

    def open_img(self):
        os.startfile("data")

    #========= Function buttons===========================
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attandance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def dev_data(self):
        self.new_window = Toplevel(self.root)
        self.app = DeveloperPage(self.new_window)

    def chatbo(self):
        self.new_window = Toplevel(self.root)
        self.app = ChatBot(self.new_window)

    def iExit(self):
        response = messagebox.askyesno("Face Recognition", "Are you sure you want to exit?", parent=self.root)
        if response:
            self.root.destroy()

        else:
            return


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
