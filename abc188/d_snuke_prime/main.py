#!/bin/python3

import sys
input = sys.stdin.readline
from decimal import Decimal

def main():
  n, C = list(map(int, input().strip().split()))
  a = []
  b = []
  c = []
  for _ in range(n):
    at, bt, ct = list(map(int, input().strip().split()))
    at -= 1
    a.append(at)
    b.append(bt)
    c.append(ct)

  events = []
  for i in range(n):
    events.append([a[i], c[i]])
    events.append([b[i], -c[i]])

  events = sorted(events)

  result = 0
  current_cost = 0
  prev_t = 0

  for t, cost in events:
    if t != prev_t:
      result += min(C, current_cost) * (t - prev_t)
      prev_t = t
    current_cost += cost

  print(result)

main()
