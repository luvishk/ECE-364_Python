#! /usr/bin/env python 3.4

import re
import sys
import os

def regexfn():
    
    if len(sys.argv) != 2:
        print "Usage function_finder.py"
	exit (0)
	

    if os.access(sys.argv[1], os.R_OK) != 1:
	print "Error: Could not read " + sys.argv[1]
	exit (0)


    with open(sys.argv[1], 'r') as myFile:
        all_lines = myFile.readlines()
        for line in all_lines:

            #print line

            m = re.search(r"def[\s]*([\w]*)[\s]*\(([\w\,\=\-\s]*)\)", line)

            if m != None:

                #print m.groups()
                print m.group(1)

                m2 = re.split(r"\,", m.group(2))

                #print m2

                i=0
                p=1
                while len(m2) > i:
                    striper = m2[i].strip()
                    print "Arg"+str(p)+": "+striper
                    i+=1
                    p+=1




            #if m.group() == "def":
             #   print "valid"
            #else:
             #   print "not valid"



if __name__ == "__main__":
    regexfn()
