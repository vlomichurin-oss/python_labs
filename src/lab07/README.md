# Лабораторная работа №6
## `cli_text.py`
```
import sys, os, argparse
sys.path.append(r"/Users/edna/Desktop/python_labs/src")
from lib.text_stats import stats_text

def cat_command(input_file: str, number_lines: bool = False):
    if not check_file(input_file):
        sys.exit(1)

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            for line_number, line in enumerate(f, start=1):
                if number_lines:
                    print(f"{line_number:6d}  {line}", end='')
                else:
                    print(line, end='')
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}", file=sys.stderr)
        sys.exit(1)

def check_file(file_path: str) -> bool:
    if not os.path.exists(file_path):
        print(f"Ошибка: файл '{file_path}' не существует", file=sys.stderr)
        return False
    if not os.path.isfile(file_path):
        print(f"Ошибка: '{file_path}' не является файлом", file=sys.stderr)
        return False

    return True

def stats_command(input_file: str, top_n: int = 5):
    if not check_file(input_file):
        sys.exit(1)
    
    if top_n <= 0:
        print("Ошибка: значение --top должно быть положительным числом", file=sys.stderr)
        sys.exit(1)
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
            stats_text(text, top_n)

    except Exception as e:
        print(f"Ошибка при анализе файла: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Лабораторная №6")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        cat_command(args.input, args.n)
    elif args.command == "stats":
        stats_command(args.input, args.top)
    else:

        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
```
### Вывод строк с номерами:

<img width="902" height="825" alt="lab06exCLI_TEXT01" src="https://github.com/user-attachments/assets/8012c44b-b233-4c75-bf13-ec71442b4b2a" />

### Вывод топ слов :

<img width="920" height="248" alt="laab06exCLI_TEXT02" src="https://github.com/user-attachments/assets/e6145e60-1dfd-4f56-a637-cfd999cff59a" />

## Help:

<img width="708" height="189" alt="lab06exCLI_TEXT03" src="https://github.com/user-attachments/assets/83a7f9a6-b96d-418e-848b-7ebc9f00bdc9" />

## `cli_convert.py`
```
import sys, argparse, os
from pathlib import Path
sys.path.append(r"/Users/edna/Desktop/python_labs/src/lab05")

from csv_xlsx import csv_to_xlsx
from json_csv import json_to_csv, csv_to_json

def check_file(file_path: str) -> bool:
    if not os.path.exists(file_path):
        print(f"Ошибка: файл '{file_path}' не существует", file=sys.stderr)
        return False
    if not os.path.isfile(file_path):
        print(f"Ошибка: '{file_path}' не является файлом", file=sys.stderr)
        return False

    return True

def cli_convert():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd", required=True)
    
    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True, help="Входной JSON файл")
    p1.add_argument("--out", dest="output", required=True, help="Выходной CSV файл")

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    p2.add_argument("--out", dest="output", required=True, help="Выходной JSON файл")

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    p3.add_argument("--out", dest="output", required=True, help="Выходной XLSX файл")
    
    args = parser.parse_args()

    try:
        if args.cmd == "json2csv":
            if not check_file(args.input):
                print(f"Ошибка: Файл {args.input} не существует или недоступен")
                sys.exit(1)
                
            json_to_csv(args.input, args.output)
            print(f"Успешно: JSON -> CSV")
            
        elif args.cmd == "csv2json":
            if not check_file(args.input):
                print(f"Ошибка: Файл {args.input} не существует или недоступен")
                sys.exit(1)
                
            csv_to_json(args.input, args.output)
            print(f"Успешно: CSV -> JSON")
            
        elif args.cmd == "csv2xlsx":
            if not check_file(args.input):
                print(f"Ошибка: Файл {args.input} не существует или недоступен")
                sys.exit(1)
                
            csv_to_xlsx(args.input, args.output)
            print(f"Успешно: CSV -> XLSX")
            
        else:
            print("Ошибка: Неизвестная команда")
            sys.exit(1)
            
        return 0
        
    except Exception as e:
        print(f"Ошибка при конвертации: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    sys.exit(cli_convert())
```
### Вывод JSON -> CSV, CSV -> JSON, CSV -> XLSX:

<img width="1001" height="152" alt="lab06exCLI_CONVERT" src="https://github.com/user-attachments/assets/9359834d-0f71-47d1-a980-c95128c27230" />

### Help:

<img width="708" height="189" alt="lab06exCLI_TEXT03" src="https://github.com/user-attachments/assets/68188263-8d0f-4070-bb98-1d86317f70a9" />
