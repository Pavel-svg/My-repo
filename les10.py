# 1
list_1 = [[1, 2, 3, 4], [3, 4, 2, 4], [5, 6, 8, 1]]
list_2 = [[7, 7, 4, 5], [5, 1, 4, 2], [1, 2, 1, 0]]


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return ('\n'.join(map(str, self.matrix))).replace(',', ' ')

    def __add__(self, other):
        c = []
        for i in range(len(self.matrix)):
            c.append([])
            for j in range(len(self.matrix[0])):
                c[i].append(self.matrix[i][j] + other.matrix[i][j])
        return ('\n'.join(map(str, c)).replace(',', ' '))


matrix_1 = Matrix(list_1)
matrix_2 = Matrix(list_2)
print(matrix_1)
print()
print(matrix_1 + matrix_2)



print("-" * 50)

# 2
class Clothes:
    def __init__(self, name_clothes):
        self.name_clothes = name_clothes

    # def name(self):
    #    print(self, name_clothes)


class Coat(Clothes):
    def __init__(self, name_clothes, size):
        super().__init__(name_clothes)
        self.size = size

    @property
    def the_size(self):
        return (self.size / 6.5 + 0.5)


class Suit(Clothes):
    def __init__(self, name_clothes, height):
        super().__init__(name_clothes)
        self.height = height

    @property
    def the_coat(self):
        return (2 * self.height + 0.3)


a = Coat("Coat:", 10)
print(a.the_size)

b = Suit("Suit", 20)
print(b.the_coat)


print("-" * 50)

#3
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity) #целое число

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        if sub > 0:
            return sub
        else:
            return "Only positive number"

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __floordiv__(self, other):
        return self.quantity // other.quantity

    def make_order(self, rows):
        return '\n'.join(['*' * rows for i in range(self.quantity // rows)]) + '\n' + '*' * (self.quantity % rows)

cell_1 = Cell(30)
cell_2 = Cell(20)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1.make_order(5))
