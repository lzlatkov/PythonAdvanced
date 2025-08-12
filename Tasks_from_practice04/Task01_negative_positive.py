numbers = [int(num) for num in input().split()]  ###### map(int, input().split())


def sums_numbers(*args):
    # positive_nums = sum([num for num in args if num > 0])
    # negative_nums = sum([num for num in args if num < 0])
    positive_nums = 0
    negative_nums = 0
    for num in args:
        if num > 0:
            positive_nums += num
        else:
            negative_nums += num

    return negative_nums, positive_nums


negative_nums, positive_nums = sums_numbers(*numbers)

print(negative_nums)
print(positive_nums)
if abs(negative_nums) > abs(positive_nums):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
