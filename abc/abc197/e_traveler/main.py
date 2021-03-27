#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n = list(map(int, input().strip().split()))[0]
  max_x = [0]* (n+1)
  min_x = [float('inf')] * (n+1)
  set_c = set()
  for i in range(n):
    x, c = list(map(int, input().strip().split()))
    max_x[c] = max(max_x[c], x)
    min_x[c] = min(min_x[c], x)
    set_c.add(c)

  list_c = sorted(list(set_c))
  mode = 'plus'
  x = 0
  result = 0
  for c in list_c[0:-1]:
    if mode == 'plus':
      result += abs(x - min_x[c])
      result += max_x[c] - min_x[c]
      mode = 'minus'
    else:
      result += abs(x - max_x[c])
      result += max_x[c] - min_x[c]
      mode = 'plus'
  c = list_c[-1]
  result += abs(x - max_x[c])
  result += max_x[c]

  print(result)

main()
