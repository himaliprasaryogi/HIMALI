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

