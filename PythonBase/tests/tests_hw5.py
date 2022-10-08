import unittest
import homework5 as hw5


class HomeWork3(unittest.TestCase):

	def test_task1(self):
		self.assertEqual(hw5.task1([]), 0)

	def test_task2(self):
		self.assertEqual(hw5.task2([]), 0)

	def test_task3(self):
		self.assertEqual(hw5.task3([]), 0)

	def test_task4(self):
		self.assertEqual(hw5.task4([]), 0)

	def test_task5(self):
		self.assertEqual(hw5.task5([]), 0)


if __name__ == '__main__':
	unittest.main()
