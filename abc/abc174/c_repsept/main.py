#!/bin/python3
# pypy3

import sys
input = sys.stdin.readline

def main():
  k = list(map(int, input().strip().split()))[0]

  num = 0
  for i in range(k):
    num = (num * 10 + 7) % k
    if num == 0:
      print(i+1)
      sys.exit()

  print(-1)

main()
