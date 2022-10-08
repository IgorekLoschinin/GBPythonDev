import unittest
from homework5 import homework5 as hw5
from moduls.rle import encode, decode


class HomeWork5(unittest.TestCase):

	def test_task1(self):
		self.assertEqual(
			hw5.task1(10, word_str="авб абв бав абв вба бав вба абв абв абв"),
			"авб бав вба бав вба"
		)
		self.assertEqual(
			hw5.task1(
				10,
				word_str="авб абв бав абв вба бав вба абв абв абв",
				opt=2
			),
			"авб бав вба бав вба"
		)

		self.assertEqual(
			hw5.task1(6, word_str="ваб вба абв ваб бва абв"),
			"ваб вба ваб бва"
		)
		self.assertEqual(
			hw5.task1(6, word_str="ваб вба абв ваб бва абв", opt=2),
			"ваб вба ваб бва"
		)

		self.assertIsNone(
			hw5.task1(-1, word_str="авб абв бав абв вба бав вба абв абв абв")
		)

	def test_rle_encode(self):
		self.assertIsNone(encode(""))
		self.assertEqual(encode("a"), "1a")
		self.assertEqual(encode("aF"), "1a1F")
		self.assertEqual(encode("ABCD"), "1A1B1C1D")
		self.assertEqual(encode(
			"aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa"
		), "5a29v4s3D3d2F4g2O3i2a")
		self.assertEqual(encode(
			"vbbwwPPuuuTTYyWWQQ"
		), "1v2b2w2P3u2T1Y1y2W2Q")

	def test_rle_decode(self):
		self.assertIsNone(decode(""))
		self.assertEqual(decode("1a"), "a")
		self.assertEqual(decode("1a1F"), "aF")
		self.assertEqual(decode("1A1B1C1D"), "ABCD")
		self.assertEqual(decode(
			"5a29v4s3D3d2F4g2O3i2a"
		), "aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa")
		self.assertEqual(decode(
			"1v2b2w2P3u2T1Y1y2W2Q"
		), "vbbwwPPuuuTTYyWWQQ")


if __name__ == '__main__':
	unittest.main()
