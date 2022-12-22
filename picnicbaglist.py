# -*- coding: utf-8 -*-
from tkinter import *
import random

root = Tk()
root.title("Picnic Bag List")
root.geometry("500x500")

label_items = Label(root)
label_random_numbers = Label(root)

list_of_items = ["Backpack", "ID", "Flashlight", "Food", "Mat", "Water", "Plates", "Utensils"]
label_items["text"] = "Items Listed: " + str(list_of_items)

def itemList():
    random_items = random.sample(range(0,9),1)
    label_random_numbers["text"] = "Place Item No. " + str(random_items) + " in the bag."
    
label_items.place(relx=0.5, rely=0.4, anchor=CENTER)

btn = Button(root, text="What Items Should You Put in the Bag", command=itemList, bg="medium aquamarine", fg="white")
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

label_random_numbers.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()