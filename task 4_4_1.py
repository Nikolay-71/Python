a = [56, 0, 1, 20, 4, 11, 0, 11, 6, 15, 4, 56]
my_set = [i for n, i in enumerate(a) if i not in a[n + 1:]]
print(my_set)
