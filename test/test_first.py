import unittest
from unittest.mock import Mock, patch, MagicMock
import runme

class TestStaticMethods(unittest.TestCase):

    @unittest.skip("Demonstrating skipping")
    def test_FailMe(self):
        self.fail("This test is supposed to be skipped so this should not happen!")

    @patch('runme.StaticClass.staticMethod')
    def test_callStaticMethod(self, mockStaticMethod):
        runme.main()
        mockStaticMethod.assert_called()

class OtherStuff(unittest.TestCase):

    def test_SimpleAssertDemo(self):
        self.assertEqual(1, 1, "One should equal one!")


if __name__ == '__main__':
    unittest.main()

