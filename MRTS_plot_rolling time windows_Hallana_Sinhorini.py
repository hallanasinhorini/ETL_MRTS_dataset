import mysql.connector
from mysql.connector import errorcode
import matplotlib.pyplot as plt

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
    # Create a cursor
    cursor = cnx.cursor()

    # uery that will retrieve the sales or revenues for 2010 for bookstores (NAICS_Code 451211), 
    # sporting goods stores (NAICS_Code 45111), and hobbies, toys, and 
    # games stores (NAICS_Code 45112) using data from the Monthly Retail Trade Survey (MRTS)

    query = """
    SELECT Year, NAICS_Code, 
    SUM(Jan) AS "January", 
    SUM(Feb) AS "February", 
    SUM(Mar) AS "March", 
    SUM(Apr) AS "April", 
    SUM(May) AS "May", 
    SUM(Jun) AS "June", 
    SUM(Jul) AS "July", 
    SUM(Aug) AS "August", 
    SUM(Sep) AS "September", 
    SUM(Oct) AS "October", 
    SUM(Nov) AS "November", 
    SUM(Decm) AS "December", 
    SUM(TOTAL) AS "Total Sales"
    FROM MRTS_Business
    WHERE NAICS_Code IN (451211, 45111, 45112)
    AND Year BETWEEN 2010 AND 2015
    GROUP BY Year, NAICS_Code
    ORDER BY Year, NAICS_Code
    """

    # Execute the query
    cursor.execute(query)

    # Retrieve the results
    results = cursor.fetchall()

# Close the cursor and connection
cursor.close()
cnx.close()

# Extract the NAICS code and total sales values from the results
naics_codes = [result[1] for result in results]
totals = [result[-1] for result in results]

# Set the x-axis values to be the years
x_values = range(len(results))

# Set the y-axis values to be the totals
y_values = totals

# Set the labels for the x-axis
x_labels = [result[0] for result in results]

# Create the line chart
plt.plot(x_values, y_values)

# Set the x-axis tick labels
plt.xticks(x_values, x_labels, rotation=45)

# Add a title and axis labels
plt.title('Total Sales by NAICS Code for 2010-2015')
plt.xlabel('Year')
plt.ylabel('Total Sales')

# Show the plot
plt.show()
