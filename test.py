import unittest
from naive import num_coins
from dynamic import min_coins
from recursive import min_change_rec

class TestNumCoins(unittest.TestCase):
    def test_no_coins(self):
        self.assertEqual(num_coins(0), 0)

    def test_coins_available(self):
        self.assertEqual(num_coins(31), 3)
        self.assertEqual(num_coins(100), 4)

    def test_min_coins(self):
        self.assertEqual(min_coins([1,10,25], 31), 4)
        self.assertEqual(min_change_rec(4, [1,2]), 2)

if __name__ == '__main__':
	unittest.main()