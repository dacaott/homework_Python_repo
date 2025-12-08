class Matrix:
    def __init__(self, rows):
        # инициализация и преобразование элементов в float
        self.rows = [list(map(float, r)) for r in rows]
        if len(self.rows) == 0:
            self.n = 0
            self.m = 0
        else:
            self.n = len(self.rows)
            self.m = len(self.rows[0])

    def __repr__(self):
        return f"Matrix({self.rows})"

    def __iter__(self):
        return iter(self.rows)

    def __eq__(self, other):
        return self.rows == other.rows

    def __add__(self, other):
        result = []
        for i in range(self.n):
            row = []
            for j in range(self.m):
                row.append(self.rows[i][j] + other.rows[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[x * other for x in row] for row in self.rows])
        result = []
        for i in range(self.n):
            row = []
            for j in range(other.m):
                s = 0
                for k in range(self.m):
                    s += self.rows[i][k] * other.rows[k][j]
                row.append(s)
            result.append(row)
        return Matrix(result)

    def __rmul__(self, other):
        return self * other

    def determinant(self):
        if self.n != self.m:
            raise ValueError("Matrix must be square!")

        if self.n == 1:
            return self.rows[0][0]
        if self.n == 2:
            return self.rows[0][0] * self.rows[1][1] - self.rows[0][1] * self.rows[1][0]

        total = 0
        for col in range(self.m):
            # создание подматрицы без первой строки и исключенного столбца
            excluded_column = self._get_excluded_column(self.rows, col)
            sign = (-1) ** col
            total += sign * self.rows[0][col] * Matrix(excluded_column).determinant()

        return total

    def _get_excluded_column(self, matrix_rows, col_to_exclude):
        # создается подматрица без первой строки и указанного столбца
        result_rows = []
        for i in range(1, self.n):  # пропускаем первую строку
            row = []
            for j in range(self.m):
                if j != col_to_exclude:
                    row.append(matrix_rows[i][j])
            result_rows.append(row)
        return result_rows
