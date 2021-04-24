#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n = list(map(int, input().strip().split()))[0]
  a = list(map(int, input().strip().split()))
  b = list(map(int, input().strip().split()))

  max_a = max(a)
  min_b = min(b)
  if max_a > min_b:
    print(0)
  else:
    print(min_b-max_a+1)

main()
