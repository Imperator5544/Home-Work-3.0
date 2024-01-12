number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))


operation = input("Enter a math operation (+, -, *, /): ")


match operation:
    case '+':
        result = number1 + number2
        print(f"Addition result: {result}")
    case '-':
        result = number1 - number2
        print(f"Subtraction result: {result}")
    case '*':
        result = number1 * number2
        print(f"The result of multiplication: {result}")
    case '/' if number2 != 0:
        result = number1 / number2
        print(f"The result of division: {result}")
    case '/':
        print("Division by 0 is impossible.")
    case _:
        print("An incorrect mathematical operation was entered.")