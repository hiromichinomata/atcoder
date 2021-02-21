#!/bin/python3

import sys
input = sys.stdin.readline
import math

def main():
  n, m = list(map(int, input().strip().split()))
  if m == 0:
    print(1)
    sys.exit()

  a = sorted(list(map(int, input().strip().split())))
  for i in range(m):
    a[i] -= 1

  spans = []
  pos = 0

  if a[0] > pos:
    spans.append(a[0])

  pos = a[0]

  for i in range(1, m):
    if a[i] - pos >= 2:
      spans.append(a[i] - pos - 1)
    pos = a[i]

  if n-1 > pos:
    spans.append(n-1 - pos)

  if len(spans) == 0:
    print(0)
    sys.exit()

  k = min(spans)
  result = 0
  for i in range(len(spans)):
    result += math.ceil(spans[i]/k)
  print(result)

main()
