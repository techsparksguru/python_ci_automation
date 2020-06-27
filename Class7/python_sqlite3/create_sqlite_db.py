from utils.helper import *

conn_instance = Connection()

# Creating database connection with custom .db file
conn_instance.create_connection(dbfile='db/sqlite3.db')

# Check the connection establishment
print(conn_instance)

# Close the connection
conn_instance.close_connection()