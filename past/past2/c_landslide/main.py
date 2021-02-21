#!/bin/python3

import copy
import sys
input = sys.stdin.readline

def main():
  n = int(input().strip())
  s = []
  for i in range(n):
    s.append(list(input().strip()))

  for i in range(n-2, -1, -1):
    for j in range(len(s[i])):
      if s[i][j] == '#':
        if j-1 >= 0 and s[i+1][j-1] == 'X':
          s[i][j] = 'X'
          continue
        elif s[i+1][j] == 'X':
          s[i][j] = 'X'
          continue
        elif j+1 < len(s[i]) and s[i+1][j+1] == 'X':
          s[i][j] = 'X'
          continue

  for i in range(n):
    print(''.join(s[i]))

main()
