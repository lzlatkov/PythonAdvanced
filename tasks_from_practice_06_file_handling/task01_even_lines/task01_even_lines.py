# Logic
with open("txt_task01.txt") as f:
    for row, line in enumerate(f):
        if row % 2 == 0:
            for el in "-,.?":
                line = line.replace(el, "@")
            print(" ".join(reversed(line.split())))

