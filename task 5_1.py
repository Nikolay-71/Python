with open("task 5_1.txt", "w") as f_obj:
    lines = []
    while True:
        a = input("Укажите фамилию: ")
        if a == "":
            exit()
        else:
            lines.append(a)
            f_obj.writelines("%s\n" % a for a in lines)