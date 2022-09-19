import sys
import re

def setup(the):
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

    pattern = re.compile(r"\n [-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)")
    for match in pattern.finditer(help):
        the[match.group(1)] = match.group(2)
    return the

def coerce(s):
    def fun(s1):
        s1 = True if s1=="true" else (False if s1=="false" else s1)
        return s1

    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return fun(s.strip())

def cli(t):
    for slot in t:
        # print("slot: "+slot)
        v = str(t[slot])
        for n, x in enumerate(sys.argv):
            # print("x: "+x)
            # print("slot[0:1]: "+slot[0:1])
            if(x == "-"+slot[0:1] or x == "--"+slot):
                v = "true" if v=="false" else ("false" if v=="true" else sys.argv[n+1])
                # print("v: "+v)
        t[slot] = coerce(v)
    if t["help"]:
        sys.exit("\nhelp\n") 
    return t

the = {}
the = setup(the)
the = cli(the)
# show result
print(the)
