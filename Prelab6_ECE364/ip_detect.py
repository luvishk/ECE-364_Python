#! /usr/bin/env python 3.4

import re
import sys

def regexfn():

    with open(sys.argv[1], 'r') as myFile:
        all_lines = myFile.readlines()
        for line in all_lines:

            m = re.search(r"([\d.-]+)\:([a-z0-9]+)", line)

            ipaddr = re.findall(r"([0-9]+)", m.group(1))
            portnumb = m.group(2)

            if int(ipaddr[0]) <= 255 and int(ipaddr[0]) >= 0 and int(ipaddr[1]) <= 255 and int(ipaddr[1]) >= 0 and int(ipaddr[2]) <= 255 and int(ipaddr[2]) >= 0 and int(ipaddr[3]) <= 255 and int(ipaddr[3]) >= 0 :
                if(portnumb == "25s"):
                    print m.group(0)+" - Invalid Port Number"
                elif int(portnumb) < 1024:
                    print m.group(0)+" - Valid (root privileges required)"
                elif int(portnumb) > 1023 and int(portnumb) < 32767:
                    print m.group(0)+" - Valid"
                elif int(portnumb) > 32767:
                    print m.group(0)+" - Invalid Port Number"
            else:
                print m.group(0)+" - Invalid IP Address"



if __name__ == "__main__":
    regexfn()
