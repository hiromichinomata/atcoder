#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
  sys.stdin=open('input1.txt')

def main():
  n = list(map(int, input().strip().split()))[0]
  a = list(map(int, input().strip().split()))
  result = 1
  for i in range(n):
    if a[i] % 2 == 0:
      result *= 2
  result = 3**n - result
  print(result)

main()
