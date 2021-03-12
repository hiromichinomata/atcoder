#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
  sys.stdin=open('input1.txt')

def main():
  n, k = list(map(int, input().strip().split()))
  result = k*(k-1)**(n-1)
  print(result)

main()
