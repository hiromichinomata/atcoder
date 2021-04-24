#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n, m = list(map(int, input().strip().split()))
  x = [0]*m
  y = [0]*m
  z = [0]*m
  for i in range(m):
    x[i], y[i], z[i] = list(map(int, input().strip().split()))

  print(x)

main()
