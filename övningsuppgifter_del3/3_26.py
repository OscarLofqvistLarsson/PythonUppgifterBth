def add_dashes(word):
    if len(word) == 0:
        return ""
    if len(word) == 1:
        return word
    return add_dashes(word[0]) + "-" + add_dashes(word[1:])
print(add_dashes("duck"))