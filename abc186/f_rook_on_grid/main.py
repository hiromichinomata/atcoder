#!/bin/python3

import sys
input = sys.stdin.readline
from collections import defaultdict

def main():
  h, w, m = list(map(int, input().strip().split()))
  x = []
  y = []
  for i in range(m):
    xt, yt = list(map(int, input().strip().split()))
    xt -= 1
    yt -= 1
    x.append(xt)
    y.append(yt)

  y2x = defaultdict(int)
  x2y = defaultdict(int)
  for i in range(m):
    y2x[y[i]] = min(y2x[y[i]], x[i])
    x2y[x[i]] = min(x2y[x[i]], y[i])

  result = 0
  x_max = w - 1
  y_max = h - 1
  x_count = 0
  y_count = 0
  if 0 in x2y.keys():
    x_max = x2y[0] - 1
  if 0 in y2x.keys():
    y_max = y2x[0] - 1

  for x in x2y.keys():
    if x > x_max:
      continue
    x_count += 1
    result += x2y[x]
  result += (x_max + 1 - x_count) * h

  for y in y2x.keys():
    if y > y_max:
      continue
    y_count += 1
    result += y2x[y]
  result += (y_max + 1 - y_count) * (w - 1)

  print(result)

main()
