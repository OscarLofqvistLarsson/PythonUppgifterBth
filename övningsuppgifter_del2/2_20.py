letter_list =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def encrypt(msg, key):
    content = msg.upper()
    encrypted = ""
    for char in content:
        if char in letter_list:
            encrypted += letter_list[(letter_list.index(char) + key) % len(letter_list)]
        else:
            encrypted += char

    return encrypted

def decrypt(msg, key):
    content = msg.upper()
    decrypted = ""
    for char in content:
        if char in letter_list:
            decrypted += letter_list[(letter_list.index(char) - key) % len(letter_list)]
        else:
            decrypted += char

    return decrypted


print(encrypt("Welcome to the dark side", 5))
print(decrypt("BJQHTRJ YT YMJ IFWP XNIJ", 5))