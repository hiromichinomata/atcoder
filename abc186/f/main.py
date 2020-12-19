#!/bin/python3

import sys
input = sys.stdin.readline
from atcoder.segtree import SegTree

def xor(a, b):
  return a^b

def main():
  n, q = list(map(int, input().strip().split()))
  a = list(map(int, input().strip().split()))

  segtree = SegTree(xor, -1, a)

  for i in range(q):
      t, x, y = list(map(int, input().strip().split()))
      x -= 1

      if t == 1:
        tmp = segtree.get(x)
        segtree.set(x, tmp^y)
      else:
        print(segtree.prod(x, y))

main()
