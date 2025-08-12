text = input()

letters_set = set()

for letter in text:
    letters_set.add(letter)

for ch in sorted(letters_set):
    print(f"{ch}: {text.count(ch)} time/s")

