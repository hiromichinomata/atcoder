#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n, x = list(map(int, input().strip().split()))
  for i in range(n):
    v, p = list(map(int, input().strip().split()))
    x -= v/100.0*p
    if int(x) < 0:
      print(i+1)
      sys.exit()

  print(-1)

main()
