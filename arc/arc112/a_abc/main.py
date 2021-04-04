#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n = list(map(int, input().strip().split()))[0]
  for _ in range(n):
    l, r = list(map(int, input().strip().split()))
    d = r - 2 * l + 1
    if d < 0:
      print(0)
    else:
      result = d * (d+1) // 2
      print(result)
main()
