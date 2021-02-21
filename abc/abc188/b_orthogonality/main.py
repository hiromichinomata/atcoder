#!/bin/python3
# pypy3

import sys
input = sys.stdin.readline
from decimal import Decimal

def main():
  n = list(map(int, input().strip().split()))[0]
  a = list(map(int, input().strip().split()))
  b = list(map(int, input().strip().split()))
  result = Decimal(0)
  for i in range(n):
    result += Decimal(a[i])*Decimal(b[i])

  if result == 0:
    print('Yes')
  else:
    print('No')

main()
