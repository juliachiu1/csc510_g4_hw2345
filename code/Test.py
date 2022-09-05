from Num import num

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


