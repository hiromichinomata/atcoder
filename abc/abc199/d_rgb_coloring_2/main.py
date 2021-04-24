#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n, m = list(map(int, input().strip().split()))
  edges = [[] for i in range(n)]
  for i in range(m):
    a, b = list(map(int, input().strip().split()))
    a -= 1
    b -= 1
    a, b = min(a,b), max(a,b)
    edges[a] += [b]

  print(edges)
  dp = [0]*n

  result = 0
  print(result)

main()
