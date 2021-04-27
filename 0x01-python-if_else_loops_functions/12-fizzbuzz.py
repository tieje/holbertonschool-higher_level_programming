#!/usr/bin/python3
def fizzbuzz():
    printThis = "a"
    for i in range(1, 101):
        if i % 15 == 0:
            printThis = "FizzBuzz"
        elif i % 3 == 0:
            printThis = "Fizz"
        elif i % 5 == 0:
            printThis = "Buzz"
        else:
            printThis = str(i)
        print(printThis, end=" ")
    return


fizzbuzz()
