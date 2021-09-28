import unittest

class Testfact(unittest.TestCase):

    def test_00(self):
        self.assertEqual(fact(4),24)

    def test_01(self):
        self.assertEqual(fact(5),120)

    def test_02(self):
        self.assertEqual(fact(1),1)

if __name__ == '__main__':
    unittest.main()
