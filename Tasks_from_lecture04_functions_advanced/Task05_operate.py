from functools import reduce


def operate(operator, *args):
    def sum_numbers():
        # return sum(args)
        return reduce(lambda x, y: x + y, args)

    def subtract_numbers():
        return reduce(lambda x, y: x - y, args)

    def multiply_numbers():
        return reduce(lambda x, y: x * y, args)

    def divide_numbers():
        return reduce(lambda x, y: x / y, args)

    if operator == "+":
        return sum_numbers()
    elif operator == "-":
        return subtract_numbers()
    elif operator == "*":
        return multiply_numbers()
    elif operator == "/":
        return divide_numbers()


print(operate("*", 3, 4))