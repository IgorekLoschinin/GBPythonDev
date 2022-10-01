import unittest
import homework3 as hw3


class HomeWork3(unittest.TestCase):

	def test_task1(self):
		self.assertEqual(hw3.task1([]), 0)
		self.assertEqual(hw3.task1([1]), 1)
		self.assertEqual(hw3.task1([1, 2]), 1)
		self.assertEqual(hw3.task1([1, 2, 3]), 4)
		self.assertEqual(hw3.task1([4, 2, 4, 9]), 8)
		self.assertEqual(hw3.task1([10, 2, 3, 8, 9]), 22)

		self.assertEqual(hw3.task1([], opt=2), 0)
		self.assertEqual(hw3.task1([1], opt=2), 1)
		self.assertEqual(hw3.task1([1, 2], opt=2), 1)
		self.assertEqual(hw3.task1([1, 2, 3], opt=2), 4)
		self.assertEqual(hw3.task1([4, 2, 4, 9], opt=2), 8)
		self.assertEqual(hw3.task1([10, 2, 3, 8, 9], opt=2), 22)

	def test_task2(self):
		self.assertEqual(hw3.task2([1, 2, 3, 4, 5, 6, 7]), [7, 12, 15, 4])
		self.assertEqual(hw3.task2([2, 5, 8, 10]), [20, 40])
		self.assertEqual(hw3.task2([2]), [2])
		self.assertEqual(hw3.task2([2, 0]), [0])
		self.assertEqual(hw3.task2([]), [])

	def test_task3(self):
		self.assertEqual(hw3.task3(0), 0)
		self.assertEqual(hw3.task3(1), 1)
		self.assertEqual(hw3.task3(2), 10)
		self.assertEqual(hw3.task3(88), 1011000)
		self.assertEqual(hw3.task3(11), 1011)

	def test_task4(self):
		self.assertIsNone(hw3.task4([]), (0, 0, 0))
		self.assertEqual(hw3.task4([5.16]), (0.16, 0.16, 0.0))
		self.assertEqual(hw3.task4([5.16, 8.62]), (0.16, 0.62, 0.46))
		self.assertEqual(
			hw3.task4([5.16, 8.62, 6.57, 7.92, 9.22]), (0.16, 0.92, 0.76)
		)
		self.assertEqual(hw3.task4([9.26, 8.5, 1.14]), (0.14, 0.5, 0.36))

		self.assertEqual(hw3.task4([5.16], opt=2), (0.16, 0.16, 0.0))
		self.assertEqual(hw3.task4([5.16, 8.62], opt=2), (0.16, 0.62, 0.46))
		self.assertIsNone(hw3.task4([], opt=2))
		self.assertEqual(
			hw3.task4([5.16, 8.62, 6.57, 7.92, 9.22], opt=2),
			(0.16, 0.92, 0.76)
		)
		self.assertEqual(
			hw3.task4([9.26, 8.5, 1.14], opt=2), (0.14, 0.5, 0.36)
		)

	def test_task5(self):
		self.assertEqual(hw3.task5(8), [-21, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21])
		self.assertEqual(hw3.task5(-8), [-21, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21])
		self.assertEqual(hw3.task5(5), [5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5])
		self.assertEqual(hw3.task5(-5), [5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5])
		self.assertEqual(hw3.task5(0), [0])
		self.assertEqual(hw3.task5(1), [1, 0, 1])
		self.assertEqual(hw3.task5(2), [-1, 1, 0, 1, 1])


if __name__ == '__main__':
	unittest.main()
