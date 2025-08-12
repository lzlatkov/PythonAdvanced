from collections import deque

parenthesis = deque(input())

open_parenthesizes = deque()

while parenthesis:
    current_parenthesis = parenthesis.popleft()

    if current_parenthesis in "([{":
        open_parenthesizes.append(current_parenthesis)
    elif not open_parenthesizes:
        print("NO")
        break
    else:
        if f"{open_parenthesizes.pop() + current_parenthesis}" not in "()[]{}":
            print("NO")
            break
else:
    print("YES")