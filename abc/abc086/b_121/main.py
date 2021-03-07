#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
  sys.stdin=open('input1.txt')

def main():
  a, b = list(map(str, input().strip().split()))
  num = int(a+b)
  if round(num**0.5)**2 == num:
    print('Yes')
  else:
    print('No')

main()
