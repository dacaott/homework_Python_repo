class Matrix:
    def __init__(self, rows):
        self.rows = [list(map(float, r)) for r in rows]
        if len(self.rows) == 0:
            self.n = 0
            self.m = 0
        else:
            self.n = len(self.rows)
            self.m = len(self.rows[0])

    def __repr__(self):
        return f"Matrix({self.rows})"

    # итерация по строкам
    def __iter__(self):
        for r in self.rows:
            yield r

    def __eq__(self, other):
        return self.rows == other.rows

    # сложение
    def __add__(self, other):
        result = []
        for i in range(self.n):
            row = []
            for j in range(self.m):
                row.append(self.rows[i][j] + other.rows[i][j])
            result.append(row)
        return Matrix(result)

    # умножение на число или матрицу
    def __mul__(self, other):
        # число
        if isinstance(other, (int, float)):
            return Matrix([[x * other for x in row] for row in self.rows])

        # матрица
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

    # обратное умножение (чтобы поддерживать 2 * a)
    def __rmul__(self, other):
        return self * other

    # определитель по рекурсии
    def det(self):
        if self.n != self.m:
            raise ValueError("Matrix must be square!")

        # базовые случаи
        if self.n == 1:
            return self.rows[0][0]
        if self.n == 2:
            return self.rows[0][0] * self.rows[1][1] - self.rows[0][1] * self.rows[1][0]

        # разложение по первой строке
        total = 0
        for col in range(self.m):
            minor = []
            for i in range(1, self.n):
                row = self.rows[i][:col] + self.rows[i][col + 1 :]
                minor.append(row)
            sign = (-1) ** col
            total += sign * self.rows[0][col] * Matrix(minor).det()

        return total
