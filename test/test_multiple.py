import unittest
from unittest.mock import Mock, patch, MagicMock
import runme

class TestMultipleMockObjects(unittest.TestCase):

    def setUp(self):
        ## Whatever goes here gets run before every test case
        pass

    def tearDown(self):
        ## Whatever goes here gets run after every test case
        pass

    # Note that
    #
    #   "When you nest patch decorators the mocks are passed in to
    #   the decorated function in the same order they applied (the normal python
    #   order that decorators are applied). This means from the bottom up..."
    #
    # https://docs.python.org/3/library/unittest.mock.html
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

