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
    edges[a] += [b]
    edges[b] += [a]

  result = 1
  for i in range(n):
    e = edges[i]
    if len(e) >= 3:
      print(0)
      sys.exit()
    count = 0
    mul = 3
    for j in e:
      if j < i:
        mul -= 1
    result *= mul

  print(result)

main()
