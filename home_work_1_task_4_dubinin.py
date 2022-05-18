# Task 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
# в байтовое и выполнить обратное преобразование (используя методы encode и decode).

encoding_string_list = ['разработка', 'администрирование', 'protocol', 'standart']
for encoding_string in encoding_string_list:
    print(encoding_string.encode('utf-8'))

print()

decoding_string_list = [b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0',
                        b'\xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5',
                        b'protocol',
                        b'standard']
for decoding_string_bytes in decoding_string_list:
    print(decoding_string_bytes.decode('utf-8'))

