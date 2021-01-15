#!/bin/python3

import sys
input = sys.stdin.readline
from decimal import Decimal

def main():
  r1, c1 = list(map(int, input().strip().split()))
  r2, c2 = list(map(int, input().strip().split()))
  r = r2 - r1
  c = c2 - c1

  if r == 0 and c == 0:
      result = 0
  elif r == c or r == -c:
      result = 1
  elif abs(r) + abs(c) <= 3:
      result = 1
  elif (r1 + c1 + r2 + c2) % 2 == 0:
      result = 2
  elif abs(r) + abs(c) <= 6:
      result = 2
  elif abs(r + c) <= 3 or abs(r - c) <= 3:
      result = 2
  else:
      result = 3
  print(result)

main()
