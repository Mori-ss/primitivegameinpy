from random import randint
x = randint(0, 9)
y = int(input('угадай число от 0 до 9 '))
while y != x:
    if y != x:
        print("случайное число было-", x)
        y = int(input ('Ты не угадал, попробуй заново '))
else:
    print('О молодец, ты угадал!')
