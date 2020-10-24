class My_class:
    def __init__(self, *args):
        self.list = []

    def my_inp(self):

        while True:
            try:
                a = int(input("Введите данные"))
                self.list.append(a)
                print(f"{self.list} \n ")
            except:
                print(f"Ошибка ввода:некорректные данные")
                s = input(f"Если хотите закончить нажмите-s  ").lower()
                if s != "s":
                    print(f.my_inp())
                else:
                    return f"The end"


f = My_class()
print(f.my_inp())
