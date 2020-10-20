class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.my_list]))

    def __add__(self, mat_2):
        for i in range(len(self.my_list)):
            for j in range(len(mat_2.my_list[i])):
                self.my_list[i][j] = self.my_list[i][j] + mat_2.my_list[i][j]
        return Matrix.__str__(self)


mat = Matrix([[10, 5, 6], [5, 7, 8]])
mat_2 = Matrix([[10, 3, 5], [4, 10, 2]])
print(mat.__add__(mat_2))
