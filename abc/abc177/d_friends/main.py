#!/bin/python3

import sys
input = sys.stdin.readline
from atcoder.dsu import DSU

def main():
  n, m = list(map(int, input().strip().split()))
  tree = DSU(n)
  for _ in range(m):
    a, b = list(map(int, input().strip().split()))
    tree.merge(a-1, b-1)

  result = 0
  for g in tree.groups():
    result = max(result, len(g))

  print(result)

main()
