# 1'. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint


#Изначальный вариант (8 строк)

# len_list = 10
# sum1 = 0
# list = [randint (0,10) for i in range (len_list)]

# for i in range (len(list)):
#     if i % 2 != 0:
#         sum1 = sum1 + list[i]
# print(f'Исходный список {list}')
# print(f'Сумма всех элементов, стоящих на нечетных позициях равна {sum1}')



# Вариант с использованием filter (5 строк)

len_list = 10
list = [randint (0,10) for i in range (len_list)]
result = [list[i] for i in range(len(list)) if i % 2 !=0]

print(f'Исходный список {list}')
# print(f'Список элементами стоящих на нечетных позициях{result}')
print(f'Сумма всех элементов, стоящих на нечетных позициях равна {sum(result)}')