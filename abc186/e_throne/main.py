#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  t = int(input().strip())
  for i in range(t):
    n, s, k = list(map(int, input().strip().split()))
    k = k % n

  print()

main()
