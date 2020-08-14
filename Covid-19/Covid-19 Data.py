#import everything 
import pymongo
from pymongo import MongoClient
import json
import csv
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


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
        self.lbl1 = tk.Label(self, text="Country")

        #comboboxes and their values
        self.number = tk.StringVar()
        self.country = ttk.Combobox(self, textvariable=7)
        self.country['values'] = ("Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Anguilla", "Antigua and Barbuda", 
                                         "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", 
                                         "Bahrain", "Argentina", "Argentina", "Argentina", "Argentina", "Argentina", "Argentina",
                                         "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda",
                                         "Bhutan", "Bolivia (Plurinational State of)", "Bonaire, Sint Eustatius and Saba", "Bosnia and Herzegovina",
                                        "Botswana", "Brazil", "British Virgin Islands", "Argentina", "Brunei Darussalam", "Bulgaria", "Burkina Faso",
                                         "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Cayman Islands", "Central African Republic",
                                         "Chad", "Chile", "China", "Colombia", "Congo", "Costa Rica", "CÃ´te dâ€™Ivoire"
                                         "Croatia", "Cuba", "CuraÃ§ao", "Cyprus", "Czechia", "Democratic Republic of the Congo", "Denmark"
                                         "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea"
                                         "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Falkland Islands (Malvinas)", "Faroe Islands", "Fiji"
                                         "Finland", "France", "French Guiana", "French Polynesia", "Gabon", "Gambia", "Georgia",
                                         "Germany", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada",
                                         "Guadeloupe", "Guam", "Guatemala", "Guernsey", "Guinea", "Guinea-Bissau", "Guyana",
                                         "Haiti", "Holy See", "Honduras", "Hungary", "Iceland", "India", "Indonesia",
                                         "International conveyance (Diamond Princess)", "Iran (Islamic Republic of)", "Iraq", "Ireland", "Isle of Man",
                                         "Israel", "Italy", "Jamaica", "Japan", "Jersey", "Jordan", "Kazakhstan",
                                         "Kenya", "Kosovo[1]", "Kuwait", "Kyrgyzstan", "Lao People's Democratic Republic", "Latvia", "Lebanon",
                                         "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi",
                                         "Malaysia", "Maldives", "Mali", "Malta", "Martinique", "Mauritania", "Mauritius",
                                         "Mayotte", "Mexico", "Monaco", "Mongolia", "Montenegro", "Montserrat", "Morocco",
                                         "Mozambique", "Myanmar", "Namibia", "Nepal", "Netherlands", "New Caledonia", "New Zealand",
                                         "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Northern Mariana Islands (Commonwealth of the)", "Norway", 
                                         "occupied Palestinian territory", "Oman", "Pakistan", "Panama", "Papua New Guinea", "Paraguay", "Peru",
                                         "Philippines", "Poland", "Portugal", "Puerto Rico", "Qatar", "Republic of Korea", "Republic of Moldova",
                                         "RÃ©union", "Romania", "Russian Federation", "Argentina", "Rwanda", "Saint BarthÃ©lemy", "Saint Kitts and Nevis",
                                         "Saint Lucia", ",Saint Martin", "Saint Pierre and Miquelon", "Saint Vincent and the Grenadines", "San Marino",
                                         "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore",
                                         "Sint Maarten", "Slovakia", "Slovenia", "Somalia", "South Africa", "South Sudan", "Spain",
                                         "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syrian Arab Republic", "Thailand",
                                         "The United Kingdom", "Timor-Leste", "Togo", "Trinidad and Tobago", "Tunisia", "Turkey", "Turks and Caicos Islands",
                                         "Uganda", "Ukraine", "United Arab Emirates", "United Republic of Tanzania", "United States of America", "United States Virgin Islands", "Uruguay",
                                         "Uzbekistan", "Venezuela (Bolivarian Republic of)", "Viet Nam", "Yemen", "Zambia", "Zimbabwe")


        #create the buttons for the gui
        self.btnTimeAllCases = tk.Button(self, command=self.TimeAllCases, text = "All cases", height = 2, width = 14)
        self.btnRestore = tk.Button(self, command=self.restoreDB, text = "Restore Database", height = 2, width = 14)
        self.btnTimeDeath = tk.Button(self, command=self.TimeDeath, text = "All deaths", height = 2, width = 14)
        self.btnSelectedNewCases = tk.Button(self, command=self.selectedNewTotalCases, text = "New total cases", height = 2, width = 14)
        self.btnSelectedNewDeaths = tk.Button(self, command=self.selectedNewDeaths, text = "New total deaths", height = 2, width = 14)
        self.btnClear = tk.Button(self, command=self.clear, text = "Clear", height = 2, width = 14)
        #create the scrolledtext for the DB to display in
        self.scr = scrolledtext.ScrolledText(self, width=75, height=10, wrap=tk.WORD)

        #place the buttons and scrolled text on the window
        self.lbl1.grid(row = 0, column=0, columnspan= 1)
        self.country.grid(row = 0, column=1, columnspan= 1)
        

        self.btnTimeAllCases.grid(row = 3, column=0, columnspan= 1)
        button1_ttp = CreateToolTip(self.btnTimeAllCases, "Displays all the total cases of all the countries")

        self.btnTimeDeath.grid(row = 3, column=1, columnspan= 1)
        button1_ttp = CreateToolTip(self.TimeDeath, "Displays the total deaths of all the countries")

        self.btnSelectedNewCases.grid(row = 3, column=2, columnspan= 1)
        button1_ttp = CreateToolTip(self.btnSelectedNewCases, "Displays a timeline of the new total cases of the selected country")

        self.btnSelectedNewDeaths.grid(row = 4, column=0, columnspan= 1)
        button1_ttp = CreateToolTip(self.btnSelectedNewDeaths, "Reload the orignal file")

        self.btnUpdateRecord.grid(row = 4, column=1, columnspan= 1)
        button1_ttp = CreateToolTip(self.btnUpdateRecord, "Update records")

        self.btnClear.grid(row = 4, column=2, columnspan= 1)
        button1_ttp = CreateToolTip(self.btnClear, "Clears the display")

        self.scr.grid(row = 5, column=0, columnspan= 3)

    #create a function to display all the cases in a bar graph
    def TimeAllCases(self):
        self.scr.delete('1.0', tk.END)

        with open('data.csv','r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                x.append(int(row[0]))
                y.append(int(row[1]))

        plt.figure(figsize - (20, 10))
        plt.bar(x = 'COUNTRY_NAME',
                hight = 'TotalCase')
        plt.title('All cases from all countries')
        plt.legend()
        plt.show()

    #create a function to Display all the deaths in a bar graph
    def TimeDeath(self):
        self.scr.delete('1.0', tk.END)

        with open('data.csv','r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                x.append(int(row[0]))
                y.append(int(row[1]))

        plt.figure(figsize - (20, 10))
        plt.bar(x = 'COUNTRY_NAME',
                hight = 'TotalDeath')
        plt.title('All cases from all countries')
        plt.legend()
        plt.show()

    #create a function to display a time graph of the total new cases of the selected country
    def selectedNewTotalCases(self):
        with open('data.csv','r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                x.append(int(row[0]))
                y.append(int(row[1]))
        x, y = np.loadtxt('data.csv', delimiter=',', unpack=True)

        plt.xlabel('Date_epicrv')
        plt.ylabel('TotalCase')
        plt.legend()
        plt.show()

    #create a function to load the original file
    def restoreDB(self):
        self.scr.delete('1.0', tk.END)

        self.cluster = MongoClient("mongodb+srv://admin:admin@who-covid-19.egabt.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")

        self.db = self.cluster["WHO-COVID-19"]
        self.collection = self.db["COVID-19-CASES_db"]

        self.x = self.collection.delete_many({})

        with open('data.json') as self.f:
            self.file_data = json.load(self.f)

        self.collection.insert_many(self.file_data)

        self.scr.insert(tk.INSERT, "Database Restored Succesfully")

    #create a function to display a time graph of the total new deaths of the selected country
    def btnSelectedNewDeaths(self):
        self.scr.delete('1.0', tk.END)
        with open('data.csv','r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                x.append(int(row[0]))
                y.append(int(row[1]))
        x, y = np.loadtxt('data.csv', delimiter=',', unpack=True)

        plt.xlabel('Date_epicrv')
        plt.ylabel('TotalDeath')
        plt.legend()
        plt.show()

    #create a function to clear the display 
    def clear(self):
        self.scr.delete('1.0', tk.END)


root = tk.Tk()
app = Application(master=root)
app.mainloop()

root.mainloop()