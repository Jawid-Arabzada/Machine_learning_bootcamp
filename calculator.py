class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def multi(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a/b
        else:
            print("divsion by zero")


print("welcome to basic calculator app using Class in python: ")
print("Please choose an operation: 1:Add  2:Substraction 3:Multiplication  4:Division")
choice = int(input("Enter Your Choice between (1-4)"))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
calcs = Calculator()

if choice == 1:
    print(f"{num1} + {num2} = ", calcs.add(num1, num2))
elif choice == 2:
    print(f"{num1} - {num2} = ", calcs.sub(num1, num2))
elif choice == 3:
    print(f"{num1} * {num2} = ", calcs.multi(num1, num2))
elif choice == 4:
    print(f"{num1} / {num2} = ", calcs.divide(num1, num2))
