from time import sleep
from datetime import datetime
from threading import Thread

time_start = datetime.now()


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf8') as file:
        for i in range(word_count):
            file.write(f"Какое-то слово №{i + 1}\n")
            sleep(0.1)


write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

time_end = datetime.now()
print("Работа функций", time_end - time_start)

time_start = datetime.now()

thr_a = Thread(target=write_words, args=(10, "example5.txt"))
thr_b = Thread(target=write_words, args=(30, "example6.txt"))
thr_c = Thread(target=write_words, args=(200, "example7.txt"))
thr_d = Thread(target=write_words, args=(100, "example8.txt"))

thr_a.start()
thr_b.start()
thr_c.start()
thr_d.start()

thr_a.join()
thr_b.join()
thr_c.join()
thr_d.join()

time_end = datetime.now()
print("Работа потоков", time_end - time_start)
