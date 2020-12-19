#!/bin/python3

import sys
input = sys.stdin.readline
from collections import defaultdict

def main():
  h, w = list(map(int, input().strip().split()))
  a = []
  for i in range(h):
    at = list(map(int, input().strip().split()))
    for j in range(w):
      a.append(at[j])

  min_a = min(a)
  result = 0
  for i in range(len(a)):
    result += a[i] - min_a
  print(result)

main()
