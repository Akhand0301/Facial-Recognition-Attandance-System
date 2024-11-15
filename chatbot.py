from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>', self.enter_fun)

        main_frame = Frame(self.root, bd=4, bg='powder blue', width=730)
        main_frame.pack(fill=BOTH, expand=True)

        # Load the image
        img_chat = Image.open(r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro\4.png")
        img_chat = img_chat.resize((200, 70), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img_chat)

        # Create the title label
        Title_label = Label(main_frame, bd=3, relief=RAISED, anchor='nw', width=730, compound=LEFT,
                            image=self.photoimg, text='CHAT ME', font=('arial', 30, 'bold'), fg='green', bg='white')
        Title_label.pack(side=TOP, fill=X)

        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=65, height=20, bd=3, relief=RAISED, font=('arial', 14), yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack(fill=BOTH, expand=True)

        btn_frame = Frame(self.root, bd=4, bg='white', width=730)
        btn_frame.pack(fill=X)

        label_1 = Label(btn_frame, text="Type Something", font=('arial', 14, 'bold'), fg='green', bg='white')
        label_1.grid(row=0, column=0, padx=5, sticky=W)

        self.entry_var = StringVar()  # Use a StringVar to track entry text
        self.entry = ttk.Entry(btn_frame, textvariable=self.entry_var, width=40, font=('arial', 16, 'bold'))
        self.entry.grid(row=0, column=1, padx=5, sticky=W)

        self.send_btn = Button(btn_frame, text="Send>>", command=self.send, font=('arial', 15, 'bold'), width=8, bg='green', fg='white')
        self.send_btn.grid(row=0, column=2, padx=5, sticky=W)

        self.clear_btn = Button(btn_frame, text="Clear Data", command=self.clear, font=('arial', 15, 'bold'), width=8, bg='red', fg='white')
        self.clear_btn.grid(row=1, column=0, padx=5, sticky=W)

        self.msg = ''
        self.label_11 = Label(btn_frame, text=self.msg, font=('arial', 14, 'bold'), fg='green', bg='white')
        self.label_11.grid(row=1, column=1, padx=5, sticky=W)

    def enter_fun(self, event):
        self.send()

    def send(self):
        user_input = self.entry_var.get()
        send = '\t\t\t' + 'You: ' + user_input
        self.text.insert(END, '\n' + send)
        self.text.yview(END)

        if user_input == '':
            self.msg = 'Please enter some input'
            self.label_11.config(text=self.msg, fg='red')
        else:
            self.msg = ''
            self.label_11.config(text=self.msg, fg='green')

        # Responses based on user input
        if user_input.lower() == 'hello':
            self.text.insert(END, '\n\n' + 'Bot: Hi')

        elif user_input.lower() == 'hi':
            self.text.insert(END, '\n\n' + 'Bot: Hello')

        elif user_input.lower() == 'how are you?':
            self.text.insert(END, '\n\n' + 'Bot: Fine and you?')

        elif user_input.lower() == 'fantastic':
            self.text.insert(END, '\n\n' + 'Bot: Nice to hear')

        elif user_input.lower() == 'who created you':
            self.text.insert(END, '\n\n' + 'Bot: Akhand using Python')

        elif user_input.lower() == 'what is your name?':
            self.text.insert(END, '\n\n' + 'Bot: My name is Robo, I am your helper')

        elif user_input.lower() == 'bye':
            self.text.insert(END, '\n\n' + 'Bot: Thank you for chatting')

        elif user_input.lower() == 'what is machine learning?':
            self.text.insert(END, '\n\n' + 'Bot: Machine learning is a branch of AI')

        elif user_input.lower() == 'what does face recognition work?':
            self.text.insert(END, '\n\n' + 'Bot: Facial recognition is a way of recognizing a human face through')

        elif user_input.lower() == 'how does face recognition work step by step?':
            self.text.insert(END, '\n\n' + 'Bot: Step 1: Face Detection The initial step involves collecting biometric data and detecting a face...\n (omitted for brevity)')

        elif user_input.lower() == 'how many countries use facial recognition?':
            self.text.insert(END, '\n\n' + 'Bot: Evidence of facial recognition use was found in only 6 countries...')

        elif user_input.lower() == 'what is python programming?':
            self.text.insert(END, '\n\n' + 'Bot: Python is a programming language...')

        elif user_input.lower() == 'what is chatbot?':
            self.text.insert(END, '\n\n' + 'Bot: Chatbots are computer programs that simulate human conversation with users.')

        else:
            self.text.insert(END, '\n\n' + "Bot: Sorry, I didn't get it")

        # Clear the entry after sending
        self.entry_var.set('')

    def clear(self):
        self.text.delete(1.0, END)
        self.entry_var.set('')

if __name__ == "__main__":
    root = Tk()
    chat_bot = ChatBot(root)
    root.mainloop()
