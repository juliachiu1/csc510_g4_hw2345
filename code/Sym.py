from curses import keyname
import math


class Sym:
    def __init__(self, c = 0, s = ""):
        self.n = 0;
        self.at = c; 
        self.name = s;
        self._has = {};
    
    def add(self, v):
        if v != "?":
            self.n = self.n + 1
            self._has[v] = 1 + self._has.get(v, 0)

    def mid(self):
        most = -1
        for k,v in self._has.items():
            if v > most:
                mode = k
                most = v
        return mode

    def div(self):
        def fun(p):
            return p * math.log(p, 2.0)
        e=0
        for _,n in self._has.items():
            if n > 0:
                e = e - fun(n/self.n)
        return e

""" TEST
sym1 = Sym()
sym1.add('a')
sym1.add('a')
sym1.add('a')
sym1.add('a')
sym1.add('b')
sym1.add('b')
sym1.add('c')
print("mode: {}".format(sym1.mid()))
print("entropy: {}".format(sym1.div()))
"""

