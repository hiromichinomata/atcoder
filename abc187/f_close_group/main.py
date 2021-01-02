#!/bin/python3

import sys
input = sys.stdin.readline
from atcoder.dsu import DSU

def main():
  n, m = list(map(int, input().strip().split()))
  tree = DSU(n)
  for i in range(m):
    a, b = list(map(int, input().strip().split()))
    a = a - 1
    b = b - 1
    if a >= b:
      tree.merge(a, b)

  print(len(tree.groups()))

main()
