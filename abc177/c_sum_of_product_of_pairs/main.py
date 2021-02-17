#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
  sys.stdin=open('input1.txt')

def main():
  n = list(map(int, input().strip().split()))[0]
  a = list(map(int, input().strip().split()))
  MOD = 10**9+7
  total = sum(a)
  result =0
  for i in range(n):
    total -= a[i]
    result += a[i] * total
    result = result % MOD
  print(result)

main()
