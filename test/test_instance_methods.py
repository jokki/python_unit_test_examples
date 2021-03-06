import unittest
from unittest.mock import Mock, patch, MagicMock
import runme

class TestInstanceMethods(unittest.TestCase):

    def setUp(self):
        ## Whatever goes here gets run before every test case
        pass

    def tearDown(self):
        ## Whatever goes here gets run after every test case
        pass

    @patch('runme.InstanceClass')
    def test_constructor(self, mockInstanceClass):
        runme.useInstanceClass()
        mockInstanceClass.assert_called()

    @patch('runme.InstanceClass')
    def test_callInstanceMethodUsingCustomMockClass(self, mockInstanceClass):

        class CustomMockClass():

            def __init__(self):
                self.someInstanceMethodCalled = False

            def someInstanceMethod(self, arg):
                self.someInstanceMethodCalled = True
                return "Custom mock object!"

            def multiArgInstanceMethod(self, a, b):
                pass

            def isCalled(self):
                return self.someInstanceMethodCalled

        customMock = CustomMockClass()
        mockInstanceClass.return_value = customMock
        runme.useInstanceClass()
        self.assertTrue(customMock.isCalled())

    @patch('runme.InstanceClass.someInstanceMethod')
    def test_instanceMethodReturnValue(self, mockInstanceMethod):
        mockMessage = "Mocked method!"
        mockInstanceMethod.return_value = mockMessage
        result = runme.useInstanceClass()
        self.assertEqual(result, mockMessage, "Unexpected result!")

    @patch('runme.InstanceClass.someInstanceMethod')
    def test_instanceMethodArg(self, mockInstanceMethod):
        dontCare = "Don't care"
        mockInstanceMethod.return_value = dontCare
        result = runme.useInstanceClass()
        mockInstanceMethod.assert_called_once_with(99)

    @patch('runme.InstanceClass.multiArgInstanceMethod')
    def test_multiArgInstanceMethodArgs(self, mockMultiArgInstanceMethod):
        dontCare = "Don't care"
        mockMultiArgInstanceMethod.return_value = dontCare
        result = runme.useInstanceClass()
        mockMultiArgInstanceMethod.assert_called_once_with(1, 2)

    @patch('runme.InstanceClass.getNext')
    def test_multiCall(self, mockGetNext):
        mockGetNext.side_effect = [4, 5, 6]
        self.assertEqual(15, runme.addStuff(), "Wrong result!")

if __name__ == '__main__':
    unittest.main()
