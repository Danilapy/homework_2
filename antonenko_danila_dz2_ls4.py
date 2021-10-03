import random

price_list = [round(random.uniform(1, 100), 2) for i in range(20)]

for p in price_list:
    print(f'{int(p)} руб. {int(p * 100 % 100):02d} коп.', end=', ', )

print('\n', sorted(price_list))

print('\n', sorted(price_list, reverse=True))

print('\n', sorted(price_list[-5:]))
