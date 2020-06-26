from tkinter import *  #import everything for the gui
import math #this is a calculator after all

class calc: #classes look good ;)

    def replace(self): #make sure the thing doesnt break
        self.expression = self.e.get() 
        self.newtext=self.expression.replace('/','/') 
        self.newtext=self.newtext.replace('x','*') 

    def equal(self): #makes the equal button work
        self.replace() 
        try: 
            self.value= eval(self.newtext) 
        except SyntaxError or NameError: 
            self.e.delete(0,END) 
            self.e.insert(0,'error') 
        else: 
            self.e.delete(0,END) 
            self.e.insert(0,self.value) 

    def squareroot(self): #makes the √x button work
        self.replace() 
        try: 
            self.value= eval(self.newtext) 
        except SyntaxError or NameError: 
            self.e.delete(0,END) 
            self.e.insert(0,'error') 
        else:
            
            self.sqrtval=math.sqrt(self.value) 
            self.e.delete(0,END) 
            self.e.insert(0,self.sqrtval) 

    def square(self): #makes the x² button work
        self.replace()
        self.value= eval(self.newtext)
        self.sqval=math.pow(self.value,2) 
        self.e.delete(0,END) 
        self.e.insert(0,self.sqval) 

    def clearall(self): # makes the CE and C button work
            self.e.delete(0,END) 

    def clear(self): #makes the ⌫ button work
        self.txt=self.e.get()[:-1] 
        self.e.delete(0,END) 
        self.e.insert(0,self.txt) 

    def action(self,argi): #makes all the buttons work
            self.e.insert(END,argi) 

    def __init__(self,calc): #finally making the calculator
        calc.title('Calulator') 
        calc.geometry() 
        self.e = Entry(calc)
        self.e.grid(row=0,column=0,columnspan=4, rowspan=1) 
        self.e.focus_set()
        #all the buttons -_-
        Button(calc,text='CE',width=11,height=2, 
            fg="black", bg="light grey", 
            command=lambda:self.clearall()).grid(row=1, column=0)
        Button(calc,text='C',width=11,height=2, 
            fg="black",bg="light grey", 
            command=lambda:self.clearall()).grid(row=1, column=1)
        Button(calc,text='⌫',width=23,height=2, 
            fg="black",bg="light grey", 
            command=lambda:self.clear1()).grid(row=1, column=2, columnspan=2)
        Button(calc,text="x²",width=11,height=2, 
            fg="black",bg="light grey", 
            command=lambda:self.square()).grid(row=2, column=1)
        Button(calc,text="%",width=11,height=2, 
            fg="black",bg="light grey", 
            command=lambda:self.action('%')).grid(row=2, column=0)
        Button(calc,text="√x",width=11,height=2, 
            fg="black",bg="light grey", 
            command=lambda:self.squareroot()).grid(row=2, column=2)
        Button(calc,text="÷",width=11,height=2, 
            fg="black",bg="light grey", 
            command=lambda:self.action('/')).grid(row=2, column=3)
        Button(calc,text="7",width=11,height=2, 
            fg="black",bg="white", 
            command=lambda:self.action(7)).grid(row=3, column=0) 
        Button(calc,text="8",width=11,height=2, 
            fg="black",bg="white", 
            command=lambda:self.action(8)).grid(row=3, column=1) 
        Button(calc,text="9",width=11,height=2, 
            fg="black",bg="white", 
            command=lambda:self.action(9)).grid(row=3, column=2)
        Button(calc,text="x",width=11,height=2, 
            fg="black",bg="light grey", 
            command=lambda:self.action('x')).grid(row=3, column=3)
        Button(calc,text="4",width=11,height=2, 
            fg="black",bg="white", 
            command=lambda:self.action(4)).grid(row=4, column=0) 
        Button(calc,text="5",width=11,height=2, 
            fg="black",bg="white", 
            command=lambda:self.action(5)).grid(row=4, column=1) 
        Button(calc,text="6",width=11,height=2, 
            fg="black",bg="white", 
            command=lambda:self.action(6)).grid(row=4, column=2)
        Button(calc,text="-",width=11,height=2, 
            fg="black",bg="light grey", 
            command=lambda:self.action('-')).grid(row=4, column=3)
        Button(calc,text="1",width=11,height=2, 
            fg="black",bg="white", 
            command=lambda:self.action(1)).grid(row=5, column=0) 
        Button(calc,text="2",width=11,height=2, 
            fg="black",bg="white", 
            command=lambda:self.action(2)).grid(row=5, column=1) 
        Button(calc,text="3",width=11,height=2, 
            fg="black",bg="white", 
            command=lambda:self.action(3)).grid(row=5, column=2)
        Button(calc,text="+",width=11,height=2, 
            fg="black",bg="light grey", 
            command=lambda:self.action('+')).grid(row=5, column=3)
        Button(calc,text="0",width=11,height=2, 
            fg="black",bg="white", 
            command=lambda:self.action(0)).grid(row=6, column=0) 
        Button(calc,text=",",width=11,height=2, 
            fg="black",bg="white", 
            command=lambda:self.action('.')).grid(row=6, column=1)
        Button(calc,text="=",width=23,height=2, 
            fg="black",bg="light green", 
            command=lambda:self.equal()).grid(row=6, column=2, columnspan=2)
         
root = Tk() #create window
obj=calc(root) #puts the thingys on the thingy
root.mainloop() #keeps window open

#Fun fact: The first mechanical calculator was invented by Blaise Pascal (one of my favourite mathematicians)