def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def divide(a,b):
    return a / b

def multiply(a,b):
    return a * b

def power(a,b):
    return a ** b
def printresult(result):
    print("Result: " + str(result))

first = "Enter first number: "
second = "Enter second number: "


print("================")
print("CALCULATOR")
print("================")
print("1) Add")
print("2) Subtract")
print("3) Divide")
print("4) Multiply")
print("5) Power")
print("6) Exit")

choice = 0
while choice != 6:
    choice = int(input("Enter choice : "))

    match choice:
        case 1:
                a = float(input(first))
                b = float(input(second))
                printresult(add(a,b))
                                
        case 2:
                a = float(input(first))
                b = float(input(second))
                printresult(sub(a,b))

        case 3:
                a = float(input(first))
                b = float(input(second))
                printresult(divide(a,b))

        case 4:
                a = float(input(first))
                b = float(input(second))
                printresult(multiply(a,b))
        case 5:
                a = float(input(first))
                b = float(input(second))
                printresult(power(a,b))
        case 6:
                print("Exiting Calculator...")
                exit()
        case _ :
                print("Invalid choice. Please enter a choice between 1-6.")              