#!/bin/python3

import sys
input = sys.stdin.readline
from atcoder.dsu import DSU

def main():
  n, q = list(map(int, input().strip().split()))
  tree = DSU(n)
  for _ in range(q):
    t, v1, v2 = list(map(int, input().strip().split()))
    if t == 0:
      tree.merge(v1, v2)
    if t == 1:
      if tree.same(v1, v2):
        print(1)
      else:
        print(0)

main()
