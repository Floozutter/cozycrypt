"""
ROT-n encoding/decoding.
"""

from string import ascii_lowercase, ascii_uppercase
from typing import Dict


lowercase2index: Dict[str, int] = {
    letter: i for i, letter in enumerate(ascii_lowercase)
}
uppercase2index: Dict[str, int] = {
    letter: i for i, letter in enumerate(ascii_uppercase)
}

def rotate_unit(shift: int, unit: str) -> str:
    """Rotates a unit of text using the given shift."""
    # Case where unit is a lowercase letter.
    lower_index = lowercase2index.get(unit, None)
    if lower_index is not None:
        return ascii_lowercase[(lower_index + shift) % 26]
    # Case where unit is an uppercase letter.
    upper_index = uppercase2index.get(unit, None)
    if upper_index is not None:
        return ascii_uppercase[(upper_index + shift) % 26]
    # Case where unit is nonalphabetic.
    return unit

def rotate(shift: int, text: str) -> str:
    """Rotates text using the given shift."""
    return "".join(map(lambda unit: rotate_unit(shift, unit), text))