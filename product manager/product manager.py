#import everything
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
#create df
df = pd.DataFrame(
    [["Chips", "Simba", "Lays", "(chips)"],
    ["Cooldrinks", "Coke", "Fanta", "(cooldrink)"],
    ["Chocolates", "Cadbury", "Tex", "(chocolate)"],
    ["Pies", "Pepper Steak", "Chicken", "(pie)"],
    ["Fruit", "Pear", "Apple", "Orange"],
    ["Cupcakes", "vanilla", "chocolate", "(cupcake)"],
    ["Veggies", "spinach", "cabbage", "(veggies)"]],
    columns = ["", "", "", ""],
    index = ["a", "b", "c", "d", "e", "f", "g"])
df.to_csv("products.txt") #write df to text file

# window
win = tk.Tk()
win.title("Product manager")

# modify adding label
aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)

# text box entry
ttk.Label(win, text="Enter product:").grid(column=0, row=0)
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=20, textvariable=name)
nameEntered.grid(column=1, row=0)

# drop down menu
ttk.Label(win, text="Choose a product type:").grid(column=0, row=1)
number = tk.StringVar()
productChosen = ttk.Combobox(win, width=17, textvariable=number)
productChosen['values'] = ("Chips", "Cooldrinks", "Chocolates", "Pies", "Fruit", "Cupcakes", "Veggies")
productChosen.grid(column=1, row=1)
productChosen.current(0)


# scrolled text
scr = scrolledtext.ScrolledText(win, width=75, height=10, wrap=tk.WORD)
scr.grid(column=0, sticky='WE', columnspan=3)
scr.insert(tk.INSERT, df)
scr.configure(state = "disabled")

# button click event (it broke :'(    )
def onClick():
    if productChosen.get() == "Chips":
        with open("products.txt", "w+") as f:
            for lines in f:
                f.write(line.replace("(chips)", nameEntered.get()))
                df = pd.read_csv("products.txt")
                scr.insert(tk.INSERT, df)
    elif productChosen.get() == "Cooldrink":
        with open("products.txt", "w+") as f:
            for lines in f:
                f.write(line.replace("(cooldrink)", nameEntered.get()))
                df = pd.read_csv("products.txt")
                scr.insert(tk.INSERT, df)
    elif productChosen.get() == "Pies":
        with open("products.txt", "w+") as f:
            for lines in f:
                f.write(line.replace("(pie)", nameEntered.get()))
                df = pd.read_csv("products.txt")
                scr.insert(tk.INSERT, df)
    elif productChosen.get() == "Chocolates":
        with open("products.txt", "w+") as f:
            for lines in f:
                f.write(line.replace("(chocolate)", nameEntered.get()))
                df = pd.read_csv("products.txt")
                scr.insert(tk.INSERT, df)
    elif productChosen.get() == "Fruits":
        with open("products.txt", "w+") as f:
            for lines in f:
                f.write(line.replace("(fruit)", nameEntered.get()))
                df = pd.read_csv("products.txt")
                scr.insert(tk.INSERT, df)
    elif productChosen.get() == "Cupcakes":
        with open("products.txt", "w+") as f:
            for lines in f:
                f.write(line.replace("(cupcake)", nameEntered.get()))
                df = pd.read_csv("products.txt")
                scr.insert(tk.INSERT, df)
    elif productChosen.get() == "Veggies":
        with open("products.txt", "w+") as f:
            for lines in f:
                f.write(line.replace("(veggies)", nameEntered.get()))
                df = pd.read_csv("products.txt")
                scr.insert(tk.INSERT, df)

# button
action = ttk.Button(win, text="Add to table", command=onClick())
action.grid(column=2, row=1)




nameEntered.focus() #set focus to input place

win.mainloop()

#Fun Fact: Charles W. Bachman designed the Integrated Database System in 1960