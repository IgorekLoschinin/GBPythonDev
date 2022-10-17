#!/usr/bin/env python
# coding: utf-8
import sys

import jmespath as jme

from pathlib import Path
from .formatter import Formatter
from AddressBook.moduls.logger import logger
from AddressBook.moduls.utils import read_to_file, write_to_file

log = logger(__name__, "apiDB.log")


class APIDBTelBook(object):

	__DB_BOOK = "dbTelBook.txt"

	def __init__(self) -> None:
		self.__db_data = None
		self._format_obj_data = Formatter()

		try:
			self._load_db()

		except Exception as e:
			log.exception(e)

	@property
	def db_data(self) -> dict | None:
		return self.__db_data

	@property
	def db_file(self) -> str:
		return APIDBTelBook.__DB_BOOK

	def _load_db(self) -> None:
		""" Подключение и загрузка быза данных. """

		if not (Path(self.db_file).is_file() and Path(self.db_file).exists()):
			print("Файл базы данных не был найден.", end="\n")
			log.error("Файл базы данных не был найден.")
			sys.exit(1)

		self.__db_data = {
			int(id_): self._form_member(form_.split(" "))
			for item in read_to_file(self.db_file)
			for id_, form_ in [tuple(item.strip().split(" ", 1))]
		}

		if len(self.db_data) == 0:
			msg = "База данных не содержит записей. "
			print(msg, end="\n\n")
			log.info(msg)

	@staticmethod
	def _form_member(lst_data: list) -> dict:
		"""  """
		fields = ("lastName", "name", "patronymic", "phoneNumber")
		return dict(zip(fields, lst_data))

	def search_(self) -> None:
		"""  """
		print("Пока не работает поиск!", end="\n\n")

	def add_(self, form_memder: dict) -> None:
		""" ДОбавление нового участника в базу данных """

		if len(self.db_data) != 0 and self.db_data is not None:
			self.db_data[max(self.db_data) + 1] = form_memder

		else:
			self.db_data[1] = form_memder

	def delete_(self, id_mem: int) -> None:
		""" Удаление участника из бд """

		if 0 < id_mem <= max(self.db_data):
			del_member = self.db_data.pop(id_mem)
			print(f"Удален: {' '.join(del_member.values())}", end="\n\n")

		else:
			print("Не верный ID!")

	def update_(self, data_for_upd: dict) -> None:
		""" Обновление информации """

		self.__db_data.update(data_for_upd)

	def import_(self, file_name: str, f_d: str) -> None:
		""" Выгрузка данных в необходимом формате """

		self._format_obj_data.handle(format_d=f_d)
		self._format_obj_data.write(self.db_data, file_name)

	def export_(self, file_name: str, f_d: str) -> dict:
		""" Экспортирование данных для последующих операций """

		self._format_obj_data.handle(format_d=f_d)

		return self._format_obj_data.read(file_name)

	def view_(self, data: dict = None) -> None:
		""" Просмотерщик информации в базе. """

		if data is None:
			data = self.db_data

		transform_data = [
			f"{id_} " + " ".join(fio_tel.values())
			for id_, fio_tel in data.items()
		]

		for i in transform_data:
			print(i)

	def save(self) -> None:
		""" СОхранение бд """
		write_to_file(self.db_file, [
			f"{id_} {' '.join(data_.values())}\n"
			for id_, data_ in self.db_data.items()
		], mode="w")
