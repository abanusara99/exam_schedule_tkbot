import tkinter as tk
import os

# Create the GUI window
root = tk.Tk()
root.title("PASCW Chatbot")
root.configure(bg="light blue")
root.geometry("600x600")

# Create a canvas for displaying the logo
title_label = tk.Label(root, text="", background="light blue")
title_label.pack() 
title_label = tk.Label(root, text="PASCW", font=("Arial", 16), fg="black",background="light blue")
title_label.pack() 


canvas = tk.Canvas(root, width=500, height=500)
canvas.configure(bg="light blue")
canvas.pack()

# Load the logo image
logo_image = tk.PhotoImage(file="enter.png")

# Display the logo on the canvas
canvas.create_image(250, 250, image=logo_image)

# Define a function to hide the logo and show the next button
def show_next_button():
    canvas.destroy()  # remove the canvas
    next_button.pack()  # show the next button

# Wait for 2 seconds
root.after(2000)

# Create the next button
def run_main():
    os.system("python tecbot.py")  # execute main.py
next_button = tk.Button(root, text="Next", font=("Arial", 28), command=run_main)
next_button.place(relx=0.7, rely=0.9, anchor=tk.CENTER)
# Start the main event loop
root.mainloop()
