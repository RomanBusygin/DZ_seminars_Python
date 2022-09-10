def couple_multiply(multiply_list: list):
    multiply = 1
    if len(multiply_list) % 2 == 0:
        count = int(len(multiply_list) / 2)
        for i in range(count):
            multiply = int(multiply_list[i]) * int(multiply_list[-i - 1])
            print(multiply, end= ' ')
    else:
        count = int(len(multiply_list) / 2) + 1
        for i in range(count):
            multiply = int(multiply_list[i]) * int(multiply_list[-i - 1])
            print(multiply, end= ' ')

number_list = input('Введите числа через пробел: ').split(' ')
couple_multiply(number_list)