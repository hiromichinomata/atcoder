#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n = list(map(int, input().strip().split()))[0]
  x = [0]*n
  c = [0]*n
  for i in range(n):
    x[i], c[i] = list(map(int, input().strip().split()))
  result = 0
  print(result)

main()
