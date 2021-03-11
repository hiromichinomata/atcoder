#!/bin/python3

import sys
# input = sys.stdin.readline
from collections import Counter

if sys.platform =='ios':
  sys.stdin=open('input1.txt')

def main():
  w = list(map(str, input().strip().split()))[0]
  c = Counter(w)
  result = 'Yes'
  for k, v in c.items():
    if v % 2 != 0:
      result = 'No'
      break
  print(result)

main()
