#!/bin/python3

import sys
input = sys.stdin.readline
from atcoder.dsu import DSU

def main():
  n, m = list(map(int, input().strip().split()))
  a = list(map(int, input().strip().split()))
  x = []
  y = []
  tree = DSU(n)

  for _ in range(m):
    xt, yt = list(map(int, input().strip().split()))
    x.append(xt-1)
    y.append(yt-1)

  for i in range(m):
    tree.merge(x[i], y[i])

  results = []
  print(tree.groups())

main()
