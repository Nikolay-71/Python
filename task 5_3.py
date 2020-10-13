with open("text_3.txt", "r", encoding='utf-8') as f:
    sal2 = []
    for a in f:
        name, sal = a.split()
        sal = float(sal)
        if sal < 20_000:
            print(name, sal)
        sal2.append(sal)
    print(f"Средняя: {sum(sal2)/len(sal2)}")

