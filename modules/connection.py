import mysql.connector
from mysql.connector import errorcode

def sql_connection():
    """[Make SQL data-base connection]

    Returns:
        [Object]: [Object of database connection -- mysql.connector.connect]
    """
    try:
        mydb = mysql.connector.connect(
        host="sql262.main-hosting.eu",
        user="u340495852_plasma_data",
        password="Plasma_data@#123",
        database = "u340495852_plasma_data"
    )
        #print("Plazma Connect - Database is connected")
        print("Data_base connected")
        return mydb

    except mysql.connector.Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                return("Somthing wrong with user name and passward")
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
                return("Databases not exist")
        else:
                return(e)

#sql_connection()



                