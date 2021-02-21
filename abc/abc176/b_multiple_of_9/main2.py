#!/bin/python3

import sys
input = sys.stdin.readline
import decimal
from decimal import Decimal

decimal.getcontext().prec=200000

def main():
  n = list(map(Decimal, input().strip().split()))[0]
  if n% Decimal(9)==0:
    print('Yes')
  else:
    print('No')

main()
