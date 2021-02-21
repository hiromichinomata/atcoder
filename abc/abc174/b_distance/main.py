#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n, d = list(map(int, input().strip().split()))
  count = 0
  for i in range(n):
    x, y = list(map(int, input().strip().split()))
    if x**2+y**2 <= d**2:
      count += 1
 
  print(count)

main()
