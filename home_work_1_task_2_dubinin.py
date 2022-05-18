# Task 2. Каждое из слов «class», «function», «method» записать в байтовом типе. Сделать это необходимо в автоматическом, а не ручном режиме,
# с помощью добавления литеры b к текстовому значению, (т.е. ни в коем случае не используя методы encode, decode или функцию bytes) и определить тип,
# содержимое и длину соответствующих переменных.

one = 'class'
two = 'function'
three = 'method'

our_list = [one, two, three]

for x in our_list:
    y = eval(f"b'{x}'")
    print(f'Тип ', type(y))
    print(f'Слово ', y)
    print(f'Длина', len(y))
