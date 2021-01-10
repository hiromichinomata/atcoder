#!/bin/python3

import sys
input = sys.stdin.readline
from decimal import Decimal

def main():
  n, c_prime = list(map(int, input().strip().split()))
  a = []
  b = []
  c = []
  for _ in range(n):
    at, bt, ct = list(map(int, input().strip().split()))
    a.append(at)
    b.append(bt)
    c.append(ct)

  result = 0
  for i in range(n):
    cost_t = min(c_prime, c[i])
    result += (b[i] - a[i] + 1) * cost_t

  print(result)

main()
