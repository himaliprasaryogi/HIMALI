'''
ex-1
Write a program that asks the user to enter the ICAO code of an airport.
The program fetches and prints out the corresponding airport name and
location (town) from the airport database used on this course.
The ICAO codes are stored in the ident column of the airport table.
'''
'''
import mysql.connector
from geopy.distance import geodesic as GD

connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='flight_game11 ',
        user='root',
        password='Yogibe@r11'
)

cus = connection.cursor()


Icao = input("Enter ICAO Code: ")

sql = "select name, municipality from airport where ident = '"+Icao+"'"
cus.execute(sql)
Info = cus.fetchall()
for i,j in Info:
    Name = i
    if j != "":
            Town = j
    else:
            Town = "[Not Available]"

print(f"The name of Airport with ICAO Code \'{Icao}\' is {Name} and it is located in {Town}")
'''
'''
ex-2
Write a program that asks the user to enter the area code (for example FI) 
and prints out the airports located in that country ordered by airport type.
 For example, Finland has 65 small airports, 15 helicopter airports and so on.
 '''
'''
import mysql.connector
from tabulate import tabulate


connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='flight_game11 ',
        user='root',
        password='Yogibe@r11'
)

cus = connection.cursor()

Area = input("Enter Area Code: ")

sql = "select name, type from airport where iso_country = '"+Area+"' order by type desc;"
cus.execute(sql)
Info_Area = cus.fetchall()

print(tabulate((Info_Area), headers = ["Name","Type"]))
'''
'''
ex-3
Write a program that asks the user to enter the ICAO codes of two airports.
The program prints out the distance between the two airports in kilometers.
The calculation is based on the airport coordinates fetched from the database.
Calculate the distance using the geopy library: 
https://geopy.readthedocs.io/en/stable/. Install the library by selecting 
View / Tool Windows / Python Packages in your PyCharm IDE, write geopy 
into the search field and finish the installation.
'''
'''
import mysql.connector
from geopy.distance import geodesic as GD
from tabulate import tabulate


connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='flight_game11 ',
        user='root',
        password='Yogibe@r11'
)

cus = connection.cursor()
def distance_airport(currentID, destinationID):
    sql = "SELECT latitude_deg, longitude_deg FROM airport"
    sql += " WHERE ident = '" + currentID + "' OR ident = '" + destinationID + "'"
    print(sql)
    cus.execute(sql)
    row = cus.fetchall()
    print(row)
    if row == 0:
        print("Bye Bye")
    else:
        location = []
        for lat, long in row:
            location.append(lat)
            location.append(long)
        dist = GD((location[0], location[1]), (location[2], location[3]))
        disArr = (str(dist)).split()
        dis = float(disArr[0])
        distance = int(dis)
        return distance


first_ICAO = input("first ICAO Code: ")
second_ICAO = input("second ICAO Code: ")
print(f"distance from first_ICAO to second_ICAO is  {distance_airport(first_ICAO,second_ICAO)}km")
'''