import itertools


def count_queen_arrangements_enumeration(board_size):
    def is_safe(queen_positions):
        for row1 in range(board_size):
            for row2 in range(row1 + 1, board_size):
                if abs(queen_positions[row1] - queen_positions[row2]) == abs(
                    row1 - row2
                ):
                    return False
        return True

    total_solutions = 0
    for permutation in itertools.permutations(range(board_size)):
        if is_safe(permutation):
            total_solutions += 1
    return total_solutions


board_size = int(input("Введите размер доски N: "))
print(
    "Количество корректных расстановок:",
    count_queen_arrangements_enumeration(board_size),
)
