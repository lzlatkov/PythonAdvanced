from collections import deque

names = deque(input().split())
toss = int(input())


while len(names) > 1:
    # for _ in range(toss - 1):
    #     kid = names.popleft()
    #     names.append(kid)
    # print(f"Removed {names.popleft()}")
    names.rotate(-toss)
    print(f"Removed {names.popleft()}")
print(f"Last is {names.popleft()}")