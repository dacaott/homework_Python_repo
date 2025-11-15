import pytest
from src.huffman.huffman_encoding import encode, decode
from src.huffman.huffman_codec import encode_file, decode_file


def test_encode_decode_basic_string():
    text = "hello huffman"
    encoded, codes = encode(text)
    decoded = decode(encoded, codes)
    assert decoded == text


def test_encode_decode_single_char():
    text = "aaaaaa"
    encoded, codes = encode(text)
    decoded = decode(encoded, codes)
    assert decoded == text
    assert all(bit == "0" for bit in encoded)


def test_encode_decode_empty_string():
    text = ""
    encoded, codes = encode(text)
    decoded = decode(encoded, codes)
    assert decoded == text
    assert encoded == ""
    assert codes == {}


def test_encode_decode_file(tmp_path):
    input_file = tmp_path / "input.txt"
    compressed_file = tmp_path / "compressed.huf"
    output_file = tmp_path / "output.txt"

    text = "This is a test of the Huffman codec.\n" * 10
    input_file.write_text(text, encoding="utf-8")

    encode_file(str(input_file), str(compressed_file))
    decode_file(str(compressed_file), str(output_file))

    decoded_text = output_file.read_text(encoding="utf-8")
    assert decoded_text == text
