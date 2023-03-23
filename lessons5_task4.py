# Найти сумму n элементов следующего ряда чисел:
# 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

def sum_order(num, sum_n=0, first_digit=1):
    if num == 0:
        return sum_n
    sum_n += first_digit
    num -= 1
    first_digit = first_digit * (-0.5)
    return sum_order(num, sum_n, first_digit)


num_el = int(input('Введите количество элементов:'))
print(f'сумма  равна: {sum_order(num_el)}')