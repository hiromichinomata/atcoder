#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n = list(map(int, input().strip().split()))[0]
  a = []
  p = []
  x = []
  for _ in range(n):
    at, pt, xt = list(map(int, input().strip().split()))
    a.append(at)
    p.append(pt)
    x.append(xt)

  flag = -1
  result = float('inf')
  for i in range(n):
    diff = 2 * x[i] - 2 * a[i] - 1
    if diff > 0:
      result = min(result, p[i])
      flag = 0

  if flag == -1:
    print(-1)
  else:
    print(result)

main()
