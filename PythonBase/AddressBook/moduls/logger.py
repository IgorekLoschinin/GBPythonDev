#!/usr/bin/env python
# coding: utf-8
import logging

# from AddressBook.moduls.utils import write_to_file

_log_format = \
    f"%(asctime)s - [%(levelname)s] - %(name)s - " \
    f"(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"


# def loggerV1(func):
# 	def wrapper(*args, **kwargs):
# 		try:
# 			func(*args, **kwargs)
#
# 		except Exception as e:
# 			write_to_file("log.txt", f"{e}\n", mode="a")
#
# 	return wrapper


def logger(name: str, file: str):
    """ Логер """

    log = logging.getLogger(name)
    log.setLevel(logging.INFO)

    file_handler = logging.FileHandler(file, mode="w")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(_log_format))

    log.addHandler(file_handler)

    return log

