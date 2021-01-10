#!/bin/python3

import sys
input = sys.stdin.readline
from decimal import Decimal

def main():
  n, cost = list(map(int, input().strip().split()))
  for _ in range(n):
    a, b, c_prime = list(map(int, input().strip().split()))
  aoki = []
  pairs = []
  for _ in range(n):
    a, b = list(map(int, input().strip().split()))
    aoki.append(Decimal(a))
    pairs.append([Decimal(a), Decimal(b)])

  aoki_score = sum(aoki)
  takahashi_score = 0
  pairs = sorted(pairs, key=lambda a: 2 * a[0] + a[1], reverse=True)
  count = 0
  for i in range(n):
    aoki, takahashi = pairs[i]
    aoki_score -= aoki
    takahashi_score += aoki + takahashi
    count += 1
    if aoki_score < takahashi_score:
      break
  print(count)

main()
