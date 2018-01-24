import unittest
from unittest.mock import Mock, patch, MagicMock
import instance_class
import runme

class TestInstanceMethodsAlternative(unittest.TestCase):

    def setUp(self):
        ## Whatever goes here gets run before every test case
        pass

    def tearDown(self):
        ## Whatever goes here gets run after every test case
        pass

    def test_alternativeMockingConstruct(self):
        with patch.object(instance_class.InstanceClass, 'someInstanceMethod',
                                return_value = 'Mocked result') as mockSomeInstanceMethod:
            result = runme.useInstanceClass()
            self.assertEqual(result, 'Mocked result', "Unexpected result")

if __name__ == '__main__':
    u
