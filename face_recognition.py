from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import cv2
import os
import numpy as np
import mysql.connector
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("icon.png")

        # Title Label
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="black", fg="red")
        title_lbl.place(x=0, y=0, width=1600, height=45)

        # Load the top image
        img_path_top = r"C:\Users\Akhan\PycharmProjects\pythonProject\images pro\9.jpg"
        try:
            img_top = Image.open(img_path_top)
            img_top = img_top.resize((1600, 800), Image.LANCZOS)
            self.photoimg_top = ImageTk.PhotoImage(img_top)
        except Exception as e:
            print(f"Error loading image: {e}")
            messagebox.showerror("Image Error", f"Failed to load image: {e}")
            return

        # Display the image on the window
        f_lbl_top = Label(self.root, image=self.photoimg_top)
        f_lbl_top.place(x=0, y=45, width=1600, height=800)

        # Create the Face Recognition button
        b1 = Button(self.root, text="Face Recognition", cursor="hand2", font=("times new roman", 20, "bold"), bg="darkgreen", fg="white", command=self.face_recog)
        b1.place(x=600, y=650, width=300, height=50)

    def mark_attendance(self, i, r, n, d):
        try:
            with open("attendance.csv", "r+", newline="\n") as f:
                myDataList = f.readlines()
                name_list = [line.split(",")[0] for line in myDataList]

                if i not in name_list:
                    now = datetime.now()
                    date = now.strftime("%d/%m/%Y")
                    time = now.strftime("%H:%M:%S")
                    f.writelines(f"\n{i},{r},{n},{d},{time},{date},Present")
        except Exception as e:
            print(f"Error marking attendance: {e}")
            messagebox.showerror("Error", f"Failed to mark attendance: {e}")

    def draw_boundary(self, img, classifier, scaleFactor, minNeighbors, color, clf):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
            id, predict = clf.predict(gray_image[y:y + h, x:x + w])
            confidence = int((100 * (1 - predict / 300)))

            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="12345@123",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT StudentId, Name, Roll, Department FROM student WHERE StudentId=%s", (id,))
                result = my_cursor.fetchone()
                conn.close()

                if result:
                    i, n, r, d = result
                else:
                    i, n, r, d = "Unknown", "Unknown", "Unknown", "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"ID:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
            except mysql.connector.Error as e:
                print(f"Database Error: {e}")
                messagebox.showerror("Database Error", f"Error: {e}", parent=self.root)

    def recognize(self, img, clf, faceCascade):
        if img is None:
            raise ValueError("Empty frame received from video capture.")
        self.draw_boundary(img, faceCascade, 1.1, 10, (255, 0, 0), clf)
        return img

    def face_recog(self):
        # Open a new window for Face Recognition
        new_window = Toplevel(self.root)
        new_window.title("Face Recognition")
        new_window.geometry("800x600")  # Adjust as needed

        def close_window():
            video_cap.release()
            cv2.destroyAllWindows()
            new_window.destroy()

        new_window.protocol("WM_DELETE_WINDOW", close_window)

        try:
            faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            if faceCascade.empty():
                raise ValueError("Failed to load Haar cascade classifier!")

            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")

            video_cap = cv2.VideoCapture(0)
            if not video_cap.isOpened():
                raise IOError("Cannot open webcam")

            while True:
                ret, img = video_cap.read()
                if not ret:
                    raise IOError("Failed to capture video frame.")

                img = self.recognize(img, clf, faceCascade)
                cv2.imshow("Welcome To Face Recognition", img)

                if cv2.waitKey(1) & 0xFF == 13:  # Press 'Enter' key to break
                    break

            video_cap.release()
            cv2.destroyAllWindows()
        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", f"An error occurred: {e}")
            close_window()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
