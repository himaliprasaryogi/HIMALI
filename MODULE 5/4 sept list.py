prompt = 'give a number?'
s = input(prompt)

values = []
while s != '':
    values.append(int(s))

    s = input(prompt)
print(values)
k = 0
while k < len(values):
    print('the value is' + str(values[k]))
    k = k+1


