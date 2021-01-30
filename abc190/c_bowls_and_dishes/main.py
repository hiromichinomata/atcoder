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
  for i in range(k):
    if dishes[c[i]] == 0:
      dishes[c[i]] += 1
    else:
      dishes[d[i]] += 1

  result = 0
  for i in range(m):
    if dishes[a[i]] > 0 and dishes[b[i]] > 0:
      result += 1
  print(result)

main()
