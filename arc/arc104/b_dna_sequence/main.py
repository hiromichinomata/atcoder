#!/bin/python3

import sys
input = sys.stdin.readline
from collections import defaultdict

def main():
  n, s = list(map(str, input().strip().split()))
  n = int(n)
  result = 0

  for i in range(n):
    d = defaultdict(int)
    for j in range(n-i):
      char = s[i+j]
      d[char] += 1
      if d['A'] == d['T'] and d['C'] == d['G']:
        result += 1

  print(result)

main()
