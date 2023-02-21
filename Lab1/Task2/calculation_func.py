def calculate(first_operand, second_operand, operation):
    operations = ("add", "sub", "mult", "div")

    if not first_operand.isdigit() or not second_operand.isdigit():
        return None
    if not operation in operations:
        return None

    first_operand = float(first_operand)
    second_operand = float(second_operand)
    
    match operation:
        case "add":
            return first_operand + second_operand
        case "sub":
            return first_operand - second_operand
        case "mult":
            return first_operand * second_operand
        case "div":
            return first_operand / second_operand