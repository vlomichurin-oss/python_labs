import sys
from io_txt_csv import read_text, write_csv, ensure_parent_dir

from pathlib import Path
import os

sys.path.append('/Users/edna/Desktop/python_labs/src/lib')

from src.lib import text as text
from text import normalize
from text import tokenize
from text import top_n
from text import count_freq


def exist_path(path_f: str):
    return os.path.exists(path_f)


def main(file: str, encoding: str = 'utf-8'):
    if not exist_path(file):
        raise FileNotFoundError(f"Файл {file} не найден")

    text_content = read_text(file, encoding=encoding)
    norm = normalize(text_content)
    tokens = tokenize(norm)
    frequencies = count_freq(tokens)
    top = top_n(frequencies, 5)

    top_sort = sorted(top, key=lambda x: (-x[1], x[0]))

    output_path = Path(file).parent / 'report.csv'
    write_csv(top_sort, str(output_path), header=('word', 'count'))

    print(f'Всего слов: {len(tokens)}')
    print(f'Уникальных слов: {len(frequencies)}')
    print('Топ-5:')
    for word, count in top_sort:
        print(f'{word}: {count}')


path = r'/Users/edna/Desktop/python_labs/src/data'
main(path + r'/input.txt')
