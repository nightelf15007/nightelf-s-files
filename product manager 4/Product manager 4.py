#import everything 
import pymongo
from pymongo import MongoClient
import json
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import json

#create a class for the tool tip because they look good ;)
class CreateToolTip(object):
    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)
    def enter(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        #creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        #Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                       background='light grey', relief='solid', borderwidth=1,
                       font=("times", "8", "normal"))
        label.pack(ipadx=1)
    def close(self, event=None):
        if self.tw:
            self.tw.destroy()

#create a class, because they look good ;)
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master) 
        self.master = master
        self.pack()
        self.create_widgets()

    #create a function for the gui
    def create_widgets(self):
        #2 labels for the comboboxes
        self.lbl1 = tk.Label(self, text="Category")
        self.lbl2 = tk.Label(self, text="Brand")

        #comboboxes and their values
        self.number = tk.StringVar()
        self.productChosen = ttk.Combobox(self, textvariable=7)
        self.productChosen['values'] = ("Chips", "Choclates", "Drinks", "Fruits", "Pies", "Sweets", "Veggies", "All")
        self.productChosen.current(0)
        self.brandChosen = ttk.Combobox(self, textvariable=16)
        self.brandChosen['values'] = ("Simba", "Lays", "No_Brand", "BarOne", "Chomp", "Coca-Cola", "Fanta", "Flake", "Maynards", "Monster Energy", "Play", "PS", "Score", "Speckles", "Sprite", "Tex")
        self.brandChosen.current(0) 

        #create the buttons for the gui
        self.btnDispCat = tk.Button(self, command=self.categoryClick, text = "Display Category", height = 2, width = 14)
        self.btnRestore = tk.Button(self, command=self.restoreDB, text = "Restore Database", height = 2, width = 14)
        self.btnTop = tk.Button(self, command=self.topThreeClick, text = "Display Top 3", height = 2, width = 14)
        self.btnDeleteBrand = tk.Button(self, command=self.deleteBrands, text = "Delete Brand", height = 2, width = 14)
        self.btnUpdateRecord = tk.Button(self, command=self.updateProduct, text = "Update Product", height = 2, width = 14)
        self.btnLeast = tk.Button(self, command=self.leastThreeBrands, text = "Least 5 Brands", height = 2, width = 14)
        #create the scrolledtext for the DB to display in
        self.scr = scrolledtext.ScrolledText(self, width=75, height=10, wrap=tk.WORD)

        #place the buttons and scrolled text on the window
        self.lbl1.grid(row = 0, column=0, columnspan= 1)
        self.productChosen.grid(row = 0, column=1, columnspan= 1)
        
        self.lbl2.grid(row = 2, column=0, columnspan= 1)
        self.brandChosen.grid(row = 2, column=1, columnspan= 1)


        self.btnDispCat.grid(row = 3, column=0, columnspan= 1)
        button1_ttp = CreateToolTip(self.btnDispCat, "Displays all the products in the specified catagory")

        self.btnTop.grid(row = 3, column=1, columnspan= 1)
        button1_ttp = CreateToolTip(self.btnTop, "Display the 3 best selling products according to available stock")

        self.btnDeleteBrand.grid(row = 3, column=2, columnspan= 1)
        button1_ttp = CreateToolTip(self.btnDeleteBrand, "Delete products under selected brand")

        self.btnRestore.grid(row = 4, column=0, columnspan= 1)
        button1_ttp = CreateToolTip(self.btnRestore, "Reload the orignal file")

        self.btnUpdateRecord.grid(row = 4, column=1, columnspan= 1)
        button1_ttp = CreateToolTip(self.btnUpdateRecord, "Update records")

        self.btnLeast.grid(row = 4, column=2, columnspan= 1)
        button1_ttp = CreateToolTip(self.btnLeast, "Displays the top 5 brand with most available stock")

        self.scr.grid(row = 5, column=0, columnspan= 3)

    #create a function to display products in selected catagory 
    def categoryClick(self):
        self.scr.delete('1.0', tk.END)

        self.cluster = MongoClient("mongodb+srv://admin:admin@cluster0.gjswf.mongodb.net/<dbname>?retryWrites=true&w=majority")

        self.db = self.cluster["DataTracker"]
        self.collection = self.db["products"]

        self.prod = self.productChosen.get()

        for x in self.collection.find({ "Category": self.prod }).sort("Availible_Stock", -1):
            string = x["Product_Name"] + '\t' + str(x["Available_Stock"]) + '\n'
            string = string.expandtabs()
            self.scr.insert(tk.INSERT, string)

    #create a function to Display the 3 best selling products according to available stock
    def topThreeClick(self):
        self.scr.delete('1.0', tk.END)

        self.cluster = MongoClient("mongodb+srv://admin:admin@cluster0.gjswf.mongodb.net/<dbname>?retryWrites=true&w=majority")

        self.db = self.cluster["DataTracker"]
        self.collection = self.db["products"]
        self.top_three = self.db["top_3_products"]

        self.x = self.top_three.delete_many({})

        self.cnt = 0

        for x in self.collection.find().sort("Available_Stock"):
            if self.cnt != 3:
                self.top_three.insert_one(x)

                string = x["Product_Name"] + '\t' + str(x["Available_Stock"]) + '\n'
                string = string.expandtabs()
                self.scr.insert(tk.INSERT, string)
                self.cnt += 1

    #create a function display everything but the selected brand
    def deleteBrands(self):
        self.scr.delete('1.0', tk.END)

        self.cluster = MongoClient("mongodb+srv://admin:admin@cluster0.gjswf.mongodb.net/<dbname>?retryWrites=true&w=majority")

        self.db = self.cluster["DataTracker"]
        self.collection = self.db["products"]
        self.top_three = self.db["top_3_products"]

        self.prod = self.brandChosen.get()

        for x in self.collection.find().sort("Available_Stock"):
            if x["Brand"] == self.prod:
                self.collection.delete_one(x)

        self.scr.insert(tk.INSERT, "Deletion Succesful")

    #create a function to load the original file
    def restoreDB(self):
        self.scr.delete('1.0', tk.END)

        self.cluster = MongoClient("mongodb+srv://admin:admin@cluster0.gjswf.mongodb.net/<dbname>?retryWrites=true&w=majority")

        self.db = self.cluster["DataTracker"]
        self.collection = self.db["products"]

        self.x = self.collection.delete_many({})

        with open('Products.json') as self.f:
            self.file_data = json.load(self.f)

        self.collection.insert_many(self.file_data)

        self.scr.insert(tk.INSERT, "Database Restored Succesfully")

    #create a function to update the products
    def updateProduct(self):
        self.scr.delete('1.0', tk.END)

        self.cluster = MongoClient("mongodb+srv://admin:admin@cluster0.gjswf.mongodb.net/<dbname>?retryWrites=true&w=majority")

        self.db = self.cluster["DataTracker"]
        self.collection = self.db["products"]
        self.top_three = self.db["top_3_products"]

        self.p_name = {"Product_Name": "Butternut"}
        self.brand_name = {"Brand": "No_Brand"}

        self.p_name_chnge = { "$set": { "Product_Name": "Aero" } }
        self.brand_name_chnge = { "$set": { "Brand": "Aero" } }

        self.top_three.update_one(self.p_name, self.p_name_chnge)
        self.top_three.update_one(self.brand_name, self.brand_name_chnge)

    #create a function to display the top 5 brand with most available stock
    def leastThreeBrands(self):
        self.scr.delete('1.0', tk.END)

        self.cluster = MongoClient("mongodb+srv://admin:admin@cluster0.gjswf.mongodb.net/<dbname>?retryWrites=true&w=majority")

        self.db = self.cluster["DataTracker"]
        self.collection = self.db["products"]
        self.top_three = self.db["top_3_products"]

        self.cnt = 0

        for x in self.collection.find().sort("Available_Stock", -1):
            if self.cnt != 5:
                self.scr.insert(tk.INSERT, x['Product_Name'] + '\n')
                self.cnt += 1

root = tk.Tk()
app = Application(master=root)
app.mainloop()

root.mainloop()
