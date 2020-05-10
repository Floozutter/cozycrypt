"""
Atbash encoding/decoding.
"""

from string import ascii_lowercase, ascii_uppercase
from typing import Dict


lowercase2index: Dict[str, int] = {
    letter: i for i, letter in enumerate(ascii_lowercase)
}
uppercase2index: Dict[str, int] = {
    letter: i for i, letter in enumerate(ascii_uppercase)
}

def flip_unit(unit: str) -> str:
    """Flips a unit of text."""
    # Case where unit is a lowercase letter.
    lower_index = lowercase2index.get(unit, None)
    if lower_index is not None:
        return ascii_lowercase[25 - lower_index]
    # Case where unit is an uppercase letter.
    upper_index = uppercase2index.get(unit, None)
    if upper_index is not None:
        return ascii_uppercase[25 - upper_index]
    # Case where unit is nonalphabetic.
    return unit

def flip(text: str) -> str:
    """Flips text. Plaintext will be flipped to ciphertext, and vice versa."""
    return "".join(map(flip_unit, text))
