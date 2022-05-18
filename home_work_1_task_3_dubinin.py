# Task 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
# Важно: решение должно быть универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем.

bytes_list = ['attribute', 'класс', 'функция', 'type']

for our_bytes in bytes_list:
    try:
        bytes(our_bytes, 'ascii')
    except UnicodeEncodeError:
        print(f' Результат: данное слово "{our_bytes}" невозможно записать в байтовом типе !!!')

