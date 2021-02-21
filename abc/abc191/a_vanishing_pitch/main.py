#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  v, t, s, d = list(map(int, input().strip().split()))
  if d < v * t or v * s < d:
    print('Yes')
  else:
    print('No')

main()
