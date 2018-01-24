import unittest
from unittest.mock import Mock, patch, MagicMock
import runme

class TestStaticMethods(unittest.TestCase):

    def setUp(self):
        ## Whatever goes here gets run before every test case
        pass

    def tearDown(self):
        ## Whatever goes here gets run after every test case
        pass

    @unittest.skip("Demonstrating skipping")
    def test_failMe(self):
        ## Test will produce a 's' in test output to denote the skipped test
        self.fail("This test is supposed to be skipped so this should not happen!")

    @patch('runme.StaticClass.staticMethod')
    def test_callStaticMethod(self, mockStaticMethod):
        runme.useStaticClass()
        mockStaticMethod.assert_called()

    @patch('runme.StaticClass.staticMethodWithStringArg')
    def test_callStaticMethodWithStringArg(self, mockStaticMethodWithStringArg):
        runme.useStaticClass()
        mockStaticMethodWithStringArg.assert_called_once_with("Hello World!")

    @patch('runme.StaticClass.staticMethodWithNumArg')
    def test_callStaticMethodWithNumArg(self, mockStaticMethodWithNumArg):
        runme.useStaticClass()
        mockStaticMethodWithNumArg.assert_called_once_with(45)

if __name__ == '__main__':
    unittest.main()

