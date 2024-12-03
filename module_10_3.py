from random import randint
from time import sleep
import threading

lock = threading.Lock()

class Bank:
    def __init__(self, balance: int, lock):
        self.balance = balance
        self.lock = lock

    def deposit(self):
        cash = 0
        for i in range(0, 100):
            random_number = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += random_number   # пополняем баланс случайной суммой
            print(f'Пополнение: {random_number}. Баланс: {self.balance}')
            sleep(0.001)


    def take(self):
        for i in range (0, 100):
            random_number = randint(50, 500)
            print(f'Запрос на снятие: {random_number}')
            if random_number <= self.balance:   # средств достаточно
                self.balance -= random_number   # уменьшаем баланс на случайную сумму
                print(f'Снятие: {random_number}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


sder = Bank(0, lock)
th1 = threading.Thread(target=sder.deposit(), args=(sder,))
th2 = threading.Thread(target=sder.take(), args=(sder,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {sder.balance}')