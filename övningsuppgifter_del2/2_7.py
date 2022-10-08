word = input("write a word")
word = word.lower()
while word != "exit":
    if word == word[::-1]:
        print("is a palindrome")
        word = input("write a word")
        word = word.lower()
    else:
        print("is not palindrome")
        word = input("write a word")
        word = word.lower()