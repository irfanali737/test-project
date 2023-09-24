def take_input():
    num1: float = float(input('Enter Number 1: '))
    num2: float = float(input('Enter Number 2: '))
    operation: str = input('Select Operator? (+, -, *, /) ')
    return num1, num2, operation

def sum(num1: float, num2: float):
    return num1 + num2

def minus(num1: float, num2: float):
    return num1 - num2

def multiply(num1: float, num2: float):
    return num1 * num2

def division(num1: float, num2: float):
    return num1 / num2

def display_calculator_output(num1, num2, operation):
    if operation == '+':
        result: float = sum(num1, num2)
    elif operation == '-':
        result: float = minus(num1, num2)
    elif operation == '*':
        result: float = multiply(num1, num2)
    elif operation == '/':
        result: float = division(num1, num2)

    print(f'Result = {result}')


if __name__ == '__main__':
    flag:str = 'y'
    while True:
        if flag.lower() == 'Y'.lower():
            x, y, operation = take_input()
            display_calculator_output(x, y, operation)
        else:
            print(f'Thank you')
            break
        flag: str = input('Continue (Y/N)')
    
