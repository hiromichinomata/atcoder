#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  n = list(map(int, input().strip().split()))[0]
  x = []
  y = []
  for _ in range(n):
    xt, yt = list(map(int, input().strip().split()))
    x.append(xt)
    y.append(yt)

  board = []
  rotate = 0
  mirror_x = True
  mirror_y = True
  m = list(map(int, input().strip().split()))[0]
  for _ in range(m):
    i, p = list(map(int, input().strip().split()))
    if i == 1:
      pass
    elif i == 2:
      pass
    elif i == 3:
      pass
    else:
      pass

    board.append(rotate, mirror_x, mirror_y)

  q = list(map(int, input().strip().split()))[0]
  a = []
  b = []
  for _ in range(q):
    at, bt = list(map(int, input().strip().split()))
    a.append(at)
    b.append(bt)

main()
