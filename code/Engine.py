from curses import pair_content
from typing import Dict
from xml.etree.ElementTree import tostring
from Num import num
from Sym import Sym
from Data import Data
from Csv import Csv
from Test import Test
# from Cli import Cli
import re
import sys

ALL = 7
help = """ 
CSV : summarized csv file
(c) 2022 Tim Menzies <timm@ieee.org> BSD-2 license
USAGE: lua seen.lua [OPTIONS]
OPTIONS:
 -e  --eg        start-up example                      = nothing
 -d  --dump      on test failure, exit with stack dump = false
 -f  --file      file with csv data                    = ../data/auto93.csv
 -h  --help      show help                             = false
 -n  --nums      number of nums to keep                = 512
 -s  --seed      random number seed                    = 10019
 -S  --seperator feild seperator                       = , ]]"""

def setup(the):
    pattern = re.compile(r"\n [-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)")
    for match in pattern.finditer(help):
        the[match.group(1)] = coerce(match.group(2))
    return the

def coerce(s):
    def fun(s1):
        s1 = True if (s1=="True" or s1=="true") else (False if (s1=="false" or s1=="False") else s1)
        return s1

    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            search = re.search(r"^\s*(.*)\s*$", s)
            return fun(search.group(1))

def cli(t):
    for slot in t:
        v = str(t[slot])
        if(len(sys.argv) > 1):
            for n, x in enumerate(sys.argv):
                if(x == "-"+slot[0:1] or x == "--"+slot):
                    v = "true" if (v=="false" or v=="False") else ("false" if (v=="true" or v=="True") else sys.argv[n+1])
        t[slot] = coerce(v)

    if t['help']:
        sys.exit("\n"+str(help)+"\n") 
    return t


def main():

    test = Test()
    result = []
    result.append(test.test_bignum())
    result.append(test.test_data())
    result.append(test.test_num())
    result.append(test.test_stats())
    result.append(test.test_sym())
    result.append(test.test_csv())

    the = {}
    the = setup(the)
    the = cli(the)

    if the:
        result.append(True)
    # show result
    print("-----------------------------------")
    print(the)
    print("!!!!!!	PASS	the	true")
    
    if result.count(True) == ALL:
        print("!!!!!!	PASS	ALL	true\n")
    else:
        print("!!!!!!	PASS	All	false\n")

    print(result.count(True), " test cases passed")
    print(result.count(False), " test cases failed")

if __name__ == '__main__':
    main()



