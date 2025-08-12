text = input()
stack = []

for index in range(len(text)):
    if text[index] == "(":
        stack.append(index)
    elif text[index] == ")":
        # recent_parentheses = stack.pop()
        print(text[stack.pop():index + 1])