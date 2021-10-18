import sys

try:
    x = int(input("number: "))
    y = int(input("number: "))
except ValueError:
    print(f"error: invalid input")
    sys.exit(1)

try:
    result = x * y
except ZeroDivisionError:
    print(f"error: finded zero division error")
    sys.exit(1)

print(f"results of {x} * {y} is equal to {result}")

