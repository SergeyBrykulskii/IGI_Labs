from calculation_func import calculate 

first_operand = input("Enter first number:   ")
second_operand = input("Enter second number:  ")
operator = input("Enter one of the operations(add/sub/mult/div):    ")


print(calculate(first_operand, second_operand, operator))
