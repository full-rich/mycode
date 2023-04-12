#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
  For - Using a file's lines as a source for the for-loop"""

with open("dnsservers.txt", "r") as dnsfile:
    #dnslist = dnsfile.readlines() - don't need this, for loop does this
    for svr in dnsfile:
        print(svr, end="")