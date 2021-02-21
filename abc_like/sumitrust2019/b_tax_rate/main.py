#!/bin/python3

import sys
input = sys.stdin.readline
import math

def main():
  n = int(input().strip())
  result = math.ceil(n / 1.08)
  if math.floor(result*1.08) == n:
    print(result)
  else:
    print(':(')

main()
