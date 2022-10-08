def find_letter(char, letter_list):
    if char in letter_list:
        return True
    else:
        return False

print(find_letter("b", ["h", "o", "u", "s", "e"]))