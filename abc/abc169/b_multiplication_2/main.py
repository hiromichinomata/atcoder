#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n = int(input().strip())
  a = list(map(int, input().strip().split()))
  result = 1
  LIMIT = 10**18
  if 0 in a:
    print(0)
    sys.exit()
  for i in a:
    result *= i
    if result > LIMIT:
      print(-1)
      sys.exit()
  print(result)

main()
