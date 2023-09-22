import random
import math
# ex 4
'''
def sum_list(num_list):
    no1=0
    for i in num_list:
        no1 += i
    return no1


num_list = []
for no in range(10):
    num_list.append(random.randint(1,10))
print(f'List is: '),
for i in range(len(num_list)):
    print(num_list[i], end = ' ')
print(f'\nSum of the list is {sum_list(num_list)}')
'''
# ex 5
'''
def even_num(list_no):
    result_list = []
    for i in range(len(list_no)):
        if list_no[i]%2 == 0:
            result_list.append(list_no[i])
    return result_list


# this is to print the whole list

def print_list(num, list_no):
    print(num, end=' ')
    for i in range(len(list_no)):
        print(list_no[i], end=' ')


numberlist=[]
for n in range(10):
    numberlist.append(random.randint(1, 99))
print()
print_list('here is the original list: ', numberlist)
cutdown_list= even_num(numberlist)
print_list('\ncut down list is: ', cutdown_list)
print()
'''

# ex 6
'''
def cal_pizza(dia, price):
    return price/(math.pi*(dia/2)**2)


p1_diameter=float(input('give me the diameter of the 1st pizza(in cm)? '))
p1_price=float(input('give the price of the 1st pizza (in euros)?'))
p2_diameter=float(input('give me the diameter of the 2nd pizza(in cm)? '))
p2_price=float(input('give the price of the 2nd pizza (in euros)?'))

if cal_pizza(p1_diameter, p1_price)< cal_pizza(p2_diameter, p2_price):
    print('the 1st pizza is a better option. grab it now!')
else:
    print('the 2nd pizza is way more better. take it!')
'''



