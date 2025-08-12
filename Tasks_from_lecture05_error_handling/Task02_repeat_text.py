user_input = input()

try:
    repeat_times = int(input())

except ValueError:
    print("Variable times must be an integer")
else:
    print(user_input * repeat_times)