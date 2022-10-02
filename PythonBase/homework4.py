#!/usr/bin/env python
# coding: utf-8
import itertools
from random import randint
from decimal import Decimal
from collections import Counter


def main():
	# """ task1 """
	# number = float(input("Enter a real number: "))
	# acc = float(input("Enter the required accuracy '0.0001': "))
	# print(task1(number, acc))

	# """ task2 """
	# number = int(input("Enter a number: "))
	# print(task2(number))

	# """ task3"""
	# size_lst = int(input("Enter count number in list: "))
	# print(f"Out task3: {task3(size_lst)}")

	# """ task4"""
	# for i in [9, 5, 3, 0, -1, 4]:
	# 	poly = [f"Degree polynomial: {i}\n\t", task4(i), "\n\n"]
	# 	write_in_file("task4_poly.txt", poly, mode="a")
	# num = int(input("Enter natural number degree: "))
	# poly = [f"Degree polynomial: {num}\n\t", task4(num), "\n\n"]
	# write_in_file("task4_poly.txt", poly, mode="a")

	""" task5 """
	task5()


def task1(num: float, accuracy: float) -> float | Decimal:
	""" Вычислить число c заданной точностью d

	in
	Enter a real number: 9
	Enter the required accuracy '0.0001': 0.000001

	out
	9.000000

	in
	Enter a real number: 8.98785
	Enter the required accuracy '0.0001': 0.001

	out
	8.988

	"""

	if num % 1 == 0:
		return Decimal(num).quantize(Decimal(str(accuracy)))

	return float(Decimal(num).quantize(Decimal(str(accuracy))))


def task2(num: int) -> list[int]:
	"""
	Задайте натуральное число N. Напишите программу, которая составит список
	простых множителей числа N.

	Простые делители числа

	in
	54

	out
	[2, 3, 3, 3]

	in
	9990

	out
	[2, 3, 3, 3, 5, 37]

	in
	650

	out
	[2, 5, 5, 13]

	"""

	factors = []
	divisor = 2
	while divisor <= num:
		if num % divisor == 0:
			factors.append(divisor)
			num = num // divisor

		else:
			divisor += 1

	return factors


def task3(size_lst: int, lst_num: list[int] = None) -> list[int]:
	"""  Задайте последовательность чисел. Напишите программу, которая
	выведет список неповторяющихся элементов исходной последовательности в
	том же порядке.

	in
	7

	out
	[4, 5, 3, 3, 4, 1, 2]
	[5, 1, 2]

	in
	-1

	out
	Negative value of the number of numbers!
	[]

	in
	10

	out
	[4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
	[6, 2, 3, 0, 9]

	"""
	rand_lst_num = []

	if size_lst < 0:
		print("Negative value of the number of numbers!")
		return rand_lst_num

	if lst_num is None:
		rand_lst_num = [randint(1, 10) for _ in range(size_lst)]

	else:
		rand_lst_num = lst_num.copy()

	return [
		item_n
		for item_n, count in Counter(rand_lst_num).items()
		if count == 1
	]


def write_in_file(file: str, data: list | str, mode: str = "w") -> None:

	with open(file, mode) as obj_file:
		if isinstance(data, list):
			obj_file.writelines(data)

		if isinstance(data, str):
			obj_file.write(data + "\n")


def task4(nat_degree: int) -> str:
	""" * Задана натуральная степень k. Сформировать случайным образом список
	коэффициентов (от 0 до 10) многочлена, записать в файл полученный многочлен
	не менее 3-х раз.

	in
	9
	5
	3

	out in the file
	3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
	4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
	4*x^2 - 4 = 0

	in
	0
	-1
	4

	out in the file
	3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
	4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
	4*x^2 - 4 = 0
	2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0

	"""

	if nat_degree <= 0:
		return "Degree less than or equal to zero!"

	coeff_sequence = [randint(0, 10) for i in range(nat_degree + 1)]
	degree_sequence = list(range(nat_degree, 0, -1))
	variables_seq = ['*x^'] * nat_degree

	polynom = " + ".join([
		f"{coeff}{var_s}{deg_s}"
		for coeff, var_s, deg_s in itertools.zip_longest(
			coeff_sequence, variables_seq, degree_sequence, fillvalue=''
		)
		if coeff != 0
	]) + " = 0"

	return polynom


def task5() -> None:
	""" ** Даны два файла, в каждом из которых находится запись многочленов.
	Задача - сформировать файл, содержащий сумму многочленов.

	in
	"poly.txt"
	"poly_2.txt"

	out in the file
	3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
	4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
	4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0

	in
	"poly.txt"
	"poly_2.txt"

	out
	The contents of the files do not match!

	"""

	def read_file(path_file: str) -> list:
		with open(path_file, "r") as file:
			return file.readlines()

	def parse_poly(poly: str) -> list:
		parse_pol = poly.rstrip(" = 0").split(' ')
		lst_sign = parse_pol[1::2]
		members = parse_pol[0::2]

		define_signs = [
			s + v for s, v in list(zip(lst_sign, members[1:]))
		]
		define_signs.insert(0, parse_pol[0])

		lst_coeff_and_degree = []
		for item in define_signs:
			value = item.split("*x^")

			if len(value) < 2:
				lst_coeff_and_degree.append((int(value[0]), 0))
			else:
				lst_coeff_and_degree.append((int(value[0]), int(value[1])))

		return lst_coeff_and_degree

	def sum_coeff(pol1: list, pol2: list) -> list:
		sum_members = [0 for _ in range((max(pol1[0][1] + 1, pol2[0][1] + 1)))]

		for item_member in pol1 + pol2:
			sum_members[item_member[1]] += item_member[0]

		res = [
			(sum_members[i], i)
			for i in range(len(sum_members))
			if sum_members[i] != 0
		][::-1]

		return res

	def create_poly(lst_mem: list) -> str:
		coeff_sequence = []
		degree_sequence = []
		for coeff, deg in lst_mem:
			coeff_sequence.append(str(coeff))

			if deg != 0:
				degree_sequence.append(str(deg))

		variables_seq = ['*x^'] * len(degree_sequence)

		lst_members = [
			f"{coeff}{var_s}{deg_s}"
			for coeff, var_s, deg_s in itertools.zip_longest(
				coeff_sequence, variables_seq, degree_sequence, fillvalue=''
			)
			if coeff != 0
		]

		polynom = [
			" + " + item
			if not item.startswith("-")
			else f" - {item.lstrip('-')}"
			for item in lst_members[1:]
		]
		polynom.insert(0, lst_members[0])
		polynom = "".join(polynom) + " = 0"

		return polynom

	file1 = 'poly.txt'
	file2 = 'poly_2.txt'
	file_sum = 'sum_polynomials.txt'

	try:
		poly1 = read_file(file1)[0]
		poly2 = read_file(file2)[0]

		split_on_member_1 = parse_poly(poly1.strip())
		split_on_member_2 = parse_poly(poly2.strip())

		sum_poly_by_coeff = sum_coeff(split_on_member_1, split_on_member_2)

		sum_poly = create_poly(sum_poly_by_coeff)
		write_in_file(file_sum, sum_poly)

	except ValueError:
		write_in_file(file_sum, "The contents of the files do not match!")


if __name__ == "__main__":
	main()
