#!/bin/python3
# pypy3

import sys
input = sys.stdin.readline
from itertools import product

def main():
  n = list(map(int, input().strip().split()))[0]
  a = list(map(int, input().strip().split()))
  result = float('inf')
  for cond in product([True, False], repeat=n):
    arr = []
    ored = None
    for i in range(n):
      if ored is None:
        ored = a[i]
      else:
        if cond[i]:
          ored |= a[i]
        else:
          arr.append(ored)
          ored = a[i]
    arr.append(ored)

    xored = arr[0]
    for i in range(1, len(arr)):
      xored ^= arr[i]
    result = min(result, xored)

  print(result)

main()
