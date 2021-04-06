#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n = list(map(int, input().strip().split()))[0]
  a = list(map(int, input().strip().split()))

  result = 0

  for i in range(1, n):
    if a[i-1] > a[i]:
      result += a[i-1] - a[i]
      a[i] = a[i-1]

  print(result)

main()
