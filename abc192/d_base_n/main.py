#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  x = list(map(str, input().strip().split()))[0]
  m = list(map(int, input().strip().split()))[0]

  d = int(sorted([char for char in str(x)], reverse=True)[0])
  result = 0
  for i in range(d+1, 36):
    converted = int(x, i)
    if converted <= m:
      result += 1

  print(result)

main()
