#!/bin/python3

import sys
input = sys.stdin.readline
from atcoder.math import floor_sum

def main():
  t = list(map(int, input().strip().split()))[0]
  for _ in range(t):
    n, m, a, b = list(map(int, input().strip().split()))
    print(floor_sum(n, m, a, b))

main()
