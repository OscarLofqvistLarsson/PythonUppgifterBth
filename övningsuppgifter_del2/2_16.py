def sum_last_dig(int_list):
    total = 0
    for num in int_list:
        num %= 10
        total += num

    return total

print(sum_last_dig([1, 2, 10]))
