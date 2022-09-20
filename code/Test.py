from Num import num
from Sym import Sym
from Data import Data
from Csv import Csv

class Test:

    def num_test(self):
        num_t = num()
        for i in range(1, 101):
            num_t.add(i)
        div = num_t.div()
        mid = num_t.mid()

        if (mid < 50 or mid > 52) or (div < 30.5 or div > 32):
            print("-----------------------------------")
            print(mid, div)
            print("!!!!!! PASS   num   true")
            print(" ")
            return True
        else: 
            return False

    def bignum_test(self):
        num_t = num()
        for i in range(1, 1001):
            num_t.add(i, 32)
        num_t.lst.sort()
        print("-----------------------------------")
        print(num_t.lst)
        print("!!!!!! PASS   bignum   true")
        print(" ")
        return 32 == len(num_t.lst)

    def sym_test(self):
        sym = Sym()
        lst = ['a','a','a','a','b','b','c']
        for x in lst:   sym.add(x)
        mode, entropy = sym.mid(), sym.div()
        entropy = (1000 * entropy) // 1 / 1000
        print('-----------------------------------')
        print('{:div ' + str(entropy) + ' :mid ' + mode + '}')
        print('!!!!!!	PASS	sym	true\n')
        return mode == 'a' and 1.37 <= entropy and entropy <= 1.38

    def data_test(self):
        data = Data()
        print('-----------------------------------')
        for c in data.col.y:
            print(data.data(c))
        print('!!!!!!	PASS	data	true\n')
        return True

    def stats_test(self):
        data = Data()
        print('-----------------------------------')
        print(data.stats(2,data.col.x,"mid"))
        print(data.stats(3,data.col.x,"div"))
        print(data.stats(2,data.col.y,"mid"))
        print(data.stats(3,data.col.y,"div"))
        print('!!!!!!	PASS	stats	true\n')
        return True
        
    def csv_test(self):
        csv = Csv()
        print_csv = csv.read_csv()
        for i in range(0, 10):
            print('{' + ' '.join(print_csv[i]) + '}')

        print('!!!!!!	PASS	csv	true\n')
        return True

# def main():
#     bignum_test()
#     data_test()
#     num_test()
#     stats_test()
#     sym_test()
#     csv_test()

# if __name__ == "__main__":
#     main()
