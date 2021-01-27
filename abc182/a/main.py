#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  x = list(map(int, input().strip().split()))[0]
  if x >= 0:
    print(x)
  else:
    print(0)

main()
