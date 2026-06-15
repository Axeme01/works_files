with open('secret.txt', 'w', encoding='utf-8') as f:
    f.write(
        "Строка для шифровки"
    )

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if 'А' <= char <= 'Я' or 'а' <= char <= 'я':
            is_upper = char.isupper()
            base = ord('А') if is_upper else ord('а')

            pos = ord(char.upper()) - ord('А')

            new_pos = (pos + shift) % 33
            new_char = chr(base + new_pos)

            result += new_char if is_upper else new_char.lower()
        else:
            result += char
    return result


with open('secret.txt', 'r', encoding='utf-8') as f:
    plain_text = f.read()
cipher_text = caesar_cipher(plain_text, 3)

with open('encrypted.txt', 'w', encoding='utf-8') as f:
    f.write(cipher_text)

with open('encrypted.txt', 'r', encoding='utf-8') as f:
    cipher_text = f.read()
decipher_text = caesar_cipher(cipher_text, -3)

with open('decrypted.txt', 'w', encoding='utf-8') as f:
    f.write(decipher_text)

print('Файл зашифрован!')