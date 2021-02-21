#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n = list(map(int, input().strip().split()))[0]
  points = []
  for _ in range(n):
    xt, yt = list(map(int, input().strip().split()))
    points.append([xt, yt])

  result = 0

  for i in range(n-1):
    for j in range(i+1, n):
      xi, yi = points[i]
      xj, yj = points[j]
      if abs( (yj - yi) / (xj - xi) ) <= 1:
        result += 1

  print(result)

main()
