#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
  sys.stdin=open('input1.txt')

def main():
  a, b = list(map(int, input().strip().split()))
  x = (a+b)//2
  y = (a-b)//2
  print(str(x) + ' ' + str(y))

main()
