import random
import math
# module 4
# ex 1
# Write a program that uses a while loop to print out all numbers
# divisible by three in the range of 1-1000.

'''
number = 1
while number <= 1000:

    if number % 3 == 0:
        print(number)
    number += 1
'''
# ex-2
# Write a program that converts inches to centimeters until the user
# inputs a negative value. Then the program ends.
'''
inch_to_cm = 2.54

while True:
    inches = float(input("enter a value in inches : "))
    if inches < 0:
        print("Exit")
        break
    centimeters = inches * inch_to_cm
    print(inches, 'inches is equal to' , centimeters,'centimeters')
'''
#Task 2
'''
print("Task#2")
M = 0
while M >= 0:
    M = float(input("Enter Inches: "))
    if M < 0:
       
        print("Program has Ended Due to Entering Negative Number.")

        break
    if M < 0:
        print(f"{M}inches is equal to ",end="")
        M = M * 2.54
        print(f"{M} in centimeters")
        print()
print()
'''
# ex-3
# Write a program that asks the user to enter numbers until they enter
# an empty string to quit. Finally, the program prints out the smallest
# and largest number from the numbers it received.
# Initialize variables for the smallest and largest numbers

'''
prompt = 'Give a number?'
s = input('give a number?')
if s != '':
    largest = int(s)
    smallest = largest

    while True:

        s = input(prompt)
        if s == '':
            break;
        n = int(s)
        if n < smallest:
            smallest = n
        elif n > largest:
            largest = n


    print(f'The smallest number given was {smallest}, and the largest was {largest}')
else:
    print('no numbers were given')
'''

# ex-4
'''
Write a game where the computer draws a random integer between 
1 and 10. The user tries to guess the number until they guess the 
right number. After each guess the program prints out a text: 
Too high, Too low or Correct. Notice that the computer must not 
change the number between guesses.
'''
'''
right_no=random.randint(1,10)
user_no=0
while user_no!=right_no:
    user_no=int(input('guess a number:'))

    if user_no>right_no:
        print('it is too high')
    elif user_no<right_no:
        print(' it is too low')
    else:
        print('correct!')
'''
# ex-5
'''
Write a program that asks the user for a username and password. 
If either or both are incorrect, the program ask the user to enter 
the username and password again. This continues until the login 
information is correct or wrong credentials have been entered five 
times. If the information is correct, the program prints out Welcome.
After five failed attempts the program prints out Access denied.
The correct username is python and password rules.
'''
'''
correct_username='himali'
correct_password='prasar'
attempts=0
while attempts<5:
    username=input('enter your username?:')
    password=input('enter your password?:')
    if username==correct_username and password==correct_password:
        print('welcome')
        break
    else:
        print('repeat the process all over again')
        attempts=attempts+1
if attempts==5:
    print('access denied')
'''
# ex-6
'''
Implement an algorithm for calculating an approximation for the value 
of pi (π). Let's assume that A is a unit circle. A unit circle 
has the radius of one and it is centered at the origin (0,0).
Smallest possible square B is drawn around the unit circle so that
circle A is completely inside the square. The corners of the 
square are now (-1,-1), (1, -1), (1, 1), and (-1, 1). 
If a large number of random points are scattered inside the square, 
the fraction of points that fall inside the circle A correlates with
the fraction of the area of circle A compared to the area of 
square B: πr^2/4 = π*1^2/4 = π/4. This can be used as a simple 
method for calculating an approximation of the value of pi: 
Let's generate a large number of random points, such as one million,
inside square B. Let N be the total number of random points. 
Each point inside the square is tested for whether it resides
inside circle A. Let n be the total number of points that fall
inside circle A. Now we have n/N≈π/4, and from that we get π≈4n/N.
Write a program that asks the user how many random points to generate,
and then calculates the approximate value of pi using the method 
explained above. At the end, the program prints out the approximation
of pi to the user. (Notice that it is easy to test if a point falls
inside circle A by testing if it fulfills the inequation x^2+y^2<1.).
'''
'''
N = int(input('how many random points to generate?'))
n = 0
i = 0
while i < N:
    x=random.uniform(-1., 1.)
    y=random.uniform(-1., 1.)
    if x**2 + y**2 < 1.:
      n = n+1
    i = i+1
pi = 4.*n/N
print(f'Pi is {pi}, error{math.pi-pi}')
'''



















