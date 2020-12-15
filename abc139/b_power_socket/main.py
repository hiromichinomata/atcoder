#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  a, b = list(map(int, input().strip().split()))
  outlet = 1
  result = 0
  while(outlet < b):
    outlet += (a - 1)
    result += 1

  print(result)

main()
