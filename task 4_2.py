a = [20, 1, 7, 4, 5, 8, 11, 7, 15]
b = [i for i in a[1:] if i > a[a.index(i)-1]]
print(b)