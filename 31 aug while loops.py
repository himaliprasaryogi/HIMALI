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



