def bits_to_bytes(bits: str) -> tuple[bytes, int]:
    """Преобразует битовую строку в байты и возвращает (байты, padding)."""
    padding = (8 - len(bits) % 8) % 8
    padded_bits = bits + "0" * padding
    data = int(padded_bits, 2).to_bytes(len(padded_bits) // 8, "big")
    return data, padding


def bytes_to_bits(data: bytes, padding: int) -> str:
    """Преобразует байты в битовую строку, убирая добивочные нули."""
    raw_bits = bin(int.from_bytes(data, "big"))[2:].zfill(len(data) * 8)
    if padding:
        raw_bits = raw_bits[:-padding]
    return raw_bits