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
		self._real = None
		self._imag = None
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
				if not self.input_arg(promt="x") or \
						not self.input_arg(promt="y"):
					continue

			if self._action == "pow":
				if not self.input_arg(promt="x") or \
						not self.input_arg(promt="degree"):
					continue

			elif self._action == "sqrt":
				if not self.input_arg(promt="x"):
					continue

			elif self._action == "complex":
				if not self.action_complex():
					continue

			elif self._action == "q":
				print("Выход из программы")
				sys.exit()

			if not self.base_operations():
				continue

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

		elif self._action == "pow":
			print(
				f'{self._x} ^ {self._degree} = '
				f'{(self._x ** self._degree)}\n'
			)

		elif self._action == "sqrt":
			print(
				f'√{self._x} = {math.sqrt(self._x)}\n'
			)

		return True

	def input_action(self, msg: str = "Действие: ") -> bool:
		act = input(msg)

		if act not in self._actions:
			print("Введеная операция отсутствует.\nВыберите из имеющихся!\n")
			log.error("Введеная операция не отсутствует.")
			return False

		self._action = act
		return True

	def input_arg(self, promt: str = "arg") -> bool:

		arg = input(f"{promt} = ")

		if not self.is_number(arg):
			print(f"{promt} не является чилом.\n")
			log.error(f"{promt} не является чилом.\n")
			return False

		match promt.lower():
			case "x":
				self._x = float(arg)

			case "y":
				self._y = float(arg)

			case "degree":
				self._degree = float(arg)

			case "real":
				self._real = float(arg)

			case "imag":
				self._imag = float(arg)

		return True

	@staticmethod
	def is_number(string_num) -> bool:
		try:
			float(string_num)
			return True
		except ValueError:
			return False

	def action_complex(self) -> bool:
		count = 1
		lst_compl_num = []

		if not self.input_action(msg="Действие над компл. чис.: "):
			return False

		if self._action in ('+', '-', '*', '/'):
			while count <= 2:
				print("Введите Real и Imag коэффициенты компл. ч.: ", end="\n")

				if not self.input_arg(promt="real") or \
					not self.input_arg(promt="imag"):
					return False

				count += 1
				lst_compl_num.append(self.complex_num())

			self._x, self._y = lst_compl_num
			return True

		match self._action:
			case "pow":
				if not self.input_arg(promt="real") or \
						not self.input_arg(promt="imag") or \
						not self.input_arg(promt="degree"):
					return False

				self._x = self.complex_num()
				return True

			case "sqrt":
				if not self.input_arg(promt="real") or \
						not self.input_arg(promt="imag"):
					return False

				self._x = self.complex_num()
				return True

		return False

	def complex_num(self) -> complex:
		if self._imag < 0:
			return complex(f"{self._real}{self._imag}j")

		else:
			return complex(f"{self._real}+{self._imag}j")


if __name__ == "__main__":
	app = Calculator()
	app.start()
