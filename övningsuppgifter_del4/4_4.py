import os
paths = os.listdir("C:/Test")
for item in paths:
    print(item)


directory = "C:/Test"
items = os.listdir(directory)
for item in items:
    path = directory + '/' + item
    print(path, ', ' , os.path.isdir(path))