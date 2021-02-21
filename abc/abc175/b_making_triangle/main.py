#!/bin/python3

import sys
input = sys.stdin.readline
from itertools import combinations

def main():
  n = list(map(int, input().strip().split()))[0]
  lis= list(map(int, input().strip().split()))

  result = 0

  for i in combinations(lis, 3):
    i = sorted(i)
    if i[0] + i[1] > i[2] and len(set(i)) == 3:
      result += 1
 
  print(result)

main()
