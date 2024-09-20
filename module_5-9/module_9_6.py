def all_variants(text):
    i = 1
    while i < len(text) + 1:
        j = 0
        while j + i != len(text) + 1:
            yield text[j:j+i]
            j += 1
        i += 1

if __name__ == '__main__':
    a = all_variants("abc")
    for i in a:
        print(i)