def palindrome(string):
    string = string.lower()
    if len(string) < 2:
        return True
    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False
print(palindrome("level"))