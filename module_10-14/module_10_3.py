from threading import Thread, Lock
import random
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()
        self.low_balance = False

    # реализовал логику, когда баланс < 500 по своему, тк в ТЗ она описана не понятно,
    # а в примере выполнения кода задачи её нет
    # из примера:
    # Запрос на 421
    # Запрос отклонён, недостаточно средств
    # Пополнение: 133. Баланс: 426 <- меньше 500, но дальше снова идёт запрос на списание
    # Запрос на 422
    def deposit(self):
        for i in range(100):
            replenishment = random.randint(50, 500)
            self.balance += replenishment
            print(f"Пополнение: {replenishment}. Баланс: {self.balance}")
            if self.low_balance:  # баланс будет пополняться минимум до 500
                self.lock.acquire()
                while self.balance <= 500:
                    replenishment = random.randint(50, 500)
                    self.balance += replenishment
                    print(f"Пополнение: {replenishment}. Баланс: {self.balance}")
                self.low_balance = False
                self.lock.release()
            sleep(0.001)

    def take(self):
        for i in range(100):
            replenishment = random.randint(50, 500)
            print(f"Запрос на {replenishment}")
            if replenishment <= self.balance:
                self.balance -= replenishment
                print(f"Снятие: {replenishment}. Баланс: {self.balance}")
            else:
                self.low_balance = True
                print("Запрос отклонён, недостаточно средств")
            sleep(0.001)


if __name__ == "__main__":
    bk = Bank()

    th1 = Thread(target=Bank.deposit, args=(bk,))
    th2 = Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print(f'Итоговый баланс: {bk.balance}')
