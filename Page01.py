
"""
05
2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

Какое самое маленькое число делится нацело на все числа от 1 до 20?
https://www.cyberforum.ru/python-beginners/thread2456814.html
"""
# Разобрать этот вариант
# n=20
# i=19
# while i>0:
#   if n%i==0:
#       i-=1
#   else:
#       n+=20
#       i=19
#   if i==1:
#     print (n)

c = 0
e = 0
while c != 20:
    c = 0
    e += 2520
    for i in range(1,21):
        if e % i == 0:
            c += 1
print(e)


"""
04
Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
"""


# def is_palindrome(int_str) -> bool:
#     # i = 0
#     # j = len(int_str) - 1
#     # while i < j:
#     #     if int_str[i] != int_str[j]:
#     #         return False
#     #     i +=1
#     #     j -= 1
#     # return True
#     # так короче :)
#     return int_str == int(str(int_str)[::-1])


# max_palindrome = 0
# min_value = 100
# max_value = 1000
#
# for i in range(min_value, max_value):
#     for j in range(i, max_value):
#         current = i * j
#         if is_palindrome(current):
#             max_palindrome = current if max_palindrome < current else max_palindrome
#
# print(max_palindrome)

"""
03
Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600 851 475 143, являющийся простым числом?
6857
"""
# num = 600851475143
# count = 2
# while 1:
#
#     if num % count == 0:
#         print(count)
#         num /= count
#         if num == 1:
#             print(count)
#             break
#     count += 1

"""
02
Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
Начиная с 1 и 2, первые 10 элементов будут:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
"""
# f1, f2 = 0, 1
# my_sum = 0
# while f2 < 4000000:
#     # f1, f2 = f2, f1 + f2
#     my_sum = my_sum + f2 if f2 % 2 == 0 else my_sum
#     f1, f2 = f2, f1 + f2
# print(my_sum)
# # вариант из готовых решений
# f1, f2, s = 0, 1, 0
# while f2 <= 4000000:
#     s = s + f2 if f2 % 2 == 0 else s
#     f1, f2 = f2, f1 + f2
# print(s)
"""
01
Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
"""
# my_sum = 0
# for ch in range(1000):
#     if ch % 3 == 0 or 0 == ch % 5:
#         print(ch)
#         my_sum += ch
# print(my_sum)
