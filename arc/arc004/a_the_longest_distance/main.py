#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n = int(input().strip())
  x = []
  y = []
  for i in range(n):
    xt, yt = list(map(int, input().strip().split()))
    x.append(xt)
    y.append(yt)

  result = 0

  for i in range(n):
    for j in range(n):
      tmp = ((x[i] - x[j])**2 + (y[i] - y[j])**2)**0.5
      result =max(result, tmp)

  print(result)
main()
