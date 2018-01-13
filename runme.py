from static_class import StaticClass

##  TODO
#   [ ] Multiple mocks (illustrate inverted order of mock names...)
#   [ ] Mock return value sequence
#       https://docs.python.org/3/library/unittest.mock-examples.html#side-effect-functions-and-iterables
#   [ ] Setup/teardown

def main():
    StaticClass.staticMethod()
    StaticClass.staticMethodWithStringArg("Hello World!")
    StaticClass.staticMethodWithNumArg(45)
    #print("Done!")

if __name__ == "__main__":
     main()


