#!/usr/bin/env python
# coding: utf-8

import jmespath as jme

from .formatter import Formatter
from AddressBook.moduls.logger import logger
from AddressBook.moduls.utils import read_to_file, write_to_file


class APIDBTelBook(object):

	__DB_BOOK = "dbTelBook.txt"

	def __init__(self) -> None:
		self.__db_data = None
		self._format_obj_data = Formatter()

		self._load_db()

	@property
	def db_data(self) -> dict | None:
		return self.__db_data

	@property
	def db_name(self) -> str:
		return APIDBTelBook.__DB_BOOK

	@logger
	def _load_db(self) -> None:
		"""  """
		self.__db_data = {
			int(id_): self._form_member(form_.split(" "))
			for item in read_to_file(self.db_name)
			for id_, form_ in [tuple(item.strip().split(" ", 1))]
		}

	@staticmethod
	def _form_member(lst_data: list) -> dict:
		"""  """
		fields = ("lastName", "name", "patronymic", "phoneNumber")
		return dict(zip(fields, lst_data))

	def search_(self) -> None:
		"""  """
		print("Пока не работает поиск!")

	def add_(self, form_memder: dict) -> None:
		"""  """
		if len(self.__db_data) != 0 and self.__db_data is not None:
			self.__db_data[max(self.__db_data) + 1] = form_memder

		else:
			self.__db_data[1] = form_memder

	def delete_(self, id_mem: int) -> None:
		"""  """
		if 0 < id_mem <= max(self.__db_data):
			del_member = self.__db_data.pop(id_mem)
			print(f"Удален: {' '.join(del_member.values())}", end="\n\n")

		else:
			print("Не верный ID!")

	def update_(self, data_for_upd: dict) -> None:
		"""  """
		self.__db_data.update(data_for_upd)

	def import_(self, file_name: str, f_d: str) -> None:
		"""  """
		self._format_obj_data.handle(format_d=f_d)
		self._format_obj_data.write(self.db_data, file_name)

	def export_(self, file_name: str, f_d: str) -> dict:
		"""  """
		self._format_obj_data.handle(format_d=f_d)
		return self._format_obj_data.read(file_name)

	def view_(self, data: dict = None) -> None:
		"""  """

		if data is None:
			data = self.db_data

		transform_data = [
			f"{id_} " + " ".join(fio_tel.values())
			for id_, fio_tel in data.items()
		]

		for i in transform_data:
			print(i)

	def save(self) -> None:
		"""  """
		write_to_file(self.db_name, [
			f"{id_} {' '.join(data_.values())}\n"
			for id_, data_ in self.db_data.items()
		], mode="w")
