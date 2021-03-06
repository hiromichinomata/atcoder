#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  a, b = list(map(int, input().strip().split()))
  total = a + b
  if total >= 15 and b >= 8:
    print(1)
  elif total >= 10 and b >= 3:
    print(2)
  elif total >= 3:
    print(3)
  else:
    print(4)

main()
