# Working with relational databases in Python
# In this chapter, you'll learn how to extract meaningful data from relational databases, an essential skill for any data scientist. You will learn about relational models, how to create SQL queries, how to filter and order your SQL records, and how to perform advanced queries by joining database tables.


# Creating a database engine
# Here, you're going to fire up your very first SQL engine. You'll create an engine to connect to the SQLite database 'Chinook.sqlite', which is in your working directory. Remember that to create an engine to connect to 'Northwind.sqlite', Hugo executed the command

# engine = create_engine('sqlite:///Northwind.sqlite')
# Here, 'sqlite:///Northwind.sqlite' is called the connection string to the SQLite database Northwind.sqlite. A little bit of background on the Chinook database: the Chinook database contains information about a semi-fictional digital media store in which media data is real and customer, employee and sales data has been manually created.

# Why the name Chinook, you ask? According to their website,

# The name of this sample database was based on the Northwind database. Chinooks are winds in the interior West of North America, where the Canadian Prairies and Great Plains meet various mountain ranges. Chinooks are most prevalent over southern Alberta in Canada. Chinook is a good name choice for a database that intends to be an alternative to Northwind.

# Import necessary module
from sqlalchemy import create_engine

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')






# In this exercise, you'll once again create an engine to connect to 'Chinook.sqlite'. Before you can get any data out of the database, however, you'll need to know what tables it contains!

# To this end, you'll save the table names to a list using the method table_names() on the engine and then you will print the list.


# Import necessary module
from sqlalchemy import create_engine

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Save the table names to a list: table_names
table_names = engine.table_names()

# Print the table names to the shell
print(table_names)



# Customizing the Hello World of SQL Queries
# Congratulations on executing your first SQL query! Now you're going to figure out how to customize your query in order to:

# Select specified columns from a table;
# Select a specified number of rows;
# Import column names from the database table.
# Recall that Hugo performed a very similar query customization in the video:

# engine = create_engine('sqlite:///Northwind.sqlite')

# with engine.connect() as con:
#     rs = con.execute("SELECT OrderID, OrderDate, ShipName FROM Orders")
#     df = pd.DataFrame(rs.fetchmany(size=5))
#     df.columns = rs.keys()


# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT LastName, Title FROM Employee")
    df = pd.DataFrame(rs.fetchmany(size = 3))
    df.columns = rs.keys()

# Print the length of the DataFrame df
print(len(df))

# Print the head of the DataFrame df
print(df.head()) 



# Filtering your database records using SQL's WHERE
# You can now execute a basic SQL query to select records from any table in your database and you can also perform simple query customizations to select particular columns and numbers of rows.

# There are a couple more standard SQL query chops that will aid you in your journey to becoming an SQL ninja.

# Let's say, for example that you wanted to get all records from the Customer table of the Chinook database for which the Country is 'Canada'. You can do this very easily in SQL using a SELECT statement followed by a WHERE clause as follows:

# SELECT * FROM Customer WHERE Country = 'Canada'
# In fact, you can filter any SELECT statement by any condition using a WHERE clause. This is called filtering your records.

# In this interactive exercise, you'll select all records of the Employee table for which 'EmployeeId' is greater than or equal to 6.

# Packages are already imported as follows:

# import pandas as pd
# from sqlalchemy import create_engine



# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('SELECT * FROM Employee WHERE EmployeeId >= 6')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print the head of the DataFrame df
print(df.head())



# Ordering your SQL records with ORDER BY
# You can also order your SQL query results. For example, if you wanted to get all records from the Customer table of the Chinook database and order them in increasing order by the column SupportRepId, you could do so with the following query:

# "SELECT * FROM Customer ORDER BY SupportRepId"
# In fact, you can order any SELECT statement by any column.

# In this interactive exercise, you'll select all records of the Employee table and order them in increasing order by the column BirthDate.

# Packages are already imported as follows:

# import pandas as pd
# from sqlalchemy import create_engine
# Get querying!


# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine in context manager
with engine.connect() as con:
    rs = con.execute('SELECT * FROM Employee ORDER BY BirthDate')
    df = pd.DataFrame(rs.fetchall())

    # Set the DataFrame's column names
    df.columns = rs.keys()


# Print head of DataFrame
print(df.head())



#  Pandas and The Hello World of SQL Queries!
# Here, you'll take advantage of the power of pandas to write the results of your SQL query to a DataFrame in one swift line of Python code!

# You'll first import pandas and create the SQLite 'Chinook.sqlite' engine. Then you'll query the database to select all records from the Album table.

# Recall that to select all records from the Orders table in the Northwind database, Hugo executed the following command:

# df = pd.read_sql_query("SELECT * FROM Orders", engine)



# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM Album', engine)

# Print head of DataFrame
print(df.head())

# Open engine in context manager and store query result in df1
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Album")
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()

# Confirm that both methods yield the same result
print(df.equals(df1))





# Pandas for more complex querying
# Here, you'll become more familiar with the pandas function read_sql_query() by using it to execute a more complex query: a SELECT statement followed by both a WHERE clause AND an ORDER BY clause.

# You'll build a DataFrame that contains the rows of the Employee table for which the EmployeeId is greater than or equal to 6 and you'll order these entries by BirthDate.



# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM Employee WHERE EmployeeId >=6 ORDER BY BirthDate', engine)

# Print head of DataFrame
print(df.head())




# The power of SQL lies in relationships between tables: INNER JOIN
# Here, you'll perform your first INNER JOIN! You'll be working with your favourite SQLite database, Chinook.sqlite. For each record in the Album table, you'll extract the Title along with the Name of the Artist. The latter will come from the Artist table and so you will need to INNER JOIN these two tables on the ArtistID column of both.

# Recall that to INNER JOIN the Orders and Customers tables from the Northwind database, Hugo executed the following SQL query:

# "SELECT OrderID, CompanyName FROM Orders INNER JOIN Customers on Orders.CustomerID = Customers.CustomerID"
# The following code has already been executed to import the necessary packages and to create the engine:

# import pandas as pd
# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///Chinook.sqlite')


# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('SELECT Title, Name FROM Album INNER JOIN Artist on Album.ArtistID=Artist.ArtistID')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print head of DataFrame df
print(df.head())





# Filtering your INNER JOIN
# Congrats on performing your first INNER JOIN! You're now going to finish this chapter with one final exercise in which you perform an INNER JOIN and filter the result using a WHERE clause.

# Recall that to INNER JOIN the Orders and Customers tables from the Northwind database, Hugo executed the following SQL query:

# "SELECT OrderID, CompanyName FROM Orders INNER JOIN Customers on Orders.CustomerID = Customers.CustomerID"
# The following code has already been executed to import the necessary packages and to create the engine:

# import pandas as pd
# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///Chinook.sqlite')


# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackId WHERE Milliseconds < 250000',engine)

# Print head of DataFrame
print(df.head())



