from tkinter import *
from pygame import *
window = Tk()
window.title("Daddy's home")
window.geometry("300x300")
window.iconbitmap('play5.ico')
mixer.init()

# LABEL
title = Label(text="What up?")
title.pack()

# Entry field

entry_field1 = Entry()
entry_field1.pack()

photo = PhotoImage(file='play (1).png')
pause = PhotoImage(file='stop.png')

lit = {
    1: 'Say You Won t Let Go.mp3',
    2: 'In the Jungle the mighty jungle.mp3'
     }
lost = ''
print(lit)

this_one = int(input('"which one?"'))
for j, i in lit.items():
    if j == this_one:
        lost = i


def pause_btn():
    mixer.music.stop()


def scale_btn(val):
    volume = int(val)/100
    mixer.music.set_volume(volume)


def play_btn():
    mixer.music.load(lost)
    mixer.music.play()


# Buttons
button1 = Button(window, image=photo, command=play_btn)
button1.pack(padx=5, pady=5)
button2 = Button(window, image=pause, command=pause_btn)
button2.pack(padx=5, pady=5)


scale = Scale(window, orient=HORIZONTAL, command=scale_btn)
scale.set(50)
scale.pack(padx=5, pady=5)

QUIT = Button(text="QUIT", fg="red", command=window.destroy)
QUIT.pack()

window.mainloop(padx=5, pady=5)





