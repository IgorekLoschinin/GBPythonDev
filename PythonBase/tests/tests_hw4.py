import unittest
import homework4 as hw4


class HomeWork4(unittest.TestCase):

	def test_task1(self):
		self.assertEqual(hw4.task1(), 0)

	def test_task2(self):
		self.assertEqual(hw4.task2(), [])

	def test_task3(self):
		self.assertEqual(hw4.task3(), 0)

	def test_task4(self):
		self.assertIsNone(hw4.task4(), (0, 0, 0))

	def test_task5(self):
		self.assertEqual(hw4.task5(), [0])


if __name__ == '__main__':
	unittest.main()
