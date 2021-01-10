#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n = int(input().strip())
  a = []
  b = []
  for i in range(n):
    at, bt = list(map(int, input().strip().split()))
    a.append(at)
    b.append(bt)


  print()

main()
