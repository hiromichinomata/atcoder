#!/bin/python3

import sys

S = input().strip()

try:
    i = int(S)
    print(i*2)
except ValueError:
    print("error")
