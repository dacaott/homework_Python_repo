import json
from .huffman_encoding import encode, decode
from .huffman_binary import bits_to_bytes, bytes_to_bits


def encode_file(input_path: str, output_path: str):
    # читаем исходный текст
    text = open(input_path, "r", encoding="utf-8").read()

    # кодируем в биты
    encoded_bits, codes = encode(text)

    # в байты
    data_bytes, padding = bits_to_bytes(encoded_bits)

    # сериализация таблицы
    codes_json = json.dumps(codes).encode("utf-8")

    with open(output_path, "wb") as f:
        f.write(len(codes_json).to_bytes(4, "big"))  # длина таблицы
        f.write(codes_json)  # таблица
        f.write(bytes([padding]))  # padding
        f.write(data_bytes)  # данные


def decode_file(input_path: str, output_path: str):
    with open(input_path, "rb") as f:
        table_size = int.from_bytes(f.read(4), "big")
        codes = json.loads(f.read(table_size).decode("utf-8"))
        padding = f.read(1)[0]
        data_bytes = f.read()

    bits = bytes_to_bits(data_bytes, padding)
    text = decode(bits, codes)

    open(output_path, "w", encoding="utf-8").write(text)
