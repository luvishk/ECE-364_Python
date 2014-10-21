#! /usr/bin/env python 3.4

import re
import sys

def regexfn():

    with open(sys.argv[1], 'r') as myFile:
        all_lines = myFile.readlines()
        for line in all_lines:
            #print line

            m = re.search(r"([\w.-]+)@([\w.-]+)([\s.-]+)([\d.-]+)\.([\d.-]+)", line)
            #print m.groups()

            purdue = m.group(2)

            if re.match("purdue.edu", purdue):
                print m.group(1)+"@ecn."+m.group(2)+m.group(3)+m.group(4)+"."+m.group(5)+"/100"

            else:
                print m.group(1)+"@"+m.group(2)+m.group(3)+m.group(4)+"."+m.group(5)+"/100"















if __name__ == "__main__":
    regexfn()

