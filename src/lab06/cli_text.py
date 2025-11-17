import argparse
import sys
import os
from pathlib import Path
sys.path.append("/Users/edna/Desktop/python_labs/src/lib")
sys.path.append("/Users/edna/Desktop/python_labs/src/lab04")
from text import normalize, tokenize, count_freq, top_n
from io_txt_csv import read_text


def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        p = Path(args.input)
        if not p.exists():
            raise FileNotFoundError("файл не найден")
        array_text = tokenize(normalize(read_text(p)))
        if args.n:
            for i, e in enumerate(array_text, 1):
                print(f"{i}. {e}")
        else:
            for e in array_text:
                print(e)

    elif args.command == "stats":
        text = args.input
        for e in top_n(count_freq(tokenize(normalize(text))), args.top):
            print(e[0], e[1])


if __name__ == "__main__":
    main()

"-m src.lab06.cli_text cat --input data/lab06/testlab06"
""
"python3 -m src.lab6.cli_text --help"