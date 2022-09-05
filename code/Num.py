import random
import statistics

class num:
    def __init__(self):
        self.lst = []

    def add(self, numbers, limit):
        for i in range(numbers):

            temp = random.randint(1, numbers)

            if temp in self.lst:
                continue
            else:
                self.lst.append(temp)

            if len(self.lst) > limit:
                self.lst.pop(random.randint(0, limit - 1))
        self.lst.sort()

    def div(self):
        return statistics.stdev(self.lst)

    def mid(self):
        return statistics.median(self.lst)

''' Test
tt = num()
tt.add(100)
print(tt.div(), tt.mid())
'''