from enum import Enum

import random
import string
import csv

class Case(Enum):
    RANDOM = 0
    LOWER = 1
    UPPER = 2

class Row:
    columns: list[str] = []
    key: str

    def __init__(self) -> None:
        self.columns = []

    def decrypt(self, translation_map: dict[str, float]) -> str:
        return self.columns[translation_map[self.key] % len(self.columns)]

def get_random_letter(case: Case = Case.UPPER) -> str:
    char = random.choice(string.ascii_letters)

    if case == Case.UPPER:
        char = char.upper()
    elif case == Case.LOWER:
        char = char.lower()

    return char

def is_letter(char: str):
    return char.upper() != char.lower()

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

def decrypt(rows: list[Row], translation_map: dict[str, float]) -> str:
    res = ""

    for row in rows:
        res += row.decrypt(translation_map)

    return res

def encrypt_text_file(input_path: str, translation_map: dict[str, float], min_columns: int = 4, max_columns: int = 8, case: Case = Case.RANDOM) -> list[Row]:
    file = open(input_path, "r", encoding="utf-8")

    return encrypt(file.read(), translation_map, min_columns, max_columns, case)

def make_csv(rows: list[Row], output_path: str):
    with open(output_path, "w", encoding="utf-8") as file:
        writer = csv.writer(file)

        max_len = 0
        for row in rows:
            cur_len = len(row.columns)

            if max_len < cur_len:
                max_len = cur_len

        columns = ["key"]
        for i in range(max_len ):
            columns.append(str(i + 1))

        writer.writerow(columns)

        for row in rows:
            writer.writerow([row.key] + row.columns)

def get_rows_from_csv(input_path: str) -> list[Row]:
    rows = []

    with open(input_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        for csv_row in reader:
            if csv_row[0] == "key":
                continue

            row = Row()
            row.key = csv_row[0]

            for i in range(1, len(csv_row)):
                row.columns.append(csv_row[i])

            rows.append(row)

    return rows

def decrypt_csv(input_path: str, translation_map: dict[str, float]) -> str:
    return decrypt(get_rows_from_csv(input_path), translation_map)
