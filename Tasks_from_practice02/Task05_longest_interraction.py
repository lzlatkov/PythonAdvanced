count = int(input())

longest_intersection = set()

for _ in range(count):
    ranges = input().split("-")
    first_start, first_end = [int(x) for x in ranges[0].split(",")]
    second_start, second_end = [int(x) for x in ranges[1].split(",")]

    first_set = set(range(first_start, first_end + 1))
    second_set = set(range(second_start, second_end + 1))

    current_intersection = first_set & second_set

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")
