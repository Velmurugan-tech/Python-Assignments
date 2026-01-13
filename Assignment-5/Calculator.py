def Add(a, b):
    return a + b

def Sub(a, b):
    return a - b

def Multiply(a, b):
    return a * b

def Division(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


while True:
    print("\n1. Add 2. Sub 3. Multiply 4. Division 5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 5:
        break

    a = float(input("Enter num1: "))
    b = float(input("Enter num2: "))

    try:
        match choice:
            case 1:
                print(Add(a, b))
            case 2:
                print(Sub(a, b))
            case 3:
                print(Multiply(a, b))
            case 4:
                print(Division(a, b))
            case _:
                print("Invalid option")

    except ZeroDivisionError as e:
        print("Invalid Operands",e)
