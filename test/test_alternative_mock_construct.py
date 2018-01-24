import unittest
from unittest.mock import Mock, patch, MagicMock
import instance_class
import runme

class TestInstanceMethodsAlternative(unittest.TestCase):

    def test_alternativeMockingConstruct(self):
        with patch.object(instance_class.InstanceClass, 'someInstanceMethod',
                                return_value = 'Mocked result') as mockSomeInstanceMethod:
            result = runme.useInstanceClass()
            self.assertEqual(result, 'Mocked result', "Unexpected result")

if __name__ == '__main__':
    u
