try:
    number1 = float(input("enter a number "))
    operator = str(input("choose an operator(+, -, *, /)"))
    number2= float(input("enter another number"))

    if operator=="+":
        print(number1 + number2)
    elif operator=="-":
        print(number1 - number2)
    elif operator=="*":
        print(number1 * number2)
    elif operator == "/" and number2 == 0:
        print("cannot divide by zero")
    elif operator=="/":
        print(number1 / number2)

except ValueError:
    print("Invalid input")
