from threading import Thread
import time
from time import sleep
from datetime import datetime

time_start = datetime.now()

class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy = 100


    def run(self):
        print(f'{self.name} на нас напали!')
        day = 1
        self.enemy -= self.power
        while self.enemy > 0:
            print(f'{self.name}, сражается {day} день, осталось {self.enemy} воинов')
            day += 1
            self.enemy -= self.power
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {day} дней!')



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

time_end = datetime.now()
res = time_end - time_start

print(f'Все битвы закончились! {res}')