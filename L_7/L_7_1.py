class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
             raise ValueError("matrices should be the same size")
        result = []
        for i in range(len(self.matrix)):
            row_1 = self.matrix[i]
            row_2 = other.matrix[i]
            if len(row_1) != len(row_2):
                raise ValueError("matrices should be the same size")
            result_row = []
            for j in range(len(row_1)):
                result_row.append(row_1[j] + row_2[j])
            result.append(result_row)
        return Matrix(result)

    def __str__(self):
        result = ""
        for row in self.matrix:
            for cell in row:
                result += str(cell) + "\t"
            result += "\n"
        return result


matrix_1 = Matrix([[31, 22], [37, 43], [51, 86]])
matrix_2 = Matrix([[3, 5], [32, 6], [76, 4]])

print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)

