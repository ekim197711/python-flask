import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        myvar = 2
        self.assertEqual(2, myvar)


if __name__ == '__main__':
    unittest.main()
