#!/bin/python3

import sys
input = sys.stdin.readline
from decimal import Decimal

def main():
  n,s,d = list(map(int, input().strip().split()))
  for i in range(n):
    x, y = list(map(int, input().strip().split()))
    if x < s and y > d:
      print('Yes')
      sys.exit()

  print('No')

main()
