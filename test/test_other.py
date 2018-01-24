import unittest

class OtherStuff(unittest.TestCase):

    def setUp(self):
        ## Whatever goes here gets run before every test case
        pass

    def tearDown(self):
        ## Whatever goes here gets run after every test case
        pass

    def test_SimpleAssertDemo(self):
        self.assertEqual(1, 1, "One should equal one!")


if __name__ == '__main__':
    unittest.main()

