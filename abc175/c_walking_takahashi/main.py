#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
  sys.stdin=open('input1.txt')

def main():
  x,k,d = list(map(int, input().strip().split()))
  x = abs(x)
  count = x//d
  if count > k:
    print(x-k*d)
    sys.exit()
  else:
    x -= count * d
    k -= count
  if k % 2 == 0:
    print(x)
  else:
    print(abs(x-d))

main()
