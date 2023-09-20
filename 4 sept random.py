import random
prompt = 'try to guess the number? '
secret_number = random.randint(1, 10)
guess = int(input('try to guess the number?'))
while guess != secret_number:
    if guess > secret_number:
        print('too high')
    else:
        print('too low')
    guess = int(input(prompt))

print('correct')
# check the video
