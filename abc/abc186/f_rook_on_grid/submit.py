import types

_atcoder_code = """
# Python port of AtCoder Library.

__version__ = '0.0.1'
"""

atcoder = types.ModuleType('atcoder')
exec(_atcoder_code, atcoder.__dict__)

_atcoder_fenwicktree_code = """
import typing


class FenwickTree:
    '''Reference: https://en.wikipedia.org/wiki/Fenwick_tree'''

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.data = [0] * n

    def add(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        return self._sum(right) - self._sum(left)

    def _sum(self, r: int) -> typing.Any:
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r

        return s
"""

atcoder.fenwicktree = types.ModuleType('atcoder.fenwicktree')
exec(_atcoder_fenwicktree_code, atcoder.fenwicktree.__dict__)
FenwickTree = atcoder.fenwicktree.FenwickTree

#!/bin/python3
# ref
# https://evolite.hatenablog.com/entry/20201220/1608418755
# pypy3

import sys
input = sys.stdin.readline
# from atcoder.fenwicktree import FenwickTree

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
