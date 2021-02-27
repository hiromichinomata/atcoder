#!/bin/python3

import sys
input = sys.stdin.readline
import math

def main():
  n = list(map(int, input().strip().split()))[0]

  result = 0
  for i in range(2, round(n**0.5+1)): 
    if round(i ** 0.5) ** 2 == i:
      continue
    result += max(int(math.log(n, i)) -1, 0)

  print(n-result)

main()
