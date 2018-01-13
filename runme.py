from static_class import StaticClass
from instance_class import InstanceClass

##  TODO
#   [ ] Multiple mocks (illustrate inverted order of mock names...)
#   [ ] Mock return value sequence
#       https://docs.python.org/3/library/unittest.mock-examples.html#side-effect-functions-and-iterables
#   [ ] Setup/teardown

def useStaticClass():
    StaticClass.staticMethod()
    StaticClass.staticMethodWithStringArg("Hello World!")
    StaticClass.staticMethodWithNumArg(45)

def useInstanceClass():
    x = InstanceClass()
    dontcare = x.multiArgInstanceMethod(1, 2)
    return x.someInstanceMethod(99)

def main():
   print("Done!")

if __name__ == "__main__":
     main()


