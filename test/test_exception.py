import unittest
from unittest.mock import Mock, patch, MagicMock
import runme

class TestException(unittest.TestCase):

    def test_exception(self):
        with self.assertRaises(runme.RunMeException) as context:
            runme.functionThatThrowsException()

        self.assertTrue('This is an exception' in str(context.exception))

if __name__ == '__main__':
    unittest.main()

