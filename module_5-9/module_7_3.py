class WordsFinder():
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', '-']
        for file_name in self.file_names:
            list_words = []
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for char in punctuation:
                        if char in line:
                            line = line.replace(char, '')
                    list_words += line.split()
                    all_words[file_name] = list_words
        return all_words

    def find(self, word):
        word = word.lower()
        found_word = {}
        all_words = self.get_all_words()
        for file_name, words_list in all_words.items():
            word_pos = 0
            for is_word in words_list:
                word_pos += 1
                if word == is_word:
                    found_word[file_name] = word_pos
                    break
        return found_word

    def count(self, word):
        word = word.lower()
        words_count = {}
        all_words = self.get_all_words()
        for file_name, words_list in all_words.items():
            count = 0
            for is_word in words_list:
                if word == is_word:
                    count += 1
            words_count[file_name] = count
        return words_count



if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT')) # 3 слово по счёту
    print(finder2.count('teXT')) # 4 слова teXT в тексте всего