def hamming_encode(data):
    m = len(data)
    r = 0  # это контрольные биты
    while (2**r) < (m + r + 1):
        r += 1
    total_length = m + r

    encoded = [0] * total_length

    j = 0
    for i in range(1, total_length + 1):
        # если позиции - степени двойки
        if (i & (i - 1)) == 0:
            continue
        else:
            encoded[i - 1] = data[j]
            j += 1

    for i_power in range(r):
        index = 2**i_power
        count_ones = 0
        for i in range(1, total_length + 1):
            if i & index:
                if encoded[i - 1] == 1:
                    count_ones += 1
        if count_ones % 2 != 0:
            parity = 1
        else:
            parity = 0
        # значение контрольного бита
        encoded[index - 1] = parity
    return encoded


def hamming_decode(encoded):
    total_length = len(encoded)
    r = 0
    while (2**r) <= total_length:
        r += 1

    error_position = 0

    for i_power in range(r):
        index = 2**i_power
        count_ones = 0
        for i in range(1, total_length + 1):
            if i & index:
                if encoded[i - 1] == 1:
                    count_ones += 1
        if count_ones % 2 != 0:
            error_position += index

    data = []
    for i in range(1, total_length + 1):
        if (i & (i - 1)) != 0:
            data.append(encoded[i - 1])

    return data, error_position


input_str = input("Введите строку битов для шифрования: ").strip()

if not all(c in "01" for c in input_str):
    print("Ошибка! строка должна состоять только из 0 и 1")
    exit()

data_bits = [int(c) for c in input_str]

# Кодируем
encoded_message = hamming_encode(data_bits)
print("Закодированное сообщение:", "".join(map(str, encoded_message)))

# Декодируем
corrected_data, error_pos = hamming_decode(encoded_message)

if error_pos == 0:
    print("Ошибок не обнаружено")
else:
    print(f"Обнаружена ошибка в позиции: {error_pos}")
