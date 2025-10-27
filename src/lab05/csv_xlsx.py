import csv
from pathlib import Path

try:
    from openpyxl import Workbook
    from openpyxl.utils import get_column_letter
except ImportError:
    raise ImportError("Для работы этого модуля требуется установить openpyxl: pip install openpyxl")


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    csv_file = Path(csv_path)
    xlsx_file = Path(xlsx_path)
    
    # Проверка существования файла
    if not csv_file.exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")
    
    # Проверка расширения
    if csv_file.suffix.lower() != '.csv':
        raise ValueError("Неверный тип файла: ожидается .csv")
    
    # Чтение CSV
    try:
        with csv_file.open('r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
    except Exception as e:
        raise ValueError(f"Ошибка чтения CSV: {e}")
    
    # Проверка данных
    if not rows:
        raise ValueError("Пустой CSV файл")
    
    # Создание Excel файла
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    
    # Запись данных
    for row in rows:
        ws.append(row)
    
    # Настройка ширины колонок
    for col_idx, _ in enumerate(rows[0], 1):
        col_letter = get_column_letter(col_idx)
        max_length = 0
        
        # Поиск максимальной длины в колонке
        for row_idx, row in enumerate(rows, 1):
            if len(row) >= col_idx:
                cell_value = str(row[col_idx - 1])
                max_length = max(max_length, len(cell_value))
        
        # Минимальная ширина 8 символов
        column_width = max(max_length + 2, 8)
        ws.column_dimensions[col_letter].width = column_width
    
    # Сохранение файла
    wb.save(xlsx_file)