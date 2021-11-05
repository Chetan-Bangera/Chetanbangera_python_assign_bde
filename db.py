import psycopg2

#Connection builder
con= psycopg2.connect(
    host="localhost",
    database="as1_db",
    user="postgres",
    password="Chetanrocks@1",
    port=5433)

#cursor connection
cur=con.cursor()
cur.execute("SELECT test_sch.chetanbangera_return_dep_people('556cde3c7369641238194600')")

#Fetching all the data
rows=cur.fetchall()

#Printing all the data
for i in rows:
    print(f"{i[0]},")

#Closing the connection
con.close()


##Sorry the task 2 was not completed as i dont know much about json file and plus the time constraints was very less
##Thank you