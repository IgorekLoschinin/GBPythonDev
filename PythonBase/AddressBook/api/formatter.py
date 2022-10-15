#!/usr/bin/env python
# coding: utf-8

import csv
from lxml import etree
from json import dumps, loads
from xml.etree import ElementTree as ET


class Formatter(object):

	def __init__(self) -> None:
		self._obj = None

	def handle(self, format_d: str = None):
		"""  """
		if format_d is None:
			format_d = ""

		match format_d.lower():
			case "xml":
				self._obj = XML()

			case "csv":
				self._obj = CSV()

			case "json":
				self._obj = Json()

			case _:
				print("Не верный формат!")

	def write(self, data: dict, file: str) -> None:
		"""  """

		if self._obj is not None:
			self._obj.to_file(data, file)

	def read(self, file: str) -> dict:
		"""  """

		if self._obj is not None:
			return self._obj.from_file(file)


class XML(object):

	def __init__(self) -> None:
		pass

	@staticmethod
	def from_file(file: str) -> dict:
		"""  """
		tree = etree.parse(f'{file}.xml')
		root = tree.getroot()

		return {
			int(item_elem.get("id")): dict(item_elem.items()[1:])
			for item_elem in root.xpath(".//member")
		}

	@staticmethod
	def to_file(data: dict, file: str) -> None:
		"""  """
		root = ET.Element('AddressBook')

		for id_, data_i in data.items():
			ET.SubElement(
				root,
				"member",
				attrib={"id": str(id_), **data_i}
			)

		tree = ET.ElementTree(root)
		ET.indent(tree, space="\t", level=0)
		tree.write(f'{file}.xml', xml_declaration=True, encoding="utf-8")


class CSV(object):

	def __init__(self) -> None:
		pass

	@staticmethod
	def from_file(file: str) -> dict:
		"""  """
		with open(f'{file}.csv', mode='r') as csv_file:
			csv_reader = csv.DictReader(csv_file)

			return {
				id_: data_ for id_, data_ in enumerate(csv_reader, 1)
			}

	@staticmethod
	def to_file(data: dict, file: str) -> None:
		"""  """

		header = ['lastName', 'name', 'patronymic', 'phoneNumber']
		with open(f'{file}.csv', 'w') as file:
			writer = csv.DictWriter(file, fieldnames=header)
			writer.writeheader()
			writer.writerows(data.values())


class Json(object):

	def __init__(self) -> None:
		pass

	@staticmethod
	def from_file(file: str) -> dict:
		"""  """
		with open(f"{file}.json", "r") as obj_file:
			return loads(obj_file.read())

	@staticmethod
	def to_file(data: dict, file: str) -> None:
		"""  """
		with open(f"{file}.json", "w") as obj_file:
			obj_file.write(dumps(data, indent=4, ensure_ascii=False))

