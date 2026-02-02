import csv
from pathlib import Path
from typing import List, Dict, Any
import os


def load_csv_files(file_paths: List[str]) -> List[Dict[str, Any]]:
    all_data = []

    for file_path in file_paths:
        if not Path(file_path).exists():
            raise FileNotFoundError(f"Файл не найден: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            all_data.extend(reader)

    return all_data
