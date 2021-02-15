#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
  sys.stdin=open('input1.txt')

def main():
  n = list(map(int, input().strip().split()))[0]
  result = 0
  for i in range(1, n):
    result += (n-1) // i

  print(result)

main()
