with open("test_2.txt", "r") as f:
    word = 0
    count = 0
    for a in f.readlines():
        count += 1
        f1 = a.split()
        word = len(f1)
        print(f'Количество слов: {word} {a}',sep=" ")
    print("Всего количество строк:", count)
