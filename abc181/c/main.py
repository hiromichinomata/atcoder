#!/bin/python3
# pypy3

import sys
input = sys.stdin.readline

def main():
  n = list(map(int, input().strip().split()))[0]
  a = list(map(int, input().strip().split()))

  result = 0

  for i in range(n):
    tmp_min = float('inf')
    for j in range(i, n):
      tmp_min = min(tmp_min, a[j])
      result = max(result, tmp_min* (j-i+1))
  print(result)

main()
