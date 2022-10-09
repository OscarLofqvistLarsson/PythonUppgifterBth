from operator import invert


def invert_dictionary(dict):
    inverted = {}
    for key in dict:
        if dict[key] in inverted:
            inverted[dict[key]].append(key)
        else:
            inverted[dict[key]] = [key]
        for ikey in inverted:
            inverted[ikey].sort()
    return inverted

print(invert_dictionary({'a':2, 'b':1, 'c':2, 'd':1}))