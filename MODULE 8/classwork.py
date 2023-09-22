import random
# random.randint(1,100)
# number= int(input("number: "))
# while number<1:
#     print('number is too low')
#     break
# while number > 100:
#     print('number is too high')
#     break
#     if number<=100 or number>=0:
#         print('you have put right number')

# correct one starts below
# hid_no=random.randint(1,100)
# player_no=0
# while not player_no== hid_no: #while player_no != hid_no:
#     player_no=int(input('guess a number:'))
#
#     if player_no>hid_no:
#         print('you are going too far, it is too high')
#     elif player_no<hid_no:
#         print('you are close but it is too low')
#     else:
#         print('hurray ! you got it!!!')

# exercise two:
while True:
    number=int(input('please give a number:'))
    if number <= 0:
        break
    factorial = 1
    new = 1
    while new<=number:
        factorial = factorial * new
        print(new)
        new += 1
        print(f'the factorial of the number{number} is {factorial}')
print('thanks and bye')