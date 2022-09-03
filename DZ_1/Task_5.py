from math import sqrt


print('Введите координаты точки А: ')
x_1 = int(input('X = '))
y_1 = int(input('Y = '))
print('Введите координаты точки B: ')
x_2 = int(input('X = '))
y_2 = int(input('Y = '))

print(f'Расстояние между точками равно: {round(sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2), 2)}')
