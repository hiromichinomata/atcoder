#!/bin/python3

import sys
input = sys.stdin.readline
from decimal import Decimal

def main():
  n, x = list(map(int, input().strip().split()))
  x = Decimal(x)
  for i in range(n):
    v, p = list(map(int, input().strip().split()))
    x -= Decimal(v) / Decimal(100) * Decimal(p)
    if x < Decimal(0):
      print(i+1)
      sys.exit()

  print(-1)

main()
