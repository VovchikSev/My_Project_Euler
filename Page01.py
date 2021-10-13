"""
08
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
Наибольшее произведение четырех последовательных цифр в нижеприведенном 1000-значном числе равно 9 × 9 × 8 × 9 = 5832.
Найдите наибольшее произведение тринадцати последовательных цифр в данном числе.

"""


"""
07
Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-е простое число - 13.

Какое число является 10001-м простым числом? 104743
"""
import math

''' 
    Решето Эратосфена. В списке bits сбрасываются биты,
    имеющие составные номера, биты с простыми номерами == 1.
    i-му по порядку элементу будет соответствовать 1, если 
    i -- простое и 0 иначе. Сложность: nloglog(n).
'''

# def bit_sieve(n):
#     if n < 2:
#         return []
#     bits = [1] * n  # <-- 11...1
#     sqrt_n = int(math.sqrt(n)) + 1
#     for i in range(2, sqrt_n):
#         if bits[i - 2]:  # если i -- простое
#             for j in range(i + i, n + 1, i):  # занулить все ему кратные
#                 bits[j - 2] = 0
#     return bits
#
#
# k = 10001
# # k-ое простое не превосходит 1,5 k ln( k ) при k > 1:
# sieve = bit_sieve(int(1.5 * k * math.log(k)) + 1)
# i = 0
# while k:
#     k -= sieve[i]
#     i += 1
# print(i + 1)

# украдено с киберфорума

#  Не очень работает 20143 это не верно
# import math
#
# result = []
# i = 2
#
# while True:
#     if i % 2 != 0:
#         if (math.sqrt(i)).is_integer() != 1:
#             result.append(i)
#
#     if len(result) == 10001:
#         break
#     i += 1
# print(result[-1])

# for i in range(1, 10001):
#     if i % 2 != 0:
#         if math.sqrt(i).is_integer() != 1:
#             print(i)

#  не рабтает
# def issimple(n):
#     # r = math.ceil(math.sqrt(n))
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
# n = 5
# my_list = [2, 3]
#
# while True:
#     if issimple(n):
#         my_list.append(n)
#     if len(my_list) == 1001:
#         break
#     n +=2
# print(my_list[-1])

"""
06
Сумма квадратов первых десяти натуральных чисел равна

12 + 22 + ... + 102 = 385
Квадрат суммы первых десяти натуральных чисел равен

(1 + 2 + ... + 10)2 = 552 = 3025
Следовательно, разность между суммой квадратов и квадратом суммы
первых десяти натуральных чисел составляет 3025 − 385 = 2640.
Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел
"""
# sum_quadrat = 0
# sum = 0
#
# for num in range(1, 101):
#     sum_quadrat += num * num
#     sum += num
#
# print(sum * sum - sum_quadrat)


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

# c = 0
# e = 0
# while c != 20:
#     c = 0
#     e += 2520
#     for i in range(1,21):
#         if e % i == 0:
#             c += 1
# print(e)


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
