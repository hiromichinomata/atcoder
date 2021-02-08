#!/bin/python3

import sys
input = sys.stdin.readline
from decimal import Decimal
def main():
  a,b,c,d= list(map(Decimal, input().strip().split()))
  result = -float('inf')
  for i in [a,b]:
    for j in [c,d]:
      result = max(result, i*j)
  print(result)

main()
