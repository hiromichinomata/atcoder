#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n = int(input().strip())
  a = list(map(int, input().strip().split()))
  result = 1
  LIMIT = 10**18
  for i in a:
    result *= i
    if i > LIMIT:
      print(-1)
      sys.exit( )
  print(result)

main()
