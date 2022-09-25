#!/usr/bin/env python
# coding: utf-8

from random import random


def main():

	print("task1", end="\n")
	num = float(input("Enter number float: "))
	print(task1(num), end="\n\n")

	print("task2", end="\n")
	num = int(input("Enter number N: "))
	print(task2(num), end="\n\n")

	print("task3", end="\n")
	num = int(input("Enter number N: "))
	print(task3(num), end="\n\n")

	print("task4", end="\n")
	pos1 = int(input("Position one: "))
	pos2 = int(input("Position two: "))
	num = int(input("Number of elements: "))
	print(task4(pos1, pos2, num), end="\n\n")

	print("task5", end="\n")
	num = int(input("Enter number N: "))
	print(task5(num), end="\n\n")


def task1(num: float) -> int:
	""" Программа, котрая принимает на вход вещественное число и показывает
	сумму его цифр.

	6782 -> 23
	0.67 -> 13
	198.45 -> 27

	"""

	num_to_str = str(num)

	# return sum([int(i) for i in num_to_str if i.isdigit()])
	return sum([int(i) for i in filter(lambda x: x.isdigit(), num_to_str)])


def task2(num:  int) -> list:
	""" Программа, котрая принимает на вход число N и выдает набор произведения
	чисел от 1 до N.
	Example: 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.

	4 -> [1, 2, 6, 24]
	6 -> [1, 2, 6, 24, 120, 720]

	"""

	def _mult(lst: list) -> int:
		mult_num = 1
		for item in lst:
			mult_num *= item

		return mult_num

	return list(map(
		_mult, [[i for i in range(1, j + 1)] for j in range(1, num + 1)]
	))
	# return [_mult([i for i in range(1, j + 1)]) for j in range(1, num + 1)]


def task3(n: int) -> int:
	""" Задается список из n чисел, заполненный по формуле (1+1/n)**n и
	возвращает их сумму.

	n = 6: [2, 2, 2, 2, 2, 3] -> 13

	"""

	lst_num = list(map(lambda x: round((1 + (1 / x)) ** x), range(1, n + 1)))
	print(lst_num, end='\n')

	return sum(lst_num)


def task4(pos_1: int, pos_2: int, num: int) -> int | None:
	""" Программа, которая принимает на вход 2 числа. Задайате список из N
	элементов, заполненных числами из промежутка [-N, N]. Найти произведение
	элементов на указанных позициях (не индексах).

	Position one: 1
	Position two: 3
	Number of elements: 5
	-> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
	-> 15

	"""

	if pos_1 <= 0 or pos_2 <= 0:
		print("Position 1 or 2 == 0")
		return None

	shift = 1
	lst_elem = list(range(-num, num + 1))

	if pos_1 > len(lst_elem) or pos_2 > len(lst_elem):
		print("One of the items is out of the list!")
		return None

	return lst_elem[pos_1 - shift] * lst_elem[pos_2 - shift]


def task5(size: int) -> list:
	""" Алгоритм перемешивания списка. (Без shuffle) """

	return sorted(range(size), key=lambda x: random())


if __name__ == "__main__":
	main()
