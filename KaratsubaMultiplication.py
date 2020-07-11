'''
Алгоритм целочисленного умножения Карацубы
'''

def karatsuba(x,y):
    list_x = list(str(x))
    list_y = list(str(y))
    middle_x = int(len(list_x) / 2)
    middle_y = int(len(list_y) / 2)
    a = int(''.join(list_x[:middle_x]))
    # Преобразуем левую половину верхнего числа из списка в число a
    b = int(''.join(list_x[middle_x:]))
    # Преобразуем правую половину верхнего числа из списка в число b
    c = int(''.join(list_y[:middle_y]))
    # Преобразуем левую половину нижнего числа из списка в число c
    d = int(''.join(list_y[middle_y:]))
    # Преобразуем правую половину нижнего числа из списка в число d
    step_1 = a * c
    step_2 = b * d
    step_3 = (a + b) * (c + d)
    step_4 = step_3 - step_1 - step_2
    step_5 = (step_1 * (10 ** 4)) + (step_2 * (10 ** 2)) + step_4
    return step_5

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
result = karatsuba(x,y)
print(result)