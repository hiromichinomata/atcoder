#!/bin/python3

import sys
input = sys.stdin.readline
from collections import defaultdict

def main():
  n, m = list(map(int, input().strip().split()))
  a = list(map(int, input().strip().split()))

  d = defaultdict(int)
  for i in range(m):
    d[a[i]] += 1

  checked = set(a[0:m])
  result = float('inf')

  for i in range(0,n+2):
    if i not in checked:
      result = i
      break

  for i in range(m,n):
    d[a[i]] += 1
    d[a[i-m]] -= 1
    if d[a[i]] <= 0:
      result = min(result, a[i])

  print(result)

main()
