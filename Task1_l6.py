# 3'. Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

from random import randint


# Исходный вариант (8 строк)

# lenght = int(input("Введите желаемое количество значений в списке: "))
# list = [randint(0,5) for i in range(lenght)]
# list2 =[]
# for i in range (lenght):
#     if list[i] not in list2:
#         list2.append(list[i])
# print(list)
# print(list2)



# Способ с использованием list comprehension (6 строк)

lenght = int(input("Введите желаемое количество значений в списке: "))
lst = [randint(0,5) for i in range(lenght)]
lst2 = set()
result = [i for i in lst if i not in lst2 and (lst2.add(i) or True)]

print(lst)
print(result)

