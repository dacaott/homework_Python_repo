def count_queen_arrangements_optimized(board_size):
    occupied_columns = set()
    occupied_main_diagonals = set()  # row - col
    occupied_anti_diagonals = set()  # row + col

    def place_queen(row):
        if row == board_size:
            return 1  # корректная расстановка найдена
        count = 0
        for col in range(board_size):
            main_diag = row - col
            anti_diag = row + col
            if (
                col in occupied_columns
                or main_diag in occupied_main_diagonals
                or anti_diag in occupied_anti_diagonals
            ):
                continue  # нельзя ставить ферзя здесь
            # ставим ферзя
            occupied_columns.add(col)
            occupied_main_diagonals.add(main_diag)
            occupied_anti_diagonals.add(anti_diag)
            count += place_queen(row + 1)
            # откат (backtracking)
            occupied_columns.remove(col)
            occupied_main_diagonals.remove(main_diag)
            occupied_anti_diagonals.remove(anti_diag)
        return count

    return place_queen(0)


board_size = int(input("Введите размер доски N: "))
print(
    "Количество корректных расстановок:", count_queen_arrangements_optimized(board_size)
)
