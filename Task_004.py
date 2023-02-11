# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел A. Последняя строка содержит число X

# from random import randint
# size = int(input('Введите размер списка: '))
# numbers = tuple(randint(1, size) for _ in range(size))
# print(*numbers)
# num_X = int(input('Введите искомое число: '))
# mod = 0
# flag = False
# for _ in range(len(set(numbers))):
#     for i in set(numbers):
#         if i == num_X - mod or i == num_X + mod:
#             print(i)
#             flag = True
#             break
#     if flag:
#         break
#     mod += 1

# 2 Variant

# l = input()
# numbers = list(map(int, input().strip().split()))
# x = int(input().strip())

# res = numbers[0]
# for i in numbers:
#     if abs(i - x) < abs(res - x):
#         res = i

# print(res)

# Variant 3
# a, n, find_num = [int(i) for i in input().split()], int(input()), 100
# for i in range(len(a)):
#     if a[i] < n:
#         find_num = -find_num
#     else:
#         find_num = find_num + 0
#     if a[i] >= n and a[i] - n <= find_num - n:
#         find_num = a[i]
#     elif a[i] <= n and find_num - n <= a[i] - n:
#         find_num = a[i]
# print(find_num)

# Variant 4
# from random import randint
# N = int(input('Введите величину массива: '))
# a = []
# for i in range(N): # Объявляем цикл заполнения списка
#     a.append(randint(1, 10)) # Заполненяем список числами от 1 до 10
# print('Последовательность: ', a)

# x = int(input('Введите искомое число: '))
# minraz = (x - a[0])**2
# b = 0
# i = 0
# while i < len(a):
#     if (x - a[i])**2 <= minraz:
#         minraz = (x - a[i])**2
#     b = i
#     i +=1
# # print('Последовательность: ', a)
# print('Самое близкое значение элемента массива: ', a[b])
# print('Индекс элемента массива: ', b)


# Variant 5
a = list(map(int, input().split()))
x = int(input())
ans = a[0]
for elem in a:
    if abs(elem - x) < abs(ans - x):
        ans = elem
print(ans)