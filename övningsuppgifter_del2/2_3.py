def count_char(str, char):
    count = 0
    for i in str:
        if i ==char:
            count +=1
    return count

print(count_char("hello world","l"))