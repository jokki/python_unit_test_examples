import unittest

class OtherStuff(unittest.TestCase):

    def test_SimpleAssertDemo(self):
        self.assertEqual(1, 1, "One should equal one!")


if __name__ == '__main__':
    unittest.main()

