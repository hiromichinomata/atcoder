#!/bin/python3
# ref
# https://evolite.hatenablog.com/entry/20201220/1608418755
# pypy3

import sys
input = sys.stdin.readline
from atcoder.fenwicktree import FenwickTree

def main():
  h, w, m = list(map(int, input().strip().split()))
  x2y = [w] * h
  y2x = [h] * w
  obs_y2x = [[] for _ in range(h)]
  for i in range(m):
    xt, yt = list(map(int, input().strip().split()))
    xt -= 1
    yt -= 1
    x2y[xt] = min(x2y[xt], yt)
    y2x[yt] = min(y2x[yt], xt)
    obs_y2x[xt].append(yt)

  result = sum(x2y[: y2x[0]]) + sum(y2x[: x2y[0]])
  tree = FenwickTree(w)
  for j in range(x2y[0]):
      tree.add(j, 1)
  for i in range(y2x[0]):
      for j in obs_y2x[i]:
          tree.add(j, -tree.sum(j, j+1))
      result -= tree.sum(0, x2y[i])
  print(result)

main()
