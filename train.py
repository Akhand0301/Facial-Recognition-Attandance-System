from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("icon.png")

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"),
                          bg="black", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_path_top = r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro\14.jpeg"  # Ensure this path is correct
        try:
            img_top = Image.open(img_path_top)
            img_top = img_top.resize((1600, 350), Image.LANCZOS)
            self.photoimg_top = ImageTk.PhotoImage(img_top)
        except Exception as e:
            print(f"Error loading image: {e}")
            messagebox.showerror("Image Error", f"Failed to load image: {e}")
            return

        f_lbl_top = Label(self.root, image=self.photoimg_top)
        f_lbl_top.place(x=0, y=45, width=1600, height=350)

        # Create the TRAIN DATA button
        b1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2",
                    font=("times new roman", 15, "bold"), bg="black", fg="white")
        b1.place(x=0, y=395, width=1600, height=60)

        img_path_bott = r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro\15.jpeg" # Ensure this path is correct
        try:
            img_bott = Image.open(img_path_bott)
            img_bott = img_bott.resize((1600, 350), Image.LANCZOS)
            self.photoimg_bott = ImageTk.PhotoImage(img_bott)
        except Exception as e:
            print(f"Error loading image: {e}")
            messagebox.showerror("Image Error", f"Failed to load image: {e}")
            return

        f_lbl_bott = Label(self.root, image=self.photoimg_bott)
        f_lbl_bott.place(x=0, y=455, width=1600, height=350)

    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image_path in path:
            img = Image.open(image_path).convert('L')  # Grey scale image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image_path)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("training", imageNp)
            cv2.waitKey(1) == 13

        ids = np.array(ids)

        # Train the classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
