import unittest
from add import add


class TestAddFunction(unittest.TestCase):

    def test1(self):
        self.assertEqual(add(2, 3), 5)

    def test2(self):
        self.assertEqual(add(1, -1), 0)


if __name__ == '__main__':
    unittest.main()
