#!/bin/python3

import sys
input = sys.stdin.readline
from collections import defaultdict

def main():
  n = int(input().strip())
  a = []
  for i in range(n):
    a.append(list(input().strip()))

  b = defaultdict(list)
  for i in range(n):
    for j in range(n):
      b[i].append(a[j][i])

  for i in range(n):
    if b[i] == b[i][::-1]:
      print(''.join(b[i]))
      sys.exit()

  print(-1)

main()
