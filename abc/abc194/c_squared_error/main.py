#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n = list(map(int, input().strip().split()))[0]
  a = list(map(int, input().strip().split()))
  a = sorted(a)
  min_a = a[0]
  if min_a < 0:
    for i in range(n):
      a[i] += abs(min_a)

  sum_prev = 0
  sum_prev_pow2 = 0
  result = 0
  for i in range(1, n):
    j = i-1
    sum_prev += a[j]
    sum_prev_pow2 += a[j]**2
    plus = i * a[i]**2 + sum_prev_pow2 - 2 * a[i] * sum_prev
    result += plus

  print(result)

main()
