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

import sys
input = sys.stdin.readline
# from atcoder.fenwicktree import FenwickTree

h, w, m = map(int, input().split())
row, col = [w] * h, [h] * w
obs = [[] for _ in range(h)]
for _ in range(m):
    i, j = map(lambda x: int(x) - 1, input().split())
    row[i] = min(row[i], j)
    col[j] = min(col[j], i)
    obs[i].append(j)
ans = sum(row[: col[0]]) + sum(col[: row[0]])
tree = FenwickTree(w)
for j in range(row[0]):
    tree.add(j, 1)
for i in range(col[0]):
    for j in obs[i]:
        tree.add(j, -tree.sum(j, j+1))
    ans -= tree.sum(0, row[i])
print(ans)
