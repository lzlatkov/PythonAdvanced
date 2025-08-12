# Read user input
from collections import deque
strength = [int(x) for x in input().split()]
accuracy = deque([int(x) for x in input().split()])
result = 0
goals = 0
# Logic
while strength and accuracy:
    current_strength = strength[-1]
    current_accuracy = accuracy[0]
    result = current_strength + current_accuracy
    if result == 100:
        strength.pop()
        accuracy.popleft()
        goals += 1
    elif result < 100:
        if current_strength < current_accuracy:
            strength.pop()
        elif current_strength > current_accuracy:
            accuracy.popleft()
        elif current_strength == current_accuracy:
            strength[-1] = current_strength + current_accuracy
            accuracy.popleft()
    else:
        strength[-1] -= 10
        accuracy.append(accuracy.popleft())

# Print output
if goals == 3:
    print("Paul scored a hat-trick!")
elif goals == 0:
    print(f"Paul failed to score a single goal.")
elif goals > 3:
    print(f"Paul performed remarkably well!")
else:
    print("Paul failed to make a hat-trick.")
if goals:
    print(f"Goals scored: {goals}")

if strength:
    print(f"Strength values left: {', '.join([str(x) for x in strength])}")
elif accuracy:
    print(f"Accuracy values left: {', '.join([str(x) for x in accuracy])}")
