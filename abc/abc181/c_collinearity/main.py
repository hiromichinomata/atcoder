#!/bin/python3

import sys
# input = sys.stdin.readline

if sys.platform =='ios':
  sys.stdin=open('input1.txt')

def main():
  n = list(map(int, input().strip().split()))[0]
  x = []
  y = []
  for i in range(n):
    xt, yt = list(map(int, input().strip().split()))
    x.append(xt)
    y.append(yt)

  for i in range(n-2):
    for j in range(i+1, n-1):
      for k in range(j+1, n):
        x1,x2,x3 = 0, x[j]-x[i], x[k]-x[i]
        y1,y2,y3 = 0, y[j]-y[i], y[k]-y[i]
        if y2 * x3 == y3 * x2:
          print('Yes')
          sys.exit()

  print('No')

main()
