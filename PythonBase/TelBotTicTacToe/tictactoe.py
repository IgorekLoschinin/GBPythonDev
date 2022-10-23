#!/usr/bin/env python
# coding: utf-8

import telebot
from telebot import types
from auth_token import TOKEN

SIZE_BOARD = 3
BOARD = list(map(lambda x: str(x), range(1, (SIZE_BOARD**2) + 1)))
COUNTER = [0]
WIN_COORD = (
	(0, 1, 2), (3, 4, 5), (6, 7, 8),
	(0, 3, 6), (1, 4, 7), (2, 5, 8),
	(0, 4, 8), (2, 4, 6)
)
FIGURE = [""]


def telegram_bot():
	bot = telebot.TeleBot(token=TOKEN)

	@bot.message_handler(commands=['start'])
	def start(message):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton("X")
		btn2 = types.KeyboardButton("O")
		markup.add(btn1, btn2)
		bot.send_message(
			message.chat.id,
			text="Игра крестики-нулики!",
			reply_markup=markup
		)

	@bot.message_handler(content_types=['text'])
	def func(message, f=FIGURE):

		if message.text == "X":
			choose_position(message)
			f[0] = message.text

		elif message.text == "O":
			choose_position(message)
			f[0] = message.text

		elif message.text not in "XO" and message.text in BOARD:
			res_win = tic_tac_toe(COUNTER, FIGURE[-1], message.text)

			if res_win is not None:
				res_handling(message, res_win)

			else:
				back_to_gen_menu(message, FIGURE[-1])

		elif message.text == "Finish!!!":
			finish(message)

		elif message.text == "Start":
			update_board()
			start(message)

		elif message.text == "Close":
			markup = types.ReplyKeyboardRemove()
			bot.send_message(
				message.chat.id,
				text="Если хотите продолжить введите сообщение /start!",
				reply_markup=markup
			)

	def choose_position(message):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton("1")
		btn2 = types.KeyboardButton("2")
		btn3 = types.KeyboardButton("3")

		btn4 = types.KeyboardButton("4")
		btn5 = types.KeyboardButton("5")
		btn6 = types.KeyboardButton("6")

		btn7 = types.KeyboardButton("7")
		btn8 = types.KeyboardButton("8")
		btn9 = types.KeyboardButton("9")

		markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
		bot.send_message(
			message.chat.id,
			text=print_board(BOARD),
			reply_markup=markup
		)

	def back_to_gen_menu(message, fig: str):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

		if fig.upper() == "X":
			btn1 = types.KeyboardButton("O")
		else:
			btn1 = types.KeyboardButton("X")

		markup.add(btn1)
		bot.send_message(
			message.chat.id,
			text=f"Next!\n\n" + print_board(BOARD),
			reply_markup=markup
		)

	def res_handling(message, res: str):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton("Finish!!!")

		markup.add(btn1)
		bot.send_message(
			message.chat.id,
			text=res,
			reply_markup=markup
		)

	def finish(message):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton("Start")
		btn2 = types.KeyboardButton("Close")
		markup.add(btn1, btn2)
		bot.send_message(
			message.chat.id,
			text="Начать игру сначала?",
			reply_markup=markup
		)

	bot.polling(none_stop=True)


def tic_tac_toe(counter, figure: str, pos_for_fig: str) -> str | None:

	choose = make_chose(figure, pos_for_fig)
	if choose is not None:
		return choose

	counter[0] += 1
	if counter[0] > 4:
		tmp = validate_on_win()
		if tmp:
			return f"Выиграл user - {figure}!"

	if counter[0] == 9:
		return "Ничья!"

	return None


def make_chose(fig: str, pos: str) -> str | None:
	valid_num = False
	while not valid_num:

		player = int(pos)

		if 1 <= player <= SIZE_BOARD**2:
			if BOARD[player - 1] not in "XO":
				BOARD[player - 1] = fig.upper()
				valid_num = True
			else:
				return "Эта позиция занята!"

		else:
			return "Номер позиции некорректен! Введите число от 1 до 9"

	return None


def validate_on_win() -> bool:
	for pos in WIN_COORD:
		if BOARD[pos[0]] == BOARD[pos[1]] == BOARD[pos[2]]:
			return True

	return False


def print_board(elemets: list) -> str | None:
	"""  """
	board_text = ""

	top = ("-----" * SIZE_BOARD) + "-" + "\n|"
	elem = " {} |" * SIZE_BOARD
	bottom = "-" + ("-----" * SIZE_BOARD)

	row = "".join([top, elem])

	num = []
	for item in range(1, (SIZE_BOARD**2) + 1):
		num.append(elemets[item - 1])
		if item % 3 == 0:
			board_text += row.format(*num) + "\n"
			num = []

	board_text += bottom

	return board_text


def update_board():
	for ind, item in enumerate(list(map(
			lambda x: str(x), range(1, (SIZE_BOARD ** 2) + 1))
	)):
		BOARD[ind] = item

	COUNTER[0] = 0


if __name__ == "__main__":
	telegram_bot()
