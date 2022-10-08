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
	# number = float(input("Enter a real number: "))
	# acc = float(input("Enter the required accuracy '0.0001': "))
	# print(task1(number, acc))

	# """ task3 """
	# number = float(input("Enter a real number: "))
	# acc = float(input("Enter the required accuracy '0.0001': "))
	# print(task1(number, acc))

	# """ task4 """
	# number = float(input("Enter a real number: "))
	# acc = float(input("Enter the required accuracy '0.0001': "))
	# print(task1(number, acc))

	# """ task5 """
	# number = float(input("Enter a real number: "))
	# acc = float(input("Enter the required accuracy '0.0001': "))
	# print(task1(number, acc))
	
	pass


def task1() -> None:
	""" Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.

	in
	Number of words: 10

	out
	авб абв бав абв вба бав вба абв абв абв
	авб бав вба бав вба

	in
	Number of words: 6

	out
	ваб вба абв ваб бва абв
	ваб вба ваб бва

	in
	Number of words: -1

	out
	The data is incorrect

	"""
	pass


def task2() -> None:
	""" Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.

	Алгоритм RLE

	in
	Enter the name of the file with the text:
	'text_words.txt'
	Enter the file name to record:
	'text_code_words.txt'
	Enter the name of the file to decode:
	'text_code_words.txt'

	out
	aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
	vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

	out in file
	'text_words.txt'
	aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
	vbbwwPPuuuTTYyWWQQ

	'text_code_words.txt'
	5a29v4s3D3d2F4g2O3i2a1
	1v2b2w2P3u2T1Y1y2W2Q

	"""
	pass


def task3() -> None:
	""" Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок
	- игрок, без бота. """
	pass


def task4() -> None:
	""" Создайте программу для игры с конфетами человек против человека.
	Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход
	друг после друга. Первый ход определяется жеребьёвкой. За один ход можно
	забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему
	последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать
	все конфеты у своего конкурента?

	Добавьте игру против бота
	Подумайте как наделить бота "интеллектом"
	"""
	pass


if __name__ == "__main__":
	main()
