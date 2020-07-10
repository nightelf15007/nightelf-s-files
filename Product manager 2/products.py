#import everything
import numpy as np
import pandas as pd
#put the stuff into a tabel
products = {
    "Chips": ["Simba", "Lays", ""],
    "Cooldrinks": ["Coke", "Fanta", ""],
    "Chocolates": ["Cadbury", "Tex", ""],
    "Pies": ["Pepper Steak", "Chicken", ""],
    "Fruit": ["Pear", "Apple", "Orange"],
    "Cupcakes": ["vanilla", "chocolate", ""],
    "Veggies": ["spinach", "cabbage", ""]}

#put the table into a dataframe
df = pd.DataFrame(products)
    
print (df)  
 
#Fun Fact: Charles W. Bachman designed the Integrated Database System in 1960