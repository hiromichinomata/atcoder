#!/bin/python3

import sys
# input = sys.stdin.readline
import math

if sys.platform =='ios':
  sys.stdin=open('input1.txt')

def main():
  n, m, k = list(map(int, input().strip().split()))
  a = list(map(int, input().strip().split()))
  b = list(map(int, input().strip().split()))
  for i in range(1, n):
    a[i] += a[i-1]
  for i in range(1, m):
    b[i] += b[i-1]
  a = [0] + a
  b = [0] + b
  n += 1
  m += 1
  ci = 0
  for i in range(n):
    if a[i] > k:
      break
    ci = i  

  result = ci
  cj = 0
  while ci >= 0:
    for j in range(cj, m):
      if a[ci] + b[j] > k:
        break
      cj = j
    result = max(result, ci+cj)
    ci -= 1

  print(result)

main()
