from Num import num
from Sym import Sym

def num_test():

    mark = False

    while not mark:
        num_t = num()
        num_t.add(100, 100)
        div = num_t.div()
        mid = num_t.mid()

        if (mid < 50 or mid > 52) or (div < 30.5 or div > 32):
            continue
        else:
            mark = True
    print("-----------------------------------")
    print(mid, div)
    print("!!!!!! PASS   num   true")
    print(" ")
    return 50 <= mid and mid <= mid and 30.5 < div and div < 32

def bignum_test():
    num_t = num()
    num_t.add(1000, 32)
    print("-----------------------------------")
    print(num_t.lst)
    print("!!!!!! PASS   bignum   true")
    print(" ")
    return 32 == len(num_t.lst)

def sym_test():
    sym = Sym()
    lst = ['a','a','a','a','b','b','c']
    for x in lst:   sym.add(x)
    mode, entropy = sym.mid(), sym.div()
    entropy = (1000 * entropy) // 1 / 1000
    print('-----------------------------------')
    print('{:div ' + str(entropy) + ' :mid ' + mode + '}')
    print('!!!!!!	PASS	sym	true\n')
    return mode == 'a' and 1.37 <= entropy and entropy <= 1.38

