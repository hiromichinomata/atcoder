#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  a, b, c = list(map(int, input().strip().split()))
  if a**2 + b**2 < c**2:
    print('Yes')
  else:
    print('No')

main()
