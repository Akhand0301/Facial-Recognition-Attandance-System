from tkinter import *


class HelpDesk:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Help Desk")

        # Page Title
        title_lbl = Label(self.root, text="Help Desk", font=("Comic Sans MS", 35, "bold"), bg="#2C3E50", fg="#ECF0F1")
        title_lbl.place(x=0, y=0, width=1530, height=70)

        # Main Frame
        main_frame = Frame(self.root, bd=5, bg="#34495E", relief=RIDGE)
        main_frame.place(x=20, y=90, width=1490, height=670)

        # Help Desk Title
        help_info_lbl = Label(main_frame, text="Welcome to the Help Desk!", font=("Comic Sans MS", 28, "bold"),
                              bg="#34495E", fg="#F1C40F")
        help_info_lbl.pack(pady=40)

        # Help Information
        help_text = (
            "This is the Help Desk section where you can find assistance for using the application.\n\n"
            "For any inquiries or issues, please contact our support team at:\n\n"
            "📧 Email: chaurasiyaakhand@gmail.com\n"
            "📞 Phone: +91 9399482258\n\n"
            "We are here to ensure you have the best experience with our application.\n"
            "Thank you for using our software!"
        )

        help_msg_lbl = Label(main_frame, text=help_text, font=("Arial", 18), bg="#34495E", fg="#ECF0F1",
                             wraplength=1400, justify=LEFT)
        help_msg_lbl.pack(padx=30, pady=30)

        # Footer
        footer = Label(self.root, text="Developed with ❤️ by Akhand Chaurasiya", font=("Comic Sans MS", 14, "italic"),
                       bg="#2C3E50", fg="#F1C40F")
        footer.place(x=0, y=760, width=1530, height=30)


if __name__ == "__main__":
    root = Tk()
    obj = HelpDesk(root)
    root.mainloop()
