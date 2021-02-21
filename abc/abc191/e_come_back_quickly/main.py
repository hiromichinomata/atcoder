#!/bin/python3

import sys
input = sys.stdin.readline
from atcoder.mincostflow import MCFGraph

def main():
  n,m = list(map(int, input().strip().split()))
  g = MCFGraph(n)
  a = []
  b = []
  c = []
  for _ in range(n):
    at, bt, ct = list(map(int, input().strip().split()))
    at = at-1
    bt = bt-1
    ct = ct-1
    a.append(at)
    b.append(bt)
    c.append(ct)
    g.add_edge(at, bt, float('inf'), ct)

  result = g.flow(a[0], a[0])
  print(result)

main()
