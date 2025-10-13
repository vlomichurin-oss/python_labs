import re
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """
    Нормализует текст: приводит к нижнему регистру, заменяет Ё на Е,
    убирает управляющие символы и схлопывает пробелы.
    """
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    # Заменяем управляющие символы (\t, \r, \n) на пробелы
    text = re.sub(r'[\t\r\n]', ' ', text)
    # Схлопываем повторяющиеся пробелы и убираем пробелы по краям
    text = re.sub(r' +', ' ', text.strip())
    return text

def tokenize(text: str) -> list[str]:
    """
    Разбивает текст на токены (слова).
    Токены состоят из букв, цифр, подчёркиваний и могут содержать дефисы внутри.
    """
    # Регулярное выражение для поиска слов:
    # \w+ - буквы/цифры/подчёркивание
    # (?:-\w+)* - ноль или более групп: дефис + буквы/цифры/подчёркивание
    pattern = r'\w+(?:-\w+)*'
    return re.findall(pattern, text)

def count_freq(tokens: list[str]) -> dict[str, int]:
    """
    Подсчитывает частоту встречаемости токенов.
    """
    tokens_set = set(tokens)
    return {x: tokens.count(x) for x in tokens_set}

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """
    Возвращает топ-N самых частых токенов.
    При равенстве частот сортирует по алфавиту.
    """
    # Сортируем сначала по убыванию частоты, затем по возрастанию слова
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]

