from calculation_func import calculate 
from constants import OPERATIONS

while True:
    try:
        first_operand = float(input("Enter first number:   "))
        second_operand = float(input("Enter second number:  "))
        break
    except:
        print("Please, enter correct numbers")
while True:   
    operator = input("Enter one of the operations(add/sub/mult/div):    ")
    if operator not in OPERATIONS:
        print("Incorrect operation")
    else: 
        break


print(calculate(first_operand, second_operand, operator))
