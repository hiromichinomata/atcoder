#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
  sys.stdin=open('input1.txt')

def main():
  a = list(map(int, input().strip().split()))
  result = 1
  for i in range(len(a)):
    result *= (1+a[i])*a[i]//2
  print(result % 998244353)
main()
