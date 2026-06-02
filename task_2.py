with open('text.txt', 'w', encoding='utf-8') as f:
    f.write("""Набор букв.
Набор слов
Слово слово""")

search_word = input("Введите слово для поиска: ").strip()

found_lines = []
count = 0
line_number = 0

with open('text.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line_number += 1
        words_in_line = line.split()
        if search_word in words_in_line:
            found_lines.append(line_number)
        count += words_in_line.count(search_word)

print(f"Найдено: {'да' if count > 0 else 'нет'}")
print(f"Количество повторений: {count}")
if found_lines:
    print(f"Встречается в строках: {', '.join(map(str, found_lines))}")
else:
    print("Встречается в строках: Нет")

with open('search_results.txt', 'w', encoding='utf-8') as out_file:
    print(f"Слово для поиска: {search_word}", file=out_file)
    print(f"Найдено: {'да' if count > 0 else 'нет'}", file=out_file)
    print(f"Количество повторений: {count}", file=out_file)
    if found_lines:
        print(f"Встречается в строках: {', '.join(map(str, found_lines))}", file=out_file)
    else:
        print("Встречается в строках: Нет", file=out_file)