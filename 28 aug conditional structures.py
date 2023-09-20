# print(11//2) gives whole number
# print(1/3) gives decimal number

# print(7//2.3) takes only the integer part not the fractional part
# print( 7% 2) gives the remainder value(remainder operator)
# print(123%10) output is 3 which is a remainder
# print(127%10)
# print(7/3)
# read iee precision integer value google it
# conditional structure main topic of today
# v=(7%3)
# is called variable assignment statement
# v1 = 1/3
# v2 = 1/5
# print(v1 < v2) boolean output false
# c= v1== v2 double equal to is comparison

# print(c)
# 4!=4 output false NOT EQUAL TO SIGN IS !=
# can use ; to seperate the lines and put in same line using semi colon
# print('i give you a truth')
# v1 = 1/6; v2 = 1/5
# # if v1 > v2:
# age = int(input('give your age?'))
# # print(f'your age is{age:03d}')
# s='years'
# # if age == -1 or age == 0 or age == 1:
# if -1 <= age <= 1:
# # if we use and then both arguments need to be true but if we use or argument then one needs to be true
# # we can use or or and arguments and add lots of values
#     s='year'
# print('your age is', age,s)

# string can be connected by comma, but if we put plus means string, need to address it
# comma can create space in output
# if age <= 0:
#     print('you are kidding')
# if 0 < age < 25:
#     print('you are young')
# # v1 = 1/3; v2 = 1 / 5
# if v1 < v2:
#     print('green is better than red')
# if 0 <= v1 < 1:
#     print('green is a beautiful color')
# print('that was it')
# conditional statement
age=int(input('give your age?'))
if age>0:
    s='years'
    if age <= 1:
        # above if is only for the top if which is called nesting
        s='year'

        print('your age is',age,s)
    if 0<age<25:
        print('you are young')
    elif 25<age<45:
        print('you are middle-aged')
    else:
        print('you are old')
    if age%2==0:
        print('your age is even')
    else:
        print('your age is odd')

else:
    print('you are kidding')
print('thats all folks')





