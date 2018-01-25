# Python Unit Test Examples
Some examples that can be used to get started with unit tests in Python. Mostly this project demonstrates different mocking scenarios. Full a description of available features see Python [documentation](https://docs.python.org/3/library/unittest.html) pages listed in the references below.

Because copying code is better than writing code!

# Usage
The tests should have fairly explanatory names to hint the exemplified scenario. Run the test by stepping into the root directory of the project and running

    $ python -m unittest discover test
    
More generally, you can run tests from anywhere

    $ PYTHONPATH=$PYTHONPATH:path/to/your/code python -m unittest discover path/to/your/tests
    
Assuming you are in the project root of this project, you can run a specific test suite like this

    $ PYTHONPATH=$PYTHONPATH:. python test/test_exception.py
    
Or, a specific test case of a specific test suite like this

    $ PYTHONPATH=$PYTHONPATH:. python test/test_exception.py TestException.test_exception
    
Adding current path "." to 'PYTHONPATH' seems to be necessary or the Python interpreter won't find the code under test.

# References
https://docs.python.org/3/library/unittest.html<br>
https://docs.python.org/3/library/unittest.mock.html
