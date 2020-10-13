with open("text_5.txt", "w", encoding='utf-8') as f:
    b = ("5", " ", "6", " ", "6", " ", "8", " ", "15", " ", "25")
    print(b)
    f.writelines(b)
with open("text_5.txt", "r", encoding='utf-8') as c:
    for a in c:
        sum = sum(map(int, a.split(" ")))
        print(sum)

