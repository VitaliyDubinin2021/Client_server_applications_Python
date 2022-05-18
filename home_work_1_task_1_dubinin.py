# Task 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание соответствующих
# переменных Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode и также проверить тип и содержимое переменных.

def type_and_value(y: list) -> None:
    for x in y:
        print(type(x))
        print(x)
    print('-' * 10)

one = 'разработка'
two = 'сокет'
three = 'декоратор'

our_list = [one, two, three]

type_and_value(our_list)

one_in_unicode = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' # разработка
two_in_unicode = '\u0441\u043e\u043a\u0435\u0442' # сокет
three_in_unicode = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440' # декоратор

list_unicode = [one_in_unicode, two_in_unicode, three_in_unicode]

type_and_value(list_unicode)






