# 5. Написать код, который выполняет пинг веб-ресурсов yandex.ru, youtube.com и преобразовывает результат из байтовового
# типа данных в строковый без ошибок для любой кодировки операционной системы.

import platform
from chardet import detect
import subprocess

our_urls = ['youtube.com', 'yandex.ru']
our_code = '-n' if platform.system().lower() == 'windows' else '-c'

for url_our in our_urls:
    args = ['ping', our_code, '5', url_our]
    ping_yandex = subprocess.Popen(args, stdout=subprocess.PIPE)
    for x in ping_yandex.stdout:
        y = detect(x)
        print(y)
        x = x.decode(y['encoding']).encode('utf-8')
        print(x.decode('utf-8'))


