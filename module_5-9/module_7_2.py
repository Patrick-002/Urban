def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
    number_of_strings = 0
    strings_positions = {}
    for string in strings:
        number_of_strings += 1
        strings_positions[(number_of_strings, file.tell())] = string
        file.write(string + '\n')
    file.close()
    return strings_positions


if __name__ == '__main__':
     info = [
         'Text for tell.',
         'Используйте кодировку utf-8.',
         'Because there are 2 languages!',
         'Спасибо!'
     ]

     result = custom_write('test.txt', info)
     for elem in result.items():
         print(elem)