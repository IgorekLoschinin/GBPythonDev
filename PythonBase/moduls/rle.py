#!/usr/bin/env python
# coding: utf-8
import re

__all__ = ['encode', 'decode']

def encode(data: str) -> str | None:
	""" String encoding by rle method """

	len_data = len(data)

	if len_data == 0:
		return None

	count = 0
	encode_str = ""
	for i in range(len_data):
		if i + 1 != len_data:
			if data[i] == data[i + 1]:
				count += 1
			else:
				encode_str += f"{count + 1}{data[i]}"
				count = 0

		else:
			encode_str += f"{count + 1}{data[i]}"
			count = 0

	return encode_str


def decode(data: str) -> str | None:
	""" String decoding by rle method """

	match len(data):
		case 0:
			return None

		case 1:
			return data

	digit = list(map(lambda x: int(x), re.findall('(\d+)', data)))
	lst_symbols = re.findall('([a-zA-Z])', data)

	return "".join([
		s * d for s, d in zip(lst_symbols, digit)
	])
