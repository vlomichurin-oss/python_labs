import sys
sys.path.append('/Users/edna/Desktop/python_labs/src/lib')
from src.lib import text as text

string = sys.stdin.readline()
tokenized = text.tokenize(string)
unique_words = text.count_freq(tokenized)
print(f"Всего слов: {len(tokenized)}")
print(f"Уникальных слов: {len(unique_words)}")
print(f"Топ-5:")
k = text.top_n(unique_words)
for token in k:
    print(token[0] + ":" + str(token[1]))




