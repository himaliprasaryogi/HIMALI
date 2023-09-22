# module 6 exercises
# ex 1
import random

'''
def rolling_dice():
    return random.randint(1,6)

while True:
    dice=rolling_dice()
    print(f'the result of this roll is:{dice}')
    if dice==6:
        break
   '''
# ex 2
'''
def rolling_dice(num_sides):
    return random.randint(1,num_sides)


num_sides=int(input('how many sides do you want? '))

while True:
    dice=rolling_dice(num_sides)
    print(f'the dice gets:{dice}')
    if dice == num_sides:
        break

'''
# ex 3
def gallons_to_litres(gallon):
    return 3.7854 * gallon

while True:
    input_gallon = float(input('how many gallon to convert?'))
    if input_gallon < 0:
        break
    print(f'{input_gallon} gallon are {gallons_to_litres(input_gallon):.1f} liters')

