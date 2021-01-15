#!/bin/python3

import sys
input = sys.stdin.readline
from decimal import Decimal

def main():
  n, x = list(map(int, input().strip().split()))
  s = input().strip()
  score = Decimal(x)

  for i in range(n):
    if s[i] == 'o':
      score += 1
    else:
      score -= 1
    score = max(score, 0)

  print(score)

main()
