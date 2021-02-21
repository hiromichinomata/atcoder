#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n,m,x,y = list(map(int, input().strip().split()))
  a = []
  b = []
  t = []
  k = []
  for _ in range(m):
    at, bt, tt, kt = list(map(int, input().strip().split()))
    a.append(at)
    b.append(bt)
    t.append(tt)
    k.append(kt)


main()
