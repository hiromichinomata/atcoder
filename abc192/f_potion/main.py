#!/bin/python3

import sys
input = sys.stdin.readline
from itertools import permutations

def main():
  n, x = list(map(int, input().strip().split()))
  a = list(map(int, input().strip().split()))
  a = sorted(a, reverse=True)

  total = 0
  result = float('inf')
  for i in range(n):
    for j in permutations(a, i+1):
      total = sum(j)
      if (x - total) % (i+1) == 0:
        result = min(result, (x - total) // (i+1))

  print(result)

main()
