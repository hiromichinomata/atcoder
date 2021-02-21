#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
  sys.stdin=open('input1.txt')

def main():
  c = list(map(int, input().strip().split()))
  c = sorted(c)
  t = c.pop()
  if sum(c) == t:
    print('Yes')
  else:
    t += c.pop(0)
    if sum(c) == t:
      print('Yes')
    else:
      print('No')

main()
