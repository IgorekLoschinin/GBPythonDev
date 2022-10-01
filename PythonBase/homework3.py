#!/usr/bin/env python
# coding: utf-8
from random import randint, uniform
import math


def main():

	""" task1, task2 """
	size_lst = int(input("Enter count number in list: "))
	rand_lst_num = [randint(1, 100) for _ in range(size_lst)]
	print(f"Random number list: {rand_lst_num}")

	print(f"Out task1: {task1(rand_lst_num)}")
	print(f"Out task1: {task1(rand_lst_num)}")
	print(f"Out task1: {task1(rand_lst_num, opt=2)}")
	print(f"Out task1: {task1(rand_lst_num, opt=2)}")

	print(f"Out task2: {task2(rand_lst_num)}")

	""" task3 """
	num = int(input("Enter number: "))
	print(f"Out task3: {task3(num)}")

	""" task4 """
	size_lst = int(input("Enter count number in list: "))
	rand_lst_num = [round(uniform(1, 100), 2) for _ in range(size_lst)]
	print(f"Random number list: {rand_lst_num}")
	print(f"Out task4: {task4(rand_lst_num)}")

	""" task5 """
	num = int(input("Enter number: "))
	print(" ".join(map(lambda x: str(x), task5(num))))


def task1(lst_num: list[int], opt: int = 1) -> int:
	""" Задайте список, состоящий из произвольных чисел, количество задаёт
	пользователь. Напишите программу, которая найдёт сумму элементов списка,
	стоящих на нечётных позициях(не индексах)

	in
	5

	out
	[10, 2, 3, 8, 9]
	22

	in
	4

	out
	[4, 2, 4, 9]
	8

	"""

	if not lst_num:
		print("List empty!")
		return 0

	match opt:
		case 1:

			return sum([
				lst_num[pos - 1] for pos in range(1, len(lst_num) + 1, 2)
			])

		case 2:

			return sum([
				lst_num[pos - 1]
				for pos in range(1, len(lst_num) + 1)
				if pos % 2 == 1
			])

		case _:
			return 0


def task2(lst_num: list[int]) -> list[int]:
	""" Напишите программу, которая найдёт произведение пар чисел списка.
	Парой считаем первый и последний элемент, второй и предпоследний и т.д.

	in
	4

	out
	[2, 5, 8, 10]
	[20, 40]

	in
	5

	out
	[2, 2, 4, 8, 8]
	[16, 16, 4]

	"""
	center = (len(lst_num) // 2)

	match len(lst_num) % 2:
		case 0:
			return [lst_num[i] * lst_num[-1-i] for i in range(center)]

		case 1:
			return [
				lst_num[i] * lst_num[-1-i]
				if i != center
				else lst_num[i]
				for i in range(center + 1)
			]

		case _:
			return []


def task3(num: int) -> int:
	""" Напишите программу, которая будет преобразовывать десятичное число в
	двоичное. Без использования встроенной функции преобразования, без строк.

	in
	88
	out
	1011000

	in
	11
	out
	1011

	"""
	copy_num = num
	bin_num = ""

	if num == 0:
		return 0

	while copy_num > 0:
		bin_num = str(copy_num % 2) + bin_num
		copy_num //= 2

	return int(bin_num)


def task4(lst_num: list[float], opt: int = 1) -> tuple | None:
	""" * Задайте список из произвольных вещественных чисел, количество задаёт
	пользователь. Напишите программу, которая найдёт разницу между
	максимальным и минимальным значением дробной части элементов.

	in
	5
	out
	[5.16, 8.62, 6.57, 7.92, 9.22]
	Min: 0.16, Max: 0.92. Difference: 0.76

	in
	3
	out
	[9.26, 8.5, 1.14]
	Min: 0.14, Max: 0.5. Difference: 0.36

	"""
	if not lst_num:
		print("List empty!")
		return None

	match opt:
		case 1:
			lst_fract_part = list(map(lambda x: round(x % 1, 2), lst_num))

		case 2:
			lst_fract_part = \
				list(map(lambda x: round(math.modf(x)[0], 2), lst_num))

		case _:
			lst_fract_part = [0]

	max_in_lst = max(lst_fract_part)
	min_in_lst = min(lst_fract_part)
	diff_in_lst = round(max_in_lst - min_in_lst, 2)

	return min_in_lst, max_in_lst, diff_in_lst


def task5(num: int) -> list[int]:
	""" ** Задайте число. Составьте список чисел Фибоначчи, в том числе для
	отрицательных индексов.

	in
	8
	out
	-21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

	in
	5
	out
	5 -3 2 -1 1 0 1 1 2 3 5

	"""

	if num > 0:
		num *= -1

	return [
		fib(item) for item in range(num, abs(num) + 1)
	]


def fib(num: int) -> int:
	""" """

	if num == 0 or num == 1:
		return num

	elif num < 0:
		return int(math.pow(-1, (abs(num) + 1))) * fib(abs(num))

	else:
		return fib(num - 1) + fib(num - 2)


if __name__ == "__main__":
	main()
