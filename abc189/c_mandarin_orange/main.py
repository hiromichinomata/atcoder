#!/bin/python3

import sys
input = sys.stdin.readline
# from atcoder.segtree import SegTree

def operation(a, b):
  return min(a,b)

def main():
  n = list(map(int, input().strip().split()))[0]
  a = list(map(int, input().strip().split()))

  segtree = SegTree(operation, float('inf'), a)
  result = 0

  for i in range(n):
    for j in range(i+1, n+1):
      result = max(result, segtree.prod(i, j) * (j-i))
  print(result)

main()
