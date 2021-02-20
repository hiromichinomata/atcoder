#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n, x = list(map(int, input().strip().split()))
  a = list(map(int, input().strip().split()))
  a = sorted(a, reverse=True)

  total = 0
  result = float('inf')
  for i in range(n):
    total += a[i]
    if (x - total) % (i+1) == 0:
      result = min(result, (x - total) // (i+1))

  print(result)

main()
