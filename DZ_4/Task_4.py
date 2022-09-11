from random import randint


def gen_polinom(degree: int) -> str:
    polinom = ""
    for i in range(k, -1, -1):
        if i > 1:
            polinom += f'{randint(0, 100)}x^{i} + '
        elif i == 1:
            polinom += f'{randint(0, 100)}x + '
        elif i == 0:
            polinom += f'{randint(0, 100)}'
    return polinom

k = int(input('Введите натуральную степень k: '))
with open('file.txt', 'w') as file:
    file.write(gen_polinom(k))