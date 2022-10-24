#!/usr/bin/env python
# coding: utf-8
import logging

_log_format = \
    f"%(asctime)s - [%(levelname)s] - %(name)s - " \
    f"(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"


def logger(name: str, file: str):
    """ Логер """

    log = logging.getLogger(name)
    log.setLevel(logging.INFO)

    file_handler = logging.FileHandler(file, mode="w")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(_log_format))

    log.addHandler(file_handler)

    return log

