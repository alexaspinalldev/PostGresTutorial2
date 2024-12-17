import psycopg2

# Connect to the DB
connection = psycopg2.connect(database="chinook")

# Create a cursor object (a list) of the connection
cursor = connection.cursor()

# Queries
# cursor.execute('SELECT * FROM "Artist"')
# cursor.execute('SELECT "Name" FROM "Artist"')
cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', ["51"])




# Set up a method to get the results from our cursor
results = cursor.fetchall()
# results = cursor.fetchone()

connection.close()

# Print results
for result in results:
    print(result)