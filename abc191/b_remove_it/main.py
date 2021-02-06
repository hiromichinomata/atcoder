#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n, x = list(map(int, input().strip().split()))
  a = list(map(int, input().strip().split()))

  result = []
  for i in range(len(a)):
    if a[i] != x:
      result.append(str(a[i]))

  print(" ".join(result))

main()
