#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  x = list(map(int, input().strip().split()))[0]
  result = -x % 100
  if result == 0:
    print(100)
  else:
    print(result)

main()
