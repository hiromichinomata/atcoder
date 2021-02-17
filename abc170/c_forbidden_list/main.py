#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
  sys.stdin=open('input1.txt')

def main():
  x, n = list(map(int, input().strip().split()))
  p = list(map(int, input().strip().split()))
  if n == 0:
    print(x)
    sys.exit()
  result = 2000
  for i in range(-105, 105):
    if i not in p:
      result = min(result, abs(i-x))
    
  if (x - result) not in p:
    print(x-result)
  else:
    print(x+result)

main()
