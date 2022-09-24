#!/usr/bin/env python
# coding: utf-8

from math import sqrt, pow


def main():

	num_day = int(input("Enter number day for checked: "))
	task1(num_day)
	print("\n")

	task2()
	print("\n")

	coord_x, coord_y = \
		(int(input(f"Enter value coordinate {item}: ")) for item in ["x", "y"])
	task3(coord_x, coord_y)
	print("\n")

	quarter_num = int(input("Enter number quarter: "))
	task4(quarter_num)
	print("\n")

	A_x, A_y, B_x, B_y = (
		int(item)
		for item in input(
			"Enter the coordinates of points A and B separated by a space: "
		).split(" ")
	)
	print(task5(A_x, A_y, B_x, B_y), end="\n")


def task1(num_day: int) -> None:
	""" Программа, котрая принимает на вход цифру, обозначающую день недели, и
	проверяет является ли этот день выходным. """

	if num_day <= 0 or num_day > 7:
		print("It's not a day of the week!")

	elif 1 <= num_day <= 5:
		print("Workday!")

	else:
		print("Weekend!")


def task2() -> None:
	""" Программа для проверки истинности утверждения
	~(X or Y or Z) = ~X and ~Y and ~Z  для всех значений предикат. """

	for x in range(2):
		for y in range(2):
			for z in range(2):

				print(x, y, z)
				if (not (x or y or z)) == (not x and not y and not z):
					print(f"Утверждение истинно", end="\n\n")
				else:
					print(f"Утверждение ложно", end="\n")


def task3(coord_x: int, coord_y: int) -> None:
	""" Программа, которая принимает на вход координаты точки (X и Y), при чем
	X != 0 and Y != 0  и выдает номер четверти плоскости, в которой находится
	эта точка (или на какой оси она находится). """

	if coord_x != 0 and coord_y != 0:
		if coord_x > 0 and coord_y > 0:
			print(1)

		elif coord_x < 0 and coord_y > 0:
			print(2)

		elif coord_x < 0 and coord_y < 0:
			print(3)

		elif coord_x > 0 and coord_y < 0:
			print(4)
	else:
		print("Error, 0 entered!")


def task4(quarter_num: int) -> None:
	""" Программа, которая по заданному номеру четверти, показывает диапозон
	возможных координат точек в этой четверти (x и y). """

	match quarter_num:
		case 1:
			print("x > 0 and y > 0")

		case 2:
			print("x < 0 and y > 0")

		case 3:
			print("x < 0 and y < 0")

		case 4:
			print("x > 0 and y < 0")


def task5(a_x: int, a_y: int, b_x: int, b_y: int) -> float:
	""" Программа, которая принимает на вход координаты двух точек и находит
	расстояние между ними в 2D пространстве. """

	distance_point = round(sqrt(
		pow((b_x - a_x), 2) + pow((b_y - a_y), 2)
	), 3)

	return distance_point


if __name__ == "__main__":
	main()
