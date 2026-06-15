words_list = [
    "Один", "Два", "Три", "Четыре", "Пять", "Шесть",
]

with open("words.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(words_list))

with open("words.txt", "r", encoding="utf-8") as f:
    words = f.read().splitlines()

alpha_sorted = sorted(words)
length_sorted = sorted(words, key=len)
reverse_sorted = sorted(words, reverse=True)

with open("sorted_alphabetically.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(alpha_sorted))

with open("sorted_by_length.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(length_sorted))

with open("sorted_reverse.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(reverse_sorted))

print("Слова отсортированы!")