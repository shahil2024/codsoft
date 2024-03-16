# 1. ADD
# 2. SUBTRACT
# 3. MULTIPLY
# 4. DIVISION
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multply(x,y):
    return x * y

def division(x,y):
    if y == 0:
        return "Error! Division by Zero."
    else:
        return x / y

print("select an operation to perform: ")
print("1. ABB")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVISION")

while True:
    operation = input("Enter operation (1/2/3/4): ")

    if operation == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(add(num1, num2))

    elif operation == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(subtract(num1, num2))

    elif operation == "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(multply(num1, num2))

    elif operation == "4":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(division(num1, num2))

    else:
        print("Invalid Entry")

