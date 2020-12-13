#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n, q = list(map(int, input().strip().split()))
  a = list(map(int, input().strip().split()))
  for i in range(q):
    t, x, y = list(map(int, input().strip().split()))
    x -= 1

    if t == 1:
      a[x] = a[x] ^ y
    else:
      result = 0
      for i in range(x, y):
        if result == 0:
          result = a[i]
        else:
          result ^= a[i]

      print(result)

main()
