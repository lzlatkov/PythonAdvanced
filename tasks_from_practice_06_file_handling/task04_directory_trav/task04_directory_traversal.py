import os

files = {}
directory = "../"

for el in os.listdir(directory):
    file = os.path.join(directory, el)
    if os.path.isfile(file):
        ext = el.split(".")[-1]
        if ext not in files:
            files[ext] = []
        files[ext].append(el)
    else:
        for element in os.listdir(file):
            filename = os.path.join(file, element)
            if os.path.isfile(filename):
                ext = element.split(".")[-1]
                if ext not in files:
                    files[ext] = []
                files[ext].append(element)

print(files)
