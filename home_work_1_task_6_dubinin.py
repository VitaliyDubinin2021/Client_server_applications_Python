# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
# Далее забыть о том, что мы сами только что создали этот файл и исходить из того, что перед нами файл в неизвестной кодировке.
# Задача: открыть этот файл БЕЗ ОШИБОК вне зависимости от того, в какой кодировке он был создан.

from chardet import detect

words = ['сетевое программирование', 'сокет', 'декоратор']
with open('test.txt', 'w') as file:
    for word in words:
        file.write(f'{word}\n')
file.close()

with open('test.txt', 'rb') as file:
    content = file.read()
encoding = detect(content)['encoding']
print(encoding)

with open('test.txt', 'r', encoding=encoding) as file:
    content = file.read()
print(content)



