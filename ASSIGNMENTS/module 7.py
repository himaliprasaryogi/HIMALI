'''
ex-1
Write a program that asks the user for a number of a month and then prints out
the corresponding season (spring, summer, autumn, winter). Save the seasons as
strings into a tuple in your program. We can define each season to last three months,
 December being the first month of winter.
'''
'''
month = int(input("enter month number: "))
season = ("spring", "summer", "autumn", "winter")
if month >= 3 and month <= 5:
    print(f"the season is {season[0]}")
elif month >= 6 and month <= 8:
    print(f"the season is {season[1]}")
elif month >= 9 and month <= 11:
    print(f"the season is {season[2]}")
elif month == 1 or month == 2 or month == 12:
    print(f"the season is {season[3]}")
else:
    print("invalid month")

'''

'''
ex-2
Write a program that asks the user to enter names until he/she enters an empty 
string. After each name is read the program either prints out New name or Existing
name depending on whether the name was entered for the first time. Finally, 
the program lists out the input names one by one, one below another in any order.
Use the set data structure to store the names.
'''
'''
user_names = set()
while True:
    name = str(input("enter your name: "))
    if name != "":
        if name in user_names:
            print(f"{name} existing name in the list")

        else:
            user_names.add(name)
            print(f"{name} new name to the list")

    else:

        print("all the names are: ")
        for i in user_names:
            print(i)
        break
'''

'''
ex-3
Write a program for fetching and storing airport data. The program asks the 
user if they want to enter a new airport, fetch the information of an 
existing airport or quit. If the user chooses to enter a new airport, 
the program asks the user to enter the ICAO code and name of the airport.
If the user chooses to fetch airport information instead, the program asks for 
the ICAO code of the airport and prints out the corresponding name. If the user 
chooses to quit, the program execution ends. The user can choose a new option as 
many times they want until they choose to quit. (The ICAO code is an identifier that
is unique to each airport. For example, the ICAO code of Helsinki-Vantaa Airport 
is EFHK. You can easily find the ICAO codes of different airports online.)
'''

'''
def options():
    print("1. enter airport: ")
    print("2. enter airport code: ")
    print("3. quit")


airports = {}

while True:
    options()
    command = input("enter your query: ")
    if command == "1":
        airport_name = input("enter name of the airport: ").title()
        airport_name += " airport "
        airport_code = input("enter ICAO code of the airport: ").upper()

        airports[airport_code] = airport_name
        print(f"{airport_name} ICAO code {airport_code} added")

    elif command == "2":
        ICAO_code = input("enter ICAO code for the airport name ").upper()

        if ICAO_code in airports:
            print(f" airport {ICAO_code} is {airports[ICAO_code]}")

        else:
            print(f"airport {ICAO_code} doesn't exist.")

    elif command == "3":
        print(" goodbye ")
        break
'''