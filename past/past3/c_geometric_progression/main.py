#!/bin/python3
# pypy3

import sys
input = sys.stdin.readline

def main():
  a, r, n = list(map(int, input().strip().split()))
  v = a
  LIMIT = 10**9
  for _ in range(n-1):
    v *= r
    if v > LIMIT:
      print('large')
      sys.exit()

  print(v)

main()
