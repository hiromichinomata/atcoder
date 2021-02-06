#!/bin/python3

import sys
input = sys.stdin.readline
from math import ceil, floor

def main():
  x, y, r = list(map(float, input().strip().split()))

  min_x = ceil(x-r)
  max_x = floor(x+r)

  result = 0
  for i in range(min_x, max_x+1):
    h = (r**2-(x-i)**2)**0.5
    result += floor(y+h) - ceil(y-h) + 1

  print(result)

main()
