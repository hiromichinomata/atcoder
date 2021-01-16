#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n, m = list(map(int, input().strip().split()))
  a = list(map(int, input().strip().split()))
  x = []
  y = []

  for _ in range(m):
    xt, yt = list(map(int, input().strip().split()))
    x.append(xt-1)
    y.append(yt-1)

  edges = [[] for _ in range(n)]

  for i in range(m):
    edges[x[i]].append(y[i])

  dp = [-float('inf')] * n
  result = -float('inf')

  for i in range(n-1, -1, -1):
    for j in edges[i]:
      dp[i] = max(dp[i], dp[j], a[j])
    result = max(result, dp[i]-a[i])

  print(result)

main()
