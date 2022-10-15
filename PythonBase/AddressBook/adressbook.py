#!/usr/bin/env python
# coding: utf-8
import sys

from AddressBook.moduls.logger import logger
from api.apiDB import APIDBTelBook


class AddressBook(object):

	__TITLE = "-------- ======= Телефонный справочник ======= --------"

	def __init__(self) -> None:
		self.__db = APIDBTelBook()

	def title(self) -> None:
		print(AddressBook.__TITLE)

	@property
	def db(self) -> APIDBTelBook:
		return self.__db

	@logger
	def run(self) -> None:
		self.title()

		while True:

			match self._choice():
				case 1:
					self._search_member()

				case 2:
					self._add_member()

				case 3:
					self._del_member()

				case 4:
					self._update_member()

				case 5:
					self._view_all_db()

				case 6:
					self._import_data()

				case 7:
					self._export_data()

				case 0:
					break

				case _:
					print("Введённый код не обрабатывается!")

		self.db.save()

	@staticmethod
	def _choice() -> int | None:
		msg_err = \
			"Не корректный ввод!!!" \
			"\nНеобходимо ввести целое число!!!"

		try:
			selector = int(input(
				'Введите "1" найти контакт\n' +
				'Введите "2" Добавить контакт\n' +
				'Введите "3" удалить контакт\n' +
				'Введите "4" обновить контакт\n' +
				'Введите "5" просмотреть всю адресную книгу\n' +
				'Введите "6" Импортирвать контакты\n' +
				'Введите "7" Экспортировать контакты\n' +
				'Введите "0" Выход\n' +
				'Ввести здесь: '
			))

		except ValueError as e:
			print(msg_err)
			raise Exception(msg_err + f"\n{e}")

		return selector

	def _search_member(self) -> None:
		"""  """
		self.db.search_()

	def _add_member(self) -> None:
		"""  """
		new_member = Member()
		self.db.add_(new_member.data_member)

	def _del_member(self) -> None:
		"""  """
		id_member = int(input(
			"Введите id человека для удаления: "
		))
		self.db.delete_(id_member)

	def _update_member(self) -> None:
		"""  """
		id_member = int(input(
			"Введите id человека для обновления инфо: "
		))
		new_member = Member()
		self.db.update_({id_member: new_member.data_member})

	def _view_all_db(self) -> None:
		"""  """
		self.db.view_()
		print()

	def _import_data(self) -> None:
		"""  """
		importing_format = input(
			"Введите формат для импортирования (xml, csv, json): "
		)
		file_name = input("Выберите название файла: ")
		self.db.import_(file_name, importing_format)

	def _export_data(self) -> None:
		"""  """
		importing_format = input(
			"Введите формат файла (xml, csv, json): "
		)
		file_name = input("Выберите название файла: ")
		export_data = self.db.export_(file_name, importing_format)

		selector = int(input(
			'Введите "1" обновить данные в базе к экспорт\n' +
			'Ввести здесь: '
		))

		match selector:
			case 1:
				self.__db.update_(export_data)

	def _exit(self) -> None:
		"""  """
		sys.exit(0)


class Member(object):

	def __init__(self) -> None:
		self._last_name = None
		self._name = None
		self._patronymic = None
		self._phone_number = None

		self._characters()

	def _characters(self) -> None:
		"""  """

		print("\nЗаполните форму: ", end="\n")
		self._last_name = input("Введите фамилию: ").capitalize()
		self._name = input("Введите имя: ").capitalize()
		self._patronymic = input("Введите отчество: ").capitalize()
		self._phone_number = input("Введите номер телефона: ").capitalize()
		print(end="\n")

	@property
	def data_member(self) -> dict:
		"""  """
		return {
			"lastName": self._last_name,
			"name": self._name,
			"patronymic": self._patronymic,
			"phoneNumber": self._phone_number
		}


if __name__ == "__main__":

	app = AddressBook()
	if not app.run():
		sys.exit(1)
