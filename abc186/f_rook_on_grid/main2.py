#!/bin/python3
# ref
# https://evolite.hatenablog.com/entry/20201220/1608418755

import sys
input = sys.stdin.readline
from atcoder.fenwicktree import FenwickTree

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
