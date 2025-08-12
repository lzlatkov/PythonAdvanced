numbers = tuple(float(x) for x in input().split())
numbers_dictionary = {}

for num in numbers:
    numbers_dictionary[num] = numbers.count(num)

for key, value in numbers_dictionary.items():
    print(f"{key} - {value} times")

