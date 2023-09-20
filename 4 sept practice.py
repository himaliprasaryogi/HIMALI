username = "python"
password = 'rules'
n = 5
while n > 0:
    u = input('give the username?')
    p = input('give the password?')
    if u == username and p == password:
        print('welcome')
        break
    n = n -1
else:

    print('access denied')
