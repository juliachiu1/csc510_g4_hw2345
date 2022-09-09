import random
import statistics

class num:
    def __init__(self):
        self.lst = []
        self.n = 0

    def add(self, numbers, limit=500):
        self.n += 1
        if self.n <= limit:
            self.lst.append(numbers)
        elif random.random() < limit / self.n:
            pos = random.randint(0, len(self.lst) - 1)
            self.lst[pos] = numbers

    def div(self):
        return statistics.stdev(self.lst)

    def mid(self):
        return statistics.median(self.lst)

