#!/usr/bin/env python
# coding: utf-8

from pathlib import Path


def write_to_file(
		file: str | Path, data: list | str, mode: str = "w"
) -> None:
	""" Запись в файл """

	with open(file, mode) as obj_file:
		if isinstance(data, list):
			obj_file.writelines(data)

		if isinstance(data, str):
			obj_file.write(data + "\n")


def read_to_file(path_file: str | Path) -> list:
	""" Чтение из файла """
	with open(path_file, "r") as file:
		return file.readlines()
