from tkinter import *
from tkinter import messagebox

class DeveloperPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer Page")

        # Page Title
        title_lbl = Label(self.root, text="Developer Page", font=("Comic Sans MS", 35, "bold"),
                          bg="#282828", fg="#FFD700")
        title_lbl.place(x=0, y=0, width=1600, height=70)

        # Main Frame
        main_frame = Frame(self.root, bd=5, bg="#1E1E1E", relief=RIDGE)
        main_frame.place(x=0, y=75, width=1590, height=710)

        # Left side label frame
        Left_frame = LabelFrame(main_frame, bd=3, bg="#333333", fg="#FFD700", relief=GROOVE,
                                text="About the Developer", font=("Comic Sans MS", 18, "bold"))
        Left_frame.place(x=20, y=20, width=500, height=650)

        # Developer Info Labels
        dev_name_lbl = Label(Left_frame, text="Name: Akhand Chaurasiya",
                             font=("Comic Sans MS", 16, "bold"), bg="#333333", fg="#FFFFFF")
        dev_name_lbl.pack(pady=15, anchor=W)

        dev_email_lbl = Label(Left_frame, text="Email: chaurasiyaakhand@gmail.com",
                              font=("Comic Sans MS", 16), bg="#333333", fg="#FFFFFF")
        dev_email_lbl.pack(pady=15, anchor=W)

        dev_phone_lbl = Label(Left_frame, text="Phone: +91 9399482258",
                              font=("Comic Sans MS", 16), bg="#333333", fg="#FFFFFF")
        dev_phone_lbl.pack(pady=15, anchor=W)

        dev_about_lbl = Label(Left_frame, text="About: This project was developed by Akhand Chaurasiya. "
                                               "Akhand is an MCA student and Python Developer who enjoys building "
                                               "innovative software solutions.",
                              font=("Comic Sans MS", 14), bg="#333333", fg="#FFFFFF",
                              wraplength=450, justify=LEFT)
        dev_about_lbl.pack(pady=20, anchor=W)

        # Right side frame for text decoration
        Right_frame = Frame(main_frame, bd=3, bg="#282828", relief=RIDGE)
        Right_frame.place(x=550, y=20, width=1000, height=650)

        # Decorative Text for Aesthetic Appeal
        heading = Label(Right_frame, text="Welcome to the Developer Page!",
                        font=("Comic Sans MS", 30, "bold"), bg="#282828", fg="#FFD700")
        heading.pack(pady=30)

        subheading = Label(Right_frame, text="Get to know the creative mind behind this project.",
                           font=("Comic Sans MS", 20), bg="#282828", fg="#FFFFFF")
        subheading.pack(pady=20)

        description = Label(Right_frame, text="This application was designed with dedication and care to showcase "
                                              "advanced development skills in Python and user interface design.\n"
                                              "Akhand Chaurasiya is passionate about technology and continues to push "
                                              "the boundaries of innovation and learning.",
                            font=("Comic Sans MS", 16), bg="#282828", fg="#D3D3D3", wraplength=900, justify=LEFT)
        description.pack(pady=40)

        # Footer for a nice touch
        footer = Label(self.root, text="Developed with ❤️ by Akhand Chaurasiya", font=("Comic Sans MS", 14, "italic"),
                       bg="#282828", fg="#FFD700")
        footer.place(x=0, y=760, width=1600, height=30)

if __name__ == "__main__":
    root = Tk()
    obj = DeveloperPage(root)
    root.mainloop()
