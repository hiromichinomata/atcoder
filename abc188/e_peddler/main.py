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
  profits = [-float('inf')] * len(tree.groups())
  index = -1
  for l in tree.groups():
    index += 1
    if len(l) <= 1:
      continue
    edges = sorted(l)
    min_value = 10**9
    for i in range(len(edges)):
      profits[index] = max(profits[index], a[edges[i]] - min_value)
      min_value = min(min_value, a[edges[i]])

  print(max(profits))

main()
