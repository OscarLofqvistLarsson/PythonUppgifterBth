def convert(char):

    get_num = ord(char)
    num = get_num - 32
    upper = chr(num)

    return upper

print(convert("h"))