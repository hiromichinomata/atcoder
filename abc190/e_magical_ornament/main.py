#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n, m = list(map(int, input().strip().split()))
  a = []
  b = []
  for _ in range(m):
    at, bt = list(map(int, input().strip().split()))
    a.append(at)
    b.append(bt)

  k = list(map(int, input().strip().split()))[0]
  c = list(map(int, input().strip().split()))


  print(-1)

main()
