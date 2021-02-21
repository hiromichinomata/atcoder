#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n = int(input().strip())
  a = list(map(int, input().strip().split()))
  a = [0] + a
  result = []

  for i in range(1, n+1):
    x = i
    for j in range(1, n+1):
      x = a[x]
      if x == i:
        result.append(j)
        break

  print(' '.join(map(str, result)))

main()
