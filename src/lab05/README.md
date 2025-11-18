# Лабораторная работы №5
## Задание A — JSON ↔ CSV

```
import json
import csv
from pathlib import Path

def is_json_file(file_path: str) -> bool:
    return os.path.splitext(file_path)[1].lower() == '.json'

def is_csv_file(file_path: str) -> bool:
    return os.path.splitext(file_path)[1].lower() == '.csv'


def json_to_csv(json_path: str, csv_path: str) -> None:
    json_file = Path(json_path)
    csv_file = Path(csv_path)

    if not json_file.exists():
        raise FileNotFoundError(f"JSON файл не найден: {json_path}")
    
    if json_file.suffix.lower() != '.json':
        raise ValueError("Неверный тип файла: ожидается .json")
    
    try:
        with json_file.open('r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка парсинга JSON: {e}")
    
    if not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")
    
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы JSON должны быть словарями")
    
    all_fields = set()
    for item in data:
        all_fields.update(item.keys())
    fieldnames = sorted(all_fields)
    
    with csv_file.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for item in data:
            row = {field: item.get(field, '') for field in fieldnames}
            writer.writerow(row)


def csv_to_json(csv_path: str, json_path: str) -> None:
    csv_file = Path(csv_path)
    json_file = Path(json_path)
    
    if not csv_file.exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")
    
    if csv_file.suffix.lower() != '.csv':
        raise ValueError("Неверный тип файла: ожидается .csv")
    
    try:
        with csv_file.open('r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    except Exception as e:
        raise ValueError(f"Ошибка чтения CSV: {e}")
    
    if not rows:
        raise ValueError("Пустой CSV файл")
    
    with json_file.open('w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)

json_to_csv("/Users/edna/Desktop/python_labs/data/lab05/samples/people.json", "/Users/edna/Desktop/python_labs/data/lab05/out/people_from_json.csv")
csv_to_json("/Users/edna/Desktop/python_labs/data/lab05/samples/people.csv", "/Users/edna/Desktop/python_labs/data/lab05/out/people_from_csv.json")
```
### Входные данные:

<img width="453" height="525" alt="lab05exA01" src="https://github.com/user-attachments/assets/53826b44-2dfb-4e1b-b6d0-f144c3d22098" />
<img width="451" height="176" alt="lab05exA02" src="https://github.com/user-attachments/assets/f5bf51e1-bb92-4897-83b8-04b5fe458efd" />

### Выходные данные:

<img width="373" height="526" alt="lab05exA03" src="https://github.com/user-attachments/assets/b22aae92-e983-41ef-820a-5d0275999fe9" />
<img width="366" height="160" alt="lab05exA04" src="https://github.com/user-attachments/assets/e1ef6858-3c99-4929-947f-ea1eb3ee8407" />


## Задание B — CSV → XLSX

```
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
```
### Входные данные:

<img width="412" height="174" alt="lab05exB01" src="https://github.com/user-attachments/assets/952e1125-2433-44fb-94a9-470ec647c64b" />

### Выходные данные:

<img width="279" height="144" alt="lab05exB02" src="https://github.com/user-attachments/assets/e2b12442-1732-41d3-94d5-fa723fc134e2" />
