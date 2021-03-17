#!/bin/python3

import sys
input = sys.stdin.readline

def calc(char):
  if char == '#':
    return 1
  else:
    return 0


def main():
  h, w = list(map(int, input().strip().split()))
  s = []
  for _ in range(h):
    st = list(map(str, input().strip().split()))[0]
    s.append(st)

  result = 0
  for i in range(h-1):
    for j in range(w-1):
      count = 0
      for k in range(2):
        for l in range(2):
          count += calc(s[i+k][j+l])
      if count == 1 or count == 3:
        result += 1

  print(result)

main()
