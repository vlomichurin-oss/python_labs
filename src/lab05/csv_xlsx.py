import csv
from pathlib import Path

try:
    from openpyxl import Workbook
    from openpyxl.utils import get_column_letter
except ImportError:
    raise ImportError("Для работы этого модуля требуется установить openpyxl: pip install openpyxl")


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    csv_file = Path(csv_path)
    xlsx_file = Path(xlsx_path)
    
    if not csv_file.exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")
    
    if csv_file.suffix.lower() != '.csv':
        raise ValueError("Неверный тип файла: ожидается .csv")
    
    try:
        with csv_file.open('r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
    except Exception as e:
        raise ValueError(f"Ошибка чтения CSV: {e}")
    
    if not rows:
        raise ValueError("Пустой CSV файл")
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    
    for row in rows:
        ws.append(row)
    
    for col_idx, _ in enumerate(rows[0], 1):
        col_letter = get_column_letter(col_idx)
        max_length = 0
        
        for row_idx, row in enumerate(rows, 1):
            if len(row) >= col_idx:
                cell_value = str(row[col_idx - 1])
                max_length = max(max_length, len(cell_value))
        
        column_width = max(max_length + 2, 8)
        ws.column_dimensions[col_letter].width = column_width
    
    wb.save(xlsx_file)

    csv_to_xlsx("/Users/edna/Desktop/python_labs/data/samples/cities.csv", "/Users/edna/Desktop/python_labs/data/out/cities.xlsx")