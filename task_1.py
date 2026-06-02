with open('input.txt', 'w', encoding='utf-8') as f:
    f.write("""Первая строка.
Вторая строка.
Третья строка.""")

lines = 0
words = 0

with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lines += 1
        words += len(line.split())

with open('statistics.txt', 'w', encoding='utf-8') as out:
    print(f"Строк: {lines}", file=out)
    print(f"Слов: {words}", file=out)
    
print(f"Строк: {lines}")
print(f"Слов: {words}")