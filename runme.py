from static_class import StaticClass
from instance_class import InstanceClass

##  TODO
#   [ ] Multiple mocks (illustrate inverted order of mock names...)
#   [X] Exceptions
#   [X] Setup/teardown
#   [X] Alternative to 'patch' when mocking
#   [ ] Document usage in README

class RunMeException(Exception):
    pass

def useStaticClass():
    StaticClass.staticMethod()
    StaticClass.staticMethodWithStringArg("Hello World!")
    StaticClass.staticMethodWithNumArg(45)

def useInstanceClass():
    x = InstanceClass()
    dontcare = x.multiArgInstanceMethod(1, 2)
    return x.someInstanceMethod(99)

def addStuff():
    result = 0
    x = InstanceClass()

    for n in range(0, 3):
        result = result + x.getNext()

    return result

def useBoth():
    x = InstanceClass()
    StaticClass.staticMethodWithStringArg("Hello Another World!")
    x.someInstanceMethod(11)

def functionThatThrowsException():
    raise RunMeException("This is an exception")

def main():
    useStaticClass()
    dontcare = useInstanceClass()
    print("Done!")

if __name__ == "__main__":
     main()


