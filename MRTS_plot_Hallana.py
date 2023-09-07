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

    # Define the query
    query = """
    SELECT Year, NAICS_Code, 
    Jan AS "January", 
    Feb AS "February", 
    Mar AS "March", 
    Apr AS "April", 
    May AS "May", 
    Jun AS "June", 
    Jul AS "July", 
    Aug AS "August", 
    Sep AS "September", 
    Oct AS "October", 
    Nov AS "November", 
    Decm AS "December", 
    TOTAL
    FROM MRTS_Business
    WHERE NAICS_Code IN (44811, 44812)
    ORDER BY Year;
    """

    # Execute the query
    cursor.execute(query)

    # Retrieve the results
    results = cursor.fetchall()

# Close the cursor and connection
cursor.close()
cnx.close()

# Extract the year, month, and total values from the results
years = [result[0] for result in results]
months = [result[2] for result in results]
totals = [result[-1] for result in results]

# Set the x-axis values to be the months
x_values = range(len(months))

# Set the y-axis values to be the totals
y_values = totals

# Set the labels for the x-axis
x_labels = months

# Create the bar chart
plt.bar(x_values, y_values, align='center')

# Set the x-axis tick labels
plt.xticks(x_values, x_labels)

# Add a title and axis labels
plt.title('TOTAL by Month and Year')
plt.xlabel('Month')
plt.ylabel('TOTAL')

# Show the plot
plt.show()
