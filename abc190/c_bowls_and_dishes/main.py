#!/bin/python3
# pypy3

import sys
input = sys.stdin.readline

def main():
  n, m = list(map(int, input().strip().split()))
  a = []
  b = []
  for i in range(m):
    at, bt = list(map(int, input().strip().split()))
    at -= 1
    bt -= 1
    a.append(at)
    b.append(bt)

  k = list(map(int, input().strip().split()))[0]
  c = []
  d = []
  for i in range(k):
    ct, dt = list(map(int, input().strip().split()))
    ct -= 1
    dt -= 1
    c.append(ct)
    d.append(dt)

main()
