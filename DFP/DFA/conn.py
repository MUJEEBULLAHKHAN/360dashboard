# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
host ="localhost",
user ="root",
passwd ="SHERAAZ_KHAN",
database = "db1"
)

# preparing a cursor object
cursorObject = dataBase.cursor()

query1 = "Select count (*) from tamam_sq_qa.aspnetusers"
query2 = "Select count (*) from tamam_sq_qa.clientvehicle"
query3 = "Select count (*) from tamam_sq_qa.clientdata"
query4 = "Select count (*) from tamam_sq_qa.workshopquotes"
query5 = "Select count (*) from tamam_sq_qa.partsuppliers"
query6 = "Select count (*) from tamam_sq_qa.workshops"
query7 = "Select vehiclemake, count(*) from tamam_sq_qa.clientvehicle group by vehiclemake with rollup order by 2 desc"
# cursorObject.execute(query1)
# cursorObject.execute(query2)
# cursorObject.execute(query3)
# cursorObject.execute(query4)
# cursorObject.execute(query5)
# cursorObject.execute(query6)
# cursorObject.execute(query7)
# r1 = cursorObject.fetchall()
# r2 = cursorObject.fetchall()
# r3 = cursorObject.fetchall()
# r4 = cursorObject.fetchall()
# r5 = cursorObject.fetchall()
# r6 = cursorObject.fetchall()
# r7 = cursorObject.fetchall()

# disconnecting from server
dataBase.close()