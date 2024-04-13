from tkinter import *
import os

def open_student_view():
    os.system("python studentview.py")

def open_teacher_view():
    os.system("python teacherview.py")

root = Tk()
root.title("Menu")
root.geometry("400x400")

# Frame for title label
frame_title = Frame(root, padx=20, pady=20)
frame_title.pack(side=TOP)

title_label = Label(frame_title, text="MENU", bg="light blue", fg="black", font=("Arial", 14))
title_label.pack(side=TOP, fill=X, padx=10, pady=10)

# Frame for student bot
frame_student = Frame(root, padx=20, pady=20)
frame_student.pack(side=TOP)

label_student = Label(frame_student, text="Student Bot")
label_student.pack(side=LEFT)

button_student = Button(frame_student, text="View", command=open_student_view)
button_student.pack(side=RIGHT)

# Frame for teacher bot
frame_teacher = Frame(root, padx=20, pady=20)
frame_teacher.pack(side=TOP)

label_teacher = Label(frame_teacher, text="Teacher Bot")
label_teacher.pack(side=LEFT)

button_teacher = Button(frame_teacher, text="View", command=open_teacher_view)
button_teacher.pack(side=RIGHT)

root.mainloop()
