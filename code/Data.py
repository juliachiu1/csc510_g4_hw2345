from Csv import Csv
from Cols import Col
import statistics
import math

class Data:
    def __init__(self):
        self.col = Col()
        self.col.new()
        self.data_dic = {}
        for k in self.col.x + self.col.y:
            lst = []
            index = self.col.file.data[0].index(k)
            for j in self.col.file.data[1:]:
                lst.append(float(j[index]))
            self.data_dic[k] = lst

    def stats(self, places, showCols, type):
        ans = []
        s = '{'
        if (type == 'mid'):
            ans = self.rnd(self.mid(showCols), places)
        elif (type == 'div'):
            ans = self.rnd(self.div(showCols), places)
        for i,cols in enumerate(showCols):
            s += ':' + cols + ' ' + str(ans[i])
            if i != len(showCols) - 1: s += ' '
        s += '}'
        return s

    def data(self, showCol):
        w = 1
        if '-' in showCol: w = -1 
        at = self.col.at[showCol]
        hi = max(self.data_dic[showCol])
        lo = min(self.data_dic[showCol])
        n  = len(self.data_dic[showCol])
        sorted = self.isSorted(showCol)
        return '{:at ' + str(at) + ' :hi ' + str(hi) + ' :isSorted ' + str(sorted) + \
               ' :lo ' + str(lo) + ' :n ' + str(n) + ' :name ' + showCol + ' :w ' + str(w) + '}'

    def mid(self, showCols):
        lst_mid = []
        for k in (showCols):
            lst_mid.append(statistics.median(self.data_dic[k]))
        return lst_mid

    def div(self, showCols):
        lst_div = []
        for k in (showCols):
            lst_div.append(statistics.stdev(self.data_dic[k]))
        return lst_div

    def rnd(self, lst, places):
        mult = 10 ^ (places or 2)
        for i,x in enumerate(lst):
            lst[i] = round(math.floor(x * mult + 0.5) / mult, 3)
        return lst

    def isSorted(self, showCol):
        lst = self.data_dic[showCol]
        lstSorted = sorted(self.data_dic[showCol])
        if (lst == lstSorted): return True
        else: return False