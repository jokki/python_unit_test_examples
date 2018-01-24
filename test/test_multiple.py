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

    @patch('runme.StaticClass.staticMethodWithStringArg')
    @patch('runme.InstanceClass')
    def test_callStaticMethodWithStringArg(self, mockInstanceClass, mockStaticMethodWithStringArg):
        instanceMock = Mock()
        mockInstanceClass.return_value = instanceMock

        runme.useBoth()
        
        mockStaticMethodWithStringArg.assert_called_once_with("Hello Another World!")
        instanceMock.someInstanceMethod.assert_called_once_with(11)

if __name__ == '__main__':
    unittest.main()

