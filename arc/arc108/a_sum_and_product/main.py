#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  s, p = list(map(int, input().strip().split()))
  for n in range(1, 10**6+1):
    if p % n == 0:
      m = p // n
      if n + m == s:
        print('Yes')
        sys.exit()
  print('No')

main()
