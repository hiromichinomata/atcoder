#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  x, y = list(map(int, input().strip().split()))
  if x == y:
    print(0)
    sys.exit()
  if x > y:
    print(x-y)
    sys.exit()

main()
