from src.huffman.huffman_encoding import encode, decode
from src.huffman.huffman_codec import encode_file, decode_file


def test_encode_decode_basic_string():
    text = "hello huffman"
    encoded, codes = encode(text)
    assert decode(encoded, codes) == text


def test_encode_decode_single_char():
    text = "aaaaaa"
    encoded, codes = encode(text)
    assert codes == {"a": "0"}
    assert encoded == "000000"
    assert decode(encoded, codes) == text


def test_encode_decode_empty_string():
    text = ""
    encoded, codes = encode(text)
    assert encoded == ""
    assert codes == {}
    assert decode(encoded, codes) == text


def test_encode_two_chars_manual():
    text = "ab"
    encoded, codes = encode(text)

    assert codes == {
        "a": "0",
        "b": "1",
    }
    assert encoded == "01"
    assert decode(encoded, codes) == text


def test_encode_aaab_manual():
    text = "aaab"
    encoded, codes = encode(text)

    assert codes == {
        "b": "0",
        "a": "1",
    }
    assert encoded == "1110"
    assert decode(encoded, codes) == text


def test_encode_abc_manual():
    text = "abc"
    encoded, codes = encode(text)

    assert codes == {
        "c": "0",
        "a": "10",
        "b": "11",
    }
    assert encoded == "10110"
    assert decode(encoded, codes) == text


def test_encode_decode_file(tmp_path):
    input_file = tmp_path / "input.txt"
    compressed_file = tmp_path / "compressed.huf"
    output_file = tmp_path / "output.txt"

    text = "This is a test of the Huffman codec.\n" * 10
    input_file.write_text(text, encoding="utf-8")

    encode_file(str(input_file), str(compressed_file))
    decode_file(str(compressed_file), str(output_file))

    assert output_file.read_text(encoding="utf-8") == text
