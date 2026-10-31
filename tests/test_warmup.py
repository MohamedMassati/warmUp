import unittest

from warmup import (
    diff21,
    makes10,
    monkey_trouble,
    near_hundred,
    parrot_trouble,
    pos_neg,
    sleep_in,
    sum_double,
)


class WarmupTests(unittest.TestCase):
    def test_sleep_in(self):
        self.assertTrue(sleep_in(False, False))
        self.assertFalse(sleep_in(True, False))
        self.assertTrue(sleep_in(True, True))

    def test_monkey_trouble(self):
        self.assertTrue(monkey_trouble(True, True))
        self.assertTrue(monkey_trouble(False, False))
        self.assertFalse(monkey_trouble(True, False))

    def test_sum_double(self):
        self.assertEqual(sum_double(1, 2), 3)
        self.assertEqual(sum_double(3, 3), 12)

    def test_diff21(self):
        self.assertEqual(diff21(19), 2)
        self.assertEqual(diff21(25), 8)

    def test_parrot_trouble(self):
        self.assertTrue(parrot_trouble(True, 6))
        self.assertFalse(parrot_trouble(True, 7))
        self.assertFalse(parrot_trouble(False, 6))

    def test_makes10(self):
        self.assertTrue(makes10(9, 1))
        self.assertTrue(makes10(10, 0))
        self.assertFalse(makes10(3, 4))

    def test_near_hundred(self):
        self.assertTrue(near_hundred(93))
        self.assertTrue(near_hundred(190))
        self.assertFalse(near_hundred(89))

    def test_pos_neg(self):
        self.assertTrue(pos_neg(1, -1, False))
        self.assertFalse(pos_neg(-1, -1, False))
        self.assertTrue(pos_neg(-1, -1, True))


if __name__ == "__main__":
    unittest.main()
