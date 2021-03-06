#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n = list(map(int, input().strip().split()))[0]
  a = []
  b = []
  sum_min = float('inf')
  for _ in range(n):
    at, bt = list(map(int, input().strip().split()))
    a.append(at)
    b.append(bt)
    sum_min = min(sum_min, at+bt)

  min_a = min(a)
  min_b = min(b)
  a_index = a.index(min_a)
  if min_b == b[a_index]:
    b.pop(a_index)
    min_b = min(b)
  result = min(sum_min, max(min_a, min_b))
  print(result)

main()
