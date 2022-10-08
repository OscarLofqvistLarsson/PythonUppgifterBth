def count_e(str):
    count = 0
    for i in str:
        if i =="e":
            count +=1
    return count

print(count_e("hello world"))