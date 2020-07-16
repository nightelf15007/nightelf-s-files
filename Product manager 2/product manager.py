import mysql.connector
from matplotlib import pyplot as plt
import pandas as pd
from pandas import DataFrame
from pandastable import Table

def get_db_data():
    cols = ["id", "Product_Name", "Category", "Availible_Stock"]

    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "admin",
    database = "productsdb",
    )

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()
    mydb.close()

    return cols, data

def display_plot():
    df_cols, db_data = get_db_data()
    data_df = pd.DataFrame(db_data, columns=df_cols).set_index("id")
    
    data_df.plot(kind='bar',x='Product_Name',y='Availible_Stock')

    plt.show()  

display_plot()

#Fun Fact: Charles W. Bachman designed the Integrated Database System in 1960
