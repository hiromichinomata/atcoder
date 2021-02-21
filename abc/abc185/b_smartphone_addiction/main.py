#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n, m, t = list(map(int, input().strip().split()))
  a = []
  b = []
  for i in range(m):
    at, bt = list(map(int, input().strip().split()))
    a.append(at)
    b.append(bt)

  battery = n
  ct = 0

  for i in range(m):
    at = a[i]
    bt = b[i]

    battery -= (at - ct)
    if battery <= 0:
      print('No')
      sys.exit()
    ct = at

    battery += (bt - at)
    if battery > n:
      battery = n
    ct = bt

  battery -= (t - ct)

  if battery <= 0:
    print('No')
  else:
    print('Yes')

main()
