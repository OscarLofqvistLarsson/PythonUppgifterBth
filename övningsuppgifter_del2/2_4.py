def search(str, substring):
    if substring in str:
        return str.index(substring)
    else:
        return -1

print(search("alligator", "g"))