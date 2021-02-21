#!/bin/python3

import sys
input = sys.stdin.readline
from collections import defaultdict

def main():
  n = list(map(int, input().strip().split()))[0]
  a = list(map(int, input().strip().split()))
  rest = a
  for i in range(n-1):
    tmp = []
    for j in range(0, len(rest), 2):
      tmp.append(max(rest[j], rest[j+1]))
    rest = tmp

  result = a.index(min(rest)) + 1
  print(result)

main()
