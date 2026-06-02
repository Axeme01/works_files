with open('file1.txt', 'w', encoding='utf-8') as f:
    f.write("""содержимое первого файла.""")

with open('file2.txt', 'w', encoding='utf-8') as f:
    f.write("""содержимое второго файла.""")

with open('file3.txt', 'w', encoding='utf-8') as f:
    f.write("""содержимое третьего файла.""")

filenames = ["file1.txt", "file2.txt", "file3.txt"]
output_filename = "combined.txt"

with open(output_filename, 'w', encoding='utf-8') as output_file:
    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as current_file:
            content = current_file.read()

        output_file.write(f"\n==={filename}===\n")
        output_file.write(content.strip() + "\n")

print(f"Содержимое объединено в файл '{output_filename}'.")