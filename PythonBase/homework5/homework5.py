#!/usr/bin/env python
# coding: utf-8

from pathlib import Path
from moduls import rle
from moduls.utils import read_to_file, write_to_file


def main():
	# """ task1 """
	# number = int(input("Number of words: "))
	# print(task1(number, word_str="авб абв бав абв вба бав вба абв абв абв"))

	# """ task2 """
	# file_encode = Path("./text_words.txt")
	# file_out = Path("./text_code_words.txt")
	# task2(file_encode, file_out, mode="encode")

	print("Uncomment Tasks!")


def task1(num_word: int, word_str: str = None, opt: int = 1) -> str | None:
	""" Напишите программу, удаляющую из текста все слова, содержащие "абв".
	В тексте используется разделитель пробел.

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

	pattern = "абв"

	if num_word < 0:
		print("The data is incorrect!")
		return None

	if word_str is None:
		str_words = " ".join([
			input("Enter word: ").strip() for _ in range(num_word)
		])

	else:
		str_words = word_str

	print(str_words)

	match opt:
		case 1:
			return " ".join([
				item.strip()
				for item in str_words.replace(pattern, "").split(" ")
				if len(item.strip()) != 0
			]).strip()

		case 2:
			return " ".join([
				item
				for item in str_words.split(" ")
				if item != pattern
			])


def task2(file_in: Path, file_out: Path, mode: str = None) -> None:
	""" Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления
	данных.Входные и выходные данные хранятся в отдельных текстовых файлах.

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
	5a29v4s3D3d2F4g2O3i2a
	1v2b2w2P3u2T1Y1y2W2Q

	"""

	if not (file_in.is_file() and file_in.exists()):
		print("Input file not exists!")
		return None

	data = list(map(lambda x: x.strip(), read_to_file(file_in)))

	match mode:
		case "encode":
			write_to_file(file_out, [rle.encode(d) + "\n" for d in data])

		case "decode":
			data_decoding = rle.decode()


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
