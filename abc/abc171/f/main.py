#!/bin/python3

import sys
input = sys.stdin.readline
from decimal import Decimal

def main():
  x, y = list(map(Decimal, input().strip().split()))
  if x == y:
    print(0)
    sys.exit()
  if x > y:
    print(x-y)
    sys.exit()

main()
