#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
  sys.stdin=open('input1.txt')

def main():
  n = list(map(int, input().strip().split()))[0]
  c = list(map(str, input().strip().split()))[0]

  left_w = 0
  right_r = 0
  for i in range(n):
    if c[i] == 'W':
      left_w += 1
    else:
      right_r += 1
  result = min(left_w, right_r)
  left_w = 0
  for i in range(n):
    if c[i] == 'W':
      left_w += 1
    else:
      right_r -= 1
    result = min(result, max(left_w, right_r))
  print(result)

main()
