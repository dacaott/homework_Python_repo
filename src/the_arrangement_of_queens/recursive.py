# recursive.py
def count_queen_arrangements_recursive(board_size):
    queen_positions = [-1] * board_size

    def is_safe(row, col):
        for prev_row in range(row):
            prev_col = queen_positions[prev_row]
            if prev_col == col or abs(prev_col - col) == abs(prev_row - row):
                return False
        return True

    def place_queen(row):
        if row == board_size:
            return 1
        count = 0
        for col in range(board_size):
            if is_safe(row, col):
                queen_positions[row] = col
                count += place_queen(row + 1)
                queen_positions[row] = -1  # откат
        return count

    return place_queen(0)


board_size = int(input("Введите размер доски N: "))
print(
    "Количество корректных расстановок:",
    count_queen_arrangements_recursive(board_size),
)
