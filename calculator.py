num1: float = float(input('Enter number 1: '))
num2: float = float(input('Enter number 2: '))

print(num1)
print(num2)

def sum(num1: float, num2: float):
    return num1 + num2

def minus(num1: float, num2: float):
    return num1 - num2

print(f'Sum of num1 and num 2 is:{sum(num1, num2)}')
print('Subtraction of num1 and num 2 is:', minus(num1, num2))