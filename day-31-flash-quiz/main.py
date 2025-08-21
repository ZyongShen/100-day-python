from tkinter import *

root = Tk()

flash_card = Canvas(root, width=800, height=526)
flash_card.pack()

card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')

wrong_img = PhotoImage(file='images/wrong.png')
right_img = PhotoImage(file="images/right.png")


