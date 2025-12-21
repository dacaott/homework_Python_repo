def build_huffman_codes(text: str) -> dict[str, str]:
    # если текст пустой — возвращаем пустой словарь
    if not text:
        return {}

    # подсчёт частоты каждого символа
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    # если только один уникальный символ — простой код
    if len(frequency) == 1:
        only_char = next(iter(frequency))
        return {only_char: "0"}

    # узлы дерева: (частота, символ/поддерево)
    nodes = [(freq, char) for char, freq in frequency.items()]

    # строим дерево Хаффмана
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x[0])
        freq1, node1 = nodes.pop(0)
        freq2, node2 = nodes.pop(0)
        nodes.append((freq1 + freq2, (node1, node2)))

    # корень дерева
    (_, root) = nodes[0]
    codes = {}

    def traverse(node, code):
        if isinstance(node, str):
            codes[node] = code
        else:
            left, right = node
            traverse(left, code + "0")
            traverse(right, code + "1")

    traverse(root, "")
    return codes


def encode(text: str) -> tuple[str, dict[str, str]]:
    codes = build_huffman_codes(text)
    encoded_bits = "".join(codes[ch] for ch in text) if text else ""
    return encoded_bits, codes


def decode(bits: str, codes: dict[str, str]) -> str:
    if not bits or not codes:
        return ""

    reverse_codes = {code: ch for ch, code in codes.items()}
    decoded = []
    current = ""

    for bit in bits:
        current += bit
        if current in reverse_codes:
            decoded.append(reverse_codes[current])
            current = ""

    return "".join(decoded)
