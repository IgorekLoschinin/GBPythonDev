#!/usr/bin/env python
# coding: utf-8
import sys
import math

from logger import logger

log = logger(__name__, "calculator.log")


class Calculator(object):

	def __init__(self) -> None:
		self._actions = ('+', '-', '*', '/', 'pow', 'sqrt', 'complex', 'q')

		self._action = None
		self._x = None
		self._y = None
		self._degree = None

	def start(self) -> None:

		print("калькулятор на Python")
		while True:
			print(
				"Выберите действие которое хотите сделать:\n"
				"Сложить: +\n"
				"Вычесть: -\n"
				"Умножить: *\n"
				"Поделить: /\n"
				"X^2: pow\n"
				"Корень: sqrt\n"				
				"Комплекс. числа: complex\n"
				"Выйти: q\n"
			)

			if not self.input_action():
				continue

			if self._action in ('+', '-', '*', '/'):
				if not self.input_arg_x() or not self.input_arg_y():
					continue

				if not self.base_operations():
					continue

			if self._action == "q":
				print("Выход из программы")
				sys.exit()

			if self._action == "pow":
				if not self.input_arg_x() or not self.input_arg_degree():
					continue

				print(
					f'{self._x} ^ {self._degree} = '
					f'{(self._x ** self._degree)}\n'
				)

			elif self._action == "sqrt":
				if not self.input_arg_x():
					continue

				print(
					f'√{self._x} = {math.sqrt(self._x)}\n'
				)

			elif self._action == "complex":
				self.action_complex()

	def base_operations(self) -> bool:
		if self._action == '+':
			print(
				f'{self._x} + {self._y} = {(self._x + self._y)}\n'
			)

		elif self._action == '-':
			print(
				f'{self._x} - {self._y} = {(self._x - self._y)}\n'
			)

		elif self._action == '*':
			print(
				f'{self._x} * {self._y} = {(self._x * self._y)}\n'
			)

		elif self._action == '/':
			if self._y != 0:
				print(
					f'{self._x} / {self._y} = {(self._x / self._y)}\n'
				)

			else:
				print("Деление на ноль!")
				log.error("Деление на ноль!\n")
				return False

		return True

	def input_action(self) -> bool:
		act = input("Действие: ")

		if act not in self._actions:
			print("Введеная операция отсутствует.\nВыберите из имеющихся!\n")
			log.error("Введеная операция не отсутствует.")
			return False

		self._action = act
		return True

	def input_arg_x(self) -> bool:
		x = input("x = ")

		if not self.is_number(x):
			print("X не является чилом.\n")
			log.error("X не является чиломю.\n")
			return False

		self._x = float(x)

		return True

	def input_arg_y(self) -> bool:
		y = input("y = ")

		if not self.is_number(y):
			print("Y не является чилом.\n")
			log.error("Y не является чилом.\n")
			return False

		self._y = float(y)

		return True

	def input_arg_degree(self) -> bool:
		degree = input("degree = ")

		if not self.is_number(degree):
			print("degree не является чилом.\n")
			log.error("degree не является чилом.\n")
			return False

		self._degree = float(degree)
		return True

	@staticmethod
	def is_number(string_num) -> bool:
		try:
			float(string_num)
			return True
		except ValueError:
			return False

	def action_complex(self) -> bool:
		complex_num = []

		count = 1
		while count <= 2:
			print(
				f"Введите Real и Imag для {count}-ого комплексного числа: ",
				end='\n'
			)
			if not self.input_arg_x() or not self.input_arg_y():
				return False

			if self._y < 0:
				complex_num.append(complex(f"{self._x}{self._y}j"))

			else:
				complex_num.append(complex(f"{self._x}+{self._y}j"))

			count += 1

		if not self.input_action():
			return False

		self._x, self._y = complex_num
		self.base_operations()


if __name__ == "__main__":
	app = Calculator()
	app.start()
