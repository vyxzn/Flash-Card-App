from tkinter import *
import pandas as p
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE = ""
DEFINITION = ""
INDEX = 0
frenchData = {}
flip_timer = 1
try:
    data = p.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = p.read_csv("data/french_words.csv")
    frenchData = original_data.to_dict(orient="records")
else:
    frenchData = data.to_dict(orient="records")

window = Tk()
window.title("Flash Cards App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(900, 626)

#give us the first definition
canvas = Canvas(width=800, height=526, highlightthickness=0)
frontCardPic = PhotoImage(file="images/card_front.png")
backCardPic = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=frontCardPic)
titleText = canvas.create_text(400, 150, text=TITLE, fill="black", font=('Ariel 40 italic'))
defText = canvas.create_text(400, 263, text=DEFINITION, fill="black", font=('Ariel 60 bold'))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column=0,row=0, columnspan=2)

def flipCard():
    canvas.itemconfig(canvas_image, image=backCardPic)
    canvas.itemconfig(defText, text=frenchData[INDEX]["English"], fill="white")
    global TITLE
    TITLE = "English"
    canvas.itemconfig(titleText, text=TITLE, fill="white")

def generateNew():
    global INDEX, DEFINITION, TITLE, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=frontCardPic)
    INDEX = random.randint(0,len(frenchData))
    DEFINITION = frenchData[INDEX]["French"]
    canvas.itemconfig(defText, text = DEFINITION, fill="black")
    TITLE = "French"
    canvas.itemconfig(titleText, text = TITLE, fill="black")
    flip_timer = window.after(3000, flipCard)
generateNew()

def learned():
    frenchData.remove(frenchData[INDEX])
    words = p.DataFrame(frenchData)
    words.to_csv("data/words_to_learn.csv")
    generateNew()

wrongBtnImg = PhotoImage(file="images/wrong.png")
wrongButton = Button(image=wrongBtnImg, highlightthickness=0, command = generateNew)
wrongButton.grid(column=0,row=1)

rightBtnImg = PhotoImage(file="images/right.png")
rightButton = Button(image=rightBtnImg, highlightthickness=0, command=learned)
rightButton.grid(column=1,row=1)
















window.mainloop()
