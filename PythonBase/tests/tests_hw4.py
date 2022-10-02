import unittest
import homework4 as hw4


class HomeWork4(unittest.TestCase):

	def test_task1(self):
		self.assertEqual(hw4.task1(9, 0.000001), 9.000000)
		self.assertEqual(hw4.task1(8.98785, 0.001), 8.988)

	def test_task2(self):
		self.assertEqual(hw4.task2(54), [2, 3, 3, 3])
		self.assertEqual(hw4.task2(9990), [2, 3, 3, 3, 5, 37])
		self.assertEqual(hw4.task2(650), [2, 5, 5, 13])

	def test_task3(self):
		self.assertEqual(hw4.task3(7, lst_num=[4, 5, 3, 3, 4, 1, 2]), [5, 1, 2])
		self.assertEqual(hw4.task3(-1), [])
		self.assertEqual(hw4.task3(10, lst_num=[4, 4, 5, 5, 6, 2, 3, 0, 9, 4]), [6, 2, 3, 0, 9])


if __name__ == '__main__':
	unittest.main()
