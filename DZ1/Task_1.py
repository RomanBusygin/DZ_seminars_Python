d = int(input('Введите номер дня недели: '))

if d in range(1,6):
    print('Сегодня будний день. Иди работай!')
elif d in range(6, 8):
    print('Сегодня выходной!')
else: print('Что-то пошло не так')
