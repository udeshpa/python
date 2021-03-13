import unittest
import unittesting.calc as calc


class TestCalc(unittest.TestCase):
    def test_add(self):       #name must start with test
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(2, -1), 1)

    def test_divide(self):
        self.assertRaises(ValueError, calc.divide, 1, 0)
        with self.assertRaises(ValueError):
              calc.divide(10,0)


if __name__ == '__main__':
    unittest.main()
