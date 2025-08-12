count = int(input())
elements_set = set()

for _ in range(count):
    element = input().split()
    for el in element:
        elements_set.add(el)

print(*elements_set, sep='\n')

####################################################################################
elements = [x for x in range(int(input())) for x in input().split()]
elements_set = set()

for element in elements:
    elements_set.add(element)

print(*elements_set, sep="\n")
###################################################################################
print(*{el for _ in range(int(input())) for el in input().split()}, sep="\n")