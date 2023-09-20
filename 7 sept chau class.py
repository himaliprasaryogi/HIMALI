# listname.pop(index)
# listname.remove(value name)
# function range
# range(start_no, stop_no)
# range(start_no, stop no, step)
'''
numbers= list(range(1,5))
print(numbers)
name_list =['bishnu','olga','himali','rahul']
print(name_list[4])
'''
# for loop
'''
name=[]
name=input('what is your name? ')
index = 0
while name != '' and index < len(name):
    print(name[index])
    # index +=1 or index=index+1 is same
    index +=1
    '''
# printing out all the characters of the user '' input, using for:
'''
name=input('what is your name?')
for character in name:
    print(character) 
    # instead of character we can use i as well helper variable
    '''
'''
for number in range(1,10):
    print(number)
    '''
'''
for number in range(1,10,2):
    print(number)
# this will print by jumping 2 steps. so (start no. end no. and jumping step)
'''

# extend a list with another one
'''
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list1.extend(list2)
print(list1)
'''
# check the index number of an item in the list
# print(list1.index(2))
'''
# sort the list of
list_name=['chau','steven','andy']
list_name.sort()
print(list_name)
list_number=[1,4,6,8]
list_number.sort()
print(list_number)
# check the length of a list
print(len(list_name))
'''
# exercise 1
# write a program that asks user how many dice to roll. the program rolls all the dice
# once and prints out the sum of the numbers. use a for loop
'''
import random
number_of_dice = int(input('how many dices do you want to roll a ?'))
dice_sum = 0
for i in range(number_of_dice):
    dice = random.randint(1,6)
    print(str(dice), end = '')
    dice_sum = dice_sum + dice
print(f'\n the sum of the dice is: {dice_sum}')
'''
'''
Exercise 2
Write a program that asks the user to enter numbers until they input an empty
string to quit. At the end, the program prints out the five greatest numbers
sorted in descending order. Hint: You can reverse the order of sorted list
items by using the sort method with the reverse=True agruement.True
'''
'''
numbers = []
prompt ='Give me a number:'
num = input(prompt)
while num !='':
    numbers.append(float(num))
    num =input(prompt)
numbers.sort()
print(numbers)
numbers.sort(reverse = True)
print(numbers)
print(numbers[0:5])
'''
# Exercise 3
# check whether a number is prime number
'''
import math
number=int(input('give a number to check: '))
for i in range (2, int(math.sqrt(number)+1)):
    if number % i == 0:
        print(f'this number is divisible by {i}')
        break
else:
    print('this is a prime number')
'''
# Exercise 4
# cities
cities = []
for i in range(5):
    city = input('type a city name: ')
    cities.append(city)
for city in cities:
    print(city)





