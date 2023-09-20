import math
import random
# module 1 and 2

# ex 1
#Write a program that greets you by your
# own name. If your name was
# Viivi Virta, the output of the program would be Hello, Viivi Virta!.
'''
name=input('enter your name: ')
print('hello!'+ ' ' + name)
'''
# EX 2
# Write a program that asks the user for the radius of a circle and
# the prints out the area of the circle.
'''
radius =int(input('enter the value of the radius of circle in cm: '))
area = (math.pi*radius*radius)
print('the area is' , float(area))
'''
# ex 3
# Write a program that asks the user for the length and width of a
# rectangle. The program then prints out the perimeter and area of
# the rectangle. The perimeter of a rectangle is the sum of the lengths
# of each four sides.
'''
length=int(input('enter length: '))
width=int(input('enter width: '))
perimeter = 2*(length+width)
area =(length*width)
print("the perimeter of the rectangle is :", '', perimeter)
print('the area of the rectangle is :', '', area)
'''

# ex 4
# Write a program that asks the user for three integer numbers.
# The program prints out the sum, product, and average of the numbers.
'''
integer1= int(input('enter first number: '))
integer2= int(input('enter second number: '))
integer3= int(input('enter third number: '))
sum= (integer3+integer2+integer1)
product=(integer3*integer2*integer1)
average=((integer3*integer2*integer1)/3)
print('the sum is:','',sum)
print('the product is:','',product)
print('the average is:','',average)
'''
# ex 5


# Write a program that asks the user to enter a mass in medieval units:
# talents (leiviskä), pounds (naula), and lots (luoti). The program
# converts the input to full kilograms and grams and outputs the result
# to the user:
#
#     One talent is 20 pounds.
#     One pound is 32 lots.
#     One lot is 13,3 grams.

'''
talent=float(input('enter talent:'))
talent1 = talent*20*32*13.3

pounds= float(input('enter pounds:' ))
pounds1= pounds*32*13.3

lots= float(input('enter lots:' ))
lots1= lots*13.3

gram1 = float(talent1+pounds1+lots1)
kilogram = int(gram1//1000)
gram = float(gram1 % 1000)
gram = (f'{gram:.2f}')


print('modern unit is:', kilogram,'kg', gram,'g')
'''
# ex 6
# Write a program that draws two random combinations of numbers for
#     a combination lock:
#
#     a 3-digit code where each number is between 0 and 9.
#     a 4-digit code where each number is between 1 and 6.





