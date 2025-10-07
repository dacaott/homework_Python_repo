def get_change(amount, coins):
    # Распаковываем список монет в отдельные переменные
    coin7, coin9, coin11 = coins

    # То, сколько максимум монет по 11₽ может быть использовано
    max_11 = amount // coin11

    # Перебираем возможное количество монет по 11₽ (от максимума к нулю)
    for count11 in range(max_11, -1, -1):
        # Считаем, сколько денег останется после использования count11 монет по 11₽
        remaining_after_11 = amount - count11 * coin11

        # То, сколько максимум монет по 9₽ можно взять на оставшуюся сумму
        max_9 = remaining_after_11 // coin9

        # Перебираем возможное количество монет по 9₽ (от максимума к нулю).
        for count9 in range(max_9, -1, -1):
            # Считаем остаток после вычитания суммы монет по 11₽ и 9₽
            remaining_after_9 = remaining_after_11 - count9 * coin9

            # Проверяем, делится ли остаток нацело на 7₽,
            # если да, значит оставшуюся сумму можно закрыть монетами по 7₽
            if remaining_after_9 % coin7 == 0:
                count7 = remaining_after_9 // coin7
                # Возвращаем результат в виде кортежа
                return count7, count9, count11

    return None


name = 7
surname = 9
patronymic = 11
mycoins = [name, surname, patronymic]

amount = int(input("Введите сумму для размена: "))

result = get_change(amount, mycoins)

if result:
    # Распаковываем кортеж в отдельные переменные
    count7, count9, count11 = result
    parts = []
    if count7 > 0:
        parts.append(f"7₽ в количестве {count7}")
    if count9 > 0:
        parts.append(f"9₽ в количестве {count9}")
    if count11 > 0:
        parts.append(f"11₽ в количестве {count11}")

    # Склеиваем все части в строку через запятую
    print(", ".join(parts))

else:
    # Если функция вернула None, значит размен невозможен
    print("-42!")
