from utils.helper import *

conn_instance = Connection()

# Creating database connection of type inmemory
conn_instance.create_connection(dbtype='inmemory')

# Check the connection establishment
print(conn_instance)

# Close the connection
conn_instance.close_connection()