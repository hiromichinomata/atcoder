#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  x, y = list(map(int, input().strip().split()))
  if abs(x-y) <= 2:
    print('Yes')
  else:
    print('No')

main()
