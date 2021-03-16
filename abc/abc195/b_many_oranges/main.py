#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
  sys.stdin=open('input1.txt')

def main():
  a,b,w = list(map(int, input().strip().split()))
  min_c = float('inf')
  max_c = 0
  for i in range(1, 1000000+1):
    if a*i <= w * 1000 <= b*i:
      min_c = min(min_c, i)
      max_c = max(max_c, i)
  if min_c == float('inf') and max_c == 0:
    print('UNSATISFIABLE')
  else:
    print(str(min_c) + ' ' + str(max_c))

main()
