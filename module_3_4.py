def single_root_words (root_word, *other_words):
    same_words = []
    for i in other_words:
        if i.lower().find(root_word.lower()) != -1:
            same_words.append(i)
        elif root_word.lower().find(i.lower()) != -1:
            same_words.append(i)
    return same_words


print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
print(single_root_words('привет', 'Привет мир', 'Прив', 'Найдёт оба совпадения'))
