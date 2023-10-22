import random
'''
ex-1
Write a function that returns a random dice roll between 1 and 6.
The function should not have any parameters. Write a main program
that rolls the dice until the result is 6. The main program should
print out the result of each roll.
'''
'''



def roll_dice():
    return random.randint(1,6)


rolls = 0
while True:
    result = roll_dice()
    rolls += 1
    print(f'{rolls}: {result}')
    if result == 6:
        break

'''
'''
ex-2
Modify the function above so that it gets the number of sides on the dice
as a parameter. With the modified function you can for example roll a 21-sided
role-playing dice. The difference to the last exercise is that the dice rolling
in the main program continues until the program gets the maximum number on the dice,
which is asked from the user at the beginning.
'''

'''
def roll_dice(num_sides):
    return random.randint(1,num_sides)


num_sides= int(input('enter number of sides on the dice: '))
rolls = 0
while True:

    result = roll_dice(num_sides)
    rolls += 1
    print(f'{rolls} : {result}')
    if result == num_sides:
        break

'''
'''
ex-3
Write a function that gets the quantity of gasoline in American gallons and 
returns the number converted to litres. Write a main program that asks for
a volume in gallons from the user and converts the value to liters. 
The conversion must be done by using the function. Conversions continue 
until the user inputs a negative value.
'''

'''
def gallons_2_litre(gallons):
    litre = gallons * 3.785
    return litre


while True:
    gallons= float(input('enter gasoline quantity in gallons or negative value to exit:'))
    if gallons < 0:
        break
    litre = gallons_2_litre(gallons)
    print(f'{gallons} gallons equals  to {litre} litres')
'''

'''
ex-4
Write a function that gets a list of integers as a parameter. 
The function returns the sum of all the numbers in the list. 
For testing, write a main program where you create a list, call 
the function, and print out the value it returned.
'''
'''
def sum(l):
    s=0
    for e in l:
        s += e
    return s

numberlist =[]
for n in range(10):
    numberlist.append(random.randint(1,10))
print('The list is: '+ str(numberlist))
print('The sum is '+ str(sum(numberlist)))
'''
'''
ex-5
Write a function that gets a list of integers as a parameter. 
The function returns a second list that is otherwise the same
as the original list except that all uneven numbers have been removed.
For testing, write a main program where you create a list, call the function,
and then print out both the original as well as the cut-down list.
'''

'''
def even_num(list_no):
    result_list = []
    for i in range(len(list_no)):
        if list_no[i] % 2 == 0:
            result_list.append(list_no[i])
    return result_list



def print_list(num, list_no):
    print(num, end=" ")
    for i in range(len(list_no)):
        print(list_no[i], end=" ")



numberlist= []
for n in range(10):
    numberlist.append(random.randint(1, 99))
print()
print_list('here is the original list:', numberlist)
cutdown_list = even_num(numberlist)
print_list('\ncut down list is: ', cutdown_list)
print()

'''



'''

ex-6
Write a function that receives two parameters: the diameter of a round pizza 
in centimeters and the price of the pizza in euros. The function calculates 
and returns the unit price of the pizza per square meter. The main program 
asks the user to enter the diameter and price of two pizzas and tells the user 
which pizza provides better value for money (which of them has a lower unit price).
You must use the function you wrote for calculating the unit prices.
'''
'''
import math


def cal_pizza(dia, price):
    return price/(math.pi *(dia/2) ** 2)


p1_diameter= float(input('give me the diameter of the 1st pizza(in cm):'))
p1_price = float(input('give the price of the 1st pizza (in euros):'))
p2_diameter= float(input('give me the diameter of the 2nd pizza(in cm):'))
p2_price = float(input('give the price of the 1st pizza (in euros):'))

if cal_pizza(p1_diameter, p1_price) < cal_pizza(p2_diameter, p2_price):
    print('the 1st pizza is a better option. grab it now!')
else:
    print('the 2nd pizza is way better. take it!')
'''






