#!/bin/python3

import copy
import sys
input = sys.stdin.readline

def main():
  s = input().strip()
  a = b = c = 0
  for i in range(len(s)):
    if s[i] == 'a':
      a += 1
    elif s[i] == 'b':
      b += 1
    else:
      c += 1

  if a >= b and a >= c:
    print('a')
  elif b >= a and b >= c:
    print('b')
  elif c >= a and c >= b:
    print('c')

main()
