
# module 3
# ex-1
# Write a program that asks a fisher the length of a zander in centimeters.
# If the zander does not fulfill the size limit, the program instructs to
# release the fish back into the lake and notifies the user of how many
# centimeters below the size limit the caught fish was.
# A zander must be 42 centimeters or longer to meet the size limit.
'''
zander_length = int(input('mention the length of the zander in cm ?: '))
zander_sort = int(42-zander_length)
if zander_length >= 42:
    print('yay!')

if 0 <= zander_length <= 42:
    print('release the fish back into the lake')

    print('your zander is less by : '+ str(zander_sort) + 'cm')
'''

# ex-2
# Write a program that asks the user to enter the cabin class of
# a cruise ship and then prints out a written description according
# to the list below. You must use an if/elif/else structure in your
# solution.
    #
    # LUX: upper-deck cabin with a balcony.
    # A: above the car deck, equipped with a window.
    # B: windowless cabin above the car deck.
    # C: windowless cabin below the car deck.
'''
cabin_class = str(input('enter a cabin class:'))


if cabin_class == 'LUX':

    print(cabin_class, ':', 'upper-deck cabin with a balcony.')


elif cabin_class == 'A':
    print(cabin_class, ':', 'above the car deck, equipped with a window.')
elif cabin_class == 'B':
    print(cabin_class, ':', 'windowless cabin above the car deck.')
elif cabin_class == 'C':
    print(cabin_class, ':', 'windowless cabin below the car deck.')
else:
    print('Invalid cabin class')
'''
# ex-3


# Write a program that asks for the biological gender and hemoglobin
# value (g/l). The program the notifies the user if the hemoglobin
# value is low, normal or high.
#
#     A normal hemoglobin value for adult females is between 117-155 g/l.
#     A normal hemoglobin value for adult males is between 134-167 g/l.
'''
gender = str(input('What is your gender ?:'))
hemoglobin_value = int(input('what is your hemoglobin value in g/l ?:'))
if gender == 'female' and 117 <= hemoglobin_value <= 155:
    print('your hemoglobin_value is normal')
elif gender == 'female' and 117 >= hemoglobin_value:
    print('your hemoglobin_value is low')
elif gender == 'female' and hemoglobin_value >= 155:
    print('your hemoglobin_value is high')
if gender == 'male' and 134 <= hemoglobin_value <= 167:
    print('your hemoglobin_value is normal')
elif gender == 'male' and 134 >= hemoglobin_value:
    print('your hemoglobin_value is low')
elif gender == 'male' and hemoglobin_value >= 167:
    print('your hemoglobin_value is high')
'''

# ex-4
# Write a program that asks the user to enter a year and notifies the
# user whether the input year is a leap year. A year is a leap year if
# it is divisible by four. However, years divisible by 100 are leap years
# only if they are also divisible by 400.
'''
year = int(input('enter value of year?'))
if year%4==0 and year%100!=0 and year%400!=0:
    print('it is a leap year')
else:
    print('it is not a leap year')
'''

