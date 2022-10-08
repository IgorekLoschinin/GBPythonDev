#!/usr/bin/env python
# coding: utf-8

SIZE_BOARD = 3
BOARD = list(map(lambda x: str(x), range(1, (SIZE_BOARD**2) + 1)))


def tic_tac_toe() -> None:
	counter = 0
	win = False
	while not win:
		print_board(BOARD)

		if counter % 2 == 0:
			user_token = "X"
			make_chose(user_token)
		else:
			user_token = "O"
			make_chose(user_token)
		counter += 1

		if counter > 4:
			tmp = validate_on_win()
			if tmp:
				print(f"Выиграл user - {user_token}!")
				win = True
				break
		if counter == 9:
			print("Ничья!")
			break
	print_board(BOARD)


def make_chose(token: str) -> None:
	valid_num = False
	while not valid_num:

		try:
			player = int(input(f"Введите позицию для {token} - "))
		except ValueError:
			print("НЕ правильный ввод. Попробуйте сново")
			continue

		if 1 <= player <= SIZE_BOARD**2:
			if BOARD[player - 1] not in "XO":
				BOARD[player - 1] = token.upper()
				valid_num = True
			else:
				print("Эта позиция занята!")

		else:
			print("Номер позиции некорректен! Введите число от 1 до 9")


def validate_on_win() -> bool:
	win_coord = (
		(0, 1, 2), (3, 4, 5), (6, 7, 8),
		(0, 3, 6), (1, 4, 7), (2, 5, 8),
		(0, 4, 8), (2, 4, 6)
	)
	for pos in win_coord:
		if BOARD[pos[0]] == BOARD[pos[1]] == BOARD[pos[2]]:
			return True

	return False


def print_board(elemets: list) -> None:
	"""  """

	top = ("----" * SIZE_BOARD) + "-" + "\n|"
	elem = " {} |" * SIZE_BOARD
	bottom = "-" + ("----" * SIZE_BOARD)

	row = "".join([top, elem])

	num = []
	for item in range(1, (SIZE_BOARD**2) + 1):
		num.append(elemets[item - 1])
		if item % 3 == 0:
			print(row.format(*num), end='\n')
			num = []

	print(bottom)


if __name__ == "__main__":
	tic_tac_toe()
