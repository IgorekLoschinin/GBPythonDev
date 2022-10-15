#!/usr/bin/env python
# coding: utf-8

from AddressBook.moduls.utils import write_to_file


def logger(func):
	def wrapper(*args, **kwargs):
		try:
			func(*args, **kwargs)

		except Exception as e:
			write_to_file("log.txt", f"{e}\n", mode="a")

	return wrapper
