# number = int(input())
# if number > 0:
#     print(True)
# else:
#     print(False)
# number = int(input())
# if number % 2 == 0:
#     print('Парне')
# if number % 5 == 0:
#     print('Кратное 5')
# вывести все число от 1 до 10
# a = 1
# while a < 11:
#     print(a)
#     a = a + 1
# for i in range(1, 11):
#     print(i)
# for i in range(1, 11, 2):
#     print(i)
# start = int(input())
# stop = int(input())
# s = 0
# for i in range(start, stop + 1):
#     s= s + i
# print('Result =', s)
# start = int(input())
# stop = int(input())
# p = 1
# for i in range(start, stop + 1):
#     p= p*i
# print('Result =', p)
# start = int(input())
# stop = int(input())
# s = 0
# for i in range(start, stop + 1):
#     if i % 2 == 0:
#         s = s + i
# print('Result =', s)
# start = int(input())
# stop = int(input())
# s = 0
# while start <= stop:
#     s = s + start
#     start += 1
# print('Result =', s)
# phone_number = '380972666666'
# p_n = int(phone_number)
# print(phone_number[-1])  # посл цифра номера
# print(p_n % 10)   # посл цифра номера
# print(len(phone_number))   # количество цир в номере
# s = 0
# for i in phone_number:   # сумма цифр номера
#     s = s + int(i)
# print(s)
# list_with_numbers = [1, 2, 3, 4]
# print(list_with_numbers)
# print(type(list_with_numbers))
# print(len(list_with_numbers))
# list_with_numbers[0] = 10
# print(list_with_numbers[0])
# list_with_height = []
# while True:
#     n = input()
#     if n == 'stop':
#          break
#     list_with_height.append(int(n))
# print(list_with_height)
# print('Max = ', max(list_with_height))
# print('Avg = ', sum(list_with_height) / len(list_with_height))
# def last_digit(number):
#     x = number % 10
#     return x
# a = last_digit(123)
# print('poslednee 4islo = ', a)
# def my_max(a, b):
#     if a > b:
#         return a
#     else:
#         return b
# print(my_max(2, 7))
# print(my_max('a', 'c'))
# def step(x, n):
#     if int(n) >= 1:
#         return (int(x)**int(n))
# a = input()
# b = input()
# print(step(a, b))
def fact(x):
    p = 1
    for i in range(1, x+1):
        p = p * i
    return p
a = int(input())
print(fact(a))
