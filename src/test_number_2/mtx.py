def serialize(matrix):
    if not matrix:
        return "0 0"

    rows = len(matrix)
    cols = len(matrix[0])

    # проверка одинаковой длины строк
    for row in matrix:
        if len(row) != cols:
            raise ValueError("All rows must have the same length")

    lines = [f"{rows} {cols}"]
    for row in matrix:
        lines.append(" ".join(str(x) for x in row))

    return "\n".join(lines)


def deserialize(text):
    lines = text.strip().splitlines()
    if not lines:
        raise ValueError("Empty input")

    # размеры матрицы
    header = lines[0].split()
    if len(header) != 2:
        raise ValueError("Header must contain two integers: rows and cols")

    rows, cols = map(int, header)
    matrix = []

    # если она пустая
    if rows == 0 and cols == 0:
        return []

    if len(lines) - 1 != rows:
        raise ValueError("Number of matrix rows does not match header")

    for line in lines[1:]:
        parts = line.split()
        if len(parts) != cols:
            raise ValueError("Incorrect number of columns in a row")
        matrix.append([float(x) if "." in x else int(x) for x in parts])

    return matrix
