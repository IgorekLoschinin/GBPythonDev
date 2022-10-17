#!/usr/bin/env python
# coding: utf-8
import sys

from api.apiDB import APIDBTelBook
from AddressBook.moduls.logger import logger

log = logger(__name__, "AddresBook.log")


class AddressBook(object):
	__TITLE = "-------- ======= Телефонный справочник ======= --------"

	def __init__(self) -> None:
		self.__db = APIDBTelBook()

	def title(self) -> None:
		""" Заголовок программы """

		print(AddressBook.__TITLE)

	@property
	def db(self) -> APIDBTelBook:
		""" БД """
		return self.__db

	def run(self) -> None:
		""" Главный метод. Запускает процесс выполнения программы. """
		self.title()

		msg_warning = "Введённый код не обрабатывается!"

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
					print(msg_warning)
					log.warning(msg_warning)

			self.db.save()

	@staticmethod
	def _choice() -> int | None:
		msg_err = \
			"Не корректный ввод!!!" \
			" Необходимо ввести целое число!!!"

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

		except ValueError:
			print(msg_err)
			log.exception(msg_err)

			selector = None

		return selector

	def _search_member(self) -> None:
		""" Поиск участника по одному из указанных параметров. """

		# selector = int(input(
		# 	'Введите "1" Поиск по id\n' +
		# 	'Введите "2" Поиск по фамилии \n' +
		# 	'Введите "3" Поиск по имени\n' +
		# 	'Введите "4" Поиск по отчеству\n' +
		# 	'Введите "5" Поиск по тел номеру\n' +
		# 	'Ввести здесь: '
		# ))

		self.db.search_()

	def _add_member(self) -> None:
		""" Добавление новой формы данных в базу. """

		new_member = Member()
		self.db.add_(new_member.data_member)

	def _del_member(self) -> None:
		""" Удаление участника и всей информации из базы данных по ид. """
		try:
			id_member = int(input(
				"Введите id человека для удаления: "
			))
			self.db.delete_(id_member)

		except ValueError:
			log.exception('Были введены символы а не число.')

	def _update_member(self) -> None:
		""" Обновление информации по ид . """

		try:
			id_member = int(input(
				"Введите id человека для обновления инфо: "
			))
			new_member = Member()
			self.db.update_({id_member: new_member.data_member})

		except ValueError:
			log.exception('Были введены символы а не число.')

	def _view_all_db(self) -> None:
		""" Вывод данных всей базы для просмотра """

		self.db.view_()
		print()

	def _import_data(self) -> None:
		""" Выгрузка данных из базы. """

		importing_format = input(
			"\nВведите формат для импортирования (xml, csv, json): "
		)
		file_name = input("Выберите название файла: ")
		self.db.import_(file_name, importing_format)

	def _export_data(self) -> None:
		""" Считаваение новых данных из заданного файла, с последующим
		добавление в базу или обновлением ."""

		importing_format = input(
			"\nВведите формат файла (xml, csv, json): "
		)
		file_name = input("Выберите название файла: ")
		export_data = self.db.export_(file_name, importing_format)

		while True:
			selector = int(input(
				'\nВведите "1" обновить данные в базе к экспорт\n' +
				'Введите "2" просмотреть экспортируемые данные\n' +
				'Введите "0" вернуться в главное меню\n' +
				'Ввести здесь: '
			))

			match selector:
				case 1:
					self.__db.update_(export_data)

				case 2:
					self.db.view_(export_data)

				case 0:
					return

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
		self._phone_number = input("Введите номер телефона: ")
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
