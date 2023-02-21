def calculate(first_operand, second_operand, operation):   
    match operation:
        case "add":
            return first_operand + second_operand
        case "sub":
            return first_operand - second_operand
        case "mult":
            return first_operand * second_operand
        case "div":
            if second_operand == 0:
                raise Exception("Can't divide by zero")
            return first_operand / second_operand
        case _:
            raise Exception("Unknown operation")