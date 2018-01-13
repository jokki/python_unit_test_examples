from static_class import StaticClass
from instance_class import InstanceClass

##  TODO
#   [ ] Multiple mocks (illustrate inverted order of mock names...)
#   [ ] Exceptions
#   [ ] Setup/teardown
#   [ ] Alternative to 'patch' when mocking
#   [ ] Document usage in README

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

def main():
    useStaticClass()
    dontcare = useInstanceClass()
    print("Done!")

if __name__ == "__main__":
     main()


