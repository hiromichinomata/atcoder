#!/bin/python3

## TODO: pass test

import copy
import sys
input = sys.stdin.readline

def main():
  n = int(input().strip())
  c = list(map(int, input().strip().split()))
  q = int(input().strip())
  result = 0

  min_all =float("INF")
  min_even = float("INF")

  def update_min(i, value):
    nonlocal min_all
    nonlocal min_even

    min_all = min(min_all, value)
    if i % 2 == 0:
      min_even = min(min_even, value)

  def single_sell(x, a):
    nonlocal result
    if c[x] - a < 0:
      return
    else:
      result += a
      c[x] -= a
      update_min(x, c[x])

  def set_sell(a):
    nonlocal result
    nonlocal min_even
    nonlocal min_all

    if min_even < a:
      return

    min_even -= a
    min_all = min(min_all, min_even)

    for i in range(0, len(c), 2):
      result += a
      c[i] -= a

  def all_sell(a):
    nonlocal result
    nonlocal min_all
    nonlocal min_even

    if min_all < a:
      return

    min_all -= a
    min_even -= a

    for i in range(len(c)):
      result += a
      c[i] -= a


  for i in range(len(c)):
    update_min(i, c[i])

  for i in range(q):
    query = list(map(int, input().strip().split()))
    if query[0] == 1:
      single_sell(query[1]-1, query[2])
    elif query[0] == 2:
      set_sell(query[1])
    elif query[0] == 3:
      all_sell(query[1])

  print(result)

main()
