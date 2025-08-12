# def recursive_power(num, power):
#         return num ** power


def recursive_power(num, power):
    if power == 1:
        return num
    result = num * recursive_power(num, power - 1)
    return result
print(recursive_power(2, 10))