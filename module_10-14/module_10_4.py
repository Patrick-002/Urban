from threading import Thread
import queue
from time import sleep
from random import randint

list_of_tables = []


class Table():
    def __init__(self, number):
        self.name = number
        self.guest = None
        list_of_tables.append(self)


class Guest(Thread):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe():
    def __init__(self, *args):
        self.queue = queue.Queue()
        self.tables = list_of_tables

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if not table.guest:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.name}')
                    break
            if not guest.is_alive():
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(
                table.guest for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.name} свободен")
                    table.guest = None
                elif not table.guest and not self.queue.empty():
                    table.guest = self.queue.get()
                    print(f"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.name}")
                    table.guest.start()


if __name__ == '__main__':
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()
