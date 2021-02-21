#!/bin/python3

import sys
input = sys.stdin.readline

def main():
  sx, sy, gx, gy = list(map(int, input().strip().split()))
  sy = - sy
  if gx < sx:
    sx, gx = gx, sx
    sy, gy = gy, sy

  gradient = (gy-sy)/float(gx-sx)
  result = -sy/gradient + sx
  print(result)

main()
