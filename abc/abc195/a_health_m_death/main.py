#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
  sys.stdin=open('input1.txt')

def main():
  m, h = list(map(int, input().strip().split()))
  if h% m == 0:
    print('Yes')
  else:
    print('No')

main()
