#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n, m = list(map(int, input().strip().split()))
  a = []
  b = []
  for i in range(m):
    at, bt = list(map(int, input().strip().split()))
    at -= 1
    bt -= 1
    a.append(at)
    b.append(bt)

  k = list(map(int, input().strip().split()))[0]
  c = []
  d = []
  for i in range(k):
    ct, dt = list(map(int, input().strip().split()))
    ct -= 1
    dt -= 1
    c.append(ct)
    d.append(dt)

  dishes = [0] * n
  candidates = [dishes]
  for i in range(k):
    new_candidates = []
    for dishes in candidates:
      new_dishes = dishes.copy()
      new_dishes[c[i]] = 1
      new_candidates.append(new_dishes)
      new_dishes = dishes.copy()
      new_dishes[d[i]] = 1
      new_candidates.append(new_dishes)
    candidates = new_candidates

  result = 0
  for c in candidates:
    score = 0
    for i in range(m):
      if c[a[i]] > 0 and c[b[i]] > 0:
        score += 1
    result = max(result, score)
  print(result)

main()
