import time

def add(x, y):
    return x + y

def substarct(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def divide(x, y):
    return x / y

print("select desired option from below... please wait...")
time.sleep(1)
print(" ")
print("1.add")
print('2.substarct')
print("3.multiplication")
print("4.divide")
time.sleep(2)

print(" ")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
else:
            print("Invalid Input")
