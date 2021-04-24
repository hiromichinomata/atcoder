#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n, m = list(map(int, input().strip().split()))
  a = [0] * n
  b = [0] * n
  for i in range(m):
    a[i], b[i] = list(map(int, input().strip().split()))

  print(a)

main()
