import csv
import pandas as pd
import mysql.connector
from mysql.connector import errorcode

#read csv file 
MRTS_DF = pd.read_csv('MRTS_Sales_2010-2015_Hallana.csv')
print(MRTS_DF)

#connect to MySQL
try:
    cnx = mysql.connector.connect(
        user='root',
        password='myluke',
        host='127.0.0.1',
        database='MRTS_sales',
        auth_plugin='mysql_native_password')

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

else:
    cursor = cnx.cursor()

    queryCreate = ("CREATE TABLE MRTS_Business (NAICS_Code VARCHAR(50) NULL,Business_kind VARCHAR(150) NULL,Year INT NULL,Jan INT NULL,Feb INT NULL,Mar INT NULL,Apr INT NULL,May INT NULL,Jun INT NULL,Jul INT NULL,Aug INT NULL,Sep INT NULL,Oct INT NULL,Nov INT NULL,Decm INT NULL,Total INT NULL);")
    cursor.execute(queryCreate)

   # Insert Dataframe into MySQLr:
    queryInsert = ("INSERT INTO MRTS_Business (NAICS_Code, Business_kind, Year, Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Decm,Total) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

    for index, row in MRTS_DF.iterrows():
       cursor.execute(queryInsert, (row.NAICS_Code, row.Business_Kind, row.Year, row.Jan, row.Feb, 
       row.Mar, row.Apr, row.May, row.Jun, row.Jul, row.Aug, row.Sep, row.Oct,row.Nov, row.Decm, row.TOTAL))
    cnx.commit()
    cursor.close()
   
   