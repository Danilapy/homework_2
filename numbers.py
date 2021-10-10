import random
number = random.randint(1, 100)

user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}
level = int(input('Введите уровень сложности от 1 до 3: '))
max_count = levels[level]

user_count= int(input('Введите число игроков: '))
users = []
for i in range(user_count):
    user_name = input(f'Введите имя игрока: {i+1} ')
    users.append(user_name)
print(users)

is_winner = False
winner_name = None

while not is_winner:
    count += 1
    if count > max_count:
        print('ГЕЙМОВЕР')
        break
    print(f'Попытка № {count}')
    for user in users:
        print(f'Ход игрока {user}')
        user_number = int(input('Введите число: '))
        if user_number == number:
            is_winner = True
            winner_name = user
            break
        elif number < user_number:
            print('Ваше число больше загаданного')
        else:
            print('Ваше число меньше загаданного')
else:
    print(f'ПОБЕДИТЕЛЬ: {winner_name}')
