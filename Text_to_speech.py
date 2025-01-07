import tkinter as tk
from tkinter import*
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
from gtts import gTTS
from playsound import playsound

# Create User interface
root=Tk()
root.title("Text to Speech Converter")
root.geometry("1000x580+200+80")
root.resizable(False, False)
root.configure(bg="#FFA100")

#text to speech
tts=pyttsx3.init()
def speaknow():
    text=text_box.get(1.0, END)
    gender=gender_box.get()
    speed=speed_box.get()
    voices=tts.getProperty('voices')

    def setvoice():
        if(gender=='Male'):
            tts.setProperty('voice',voices[0].id)
            tts.say(text)
            tts.runAndWait()
        else:
            tts.setProperty('voice', voices[1].id)
            tts.say(text)
            tts.runAndWait()

    if(text):
        if(speed=='Fast'):
            tts.setProperty('rate',250)
            setvoice()
        elif(speed=='Medium'):
            tts.setProperty('rate',150)
            setvoice()
        else:
            tts.setProperty('rate',60)
            setvoice()

# Load and resize the logo
image_path = "C:\\Users\\ayans\\OneDrive\\Pictures\\Saved Pictures\\logo_png.png"
image = Image.open(image_path)

# Resize the image to fit a specific size 
image = image.resize((50, 30))  # Maintains quality while resizing

# Convert the resized image to a Tkinter-compatible format
my_logo = ImageTk.PhotoImage(image)

Label(root, image=my_logo, bg="#F7AC40").place(x=940, y=540)

#root.mainloop()
logo_image=PhotoImage(file="C:\\Users\\ayans\\OneDrive\\Pictures\\Saved Pictures\\text to speech.png")
root.iconphoto(False,logo_image)

#Upper Frame
upper_frame=Frame(root, bg="#14A7DD", width=1200, height=130)
upper_frame.place(x=0, y=0)

# Load and resize the image
image_path = "C:\\Users\\ayans\\OneDrive\\Pictures\\Saved Pictures\\text to speech.png"  # Replace with the path to your image
try:
    image = Image.open(image_path)
except FileNotFoundError:
    print("Error: File not found at the specified path!")
    exit()

# Resize the image to fit the specified area (1200x130)
image = image.resize((170, 70), Image.Resampling.LANCZOS)

# Convert the image to a format compatible with Tkinter
photo = ImageTk.PhotoImage(image)

# Place the image at the desired position
label = Label(root, image=photo, bg="#7FAC40")
label.place(x=90, y=30)  

# Run the application
Label(upper_frame, text="Text to speech converter",font="TimesNewroman 40 bold", bg="#14A7DD", fg="white").place(x=270, y=30)

#text Box
text_box=Text(root, font="calibri 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
text_box.place(x=30, y=150, width=940, height=180)

#SPEED AND VOICE
gender_box=Combobox(root, values=['Male','Female'], font="Robote 12", state='r', width=12)
gender_box.place(x=340, y=400)
gender_box.set('Male')

#Speed box
speed_box=Combobox(root, values=['Fast','Medium','Slow'], font="Robote 12", state='r', width=12)
speed_box.place(x=540, y=400)
speed_box.set('Medium')

#LABEL
Label(root, text="Select Voice", font='TimesNewRoman 15 bold',bg="#F7AC40", fg="black").place(x=340, y=370)
Label(root, text="Select Speed", font='TimesNewRoman 15 bold',bg="#F7AC40", fg="black").place(x=540, y=370)

# Load and resize the image
image_path = "C:\\Users\\ayans\\OneDrive\\Pictures\\Saved Pictures\\play_button.png"  # Replace with the path to your image
try:
    image = Image.open(image_path)
except FileNotFoundError:
    print("Error: File not found at the specified path!")
    exit()

# Resize the image to fit the specified area
image = image.resize((80, 70), Image.Resampling.LANCZOS)

# Convert the image to a format compatible with Tkinter
play_button = ImageTk.PhotoImage(image)
 
#PLAY BUTTON
play_but=Button(root, text="Play", compound=LEFT, image=play_button, bg='white', width=130, font="arial 14 bold", borderwidth='0.1c', command=speaknow)
play_but.place(x=435, y=450)

root.mainloop()
