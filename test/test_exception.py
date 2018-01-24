import unittest
from unittest.mock import Mock, patch, MagicMock
import runme

class TestException(unittest.TestCase):

    def setUp(self):
        ## Whatever goes here gets run before every test case
        pass

    def tearDown(self):
        ## Whatever goes here gets run after every test case
        pass

    def test_exception(self):
        with self.assertRaises(runme.RunMeException) as context:
            runme.functionThatThrowsException()

        self.assertTrue('This is an exception' in str(context.exception))

if __name__ == '__main__':
    unittest.main()

