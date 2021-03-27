#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n = list(map(int, input().strip().split()))[0]
  max_x = [-float('inf')]* (n+1)
  min_x = [float('inf')] * (n+1)
  set_c = set()
  for i in range(n):
    x, c = list(map(int, input().strip().split()))
    max_x[c] = max(max_x[c], x)
    min_x[c] = min(min_x[c], x)
    set_c.add(c)

  list_c = sorted(list(set_c))
  x = 0
  result = 0
  mode = 'plus'
  print(min_x)
  print(max_x)
  for c in list_c:
    if abs(x - min_x[c]) > abs(x-max_x[c]):
      mode = 'minus'
    else:
      mode = 'plus'
    if mode == 'plus':
      result += abs(x - min_x[c])
      result += max_x[c] - min_x[c]
      x = max_x[c]
    elif mode == 'minus':
      result += abs(x - max_x[c])
      result += max_x[c] - min_x[c]
      x = min_x[c]
    print(result)
  result += abs(x)

  print(result)

main()
