import random
import operator

def merge_sort(L, compare=operator.lt):
    #compare=оператор lt(a, b) эквивалентен операции сравнения a < b
    if len(L) < 2:
        #если в списке один элемент, то копируем его [:]
        print(f'Копируем {L}')
        return L[:]
    else:
        print(f'Не копируем {L}')
        middle = int(len(L) / 2)
        #получаем длину разделенного списка на 2
        print(f'middle {middle}')
        left = merge_sort(L[:middle], compare)
        #сортируем левую часть списка
        right = merge_sort(L[middle:], compare)
        #сортируем правую часть списка
        return merge(left, right, compare)

def merge(left, right, compare):
    print(f'Объединяем левый и правык список, сравнивая {left} и {right}')
    result = []
    #создаем пустой список result
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            #сравниваем left[i] и right[j]
            result.append(left[i])
            #добавляем в конец списка result left[i], если left[i] больше right[j]
            i += 1
        else:
            result.append(right[j])
            #добавляем в конец списка result right[j], если left[i] меньше right[j]
            j += 1
    while i < len(left):
        result.append(left[i])
        #добавляем в конец списка result left[i], если длина списка left меньше i
        i += 1
    while j < len(right):
        result.append(right[j])
        #добавляем в конец списка result right[j], если длина списка right меньше j
        j += 1
    return result

list_random = [random.randint(1,50) for value in range(1,10)]
list_random_merge_sort = merge_sort(list_random)
print(f'Отсортировал {list_random_merge_sort}')