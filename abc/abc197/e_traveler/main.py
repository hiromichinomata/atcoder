#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n = list(map(int, input().strip().split()))[0]
  max_x = [-float('inf')]* (n+2)
  min_x = [float('inf')] * (n+2)
  set_c = set()
  for i in range(n):
    x, c = list(map(int, input().strip().split()))
    max_x[c] = max(max_x[c], x)
    min_x[c] = min(min_x[c], x)
    set_c.add(c)

  LAST = n+1
  min_x[LAST] = 0
  max_x[LAST] = 0
  set_c.add(LAST)
  list_c = sorted(list(set_c))

  result = 0
  dp = [[float('inf')]*2 for i in range(len(list_c))]
  for i in range(len(list_c)):
    c = list_c[i]

    if i == 0:
      dp[0][0] = abs(max_x[c]) + max_x[c] - min_x[c]
      dp[0][1] = abs(min_x[c]) + max_x[c] - min_x[c]
      continue

    prev_c = list_c[i-1]

    a = dp[i-1][0] + abs(max_x[c]-min_x[prev_c]) + max_x[c] - min_x[c]
    b = dp[i-1][1] + abs(max_x[c]-max_x[prev_c]) + max_x[c] - min_x[c]
    dp[i][0] = min(a, b)

    a = dp[i-1][0] + abs(min_x[c]-min_x[prev_c]) + max_x[c] - min_x[c]
    b = dp[i-1][1] + abs(min_x[c]-max_x[prev_c]) + max_x[c] - min_x[c]
    dp[i][1] = min(a, b)

  result = min(dp[-1][0], dp[-1][1])
  print(result)

main()
