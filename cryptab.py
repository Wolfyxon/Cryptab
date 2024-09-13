from enum import Enum

import random
import string

class Case(Enum):
    RANDOM = 0,
    LOWER = 1
    UPPER = 2

class Row:
    columns: list[str] = []
    key: str

    def __init__(self) -> None:
        self.columns = []

    def decrypt(self, translation_table: dict[str, float]) -> str:
        return self.columns[translation_table[self.key] % len(self.columns)]

def get_random_letter(case: Case = Case.UPPER) -> str:
    char = random.choice(string.ascii_letters)

    if case == Case.UPPER:
        char = char.upper()
    elif case == Case.LOWER:
        char = char.lower()

    return char

def is_letter(char: str):
    return char in string.ascii_letters

def encrypt(text: str, translation_map: dict[str, float], min_columns: int = 4, max_columns: int = 8, case: Case = Case.RANDOM) -> list[Row]:
    rows = []

    for char in text:
        if not is_letter(char):
            continue

        row = Row()
        key = random.choice(list(translation_map.keys()))
        row.key = key

        for _ in range(random.randint(min_columns, max_columns)):
            row.columns.append(get_random_letter(case))

        row.columns[translation_map[key] % len(row.columns)] = char

        rows.append(row)

    return rows
