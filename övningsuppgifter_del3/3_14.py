def count_instances(DNA):
    res = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
    for key in DNA:
           res[key] += 1
    return res

print(count_instances("CTATCGGCACCCTTTCAGCA"))