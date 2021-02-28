#!/bin/python3

import sys
input = sys.stdin.readline
import math

def main():
  n = list(map(int, input().strip().split()))[0]

  result = set()
  for i in range(2, round(n**0.5+1)):
    max_power = int(math.log(n, i))
    for j in range(2, max_power+1):
      result.add(i**j)

  print(n-len(result))

main()
