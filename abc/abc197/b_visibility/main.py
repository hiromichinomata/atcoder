#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  h, w, x, y = list(map(int, input().strip().split()))
  x -= 1
  y -= 1
  s = [0]*h
  for i in range(h):
    s[i] = list(map(str, input().strip().split()))[0]

  result = 0
  for i in range(x+1, h):
    if s[i][y] == '.':
      result += 1
    else:
      break

  for i in range(x-1, -1, -1):
    if s[i][y] == '.':
      result += 1
    else:
      break

  for j in range(y+1, w):
    if s[x][j] == '.':
      result += 1
    else:
      break

  for j in range(y-1, -1, -1):
    if s[x][j] == '.':
      result += 1
    else:
      break

  result += 1
  print(result)

main()
