import random
# ex-1
'''
Write a program that asks the user how many dice to roll.
The program rolls all the dice once and prints out the sum of the
numbers. Use a for loop.
'''
'''
num_of_dice=int(input('how many dice you want to roll?: '))
dice_sum=0
for i in range (num_of_dice):
    dice=random.randint(1,6)
    print(str(dice), end='')
    dice_sum=dice_sum+dice
print(f'\n the sum of the dice is: {dice_sum}')
'''
# ex-2
'''
Write a program that asks the user to enter numbers until they 
input an empty string to quit. At the end, the program prints out 
the five greatest numbers sorted in descending order. Hint: 
You can reverse the order of sorted list items by using the sort 
method with the reverse=True argument.
'''
'''
numbers=[]
prompt= 'give me a number:'
num= input(prompt)
while num!='':
    numbers.append(float(num))
    num=input(prompt)
numbers.sort()
numbers.sort(reverse=True)
print(numbers)
print(numbers[0:5])
'''


'''
ex-3
Write a program that asks the user for an integer and tells if the number 
is a prime number. Prime numbers are number that are only divisible by one 
or the number itself.
For example, 13 is a prime number as it can only be divided by 1 or 13 so 
that the result is an integer.
On the other hand, 21 is not a prime number as it is divisible by 3 and 7.
'''
'''
import math
number=int(input('give a number to check:'))
for i in range(2, int(math.sqrt(number)+1)):
    if number % i == 0:
        print(f'this number is divisible by also {i}')
        break
else:
    print('this is a prime number')
'''
'''
ex-4
Write a program that asks the user to enter the names of five cities one by
 on (use a for loop for reading the names) and stores them into a list structure.
  Finally, the program prints out the names of the cities one by one, one city per
   line, in the same order they were read as input. Use a for loop for asking 
   the names and a for/in loop to iterate through the list.
'''
'''
cities = []
for i in range(5):
    city = input('type a city name:')
    cities.append(city)
for city in cities:
    print(city)
'''




















