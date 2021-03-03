#!/bin/python3

import sys
input = sys.stdin.readline
from itertools import product

def main():
  h, w, k = list(map(int, input().strip().split()))
  pairs = [True, False]
  c = []
  for _ in range(h):
    ct = list(map(str, input().strip().split()))[0]
    c.append(ct)

  result = 0
  for selection_h in product(pairs, repeat=h):
    for selection_w in product(pairs, repeat=w):
      count = 0
      for hi in range(h):
        for wi in range(w):
          if selection_h[hi] or selection_w[wi]:
            continue
          elif c[hi][wi] == '#':
            count += 1
      if count == k:
        result += 1
  print(result)

main()
