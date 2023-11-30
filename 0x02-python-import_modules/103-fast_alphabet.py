#!/usr/bin/python3
import sys
print(*(chr(i) for i in range(ord('A'), ord('Z') + 1)), sep='', end='\n', file=sys.stdout)