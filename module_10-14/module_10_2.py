from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        number_of_enemy = 100
        count_of_days = 0
        while number_of_enemy > 0:
            number_of_enemy -= self.power
            count_of_days += 1
            if number_of_enemy < 0:
                number_of_enemy = 0
            print(f"{self.name} сражается {count_of_days} день(дня)..., осталось {number_of_enemy} воинов.\n")
            sleep(1)
        print(f"{self.name} одержал победу спустя {count_of_days} дней(дня)!")


if __name__ == '__main__':
    # Создание класса
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    # Запуск потоков и остановка текущего
    first_knight.start()
    second_knight.start()
    # Вывод строки об окончании сражения
    first_knight.join()
    second_knight.join()
    print("Все битвы закончились!")
