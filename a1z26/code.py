"""
A1Z26 encoding/decoding.
"""

from string import ascii_lowercase
from typing import Dict


letter2number: Dict[str, int] = {
    letter: i+1 for i, letter in enumerate(ascii_lowercase)
}
number2letter: Dict[int, str] = {
    number: letter for letter, number in letter2number.items()
}

def encode_unit(unit: str) -> str:
    """Encodes a single unit of plaintext to ciphertext."""
    return str(letter2number.get(unit.lower(), unit))

def decode_unit(unit: str) -> str:
    """Decodes a single unit of ciphertext to plaintext."""
    if not unit.isdigit():
        return unit
    n = int(unit)
    return number2letter.get(n, unit)

def encode(plaintext: str, separator: str=" ") -> str:
    """Encodes plaintext to ciphertext."""
    return separator.join(map(encode_unit, plaintext))

def decode(ciphertext: str, separator: str=" ") -> str:
    """Decodes ciphertext to plaintext."""
    return "".join(map(decode_unit, ciphertext.split(separator)))
